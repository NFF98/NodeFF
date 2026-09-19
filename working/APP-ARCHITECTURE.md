# NodeFF App Architecture

> 狀態：Working。本文定義 NodeFF App 的整體架構、使用者體驗邊界、四層 Engine、Capability Fabric 接點、LLM Provider 抽象與跨層 Recovery。具體 Function 實作留待 `APP-DETAILED-DESIGN.md` / `working/functions/`。

# 1. 系統定位

NodeFF 是一個 **Intent-to-App Runtime Platform**。

產品核心：

> **意圖就是 App。**

使用者不必先找 App、安裝 App、學 App，而是描述需求，由 NodeFF 將 Intent 轉成可互動、可分享、可 Remix 的 Micro-App。

NodeFF 部署的是：

> **Experience Shell + Semantic Compiler + Trusted Contract + Universal Runtime + Capability Fabric**

不是為每個使用者重新部署一個獨立 App。

---

# 2. 整體架構

~~~mermaid
flowchart TB
    U[User]

    subgraph UX["Experience Shell / 靈感精靈"]
        INSPIRE[Inspiration Capsules / Ghost Text]
        REFINE[Progressive Refinement]
        RECOVERY[Humanized Recovery UX]
    end

    subgraph ENGINE["NodeFF Engine"]
        L1[Layer 1
Ingestion & Routing]
        L2[Layer 2
Semantic Compiler]
        L3[Layer 3
LegoSpec Contract + Validation]
        L4[Layer 4
Universal Runtime]
    end

    FABRIC[Capability Fabric / Registry]
    MODEL[Model Gateway / Provider Adapters]
    APP[Interactive Micro-App]

    U --> UX
    UX --> L1
    L1 --> L2
    L2 <--> MODEL
    L2 <--> FABRIC
    L2 --> L3
    L3 <--> FABRIC
    L3 --> L4
    L4 <--> FABRIC
    L4 --> APP

    L1 -. recovery state .-> RECOVERY
    L2 -. recovery state .-> RECOVERY
    L3 -. recovery state .-> RECOVERY
    L4 -. recovery state .-> RECOVERY
~~~

核心觀念：

- **Experience Shell**：負責讓人容易開始、容易修正、容易理解失敗。
- **四層 Engine**：負責把 Intent 可靠地變成可執行 Blueprint。
- **Capability Fabric**：決定 NFF 真正「會做什麼」。
- **Model Gateway**：讓 Semantic Compiler 不綁死任何單一 LLM。
- **Recovery UX**：確保錯誤最後都變成使用者可以理解與採取下一步的產品狀態。

---

# 3. Experience Shell — 靈感精靈 / 創作引導系統

靈感精靈不是另一個 AI Engine，也不是展示 Demo。

它是使用者進入 NodeFF 的 **Creation Experience Shell**，目標是降低「空白 Prompt」的思考成本。

目前已確立的 UX 機制：

## 3.1 Inspiration Capsules

顯示「可以做什麼」的可編輯範例。

點擊後不是只看 Demo，而是：

~~~text
Capsule
 → Fork Prompt
 → 修改關鍵變數
 → Generate
 → Use / Remix
~~~

原則：

> **編輯一個好範例，要比從零想 Prompt 更容易。**

## 3.2 Ghost Text

空白輸入時，以自然語言範例持續示範：

> 普通人的日常描述，就可以成為 App 的起點。

## 3.3 Progressive Refinement

第一次 Intent 不必完美。

~~~text
粗略 Intent
 → 先產生可用 App
 → 提供情境化 Refinement Suggestions
 → User 選擇修改
 → Semantic Delta
 → 新 Blueprint
~~~

## 3.4 Fork & Remix Learning Loop

~~~text
Copy
 → Modify
 → Combine
 → Create
~~~

產品原則：

> **先完成，再學會；不是先學會，才能完成。**

Experience Shell 同時也是後述 Error / Capability Gap 的主要人性化呈現層。

---

# 4. Layer 1 — Ingestion & Routing

責任：

- 接收 Intent；
- request normalization；
- safety / policy / quota gate；
- exact / trusted reuse lookup；
- routing；
- 保存原始 Intent 與 recovery context。

Layer 1 不負責：
- 自由文字業務語意理解；
- 決定 Capability 組合；
- 選擇 fallback App 意義。

