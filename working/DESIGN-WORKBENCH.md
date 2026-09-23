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
- `APP-DETAILED-DESIGN-OVERVIEW.md`：採 Function-Oriented 詳細設計。
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


---

### PENDING-FUNC-003 — App Architecture Review：Experience Shell / Model Gateway / Capability Gap / Humanized Recovery

來源：
- `working/APP-ARCHITECTURE.md`
- `working/ProjectManagement/PRODUCT-DISCUSSION.md`
- `working/ProjectManagement/CAPABILITY-FABRIC.md`

> 本項只記錄本輪新增差異；前面已同步／已記錄的 Architecture、Infra、Capability Contract 內容不重複。

後續 Function Design 必須反映：

1. **Experience Shell / 靈感精靈**
   - Inspiration Capsules
   - Ghost Text
   - Fork & Remix
   - Progressive Refinement
   - Humanized Recovery UI
   - 其定位是 Creation / Recovery Experience Shell，不是另一個 Semantic Engine。

2. **LLM Provider Abstraction**
   - 邏輯位置：Layer 2 Semantic Compiler。
   - 使用 NFF-owned Model Gateway / Model Router / Provider Adapter。
   - Provider / Model 可依 capability、cost、latency、quota、availability、fallback policy 切換。
   - LegoSpec、Runtime、Layer 3 Contract 不得依賴特定 LLM vendor。
   - 使用者手動選模型是否提供，屬未來 Product Feature，不是核心 Architecture 要求。

3. **Capability Coverage Resolution**
   - Intent 必須被分類為：
     - FULLY_SUPPORTED
     - PARTIALLY_SUPPORTED
     - EXTERNAL_OR_HEAVY_REQUIRED
     - UNSUPPORTED
   - Layer 2 負責判斷語意上的 fallback；
   - Layer 3 驗證 Capability / degradation metadata；
   - Layer 4 只執行，不自行猜測替代語意。
   - Unsupported Intent 不可生成「看起來正常但解錯問題」的假 App。
   - Capability Gap 應形成 Evidence，回饋 Capability Fabric POC / backlog。

4. **Recovery UX Contract**
   - Internal HTTP / validation / provider code 不直接顯示給 Consumer。
   - 各層 failure 統一轉為 Recovery UX State：
     - status
     - human message
     - preserved context
     - next actions
     - internal technical code
   - 例如 401 / 402 / 404 / timeout / runtime exception 都必須轉成人話與可操作下一步。

5. **Recovery Context**
   - App state model 後續需考慮 Recovery Context：
     - original Intent
     - user input
     - partial progress
   - 目標是 failure 不等於全部重來。

6. **Error Responsibility**
   - L1：routing / policy / access prerequisite
   - L2：provider / generation / semantic uncertainty / capability mismatch
   - L3：schema / reference / permission / resource / compatibility
   - L4：runtime / component isolation
   - Experience Shell：統一呈現「發生什麼、保留什麼、下一步做什麼」

7. **Phase 1 Acceptance Direction**
   - 不只測「成功生成 App」；
   - 也要測：
     - unsupported intent 是否誠實處理；
     - provider failure 是否可 recovery；
     - invalid blueprint 是否不進 Runtime；
     - component crash 是否不造成整頁崩潰；
     - user input 是否在失敗後保留；
     - consumer 是否永遠看到 humanized next action。

主要影響 Function：
- F01 Intent Compilation
- F02 Blueprint Validation
- F03 Runtime Execution
- F04 Capability Registry
- F05 Share / Restore
- F06 Remix / Refine
- F07 Anonymous Identity & Evidence
- F11 External Capability Execution
- 未來需評估是否新增獨立 Experience Shell / Recovery Function，或由上述 Function 共同承接。

同步規則維持不變：
- 本輪先不修改 `APP-DETAILED-DESIGN-OVERVIEW.md`；
- 不逐項改 `working/functions/`；
- 等使用者完成 APP Architecture / Working 文件 Review 後再一次同步。


---

## Sync Status — 1／3／6 個月 Design Baseline

以下待同步項已於本輪吸收到新版 Working Design，後續不再重複處理：

