# NodeFF 應用程式架構

> 狀態：Working。除非依 NodeFF SSOT 流程正式升格，否則不具權威性。

## 1. 系統定位

NodeFF 是一套 **Intent-to-Interactive-App 協定與 Runtime**。

使用者以自然語言描述意圖；NodeFF 將該意圖編譯成經驗證的宣告式 Blueprint，再由可信任的瀏覽器 Runtime 執行為互動式 Micro-App。

```text
Intent
  ↓
Semantic Compiler
  ↓
Validated LegoSpec Blueprint
  ↓
Universal Lego Player
  ↓
Interactive Micro-App
```

NodeFF 不會為每一個使用者請求生成並部署一套新的 App bundle。

> **NFF 部署的是 Runtime，不是每一個生成出來的 App。**

LLM 主要扮演**建立／微調階段的語意編譯器**。對既有 Blueprint 的一般互動，應盡可能在本地端以確定性方式執行。

---

## 2. 產品執行循環

```text
Intent
 → Compile
 → Validate
 → Execute
 → Interact
 → Share
 → Remix / Refine
 → Reuse
```

對已有效的 Blueprint 版本：

- 開啟時不應要求 LLM 重新編譯；
- 一般輸入、Slider、骰子、計分與規則互動不應呼叫 LLM；
- 使用者提出語意上的修改時，可再次呼叫 Semantic Compiler；
- 只有明確宣告的 runtime-AI capability 才可呼叫經核准的外部 AI 能力。

核心原則：

> **Compile Once → Reuse Many → Execute Locally**

---

## 3. 四層責任模型

### Layer 1 — Ingestion & Routing

負責：
- 接收請求；
- Tier／安全／政策閘門；
- Normalization；
- exact／canonical-intent 查找；
- cache／registry 路由；
- 請求限制與 dispatch。

不負責：
- 自由文字的語意理解；
- 發明業務規則；
- 生成 UI 語意。

### Layer 2 — Semantic Compiler

負責：
- 自然語言理解；
- Intent decomposition；
- 必要時進行 compiler-level archetype 選擇；
- 從 Capability Registry 選擇能力；
- 設計 State／Action／Rule／View／Effect；
- 抽取與標記假設；
- 產生結構化 Candidate；
- validation failure 後的有界修復；
- 使用者更正後的語意微調。

不負責：
- 生成任意 JavaScript；
- 執行 Browser Runtime；
- 隱藏式語意降級。

Archetype 是 Compiler 的輔助抽象，不是 Player 裡的 keyword router。

### Layer 3 — LegoSpec Contract

負責 Compiler 與 Runtime 之間的版本化資料合約。

合約描述：
- state；
- layout／component instance；
- actions 與 state transition；
- rules；
- effects；
- presets／patches；
- assumptions／provenance；
- capability references；
- compatibility／version metadata；
- 必要時的 degradation／notice 狀態。

Validation 不能只檢查 JSON 外型，至少需要涵蓋：

1. schema／type 正確性；
2. state binding 與 cross-reference 正確性；
3. Rule AST／operator 正確性；
4. capability allowlist 正確性；
5. patch path／operation 正確性；
6. version compatibility；
7. size／complexity／resource limits；
8. security／policy constraints；
9. 已定義時的 semantic／capability quality gate。

> **Schema Valid ≠ Semantic Correct。**

結構完全合法的 Blueprint，仍然可能解錯問題。

### Layer 4 — Universal Lego Player

負責：
- hydration；
- Component Registry／Factory；
- reactive Instance state；
- 經核准的 state transition；
- Rule VM 執行；
- 有界的 effect；
- local error isolation；
- snapshot／share restoration；
- optional realtime binding。

不負責：
- 自然語言分類；
- Regex／keyword intent routing；
- 推測業務語意；
- 發明公式；
- 執行任意程式碼；
- 靜默式 semantic fallback。

Player 是通用執行器，不是第二個 Semantic Compiler。

---