若 request 被阻擋，也不能只回傳 HTTP code；必須產生可由 Experience Shell 呈現的 Recovery State。

---

# 5. Layer 2 — Semantic Compiler

Layer 2 是 NodeFF 的語意大腦。

責任：

- 理解 Intent；
- 拆解 requirements；
- 查詢 Capability Fabric；
- 判斷 Capability Coverage；
- 選擇與組合 Capability；
- 建立 State / Rule / Event / Action wiring；
- 產生 Blueprint Candidate；
- bounded repair / refinement。

核心輸出：

> **結構化 Blueprint，而不是 JavaScript。**

---

# 6. LLM 自由切換放在哪裡？

LLM Provider / Model 的自由切換屬於：

> **Layer 2 Semantic Compiler 內的 Model Gateway / Provider Adapter**

架構：

~~~text
Semantic Compiler
      ↓
Model Router
      ↓
NFF Model Interface
 ├─ Provider Adapter A
 ├─ Provider Adapter B
 ├─ Provider Adapter C
 └─ Future Model
~~~

Model Router 可以依：

- task type；
- model capability；
- structured-output support；
- latency；
- cost；
- quota；
- availability；
- fallback policy；

選擇模型。

重要邊界：

1. LegoSpec 不知道使用的是哪一家 LLM。
2. Runtime 不知道使用的是哪一家 LLM。
3. Provider SDK / response format 不能滲透進 Layer 3 Contract。
4. Provider failure 可切換 Adapter，但所有輸出仍必須經同一套 Validation。
5. 是否提供「使用者手動選模型」是 Product Feature，不是 Architecture 必要條件。

因此 NFF 可以換模型而不改 Runtime / Blueprint。

---

# 7. Capability Fabric 在整體架構中的位置

Capability Fabric **不是四層中的第五層**。

它是一個跨 Layer 2 / 3 / 4 共用的可信任能力系統：

~~~text
Capability Fabric
      │
      ├─ Layer 2：知道「有哪些能力、何時適合用」
      ├─ Layer 3：驗證「這些能力能否合法組合」
      └─ Layer 4：提供「真正可執行的 Runtime implementation」
~~~

Capability Fabric 詳細定義位於：

- `working/ProjectManagement/CAPABILITY-FABRIC.md`

Phase 1 Registry 應由同一份 versioned source 產生：

- Compiler semantic metadata；
- Validator contract；
- Runtime registration；
- compatibility metadata。

禁止 Compiler、Validator、Runtime 各自維護不同能力清單。

---

# 8. User Intent 無法對應 Capability 時怎麼辦？

NodeFF 不允許 LLM「假裝會」。

Layer 2 必須先做 **Capability Coverage Resolution**。

每個 Intent 最終至少落入四種結果：

## FULLY_SUPPORTED

現有 Capability 足以保持核心 Intent。

~~~text
Intent
 → Compose
 → Validate
 → Execute
~~~

## PARTIALLY_SUPPORTED

只有在「核心語意仍然成立」時，才能提供降級版本。

例如：

> 視覺效果較簡化，但遊戲規則仍完全成立。

必須明確告知使用者差異，不可 silent downgrade。

## EXTERNAL_OR_HEAVY_REQUIRED

需求可由 approved external / heavy Capability 完成，但可能需要：

- 額外時間；
- permission；
- login；
- paid entitlement；
- external cost。

Experience Shell 應先給使用者清楚選擇，不偷偷執行付費或敏感行為。

## UNSUPPORTED

沒有合法 Capability 能保持核心 Intent 時：

> **不要捏造一個看起來像 App、其實解錯問題的結果。**

系統應：

1. 保留原始 Intent；
2. 用人話說明「目前哪一部分還做不到」；
3. 如果存在合理替代方案，讓使用者選擇；
4. 提供 Refinement；
5. 記錄 Capability Gap Evidence。

Capability Gap 會回饋：

~~~text
Unsupported Intent
 → Capability Gap Evidence
 → Product / Capability Review
 → POC
 → Future Capability
~~~

這讓真實需求反過來決定 Capability Fabric 應該長什麼。

---

# 9. Layer 3 — LegoSpec Contract + Validation

Layer 3 是 Compiler 與 Runtime 之間的信任邊界。

主要定義：

- State；
- Capability references；
- Actions / Events；
- Rules；
- Bindings；
- Assumptions；
- version / compatibility；
- support / degradation metadata；
- recovery / notice metadata。