- PENDING-FUNC-001 — Capability Card Contract 擴充 → 已反映於 CAPABILITY-FABRIC.md 與 APP-DETAILED-DESIGN-OVERVIEW.md。
- PENDING-FUNC-002 — Infrastructure Baseline → 已反映於 APP-DETAILED-DESIGN-OVERVIEW.md 的 Function boundary / phase dependency；Infra 細節仍以 INFRA-ARCHITECTURE.md 為準。
- PENDING-FUNC-003 — Experience Shell / Model Gateway / Capability Gap / Humanized Recovery → 已反映於 APP-ARCHITECTURE.md 與 APP-DETAILED-DESIGN-OVERVIEW.md。

統一時間基準：

~~~text
0–1 個月
Core Proof

2–3 個月
Reuse / Identity / Creator Value

4–6 個月
Scale Readiness / External Paid Capability Pilot

6 個月後
Intent Commerce / Capability Network 持續擴張
~~~

管理規則：
- 上述三項之後視為 SYNCED，不再重複進待同步佇列。
- 新 Review 只記錄相對於目前 baseline 的新差異。


---

## Phase 1 UI/UX — S01 Discover / Start Review Notes

> Sync status：已同步到 Screen Working Design。
> Sync target：`working/UI-UX/screens/S01-DISCOVER-START.md`
>
> 狀態：WORKBENCH HISTORY — 保留討論脈絡，不再作 Screen Current Truth。
> 來源：Phase 1 Screen Inventory / S01 Low-fi Review。

### S01 已確認方向

1. **核心內容與資訊架構保留**：
   - 「意圖就是 App」主訊息；
   - Prompt-first、Inspiration Capsules supporting；
   - Create CTA；
   - Explore / Inspiration 作為降低空白輸入門檻的輔助；
   - Desktop / Mobile 皆維持乾淨、低干擾的畫面。

2. **Visual guardrail**：
   - Must not resemble Google / Search UI；
   - 避免「中央 Logo + 大搜尋框 + 大量空白」的搜尋首頁語言；
   - 畫面以 Creator / App-making experience 為核心。

3. **視覺簡化**：
   - 右上角及 Header 不必要的圖示、裝飾、入口先移除；
   - Phase 1 首屏只保留會直接幫助 Create / Explore 的元素；
   - 整體畫面優先乾淨、清楚、低認知負擔。

### Brand Color Direction — Tiffany Blue → Yellow

主色方向採 **Tiffany Blue → Yellow** 的雙色／漸變視覺語言作為 High-fi 探索基準。

參考：PR EDGE〈Tiffanyが期間限定でティファニーブルーからイエローに変更〉
https://predge.jp/210039/

使用原則：
- 此處是色彩方向參考，不複製 Tiffany 品牌識別；
- High-fi 階段再確認實際 HEX、gradient stop、contrast、dark/light surface、accessibility；
- 黃色偏 accent / energy / completion，藍綠色偏 creation / calm / brand anchor；
- 最終 palette 必須形成 NodeFF 自己的 brand system。

### 新增 UX 候選 — Visible Generation Progress

使用者在本次 UI 生成過程中特別確認：**可視化生成進度非常有價值，NodeFF 也應納入此體驗。**

候選方向：

~~~text
User submit Intent
→ Analyze
→ Understand / Clarify if required
→ Compose App
→ Validate
→ Prepare Runtime
→ Ready
~~~

UX 原則：
- 不只顯示 generic spinner；要讓 User 感覺「事情正在往前完成」。
- 進度可使用 progress bar + human-readable stage label。
- 不暴露 Prompt A / Prompt B / Validator 等內部工程術語。
- 不假裝精確百分比；若 backend 無可靠 percentage，應以 stage-based progress / bounded animation 表達。
- 若進入 Clarification / Recovery，progress 必須自然切換，不可讓 User誤以為仍在自動完成。
- 此模式未來可延伸到 Refine / Remix / Correction，但需由各 Function UX contract確認。

候選 Consumer copy：

~~~text
理解你的想法…
整理成 App…
確認可以安全執行…
準備你的 App…
完成
~~~

### 尚未升格事項

以下仍待後續 Screen / High-fi Review：
- Progress bar 的實際位置、動畫、stage 數量與 duration；
- Tiffany Blue → Yellow 的正式 Design Token；
- Header 最終保留哪些 controls；
- Capsule 卡片 High-fi visual language；
- S01 Desktop / Mobile 的 final responsive composition。