## 4. 宣告式執行模型

核心 wiring model：

```text
Action
  ↓
State Transition
  ↓
Rule / Capability
  ↓
View
  ↓
Effect
```

例如：

```text
DiceRoller
  ↓
state.dice
  ↓
approved Rule AST
  ↓
StatCard / LeaderBoard
  ↓
condition → Confetti
```

Compiler 負責產生 wiring Blueprint；Player 只執行已核准的語意。

---

## 5. Capability Registry

Capability Registry 是「模型創造力」與「可信任執行」之間的核心邊界。

```text
Capability Registry
  ├─ Compiler capability metadata
  ├─ Layer 3 schema constraints
  ├─ Layer 4 component/function registry
  ├─ Compatibility metadata
  ├─ Tests
  └─ Documentation
```

同一份 capability 定義不得在多個地方各自人工維護。Registry 應成為來源，Compiler context、Runtime registration 與 validation constraints 都由它衍生。

每個 capability 最終應定義：
- name／type；
- version；
- props schema；
- state／binding contract；
- inputs／outputs；
- actions／events；
- 可使用的 rule／operator dependencies；
- fallback behavior；
- security classification；
- runtime compatibility。

新增 primitive 是受控的平台變更，不是只修改 System Prompt。

---

## 6. 初始 Rich Primitive 能力面

目前候選 catalog：

### Input Controls
1. `NumberInput`
2. `TextInput`
3. `SelectChoice`
4. `ToggleSwitch`

### Data & Visualization
5. `StatCard`
6. `DataTable`
7. `ChartVisualizer`

### Rich Media & Interaction
8. `Model3DViewer`
9. `LottieAnimator`
10. `WheelSpinner`
11. `DiceRoller`
12. `VideoPlayer`
13. `ConfettiTrigger`

### Layout & Composition
14. `Container`
15. `Repeater`

這 15 個是初始候選能力面，不是永久上限。

新增 primitive 至少必須同時具備：
- contract definition；
- runtime implementation；
- validation；
- security policy；
- tests；
- version／compatibility metadata。

---

## 7. Rule 表示方式

Runtime 必須避開兩個極端：

1. 將每一個 domain rule 都硬編進 Universal Player；
2. 允許 Compiler 產生不受控的 expression string 或程式碼。

目前較佳方向：

> **Typed declarative Rule AST + 經審核的通用 operator library。**

候選 operator：
- arithmetic；
- comparison；
- boolean logic；
- `IF`；
- `SUM`；
- `MIN`；
- `MAX`；
- `COUNT`；
- `UNIQUE`；
- `COUNT_MATCHES`；
- 有界的 normalization；
- 在安全規格下定義的有界 collection transforms。

概念範例：

```json
{
  "op": "SUM",
  "args": [
    {
      "op": "UNIQUE",
      "args": [{ "ref": "state.dice" }]
    }
  ]
}
```

優點：
- static reference checking；
- operator allowlisting；
- dependency analysis；
- resource limits；
- deterministic serialization；
- migration／versioning；
- auditability。

只有當通用 Rule grammar 無法安全且合理表達某項行為時，才考慮將 domain-specific function 做成明確、版本化的 Capability Registry extension。它不能偷偷成為 Universal Player 內的業務邏輯。

---

## 8. State Model

NodeFF 將以下四個概念視為第一級物件。

### Blueprint

不可變、可重用的宣告式定義，描述：
- UI composition；
- state schema／defaults；
- actions；
- rules；
- effects；
- capability dependencies。

### Instance

某次實際執行的當前現實：
- 使用者輸入值；
- 當前遊戲／工具狀態；
- optional room／session state；
- runtime progress。

### Context

由一個 Micro-App 明確傳給下一個 Micro-App、且受 Schema 控制的輸出。

候選欄位：
- `summary`
- `rawText`
- `structuredData`

### Delta

對可變 Instance state 套用的已驗證變更；或在語意 refinement 時，用來產生新 Blueprint candidate／revision 的變更。