Validation 不只檢查 JSON shape。

還必須確保：

- Capability 存在；
- references 合法；
- wiring 合法；
- resource bounded；
- permissions 合法；
- fallback 不冒充 full support；
- unsupported semantics 不被 Runtime 猜測。

原則：

> **Schema Valid ≠ Semantic Correct。**

---

# 10. Layer 4 — Universal Runtime

責任：

- Hydration；
- State execution；
- Rule evaluation；
- Capability rendering / invocation；
- Event handling；
- Effect；
- share / restore；
- optional realtime binding；
- local component isolation。

Runtime 不負責：

- 猜 Intent；
- 選 LLM；
- 發明不存在的 Capability；
- 自己決定語意降級方案；
- 執行 arbitrary generated code。

核心路徑：

~~~text
Action
 → State
 → Rule / Capability
 → View
 → Effect
~~~

---

# 11. 三條核心產品路徑

## Create

~~~text
Inspiration / Intent
 → Route
 → Compile
 → Capability Resolution
 → Validate
 → Blueprint
 → Execute
~~~

## Use / Share

~~~text
Existing Blueprint
 → Resolve / Restore
 → Compatibility + Trust Check
 → Execute Locally
~~~

既有有效 Blueprint 一般互動預設 0 次 LLM call。

## Remix / Refine

~~~text
Existing Blueprint
 + User Change
 → Semantic Delta
 → Compile / Validate
 → New Immutable Blueprint Revision
~~~

Runtime state change 與 Blueprint semantic change 必須分開。

---

# 12. 全域 Error Handling：技術錯誤不能直接丟給使用者

NodeFF 內部可以有 HTTP 401 / 404 / 402 / 500、validation code、provider error。

但：

> **這些是工程訊號，不是產品文案。**

所有 Layer 的 failure 最後都必須轉成統一的 **Recovery UX State**。

建議架構：

~~~text
Technical Failure
 → Error Classification
 → Recovery Policy
 → Recovery UX State
 → Experience Shell
 → Human Message + Useful Next Action
~~~

---

# 13. Recovery UX State

每個可預期錯誤至少應產生：

- **Status**：retryable / needs_input / degraded / unsupported / blocked；
- **Human Message**：使用者看得懂的說明；
- **Preserved Context**：原始 Intent / 已輸入資料盡量保留；
- **Next Actions**：Retry / Refine / Use Alternative / Sign In / Continue；
- **Technical Code**：僅供 telemetry / debug，不直接顯示給一般使用者。

例如：

| Internal | User Experience |
|---|---|
| 401 | 「這個內容需要登入後才能繼續。」＋登入按鈕 |
| 402 / entitlement | 「這項能力需要額外額度／付費能力。」＋選擇替代或繼續 |
| 404 share | 「這個 App 連結目前找不到或已失效。」＋返回／重新建立 |
| compiler timeout | 「這次還沒成功做出 App，你的需求已保留。」＋重試 |
| capability gap | 「目前還不能完整做到這個效果。」＋可行替代／調整需求 |
| runtime component error | 只隔離該區塊，其他 App 繼續運作 |

---

# 14. Error Recovery Pipeline

~~~mermaid
flowchart TD
    A[User Request / Interaction] --> B{哪一類問題?}

    B -->|Routing / Network| R1[Retry / Restore Context]
    B -->|Compilation| R2[Bounded Repair / Provider Fallback]
    B -->|Validation| R3[Reject Candidate / Repair]
    B -->|Semantic Mismatch| R4[User Refinement]
    B -->|Capability Gap| R5[Explain + Alternative / Refine]
    B -->|Runtime Component| R6[Local Isolation / Safe Fallback]
    B -->|Permission / Entitlement| R7[Humanized Permission / Upgrade Choice]

    R1 --> UX[Experience Shell Recovery UI]
    R2 --> UX
    R3 --> UX
    R4 --> UX
    R5 --> UX
    R6 --> UX
    R7 --> UX
~~~

核心原則：

1. **不中斷流程，但不隱瞞錯誤。**
2. **不丟 White Screen。**
3. **不直接顯示工程碼作為答案。**
4. **盡可能保留使用者已輸入內容。**
5. **每次失敗至少提供一個有意義的下一步。**
6. **Retry 有上限，不無限自動重試。**
7. **降級不得改變核心語意後還假裝成功。**

---

# 15. 錯誤責任分層