## Future Share Modes Boundary

> Sync status：**SYNCED TO WORKING**。
> Sync targets：`working/functions/F05-SHARE-RESTORE.md`、`working/functions/F09-REALTIME-ROOM.md`、`working/UI-UX/overlays/O01-SHARE.md`。
> 狀態：WORKBENCH HISTORY — 後續以對應 Working 文件為 Current Truth。

- Phase 1 O01 / F05：只分享 App definition / Blueprint reference，不分享 Runtime input 或 current result。
- Future「分享結果」：需獨立 Function / contract，不能偷擴張 F05。
- Future「共同遊玩 / 即時共享狀態」：由 F09 Realtime Room方向承接；目前 Deferred。
- UI future direction可拆成：分享 App / 分享結果 / 開啟共同遊玩 Room，但 Phase 1 只落地「分享 App」。


## Runtime Global Loading + Timeout Function Delta

> Sync status：**WORKING DELTA CLOSED — MACHINE REGISTRIES SYNCED**。
> Sync targets：F00、F03、F12、S03、O05、Phase 1 Screen Inventory、recovery / evidence / acceptance registries。
> 狀態：MATERIAL FUNCTION DELTA — CLOSED 2026-09-22 / FORMAL REFRESH PENDING
>
> 來源：O05 Loading / Building / Hydration ④A Low-fi Review。
>
> 影響 Function：F00 Experience Shell + F03 Runtime Execution + F12 Humanized Recovery。
>
> 注意：此節已成為 Working Current Truth，但未改寫 Formal Spec；待 pre-Cursor Formal Spec Refresh一次同步。

### 1. Closed UX Contract

- 每個被 F03接受執行的 S03 Runtime interaction都建立唯一 operation token，並進 logical global processing state。
- 極快、同一 render frame完成的 interaction可以不 paint完整 loading frame；不得為了動畫人工延遲。
- 全站 progress採 Stage label + checkpoint-derived Progress %。
- checkpoint plan在 operation開始時固定；%只表示 completed / planned work checkpoints。
- 沒有可靠 checkpoints就只顯示 stage；只有 commit成立後才可顯示100%。

### 2. Operation / Timeout Contract

~~~text
STARTED → PROCESSING → COMMITTED
                     → TIMED_OUT
                     → FAILED
                     → CANCELLED
~~~

Soft Timeout：
- 是 `PROCESSING` 上的 non-terminal wait condition。
- committed store不動；progress停在最後真實 checkpoint。
- 顯示「還在處理，你的 App 和目前內容都還在。」

Hard Timeout：
- close token as `TIMED_OUT`。
- discard working transaction、staged effects與未 enqueue events。
- committed store保持原樣；不是把 state rollback回去。
- late / stale completion永遠不得 commit。
- integrity成立 → `F03-ERR-021 → F12-POL-011 → APP_CURRENT`。
- integrity無法證明 → `F03-ERR-018 → F12-POL-001 → terminal safe-state`。

### 3. Browser-first Enforcement

Phase 1不假設 `setTimeout()`可強制中斷卡住的 main thread。F03使用 monotonic deadline，並在 action-step、derived/rule recompute、capability return與 pre-commit guard point檢查。

若 trusted synchronous handler在 deadline後才返回，pre-commit仍拒絕 commit。真正無法返回的 trusted code由 Capability CI、code review與 resource guard防守；此 Delta不改變 Browser-first、0 LLM / 0 server normal Runtime path或 synchronous Action architecture。

### 4. Retry / Recovery Episode

- 同一 F12 recovery episode可以多次 Retry，但每次 Retry建立新的 F03 operation token。
- closed token永不復用。
- Retry click不等於 recovered；新 operation成功回 safe continuation後才標 `RECOVERED`。

### 5. Stable ID / Formal Refresh Handling

- 既有 `F00-AC-008`已進 Formal Spec，因此保留原 ID與原語意，不重寫。
- Working將它標為 superseded；pre-Cursor Formal Spec Refresh時 deprecated。
- 新增 F00-AC-029–032、F03-AC-030–036、F12-AC-029–031與對應 Test Contracts。
- 新增 `F03-ERR-021 RUNTIME_ACTION_TIMEOUT`與 `F12-POL-011 Runtime Timeout Preserve Last Known Good`。
- recovery / evidence / acceptance machine registries與 Markdown同 commit同步。