> **Blueprint 定義可重用能力；Instance 定義當前現實；Context 連接 Micro-App；Delta 改變狀態或產生新 revision。**

---

## 9. State Binding

互動元件將 typed update 寫入 Instance state。

```text
User Action
 → validated state update
 → dependency-aware rule evaluation
 → affected views/effects
```

Binding 必須驗證：
- path 是否存在；
- type 是否符合；
- 是否可變；
- 是否位於允許寫入的 scope。

Component 不得隱藏無法由 contract 表示的重要 business state。

Runtime state patch 不得修改受保護的 Blueprint metadata 或 capability declaration。

---

## 10. 假設與模糊語意

模糊的人類意圖應轉成**可檢視、可編輯的模型**，而不是藏在模型內部的猜測。

候選 provenance：
- `user_provided`
- `compiler_assumption`
- `template_default`
- `external_capability`

例如「20 人公司聚餐依職級分帳」，Compiler 可以建立可編輯的群組、人數、權重與 scenario；但自動產生的職級權重只是 assumption，不是事實，更不是「公平」的判決。

規則：

> **Compiler 產生的假設必須可見、可編輯，而且要與使用者提供的事實清楚區分。**

對文化差異、爭議性或 domain-sensitive 規則，LLM 的 world knowledge 不具權威性。Compiler 必須揭露採用的 rule variant，或要求 refinement。

---

## 11. 語意正確性與 Failure Model

主要 failure class：

- `GENERATION_FAILED`
- `VALIDATION_FAILED`
- `SEMANTIC_MISMATCH`
- `UNSUPPORTED_SEMANTICS`
- `RUNTIME_COMPONENT_ERROR`
- `BLUEPRINT_DEGRADED`

畫面成功 render，不代表使用者任務成功。

> **render_success ≠ task_success**

Recovery model：

```text
Candidate
 → Contract Validation
 → Capability/Security Validation
 → Semantic Quality Gate
 → Trusted Blueprint

Failure
 ├─ bounded compiler repair
 ├─ targeted user refinement
 ├─ transparent degradation
 └─ unsupported response
```

Runtime failure 應在本地隔離並記錄，不能因此授權 Player 重新解讀原始 intent。

---

## 12. 從 Failure Cases 萃取出的設計法則

除非透過 SSOT change control 明確取代，以下視為持續有效的設計限制。

### 禁止 Client-Side Semantic Guessing

Player 不得使用以下方式推測開放式 intent：
- Regex；
- 抽取數字後自行猜公式；
- keyword routing；
- 不斷膨脹的 `if/else` heuristic；
- 將不相關 Blueprint 改標題後重用。

失敗模式：

```text
Prompt → frontend heuristic → guessed logic → plausible but wrong app
```

禁止。

正確路徑：

```text
Prompt → Semantic Compiler → validated contract → deterministic Player
```

### Dynamic Form 是 Rendering Fallback，不是 Meaning Fallback

Generic form 可以呈現已知的 typed semantics，但不得憑空發明 domain facts、公式、選項或 transformation。

> **未知 UI 可以安全降級；未知語意不能被捏造。**

### Validation 是多層的

Zod 等 runtime schema 可以驗證 shape 與 cross-field invariant，但不能證明 semantic correctness。

### Contract 只能有一個定義來源

同一份 contract 不得同時維護兩套可獨立修改的 TypeScript interface 與 runtime schema。應由單一來源產生／infer 次級表示。

### Safe Interpreter 仍是安全邊界

「沒有使用 `eval`」不等於安全。Rule VM 必須明確限制 operator、reference、complexity 與 resource usage。

---

## 13. 透明降級

當需求超出能力範圍：

1. 保留原始 intent；
2. 判斷現有 approved primitives 是否能維持核心語意；
3. 只有在任務仍實質等價時才降級表現方式；
4. material degradation 必須顯示明確 notice；
5. 無法維持核心語意時，回傳 unsupported／refinement 狀態。

