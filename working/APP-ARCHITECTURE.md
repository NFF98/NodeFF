# NodeFF App Architecture

> 狀態：Working。本文只描述 NodeFF 應用系統的整體架構、責任邊界與設計文件分工；具體 Capability 與功能實作細節由其他設計文件承接。

# 1. 系統定位

NodeFF 是一個 **Intent-to-App Runtime Platform**。

產品核心：

> **意圖就是 App。**

使用者不需要先搜尋、安裝與學習既有 App，而是直接描述當下的 Intent，由 NodeFF 轉成可互動、可分享、可 Remix 的 Micro-App。

~~~text
Intent
  ↓
Semantic Compiler
  ↓
Validated Blueprint
  ↓
Universal Runtime
  ↓
Interactive Micro-App
~~~

NodeFF 部署的是 Runtime 與 Capability，不是每個生成 App 的獨立程式碼。

---

# 2. 整體四層架構

四層架構只負責說明系統責任，不承載每個功能的詳細設計。

## Layer 1 — Ingestion & Routing

負責：
- 接收 Intent；
- request normalization；
- safety / policy / quota gate；
- cache / reuse lookup；
- request routing。

不負責理解自由文字業務語意。

## Layer 2 — Semantic Compiler

負責：
- 理解 Intent；
- 拆解需求；
- 選擇 Capability；
- 建立 State / Rule / Event / Action wiring；
- 產生 Blueprint；
- 必要時進行 bounded repair / refinement。

核心輸出是結構化 Blueprint，不是 JavaScript。

## Layer 3 — LegoSpec Contract

負責定義 Compiler 與 Runtime 之間的可信任合約，包括：
- State；
- Capability references；
- Actions / Events；
- Rules；
- Bindings；
- Assumptions；
- Version / compatibility metadata。

Blueprint 必須通過結構、語意邊界、安全與資源限制驗證。

## Layer 4 — Universal Runtime

負責：
- Hydration；
- State execution；
- Rule evaluation；
- Capability rendering / invocation；
- Event handling；
- Effects；
- Share / restore；
- Optional realtime binding。

Runtime 不重新猜測原始 Intent，也不執行任意 generated code。

---

# 3. 三條核心執行路徑

## 3.1 Create

~~~text
Intent
 → Route
 → Compile
 → Validate
 → Blueprint
 → Execute
~~~

這是主要 Cold Path。

## 3.2 Use / Share

~~~text
Existing Blueprint
 → Resolve / Restore
 → Compatibility + Trust Check
 → Execute Locally
~~~

既有有效 Blueprint 的一般互動預設不重新呼叫 LLM。

## 3.3 Remix / Refine

~~~text
Existing Blueprint
 + User Change
 → Semantic Delta
 → Recompile / Validate
 → New Blueprint Revision
~~~

Runtime state change 與 Blueprint semantic change 必須分開。

---

# 4. Capability 是 Runtime 的能力邊界

NodeFF 的 App 能做什麼，不由 LLM 自由決定，而由 **Capability Fabric** 決定。

~~~text
Intent
 → Compiler selects Capabilities
 → Blueprint wires them
 → Runtime executes them
~~~

詳細 Capability family、Card Contract、Phase 1 能力與未來 Game / AV / 3D / XR 能力，統一記錄於：

- `working/CAPABILITY-FABRIC.md`

APP Architecture 只定義 Capability 在系統中的位置，不重複維護能力清單。

---

# 5. 核心狀態模型

架構上必須分清四個概念：

- **Blueprint**：不可變的 App 定義。
- **Instance**：某次執行中的可變狀態。
- **Context**：App 之間經允許傳遞的資料。
- **Delta**：對 Instance 或 Blueprint revision 的受控變更。

原則：

> Blueprint 定義能力；Instance 表示當前現實。

---

# 6. Identity 與 Evidence

Phase 1 採 Anonymous-First，但不是 No-Tracking。

~~~text
anonymous_id
 → Intent
 → Blueprint
 → Use
 → Share
 → Remix
~~~

短期需要保存最小必要的產品證據，以支援：
- Semantic Reliability；
- Share / Remix Funnel；
- Blueprint Reuse；
- 未來 Anonymous → Account migration。

Account Identity、Ownership 與 Durable Value 在需要時再加入，不作為 First Value 的門檻。

---

# 7. 設計文件分工

為避免 Architecture、Capability 與實作細節混在一起，Working 設計文件分工如下：

~~~text
APP-ARCHITECTURE.md
= 整體系統架構與責任邊界

CAPABILITY-FABRIC.md
= NFF 引擎底座能做什麼、有哪些能力卡、如何組合

APP-DETAILED-DESIGN.md
= 功能詳細設計總表、設計規範、開發與 Release 對應

working/functions/
= 每個 Function 的具體詳細設計
~~~

Infrastructure 另由：

- `working/INFRA-ARCHITECTURE.md`

負責部署、服務邊界、資料存放、Cache、Realtime、Security、Observability 等基礎設施設計。

---

# 8. Function-Oriented 詳細設計

詳細設計不以「Frontend 一份、Backend 一份」拆開。

每個 Function 由同一份設計從頭描述：

~~~text
Function
 ├─ Product Behavior
 ├─ User Flow
 ├─ Frontend
 ├─ Backend
 ├─ API / Contract
 ├─ Data / State
 ├─ Error / Recovery
 ├─ Security / Permission
 ├─ Telemetry
 ├─ Acceptance Criteria
 └─ Release Dependency
~~~

原因是 NodeFF 的核心功能通常跨越前後端，例如 Compile、Share、Remix、Realtime、Identity。

只有當某一側複雜度足夠高時，才從 Function Design 再拆專門子文件。

---

# 9. Function Design 與開發 / Release

`APP-DETAILED-DESIGN.md` 是功能總表。

每個可進入開發的 Function 必須具備：
1. 明確目的與 scope；
2. 前後端責任；
3. Contract / Data Flow；
4. Acceptance Criteria；
5. Dependencies；
6. Target Release / Sprint。

~~~text
Architecture
 → Function Design
 → Acceptance
 → Backlog / Sprint
 → Implementation
 → Release
~~~

因此 Cursor 執行的是已核准的 Function Design，而不是自行補架構決策。

---

# 10. 架構 Guardrails

1. 不生成或執行任意 JavaScript。
2. Runtime 不負責自由文字 Intent 推理。
3. Schema Valid 不等於 Semantic Correct。
4. Capability Registry 是可執行能力的唯一入口。
5. Blueprint、Instance、Context、Delta 必須分離。
6. 既有 Blueprint 的一般互動預設不重複消耗 LLM。
7. Share / Remix 是核心產品路徑，不是附加 Export。
8. Anonymous-First 必須保留最小必要 Evidence。
9. Heavy Compute 由專門 Capability / Worker / External Service 承接。
10. 詳細設計以 Function 為單位，避免前後端文件失去完整流程。

---

# 11. 現階段重點

Phase 1 架構優先證明：

> **Intent → Correct App → Use → Share → Remix**

因此近期技術重點是：

~~~text
Capability Fabric
 + Composition Intelligence
 + Reliable Compiler
 + Trusted Runtime
 + Share / Remix
 + Anonymous Evidence
~~~

長期的 Learning Graph、Trusted Blueprint Families、Creator / Commerce Layer，建立在這個基礎之上。