### 6. Next Gate

Function Delta已閉合。下一步是 Cross-Screen Consistency Review；Formal Spec與 Cursor implementation維持 HOLD。


---

## Session Closeout — 2026-09-21

### Today closed

- S04 Shared App Entry / Restore ④A Low-fi。
- S05 Refine / Remix Workspace ④A Low-fi。
- S06 Correction Compare ④A Low-fi。
- O01 Share Overlay ④A Low-fi。
- O02 Correction Composer ④A Low-fi。
- O03 Recovery Overlay ④A Low-fi。
- O04 Revert Confirmation ④A Low-fi。
- O05 Loading / Building / Hydration direction reviewed。
- Future Share Modes boundary同步到 F05/F09 Working。
- Runtime Global Loading + Timeout gap同步到 F00/F03/F12 Working。

### Next session first task

> **F00/F03 Runtime Loading + Timeout Function Delta Review**

Review目標：
1. F00 global processing/loading presentation semantics。
2. F03 operation token / checkpoints / soft timeout / hard timeout / stale completion。
3. F12 TIMEOUT → safe S03 recovery mapping。
4. Proposed Acceptance/Test seeds。
5. User批准 Working Function Delta後，再做 Cross-Screen Consistency Review。

### Formal Spec / Cursor rule

- Formal Spec **暫不修改**。
- Cursor implementation維持 HOLD。
- 先完成 UI/UX與 Cursor Build / Operating Model討論。
- 正式 Cursor development前，再執行一次短期 Formal Spec Refresh。

---

## Session Progress — 2026-09-22

### Closed

- F00 / F03 / F12 Runtime Loading + Timeout Function Delta完成 User Review並閉合為 Working Current Truth。
- S03 / O05移除 `FUNCTION_DELTA_PENDING`，改為 `FUNCTION_DELTA_CLOSED`。
- `F00-AC-008`保留 stable ID與原語意，Working標記 superseded；未來 Formal Refresh時 deprecated。
- 新增 F00 4項、F03 7項、F12 3項 Acceptance / Test Contracts。
- 新增 `F03-ERR-021`、`F12-POL-011`及 F03 operation / timeout evidence events。
- recovery / evidence / acceptance Working registries已同步。

### Next

> **Cross-Screen Consistency Review**

Formal Spec、Backlog / Sprint、Cursor implementation仍維持 HOLD；待 High-fi與 Cursor Build / Operating Model完成後，才執行 pre-Cursor Formal Spec Refresh。


---

## PENDING-FUNC-004 — F01 Creation Progress Checkpoint Contract

> Sync status：**CLOSED / WORKING CURRENT TRUTH APPROVED — FORMAL_REFRESH_PENDING**
>
> 來源：S02 Create Workspace ④B High-fi Review。
>
> 影響 Function：F01 Intent Compilation + F00 Experience Shell + O05 Loading / Building / Hydration presentation。
>
> Formal Spec：不動；待 Working Function Delta Review閉合後，於 pre-Cursor Formal Spec Refresh一次同步。

### 1. Problem

目前 S02 / O05 已批准：

- 有 reliable checkpoints → `Stage + checkpoint-derived Progress %`
- 沒有 reliable checkpoints → `Stage only`

但目前 F01 雖已有完整 lifecycle：

~~~text
ANALYZING
→ NEEDS_CLARIFICATION / READY_WITH_VISIBLE_ASSUMPTIONS / READY
→ COMPOSING
→ VALIDATING
→ VALIDATED
~~~

以及 API status / questions / assumptions / validated result，

**尚未正式定義 creation operation 的 canonical checkpoint plan、completed checkpoints、planned checkpoints，以及供 S02 計算 progress_percent 的 Function contract。**

因此 UI 已具備顯示 truthful % 的 presentation rule，但 F01 backend contract 尚未保證每次 creation operation都能提供可量測 work checkpoints。

### 2. Approved Direction

F01 Creation Progress 應補一層 NFF-owned checkpoint contract。

Candidate logical checkpoints：