## Layer 1
處理：
- invalid request；
- rate / policy；
- network / routing；
- access prerequisite。

產物：Recovery State，不是裸 HTTP error。

## Layer 2
處理：
- provider failure；
- malformed generation；
- semantic uncertainty；
- capability mismatch；
- repair / refinement。

## Layer 3
處理：
- schema；
- reference；
- capability；
- rule；
- permission；
- resource；
- compatibility validation。

不安全 Candidate 不進 Runtime。

## Layer 4
處理：
- runtime exception；
- single Capability crash；
- invalid local state；
- rendering failure。

採 component-level isolation，不讓整個 Micro-App 一起崩。

## Experience Shell
統一把所有錯誤翻譯成：

> **發生什麼 + 我保留了什麼 + 現在可以做什麼**

---

# 16. Failure Evidence 是產品輸入

Error 不只是 logging。

NodeFF 應區分：

- generation failure；
- validation failure；
- semantic mismatch；
- capability gap；
- runtime failure；
- degraded result；
- recovery success / failure。

這些 Evidence 未來會直接改善：

- Composition Intelligence；
- Capability Fabric；
- Trusted Blueprint Reuse；
- Reliability Knowledge。

因此：

> **一次失敗，至少要讓系統知道下一次應該改善什麼。**

---

# 17. 核心狀態模型

必須分清：

- **Blueprint**：不可變 App 定義。
- **Instance**：某次執行的可變狀態。
- **Context**：經允許跨 App 傳遞的資料。
- **Delta**：受控變更。
- **Recovery Context**：失敗時保留的 Intent / Input / Progress。

原則：

> Blueprint 定義能力；Instance 表示當前現實；Recovery Context 確保失敗不等於全部重來。

---

# 18. Identity 與 Evidence

Phase 1 採 Anonymous-First，但不是 No-Tracking。

~~~text
anonymous_id
 → Intent
 → Blueprint
 → Use
 → Share
 → Remix
~~~

短期保存最小必要 Evidence，用於：

- Semantic Reliability；
- Share / Remix Funnel；
- Capability Gap；
- Blueprint Reuse；
- 未來 Anonymous → Account migration。

Account / Ownership 不作為 First Value 的門檻。

---

# 19. 文件分工

~~~text
APP-ARCHITECTURE.md
= Experience Shell + 四層架構 + 跨層責任

ProjectManagement/CAPABILITY-FABRIC.md
= NFF 到底有哪些能力卡、Card Contract、Maturity

APP-DETAILED-DESIGN.md
= Function Design 總表與 Release 對應

working/functions/
= 各 Function 的 Frontend / Backend / API / Data / Recovery 詳細設計

INFRA-ARCHITECTURE.md
= Browser / Edge / Serverless / DB / External Capability 的部署設計
~~~

---

# 20. Architecture Guardrails

1. 不生成或執行任意 JavaScript。
2. Runtime 不做 free-form Intent 推理。
3. Schema Valid 不等於 Semantic Correct。
4. Capability Fabric 是可執行能力唯一邊界。
5. Unsupported Intent 不得以錯誤語意假裝成功。
6. LLM Provider 必須藏在 Layer 2 Model Gateway 後。
7. Blueprint / Instance / Context / Delta / Recovery Context 必須分離。
8. Existing Blueprint 一般互動預設 0 LLM。
9. Share / Remix 是核心產品路徑。
10. Error code 不能直接成為 Consumer UX。
11. Failure 必須轉換成 Humanized Recovery State。
12. Component failure 不得擴散成整個 Micro-App White Screen。
13. Heavy / Paid Capability 必須明確經 Capability Boundary。
14. Architecture 決定邊界；Function Design 才決定實作細節。

---

# 21. Phase 1 Architecture Focus

Phase 1 要證明的不是「所有 Intent 都能做」。

而是：

> **NodeFF 能可靠地把可支援的 Intent 變成正確 App；遇到做不到或出錯時，也能給使用者清楚、友善、可繼續的交代。**

因此 Phase 1 核心：

~~~text
Inspiration / Intent
        ↓
Reliable Compiler
        ↓
Capability Resolution
        ↓
Trusted Blueprint
        ↓
Local Runtime
        ↓
Use / Share / Remix
        ↓
Humanized Recovery + Evidence
~~~

這才是 NodeFF 從 POC 走向可信任產品的完整核心循環。
