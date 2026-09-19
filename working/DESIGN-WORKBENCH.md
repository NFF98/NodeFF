# NodeFF Design Workbench

> 狀態：Working Discussion Buffer  
> 用途：暫存目前正在收斂中的產品／商業／架構觀點。  
> 規則：本文件不是正式 SSOT；在使用者明確說 `sync` 前，不自動同步到其他 Working Docs、`spec/` 或 `decisions/`。

---

## 目前主題：Anonymous-First 與中期 Reuse / Identity 的銜接

### 問題

目前 Business Plan 有一個邏輯缺口：

短期強調 **No Registration**，但如果同時沒有 Usage Record、Anonymous Identity 與 Blueprint Lineage，就無法支撐中期的：

- Trusted Blueprint Reuse
- Creator Identity
- Blueprint Ownership
- Share / Remix Funnel
- Semantic Reliability Learning
- Anonymous → Registered Conversion

因此：

> **No Registration ≠ No Usage Record**

---

## 建議模型

### 短期：Anonymous Identity + Evidence Collection

短期不強制註冊，但從 Day 1 就建立 privacy-conscious anonymous product identity 與最小必要 telemetry。

候選識別：

- `anonymous_id`
- `session_id`
- `intent_id`
- `blueprint_id`
- `instance_id`
- `share_id`
- `parent_blueprint_id`

用來追蹤：

```text
Intent
 → Blueprint
 → Use
 → Share
 → Recipient Open
 → Recipient Use
 → Remix
```

因此 Phase 1 已經可以量測：

- Share Rate
- Share → Open
- Open → Use
- Use → Remix
- Repeat Creation
- Semantic Mismatch
- Blueprint Reuse

---

### 中期：Account Identity + Trusted Reuse + Creator Value

中期不是才開始建立 Identity，而是把既有 Anonymous Identity 升級成 Account Identity。

```text
anonymous_id
 → durable value requested
 → authenticate
 → ownership claim
 → user_id
```

可銜接：

- 先前建立的 Blueprint
- Remix History
- Saved Artifact
- Creator Ownership
- Durable History
- Paid Capability

---

## 關鍵修正

Business Plan 的階段描述應調整為：

### 短期
**Anonymous Identity + Measurement + Evidence Collection**

目的：
- 不阻擋 First Value；
- 但完整保留 PMF 與中期所需的產品證據。

### 中期
**Account Identity + Trusted Reuse + Creator Value**

目的：
- 將已累積的匿名使用證據轉成可重用、可擁有、可保存、可付費的產品層。

### 長期
**Intent Commerce + Capability Network**

---

## 目前原則

1. No Registration 不等於 No Tracking。
2. Anonymous tracking 必須 privacy-conscious，避免預設 fingerprinting。
3. Phase 1 就開始收集 Reuse / Share / Remix / Failure Evidence。
4. 中期主要是「利用已累積的 Evidence」，不是中期才開始收集。
5. Anonymous → Account 必須有 ownership claim / migration 機制。
6. 只收集產品所需的最小資料，不把 Anonymous Usage 視為 unrestricted training consent。

---

## 待同步文件

等使用者說 `sync` 後，再評估同步到：

- `working/BUSINESS-PLAN.md`
- `working/APP-ARCHITECTURE.md`
- `working/INFRA-ARCHITECTURE.md`
- `working/TECHNICAL-MOAT.md`


---

## 新主題：NodeFF 的核心不是 Decision App，而是 Idea-to-App

### 問題

Business Plan 目前有一句：

> 「任何人遇到一個複雜決策 → NodeFF 立即變成一個可互動、可分享、可交易的小 App」

這個描述把 NodeFF 的產品範圍縮得太窄。

NodeFF 不應被定義成「Decision Generator」。

Decision 只是目前容易理解、容易建立 use case 的其中一類。

---

## 修正方向

更接近 NodeFF 本質的描述是：