~~~text
Intent analyzed
→ Policy evaluated
→ Clarification resolved
→ Capability checked
→ Blueprint composed
→ Blueprint validated
→ Runtime prepared
~~~

Consumer-facing stage仍使用人話，不暴露上述 internal checkpoint名稱。

實際 operation只納入該次流程真正需要的 checkpoints。

Example：

~~~text
Fast Path
planned:
- Intent analyzed
- Policy evaluated
- Capability checked
- Blueprint composed
- Blueprint validated
- Runtime prepared

Clarification Path
planned:
- Intent analyzed
- Policy evaluated
- Clarification resolved
- Capability checked
- Blueprint composed
- Blueprint validated
- Runtime prepared
~~~

### 3. Progress Calculation

Canonical rule：

~~~text
progress_percent
= completed_checkpoints / planned_checkpoints * 100
~~~

Rules：

- % 代表 **work completion**，不是 time remaining。
- checkpoint plan必須由 Function truth建立，不由 UI自行估算。
- UI不得使用 elapsed time、animation timer或provider latency推算 %。
- 已完成 checkpoint才能推進 numerator。
- 某 checkpoint等待時，%停在最後真實完成值。
- 100%只在 target ready condition成立後。
- operation若沒有 reliable checkpoint plan，presentation退回 Stage only。

最終 presentation只有兩條：

~~~text
reliable checkpoints
→ Stage + checkpoint-derived Progress %

no reliable checkpoints
→ Stage only
~~~

不存在「沒有 reliable checkpoints但仍顯示 %」的第三條規則。

### 4. Ownership Boundary

F01應擁有 creation semantic/compiler lifecycle checkpoints。

F03應繼續擁有 Runtime / hydration execution lifecycle checkpoints。

F00 / O05只負責：

- 將 Function checkpoint projection成 consumer stage。
- 顯示 completed / planned計算出的 %。
- 不自行推進 checkpoint。
- 不自行猜 planned work。
- 不把 provider等待時間當 work completion。

### 5. Clarification Batching — Confirmed

Clarification UX / Function既有方向確認如下：

~~~text
每輪最多 3 個最高優先 material questions
→ User回答
→ merge answers
→ re-run Clarification Policy
→ 若仍有必要問題，再出下一輪最多 3 題
→ 持續直到所有 required / material unknowns resolved
~~~

Question priority沿用 F01既有 ranking：

~~~text
Safety / Money / Permission
> Execution Blocker
> High Outcome Divergence
> Core Business Rule
> Secondary Preference
> Cosmetic
~~~

Important：

- 不是把所有問題固定切成 3 題一組後機械式問完。
- 每輪答案都可能讓後續 ambiguity消失、產生新問題，或改變 priority。
- answered question不重問，除非 upstream fact changed。
- Clarification完成條件不是「問完原始 question list」，而是重新 evaluation後不再有 blocking / material unknown。

此項是對既有 F01 contract的 UX interpretation確認，**目前不需要新增 Function Delta**。

### 6. Next Function Review

後續需獨立執行：

> **F01 Creation Progress Checkpoint Function Delta Review**

Review至少確認：

1. canonical checkpoint schema。
2. operation開始時 planned checkpoint plan何時凍結／何時可合法重算。
3. clarification新增 round時 checkpoint plan如何處理。
4. F01 → F00/S02 的 progress projection interface。
5. F01 / F03 handoff時 Runtime prepared checkpoint ownership。
6. cancellation / retry / failure時 checkpoint lifecycle。
7. Acceptance / Test seeds。

在此 Delta閉合前：
- S02 High-fi可以設計 presentation位置與 hierarchy；
- 但不得把未定義的 exact backend progress payload當成已完成 implementation contract。


### 7. Deferred Decision — 2026-09-22

User confirmed：

- F01 Creation Progress Delta remains **OPEN**。
- Do **not** update `working/functions/F01-INTENT-COMPILATION.md` yet。
- Do **not** add F01 Acceptance / Test / Evidence contract yet。
- First perform **O05 High-fi / Processing Review** to define the cross-flow progress model for Create / Refine / Remix / Correction / Restore / Share / Retry / Revert。
- After O05 review, return to each semantic owner (F01 / F05 / F06 / F16 / F03 etc.) to add only the Function-specific checkpoint contract actually needed。
- Formal Spec remains frozen。