Layer 2 決定 degradation contract；Layer 3 驗證；Layer 4 只負責呈現。

UX 原則：

> **不中斷流程，但不隱瞞錯誤。**

禁止 silent substitution。

---

## 14. 產品能力邊界

強項：
- 離散、回合制互動；
- 骰子、轉盤、卡牌、計時器、投票、排行榜；
- 算術與權重分配；
- 互動式 calculator；
- decision model；
- 臨時社交／群組協作；
- 經核准的 media／visualization primitive。

除非另有專門且已核准的 capability，核心邊界之外：
- 任意 60fps 連續物理；
- 無限制 Canvas／custom rendering；
- 任意 generated function／script；
- 無界 RPG／agent state machine；
- 無限制 OS／system access。

限制不是「JSON 做不到」，而是 **Trusted Capability Registry 與 Runtime 邊界刻意不提供這些能力**。

受控的 `Model3DViewer` 不代表支援通用 3D game engine。

---

## 15. 分享、持久化與協作

### Portable Snapshot

適用於小型、非敏感資料：

```text
Blueprint/Instance
 → canonicalize
 → compress
 → URL fragment
 → decode
 → validate
 → hydrate
```

規則：
- URL Hash 是 transport，不是 database；
- compression 不是 encryption；
- sensitive data 預設不得進 URL；
- 必須有 size／resource limits；
- persistence 應使用 explicit share 或 debounce／batch，而不是每次 state mutation 都寫入。

### Ephemeral Live Room

```text
Blueprint Reference
 + Room ID
 + Mutable Instance State
 + Validated Deltas
```

Realtime state 絕不能直接修改 immutable Blueprint content。

### Durable Save

持久化需分離：
- immutable Blueprint body；
- logical Blueprint identity；
- revision／lineage；
- user ownership／save pointer；
- 只有產品行為需要時才保存 persistent Instance state。

修改 immutable Blueprint 內容時，產生新的 content identity／revision。

---

## 16. Blueprint Identity 與 Content Addressing

經 canonicalize 且 validation 通過的 Blueprint 可以使用 content addressing：

```text
Canonical Blueprint
 → Content Hash
 → Common Pool
```

識別需分離：
- `content_id/hash`：精確 immutable content identity；
- `blueprint_id`：可選的穩定 logical identity；
- lineage／revision metadata；
- `instance_id`：實際執行 state。

Hash identity 不代表：
- authorship；
- ownership；
- trust；
- safety；
- authorization。

Personal state 不得被默默併入 global Blueprint body 進行 dedupe。

---

## 17. Cache 語意

必須分清：

### Prompt / Canonical-Intent Lookup
用來發現可能可重用的 Blueprint candidate。

### Blueprint Content Hash
用於 immutable content 的精確 identity。

Normalized Prompt hash 只能當 exact-cache optimization，不代表 semantic equivalence。

可重用 artifact 必須綁定：
- schema version；
- Registry version；
- Runtime compatibility；
- policy／security status；
- quality／trust status。

Schema-valid 但 semantic-wrong 的 Blueprint 不得進入或繼續保留在 trusted Common Pool。

---

## 18. Determinism 與 Replay

相同 Blueprint content 不代表一定得到完全相同的執行結果。

精確 replay 可能需要：
- Blueprint hash／version；
- Runtime version；
- capability versions；
- Rule VM version；
- initial Instance state；
- RNG seed／outcomes；
- action／delta log；
- external-data snapshot／version。

Dice／Wheel 等 randomness 必須由 trusted runtime action 產生，不得使用由模型生成的 `Math.random()` 程式碼。

---

## 19. App-to-App Composition

Composition 必須明確：

```text
App A Result
 → user-selected next capability
 → approved Context payload
 → App B hydration
```

不得進行隱藏式 cross-app data transfer。

Context 必須：
- schema-controlled；
- permission-aware；
- privacy-aware；
- 由使用者或明確產品流程選擇。