> **任何人有一個想法、需求、情境或互動構想，只要它適合被做成一個 App，就不需要先去搜尋哪個既有 App 可以完成，而是直接讓 NodeFF 幫他把想法變成可用的 Micro-App。**

概念轉換：

```text
Old Model
Idea / Need
 → Search App
 → Install / Learn / Configure
 → Use

NodeFF Model
Idea / Need
 → Describe Intent
 → NodeFF creates usable Micro-App
 → Use / Share / Remix
```

因此 NodeFF 解決的不是單一 domain 問題，而是：

> **從「Search for an App」轉成「Create the App I need now」。**

---

## Use Case 不應過早定死

目前已知可能包括：

- Decision
- Fun / Party
- Social Interaction
- Sentimental / Emotional Expression
- Personal Utility
- Group Activity
- Temporary Tool
- Creative Interaction
- 其他目前尚未發現的 Micro-App 類型

Phase 1 可以先選幾個容易驗證的 use case 作為 Wedge，但不能把這些 Wedge 誤寫成 NodeFF 的最終產品定義。

正確關係：

```text
Product Vision
= Idea / Need → Micro-App

Phase 1 Wedge
= 從少數高機率 use cases 開始驗證

Observed Usage
= 用真實數據重新判斷最強 category
```

---

## 目前產品定位候選

較佳候選句：

> **NodeFF 讓任何人不必先找 App，而是直接把當下的想法或需求變成 App。**

更完整版本：

> **當一個人產生「如果現在有個 App 可以幫我做這件事就好了」的念頭時，NodeFF 直接把這個念頭變成可互動、可分享、可 Remix 的 Micro-App。**

---

## 對 Business Plan 的影響

未來 `sync` 時需修正：

- 商業核心：從「複雜決策」提升為「Idea / Need → App」
- Phase 1 use case：明確標示為 Wedge，不是產品邊界
- Product Vision：不可被 Decision / Calculator / Party 任一類型綁死
- PMF 方法：實際 use case category 由真實 usage data 驗證，而不是事先假定



---

## CEO 主口號 / 核心宣言

> **意圖就是 App。**

定位：
- NodeFF 的 CEO 主口號；
- 對外最核心、最簡潔的產品宣言；
- 表達 NodeFF 想改寫「先找 App，再使用 App」的傳統軟體心智。

其背後的產品轉換：

```text
Old Model
Intent
 → Search App
 → Install / Learn / Configure
 → Use

NodeFF
Intent
 → App
```

此口號不限定 Decision、Utility、Fun、Social 或其他 use case。

它表達的是更高層的產品願景：

> **使用者不再先尋找一個既有 App；使用者的意圖本身，就成為 App 的起點。**


---

## Sync 狀態 — Architecture 文件重構

本輪已將成熟結論同步至 Working Design：

- `APP-ARCHITECTURE.md`：只保留四層整體架構、核心流程與責任邊界。
- `CAPABILITY-FABRIC.md`：獨立承接 NFF 引擎底座 Capability。
- `APP-DETAILED-DESIGN.md`：採 Function-Oriented 詳細設計。
- `working/functions/`：未來每個 Function 的 Frontend / Backend / Contract / Acceptance 詳細設計。
- `INFRA-ARCHITECTURE.md`：收斂為 Infrastructure 設計結果。
- `DECISION-CANDIDATES.md`：只記錄需要方案選擇的 Decision Gate。
- `OPEN-QUESTIONS.md`：只記錄需更多 Evidence 才能回答的問題。

Workbench 中的「Anonymous-First ≠ No Usage Record」與「Idea / Need → App」已作為本輪 Architecture 輸入；Workbench 仍保留原討論脈絡，不作 SSOT。


---

## 待同步佇列 — ProjectManagement Review → Function Design

> 管理規則：本區只記錄 **尚未同步到 `working/functions/` 的新結論**。已同步項目不重複記錄；等本輪 Review 完成後一次整理與更新 Function 文件。

### PENDING-FUNC-001 — Capability Card Contract 擴充