### 8. Function Delta Closure — 2026-09-23

O05 High-fi Step 1 已先鎖定 shared processing rule；其後已完成 F01 Creation Progress Function Delta Review。

Closed outcome：

1. F01 CREATE 固定六個 compiler checkpoints。
2. Clarification / Assumption waiting 不新增 denominator、不推進 progress。
3. material Intent edit 開始新的 logical progress operation。
4. CREATE API success response提供 machine-readable progress snapshot；Phase 1不新增 polling / SSE / WebSocket。
5. F00以 F01六個 checkpoints + F03 APP_READY 組成 S02固定七 milestone composite progress。
6. F01 VALIDATED只到 composite 6/7（85%）；F03 READY才可100%。
7. network retry不重複 checkpoint；User-triggered retry建立新 logical progress operation。
8. 新增 F01-AC-025–029、F00-AC-033–035與對應 Tests。
9. 不新增 DB schema。
10. 不新增 Evidence Event ID；沿用既有 F01 lifecycle events。
11. Formal Spec仍 frozen，待 pre-Cursor Refresh promotion。

`PENDING-FUNC-004` 至此轉為 **CLOSED / FORMAL_REFRESH_PENDING**。



---

## 新主題：LLM-generated App Reliability — Model Proposal ≠ READY Truth

> 來源：2026-09-23 S04 / S05 artifact pipeline 事故檢討。
>
> 狀態：WORKING DESIGN INPUT。Formal Spec 維持 freeze；優先帶入後續 **F00 / F03 Runtime Loading + Timeout Function Delta Review**。

### 核心問題

本次 artifact pipeline 暴露一個對 NodeFF Runtime 同樣重要的風險：

> **「模型說完成」不等於「系統真的完成」。**

LLM 可以產生合理-looking output，也可能在工具失敗、validation 不完整、artifact 不可用時仍誤判為 success。

因此 NodeFF 不可把 LLM 自己的 completion / confidence 當成 App READY truth。

### 核心原則

> **LLM = Proposal Engine，不是 Truth Engine。**

LLM 的責任是：

- 理解 Intent；
- 提出 LegoSpec / Blueprint；
- 在允許範圍內做 semantic refinement；
- 必要時提出 recovery / clarification 建議。

LLM 不得單方面宣告：

- Blueprint 合法；
- Runtime 可執行；
- Capability 可用；
- App 已 READY；
- 使用者要求已真正完成。

### 建議 Runtime Gate

~~~text
Prompt / Intent
→ LLM proposes Blueprint
→ Schema Validate
→ Semantic / Reference Validate
→ Policy / Capability Validate
→ Dry-run / Runtime Validate
→ Acceptance / Health Check
→ READY
~~~

只有 deterministic / independently verifiable gate 全部通過，才可進 READY。

### 五個不可妥協 Guardrails

1. **Bounded Retry**
   - 相同 failure path 只允許有限次 retry。
   - 不允許 LLM 無限自我修正／無限工具重試。

2. **Hard Timeout**
   - Compiler / Hydration / Runtime / External capability 必須有 timeout budget。
   - Timeout 後進 Recovery State，不繼續「再等等」。

3. **Deterministic Validation**
   - JSON Schema / Zod。
   - Component Registry reference。
   - state / binding / action reference。
   - capability / permission / compatibility。
   - resource / cost / loop guard。
   - 以上由可重現程式規則判定，不由 LLM 自評。

4. **Independent READY Gate**
   - Model output complete ≠ App READY。
   - 至少需通過 Contract + Runtime mount / hydration + required health checks。

5. **Observable Failure Reason**
   - Internal system保留可診斷 failure reason / checkpoint。
   - Consumer只看到 humanized recovery message + preserved context + next action。
   - 不因錯誤而假裝成功。

### Success Truth

~~~text
LLM: "完成"
      ↓
不算 READY

Schema PASS
+ Contract PASS
+ Capability PASS
+ Runtime / Hydration PASS
+ Required Interaction / Health PASS
      ↓
READY
~~~

### 對現有四層的暫時影響

此項先不重構 Layers，但後續 Review 必須確認：