---

## 20. Identity 與 Progressive Authentication

Consumer：
- 可在不強制建立帳號的情況下開啟／使用 shared Micro-App。

Creator：
- 可在可行時匿名建立／分享 ephemeral artifact。

只有當 durable value 需要身份時才要求 authentication：
- ownership；
- permanent editing；
- history；
- publishing；
- paid quota；
- monetization；
- cross-device persistence。

匿名 continuity 優先使用 random first-party `anonymous_id`，不預設使用 device fingerprinting。

Anonymous-to-account claim 需要 ownership proof／claim token／replay protection。擁有分享 URL 不等於擁有 ownership。

---

## 21. Heavy Capability 邊界

NodeFF core 是 lightweight control plane。

Heavy work 委派給：
- browser Web Workers／WASM；
- 專業 external API／worker；
- external durable store。

Micro-App 可以控制參數、顯示進度與呈現結果，但 heavy operation 在其他執行面完成。

長期 chat／social-network 不屬於 NFF core。Ephemeral room chat 可作為受限 realtime capability。

---

## 22. 實作治理

Architecture／Specification 負責決定：
- contract definition；
- security boundaries；
- Capability Registry；
- rule grammar；
- state ownership；
- framework／dependency constraints；
- acceptance criteria。

Cursor 執行已核准的決策。

> **Cursor 不得默默引入新的架構決策。**

實作不得建立：
- 第二個 semantic router；
- 平行 contract；
- 第二套 runtime；
- 任意 execution path；
- Player 內隱藏的 business logic。

---

## 23. 候選技術

目前皆為候選，尚未鎖定：
- React；
- Tailwind／shadcn；
- Zod；
- Zustand 或 reducer-based state；
- Vercel AI SDK 或透過 NFF adapter 的 provider SDK；
- PartyKit 或其他 realtime provider；
- Supabase／Cloudflare／其他 persistence；
- typed Rule AST／VM；
- `expr-eval` 僅在 threat-model 驗證通過後才可能採用；
- `lz-string` 或其他 snapshot compression。

更換 vendor 不得改變核心 contract semantics。

---

## 24. 候選 Build Order

1. Capability Registry contract
2. Layer 3 schema 與 versioning
3. state transition model
4. Rule AST + Rule VM
5. 最小 Universal Player
6. 初始 primitive set
7. validation／security gates
8. Semantic Compiler
9. snapshot／share
10. CAS／registry／cache
11. realtime
12. progressive auth／durable persistence
13. telemetry／reliability loop

每個 implementation stage 擴張前，都必須有明確 acceptance tests。

---

## 25. 尚未決定

- Rule AST vs restricted expression representation；
- 最終初始 primitive set 與 props；
- Registry source format；
- Blueprint version／compatibility policy；
- CAS canonicalization／digest policy；
- semantic quality／admission gate；
- retry／repair budget；
- snapshot size threshold；
- realtime protocol／provider；
- runtime-AI Tier boundary；
- external media policy；
- anonymous-to-owner claim protocol。

---

## 26. 不可違反的 Guardrails

1. 不允許任意 generated JavaScript。
2. 不允許 `eval()` 或 `new Function()`。
3. Player 不得推測 free-form intent。
4. Schema validity 不等於 semantic correctness。
5. Generic fallback 不得捏造未知語意。
6. Blueprint、Instance、Context、Delta 必須分離。
7. URL Hash 是 transport，不是 DB。
8. LocalStorage 是 local recovery convenience，不是 authoritative persistence。
9. Sensitive state 預設不得放入 URL。
10. 既有 valid Blueprint 預設以 0 次 LLM call 執行。
11. Heavy work 不進入核心 Runtime。
12. Cache 不得繞過 compatibility／security／quality check。
13. Degradation 必須透明。
14. Runtime core 必須維持 generic。
15. Architecture 以 GitHub SSOT／Brain 為準，不依賴對話記憶。