來源：
- `working/ProjectManagement/CAPABILITY-FABRIC.md`
- `working/ProjectManagement/BUSINESS-PLAN.md`

後續 Function Design 必須反映：

1. Capability 不只包含 Technical Contract，還要包含：
   - Product Contract
   - Reuse / Creator hooks
   - Commerce / Network hooks
   - Evidence / Maturity

2. 五個產品原則要能從 Capability 原子層被支援：
   - No install setup
   - Everyone is the creator
   - Sharable, linkable
   - Intent Commerce
   - Fun and socialable

3. 中期能力不能到中期才重做底座；原子層需預留：
   - Remix / Reuse
   - Attribution
   - Version / Compatibility
   - Ownership / Creator configuration
   - Paid / Entitlement metadata

4. 長期 External / Paid Capability 應沿用同一套 Runtime / Registry，不另建第二套 Commerce Runtime。

5. Capability 狀態採：
   - PROPOSED
   - POC
   - BUILT
   - TESTED
   - VALIDATED
   - RELEASED

6. **待補強項**：Capability Contract 需明確加入 Identity / Ownership Hooks，例如：
   - anonymous allowed
   - account required
   - ownership required
   - creator attribution
   - recipient permission
   - entitlement scope

主要影響 Function：
- F03 Runtime Execution
- F04 Capability Registry
- F05 Share / Restore
- F06 Remix / Refine
- F07 Anonymous Identity & Evidence
- F08 Durable Identity / Ownership
- F10 Blueprint Reuse / Retrieval
- F11 External Capability Execution

### PENDING-FUNC-002 — Infrastructure Baseline（已重新推導）

來源：
- `working/INFRA-ARCHITECTURE.md`
- `working/ProjectManagement/PRODUCT-DISCUSSION.md`
- `working/ProjectManagement/BUSINESS-PLAN.md`
- `working/ProjectManagement/CAPABILITY-FABRIC.md`
- `working/TECHNICAL-MOAT.md`

後續 Function Design 採用：

~~~text
Browser Runtime Plane
+ Cloudflare Edge / Serverless Control Plane
+ Supabase PostgreSQL Durable State Plane
+ Pluggable External Capability Plane
~~~

新的 Function Design 約束：
- Phase 1 Runtime interaction 優先 Browser-local；
- Cloudflare Static/CDN + Workers 為 Phase 1 Edge / Serverless baseline；
- Supabase Postgres 為唯一 durable System of Record；
- Capability Registry Phase 1 是 versioned code/build artifact，不先做動態 Registry service；
- immutable Blueprint 使用 content hash + CDN immutable cache，不先依賴 Edge KV；
- LLM 僅經 Compiler API；
- telemetry 只收 meaningful events 並 batch；
- Supabase Auth / Realtime / Storage 在需要前不啟用；
- semantic reuse 優先沿用 Postgres / pgvector，有證據後再啟用，不先建 dedicated Vector DB；
- Queue / Background Worker 只為 Heavy Capability 啟動；
- 中長期 Capability Gateway / Provider Registry / Entitlement / Metering / Transaction layer 必須沿用相同 Blueprint / Runtime model；
- Cloudflare / Supabase / LLM / Realtime / Payment 等 Vendor 必須藏在 NFF-owned adapter 後面。

主要影響 Function：
- F01 Intent Compilation
- F02 Blueprint Validation
- F03 Runtime Execution
- F04 Capability Registry
- F05 Share / Restore
- F07 Anonymous Identity & Evidence
- F08 Durable Identity / Ownership
- F09 Realtime Room
- F10 Blueprint Reuse / Retrieval
- F11 External Capability Execution

### 同步時機

本輪使用者仍在 Review 其他 Working 文件。

在明確要求統一同步前：
- 不逐項修改 `working/functions/`；
- 不重複同步已記錄內容；
- 新發現只追加「新的差異」到本待同步佇列；
- Review 完成後一次整理 Function 總表、個別 Function Design 與 Release dependency。