- Layer 2 Semantic Compiler：只提出 Blueprint / semantic proposal。
- Layer 3 Contract：負責 deterministic contract validation / enforceable truth。
- Layer 4 Runtime：負責真正 execution / hydration / runtime health。
- Experience Shell / O03 / O05：負責 timeout、checkpoint、recovery presentation。

### 待 Review

後續 **F00 / F03 Runtime Loading + Timeout Function Delta Review** 至少要明確決定：

- retry count / retry eligibility；
- compiler timeout；
- hydration timeout；
- runtime health check；
- READY gate；
- failure checkpoint；
- preserved context；
- consumer recovery action。

> Working principle：**Never trust model-declared success. Trust independently verified state.**


---

## 中期必做：Layer 4 升級為 App Execution & Runtime Layer

> 狀態：**MID-TERM MUST IMPLEMENT**
>
> 目的：避免 NodeFF 永遠停留在「只生成 UI」；中期必須支援真正可運作的 full-stack Micro-App。
>
> Formal Spec 目前仍 freeze；本節先作 Working Architecture Direction。

### 為什麼要升級

目前 Layer 4 若只被理解為：

> React Frontend Renderer

則不足以支撐 NodeFF 的核心願景：

> **意圖就是 App。**

真正的 App 中期一定會需要：

- 儲存資料；
- API call；
- Database；
- Workflow；
- 定時任務；
- 外部 Capability；
- 多人狀態；
- Auth / Permission；
- AI call；
- server-side calculation。

因此四層架構本身可以保留，但 Layer 4 的責任必須擴大。

### 中期 Layer 4 定義

> **Layer 4 — App Execution & Runtime Layer**

建議內部分成：

~~~text
4A UI Runtime
React / Components / Interaction

4B Logic Runtime
Actions / Conditions / Workflow / Computation

4C Data Runtime
Local state / Persistence / DB

4D Capability Runtime
API / AI / Map / Payment / External services
~~~

### Layer 2 與 Layer 4 的分工

Layer 2 的 LLM 是 **App Builder / Semantic Compiler**，負責把 User Intent 轉成更完整的 App Definition。

中期 Blueprint 不只描述 UI，還要能描述：

~~~text
畫面
+ 狀態
+ 邏輯
+ workflow
+ data binding
+ capability calls
~~~

Layer 3 必須對上述 App Definition 做 deterministic validation。

Layer 4 只執行已通過 Contract 的內容。

### 重要原則

> **Build App 要 LLM；Run App 不應依賴 LLM 才能成立。**

正常流程：

~~~text
User Intent
→ Layer 2 LLM builds / proposes App Blueprint
→ Layer 3 validates
→ Layer 4 executes
→ App
~~~

只有當某個 App 的功能本身需要 AI，例如摘要、生成、分類等，Layer 4 才透過受控 AI Capability 呼叫 LLM。

### 安全邊界

中期即使支援更完整 App，也維持：

- LLM 不直接生成並執行任意 backend code；
- LLM 只能使用 NFF 定義好的 declarative contract；
- API / DB / AI / Payment / external service 必須走受控 Capability；
- Layer 3 驗證 schema / permission / capability / resource / compatibility；
- Layer 4 不自行猜測 semantic intent。

### 中期目標

使用者感受到：

> **「NodeFF 幫我做了一個完整 App。」**

但底層仍然是：

> **LLM 產生 App Definition → Contract 驗證 → Runtime 執行**

而不是：

> LLM 直接亂寫任意前後端程式並執行。

### Architecture Review Trigger

中期 Architecture Review 時，必須正式檢查：

1. Layer 2 Blueprint 是否足以描述 full-stack intent；
2. Layer 3 Contract 是否足以驗證 workflow / data / capability；
3. Layer 4 是否已從 Frontend Renderer 升級為 App Execution Runtime；
4. 4A–4D 的責任是否清楚；
5. 是否仍能維持 No Arbitrary Code Execution 原則。



---

## 中期必做：Layer 3 升級為 Full App Contract & Deterministic Validation Layer

> 狀態：**MID-TERM MUST IMPLEMENT**
>
> Trigger：與「Layer 4 — App Execution & Runtime Layer」升級同步設計、同步驗收。
>
> 原因：如果 Layer 4 中期開始支援 Logic / Data / Capability，但 Layer 3 仍只驗 UI Schema，NodeFF 會失去最重要的安全與可靠性邊界。

### 核心結論

> **Layer 4 能執行什麼，Layer 3 就必須能在執行前驗證什麼。**

因此 Layer 3 不應只被理解為 LegoSpec UI JSON Schema。

中期應升級為：

> **Layer 3 — Full App Contract & Deterministic Validation Layer**

### Layer 3 中期驗證範圍

#### 3A — UI Contract Validation

- component type 是否存在；
- props 型別是否正確；
- layout nesting 是否合法；
- bind target 是否存在；
- event / action reference 是否有效；
- responsive / required accessibility contract 是否符合最低要求。

#### 3B — Logic Contract Validation

- action / condition / workflow graph 是否合法；
- state reference 是否存在；
- input / output type 是否匹配；
- workflow 是否存在 impossible / invalid transition；
- loop / recursion 是否超過允許範圍；
- side effect 是否只有在允許的 action type 中出現。

#### 3C — Data Contract Validation

- data source / collection / entity reference 是否合法；
- schema / field type 是否匹配；
- read / write scope 是否允許；
- persistence policy 是否明確；
- anonymous / account / ownership requirement 是否符合；
- 不允許 Blueprint 任意指定未註冊 DB / table / raw query。

#### 3D — Capability Contract Validation

- API / AI / Map / Payment / External Service capability 是否已在 Registry；
- capability version 是否相容；
- required permission / entitlement 是否具備；
- input / output contract 是否符合；
- cost / quota / latency class 是否在允許範圍；
- capability unavailable 時 degradation / recovery path 是否存在。

#### 3E — Runtime Safety / Resource Validation

- hard timeout / execution budget；
- retry limit；
- concurrency limit；
- payload / state size limit；
- network / external call limit；
- no arbitrary code execution；
- prohibited side effect / unsupported operation 必須 fail closed。

### Deterministic Validation 原則

Layer 3 的核心判定應由可重現程式規則完成，不交給 LLM 自評。

可包含：JSON Schema / Zod、Registry lookup、Type checking、Reference resolution、Permission / entitlement rules、Resource / timeout policy、Workflow graph validation、Capability compatibility validation。

同一 Blueprint + 同一 Registry / Policy version 應得到可重現的 PASS / FAIL 結果。

### 與 L2 / L4 的邊界

Layer 2 LLM = propose App Definition。

Layer 3 Deterministic Contract = decide whether the Definition is valid and allowed。

Layer 4 Runtime = execute only validated Definition。

LLM 可以幫忙修正被拒絕的 Blueprint，但：

> **LLM 不能覆寫 Layer 3 的 PASS / FAIL。**

### READY Gate

中期 Full App READY 至少應成立於：

UI Contract PASS + Logic Contract PASS + Data Contract PASS + Capability Contract PASS + Runtime Safety PASS + Hydration / Mount / Required Health Check PASS → READY。

任何一項不通過 → NOT READY → Recovery / Clarification / Regeneration。

不得因 LLM 宣稱「完成」而跳過驗證。

### 與 Layer 4 的共同設計規則

Layer 3 / Layer 4 必須成對演進：L4 新增可執行能力 → 先有 L3 Contract / Validation → 再允許 Blueprint 使用。

不得先讓 Runtime 能執行，之後才補 Validator。

> **No Runtime Capability Without Contract Coverage.**

### 中期 Architecture Acceptance

中期正式升級前至少確認：

1. L4 4A–4D 每個 executable primitive 都有對應 L3 contract；
2. 每個 Data / Capability side effect 都可在執行前被驗證；
3. 不存在「LLM 可以繞過 Validator 直接叫 Runtime」的路徑；
4. Registry / Policy / Contract 都有 versioning；
5. Validation failure 有 machine-readable reason；
6. Consumer failure 仍轉成 humanized Recovery UX；
7. READY 由 independent gate 判定，不由 LLM 自宣告。

### 與 Layer 4 的中期共同目標

> **Layer 2 擴大生成能力，Layer 3 擴大可驗證範圍，Layer 4 擴大可執行能力。**

三者必須同步：L2 can describe ≤ L3 can validate ≤ L4 can safely execute。

若 L2 生成超出 L3 / L4 能力，必須降級、clarify 或拒絕，不能產生「看似成功、實際不可用」的 App。
