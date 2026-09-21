# F00 — Experience Shell / 靈感精靈

> 狀態：WORKING_BASELINE
>
> Canonical Role：Phase 1 Consumer Experience Shell、Creation UX、Clarification / Assumption UX、Runtime Frame、Result Feedback Entry、Share / Remix / Recovery Entry 的 Working Current Truth。
>
> 上游：APP-ARCHITECTURE、F01 Intent Compilation、F03 Runtime、F04 Capability Registry、DESIGN-TO-DELIVERY。
>
> 主要下游 / collaborators：F05 Share / Restore、F06 Remix / Refine、F07 Evidence、F12 Humanized Recovery、F16 Result Correction。
>
> F00 不擁有 Intent semantic truth、Blueprint validation、Runtime semantics、Recovery policy 或 Correction semantics；它只把各 Function 的 Current Truth 轉成一致、可理解、可操作的 Consumer UX。

# 1. Purpose / User Outcome

User Outcome：

> User 打開 NodeFF 後，不需要理解 Prompt Engineering、Blueprint、Capability、Validation 或 Runtime，就能從靈感開始、說出需求、回答必要問題、立即得到可玩的 App、分享、Remix、修正結果，且失敗時不丟掉已做的事情。

Phase 1 UX thesis：

~~~text
See inspiration
→ say what you want
→ answer only necessary questions
→ see assumptions before they matter
→ build App
→ use App immediately
→ share / remix / correct
→ recover without restarting
~~~

# 2. Scope / Non-Scope

F00 Phase 1 負責：

- app shell
- Inspiration Capsules
- prompt composer
- Ghost Text
- progressive refinement entry
- creation state machine
- clarification UI state
- visible assumption UI state
- build / compile progress presentation
- runtime frame / chrome
- result feedback entry
- correction comparison entry
- share / remix entry
- humanized recovery presentation
- preservation of user draft / visible context
- loading / cancel / retry behavior
- responsive / keyboard / accessibility baseline
- UX telemetry seed
- acceptance / tests

F00 不負責：

- F01 Clarification Policy decision
- F01 Prompt A / Prompt B
- F02 validation semantics
- F03 action / state / timer runtime semantics
- F05 share persistence contract
- F06 semantic delta algorithm
- F12 technical error classification / retry policy
- F16 correction compiler semantics
- Account / ownership UX
- Marketplace
- realtime multiplayer UI

# 3. UX Principles

## F00-UX-001 — First Value Before Registration

User 在得到第一個可用 App 前，不要求 account。

## F00-UX-002 — Progressive Disclosure

只在需要時顯示下一層複雜度。

User 不需要看到：

~~~text
schema_version
registry_version
validation stage
capability IDs
HTTP status
provider name
runtime internals
~~~

除非是 internal/debug surface。

## F00-UX-003 — Preserve Context

任何 recoverable failure 預設保留：

- prompt draft
- clarification answers
- accepted assumptions
- current Blueprint
- current usable Runtime Instance when safe
- correction draft
- comparison context

## F00-UX-004 — No Blank-page Dead End

每個主要空白狀態至少有一個可執行下一步：

- Try a Capsule
- Type your idea
- Continue answering
- Retry
- Edit request
- Keep current App
- Remix
- Correct result

## F00-UX-005 — Human Words, Technical Truth

F00 可以把 technical state 翻成人話，但不能假裝成功。

例：

~~~text
F02 validation rejected
不顯示：
SCHEMA_INVALID

顯示：
「這個 App 還差一點才能安全執行，我們保留了你的需求。」
~~~

# 4. UX State Model

F00 採 hierarchical state，而不是單一巨大 enum。

~~~text
Shell
├─ Surface State
├─ Creation State
├─ Runtime State
└─ Overlay State
~~~

這避免：

~~~text
RUNNING_WITH_SHARE_MODAL_WITH_RECOVERY_WITH...
~~~

的組合爆炸。

# 5. Surface State

## F00-STATE-001

~~~text
DISCOVER
CREATE
APP
COMPARE
~~~

DISCOVER：
- 首頁 / Inspiration Capsule discovery
- prompt 可直接輸入

CREATE：
- Intent analysis / clarification / assumption / build
- User 尚未進主要 Runtime

APP：
- validated Blueprint 已 hydrate
- Runtime 是主要 surface

COMPARE：
- F16 old/new result compare
- current usable App context仍保留

Transitions：

~~~text
DISCOVER → CREATE
CREATE → APP
APP → CREATE       // Refine / Remix / new create
APP → COMPARE      // Correction generated
COMPARE → APP      // Accept / Revert / Close
APP → DISCOVER     // explicit start new
~~~

# 6. Creation State Machine

## F00-STATE-002

~~~text
IDLE
→ EDITING
→ ANALYZING
→ CLARIFICATION_REQUIRED
→ ANALYZING
→ ASSUMPTION_REVIEW
→ READY_TO_BUILD
→ BUILDING
→ HYDRATING
→ APP_READY
~~~

Possible failure branches：

~~~text
ANALYZING → RECOVERABLE_FAILURE
BUILDING → RECOVERABLE_FAILURE
HYDRATING → RECOVERABLE_FAILURE | TERMINAL_FAILURE
~~~

State source：

- ANALYZING / CLARIFICATION / ASSUMPTION / BUILDING 来自 F01 lifecycle。
- HYDRATING / APP_READY 来自 F03 lifecycle。
- Failure presentation 来自 F12 Recovery State。

# 7. State → User Presentation Mapping

| Internal State | User-facing intent | Primary Action |
|---|---|---|
| IDLE | 想做什麼？ | Start typing / Capsule |
| EDITING | 說出你想要的 App | Create |
| ANALYZING | 正在理解你的需求 | Cancel |
| CLARIFICATION_REQUIRED | 還差幾個關鍵資訊 | Answer / Continue |
| ASSUMPTION_REVIEW | 這些是目前的建議設定 | Accept / Edit |
| READY_TO_BUILD | 資訊已足夠 | Build |
| BUILDING | 正在把需求變成 App | Cancel where safe |
| HYDRATING | App 準備好了，正在啟動 | none |
| APP_READY | 可以直接使用 | Use / Share / Remix |
| RECOVERABLE_FAILURE | 沒完成，但你的內容還在 | Retry / Edit / Keep current |
| TERMINAL_FAILURE | 目前無法安全繼續 | Start over / Return to safe state |

Consumer copy 不使用 Compiler / Validator / Registry / Runtime 等工程詞彙。

# 8. Discover / Inspiration Capsules

## F00-UX-006

Capsule 是：

> 可立即 Fork / Edit / Run 的教學型 Prompt + outcome preview，不是純展示卡。

Capsule minimum display：

~~~text
title
one-line use case
example outcome / preview
difficulty or refinement depth optional
primary CTA: Try / Fork
secondary: View how it works optional
~~~

Capsule interaction：

~~~text
Capsule
→ prefill editable prompt
→ optional preset variables
→ User can edit before create
→ F01 create lifecycle
~~~

Rules：

1. Capsule 不直接 bypass F01。
2. Capsule metadata 可提供 Prompt A context，但不可當 User Explicit fact。
3. Capsule preset 若 material，來源要標為 NFF_DEFAULT / template proposal。
4. User 一改值，User value 優先。

# 9. Prompt Composer

## F00-UX-007

Composer minimum：

- multiline editable input
- Create CTA
- capsule-prefilled state
- Ghost Text
- character / request size feedback when near limit
- preserve draft on recoverable failure

Primary states：

~~~text
EMPTY
TYPING
PREFILLED
SUBMITTING
LOCKED_DURING_CRITICAL_TRANSITION
~~~

Rules：

- EMPTY 不送 request。
- SUBMITTING 時避免 duplicate submit。
- Idempotency-Key 由 Client operation layer產生並保存到 logical operation結束。
- User 可以在 ANALYZING 前取消本地 submit；provider已開始後的 cancel依 F01 contract。
- prompt draft不因 server error清空。

# 10. Ghost Text

## F00-UX-008

Ghost Text 目的是降低空白輸入負擔。

Allowed：

- example phrasing
- variable hints
- suggested continuation
- Capsule contextual hint

Not allowed：

- 看起來像 User 已輸入的實際值
- 將 LLM proposal 當已確認 fact
- 自動 submit

Ghost Text 必須視覺上與 User text 分離，User開始輸入後可淡出。

# 11. Clarification UX

## F00-UX-009

F00 只呈現 F01 已選好的 1–3 questions。

支持：

~~~text
FREE_TEXT
NUMBER
BOOLEAN
SINGLE_CHOICE
MULTI_CHOICE
STRUCTURED_FIELDS
~~~

Presentation rules：

1. 問題必須與主要 prompt 保持同一 creation context。
2. 一次顯示最多 3 個 material questions。
3. required / optional 要清楚。
4. 已回答值可編輯。
5. submit 前做 client-side type/required validation，但 server F01仍是 truth。
6. stale intent version conflict → reload current answers，不把 User input直接丟掉。
7. User 不需要知道 policy ID。

Question interaction：

~~~text
Answer
→ Continue
→ local validation
→ F01-API-002
→ new clarification state
~~~

# 12. Visible Assumption UX

## F00-UX-010

Material assumption 必須顯示：

~~~text
what is assumed
current value
source type
editable?
impact summary when useful
~~~

User-facing labels：

~~~text
FACT → 已提供
DEFAULT → 預設
PROPOSAL → 建議
UNKNOWN → 尚未決定
~~~

不要顯示 raw provenance enum。

Actions：

~~~text
Accept
Edit
Reject
~~~

Rules：

- material proposal不能 hidden。
- Accept 後 F01 source becomes USER_ACCEPTED_PROPOSAL。
- Edit 後 edited value當 User Explicit。
- Reject 後可能回 Clarification。
- cosmetic default 可以不打斷流程，但應可在後續 Refine 中改。

# 13. Fast Path UX

## F00-UX-011

Clear Intent：

~~~text
Create
→ ANALYZING
→ READY
→ BUILDING automatically
~~~

不額外插入確認頁。

Material assumptions：

~~~text
Create
→ ANALYZING
→ ASSUMPTION_REVIEW
→ User accepts/edits
→ BUILDING
~~~

Critical missing：

~~~text
Create
→ ANALYZING
→ CLARIFICATION_REQUIRED
→ answer
→ ANALYZING
→ ...
~~~

原則：

> 不為了展示 AI 很聰明而增加步驟；只在 product truth需要 User decision 時停下來。

# 14. Build / Compilation UX

## F00-UX-012

BUILDING 對 User 是一個整體狀態；內部可對應 F01 COMPOSING / VALIDATING。

Default copy 不顯示：

~~~text
Prompt B
F02 V07
registry digest
~~~

可顯示簡單 progress copy：

~~~text
正在組合你的 App
正在檢查互動是否可安全執行
快完成了
~~~

Rules：

- progress是 phase-based，不偽造百分比。
- operation timeout，保留 Intent。
- validation-driven recompose最多一次時，不需閃爍回上一頁；同 BUILDING surface內完成。
- 若需要新 User decision，才回 Clarification / Assumption。

# 15. Hydration UX

## F00-UX-013

F01 VALIDATED 後：

~~~text
content_hash
→ create F03 Instance
→ HYDRATING
→ READY
→ Surface = APP
~~~

Hydration loading應短而穩定，不再顯示 Compiler copy。

若 F03 recoverable node issue：

- App仍可進 APP surface when core usable。
- affected node由 F03/F12 fallback呈現。

若 F03 fatal hydration failure：

- 不顯示半個 App。
- 進 F12 recovery presentation。

# 16. Runtime Frame / App Chrome

## F00-UX-014

APP surface分兩層：

~~~text
NFF Shell Chrome
+ Generated App Runtime Frame
~~~

Shell Chrome Phase 1 minimum：

- App title
- New / Home
- Share
- Remix / Refine
- Correct result entry when result exists
- recovery notice area when needed

Generated App area：

- F03 controls render
- F00 不直接讀/改 Blueprint state
- F00 不攔截正常 local interaction

Rules：

- runtime normal interaction不因 shell chrome產生 server calls。
- Shell control 與 generated App control視覺上要有區隔。
- mobile時 chrome可 compact，但核心操作仍可達。

# 17. Result Surface

## F00-UX-015

如果 Blueprint result.outputs 有 AVAILABLE outputs：

F00 可以提供 result chrome：

~~~text
Result summary area optional
Adjust result / 邏輯不對
Share
Remix
~~~

F00 不從 DOM 猜結果，使用 F03 evaluateResult() / canonical result surface。

如果 output ERROR：

- 不顯示 fake value。
- 交 F12 recovery。
- 其他可用 App功能可保持。

# 18. Correction Entry / F16

## F00-UX-016

入口 copy：

~~~text
調整結果
邏輯不對
結果不是我想要的
~~~

不使用：

~~~text
Report model hallucination
Validation error
~~~

Entry 必須保留：

- current Blueprint
- current visible inputs where policy allows
- current result
- correction text draft

Correction submit後由 F16/F01/F02處理。

F00只負責：

~~~text
APP
→ Correction Composer Overlay
→ Correcting
→ Compare
~~~

# 19. Compare State

## F00-STATE-003

COMPARE surface minimum：

~~~text
Previous Result
New Result
Changed explanation summary when available
Actions:
  Accept New
  Keep Previous
  Adjust Again
~~~

Rules：

1. old result / old Blueprint仍可用。
2. new result未 accepted前不破壞 old current truth。
3. Accept New → new Blueprint/Instance成 active。
4. Keep Previous → 回 old APP。
5. Adjust Again →保留 correction context。
6. Technical diff不是 consumer default；顯示 semantic/user-visible差異。

# 20. Share Entry

## F00-UX-017

Phase 1 Shell 必須有 Share CTA。

F00責任：

- collect active Blueprint reference
- invoke F05 share flow
- show pending / success / failure state
- copy/share link UI
- failure保留 App

F00不決定：

- durable vs portable default mode
- share persistence schema
- expiry policy

這些屬 F05。

# 21. Remix / Refine Entry

## F00-UX-018

APP surface提供：

~~~text
Remix / 改成我的版本
Refine / 修改這個 App
~~~

Entry behavior：

~~~text
Current Blueprint
→ open Create surface with context
→ prefill semantic editing context
→ User describes change
→ F06/F01
~~~

Rules：

- original App仍可返回。
- Runtime state mutation不等於 Refine。
- Remix / Refine failure不破壞 original App。

# 22. Recovery Overlay Model

## F00-STATE-004

Recovery不作獨立產品流程，而是可套在 CREATE / APP / COMPARE 的 overlay。

~~~text
RecoveryOverlay
├─ NONE
├─ INLINE_NOTICE
├─ BLOCKING_RECOVERABLE
└─ TERMINAL
~~~

Data來自 F12 Recovery State：

~~~text
status
human_message
preserved_context
next_actions
technical_code
~~~

Consumer預設只看：

~~~text
human_message
next_actions
~~~

technical_code只進 diagnostics / support context。

# 23. Recovery UX Rules

## F00-UX-019

Recoverable：

- 保留當前 surface。
- 保留安全 context。
- next action 1–3個。
- primary action必須可執行。

Examples：

~~~text
Retry
Edit request
Keep current App
Use simpler version
Return to previous result
~~~

Terminal：

- 不無限 retry。
- 說清楚目前不能安全完成。
- 提供返回安全狀態 / start new。
- 不顯示 raw stack。

# 24. Unsupported / Degraded UX

## F00-UX-020

F04 coverage = PARTIALLY_SUPPORTED：

- material degradation 在 build前明確顯示。
- User可接受 / edit Intent。

UNSUPPORTED / EXTERNAL_REQUIRED in Phase 1：

- 誠實說「目前這部分還做不到」。
- 保留其餘 Intent。
- 可提供 remove/simplify/refine path。
- 不產生看起來成功但 semantic core已改掉的 App。

# 25. Local Frontend State

## F00-DATA-001

Conceptual ShellState：

~~~text
ShellState
├─ surface
├─ creation
│  ├─ prompt_draft
│  ├─ source_capsule_id?
│  ├─ intent_id?
│  ├─ intent_version?
│  ├─ questions[]
│  ├─ answer_drafts
│  ├─ visible_assumptions[]
│  ├─ assumption_drafts
│  └─ operation_idempotency_key?
├─ app
│  ├─ active_blueprint_hash?
│  ├─ runtime_instance_id?
│  └─ result_summary?
├─ compare
│  ├─ previous_blueprint_hash?
│  ├─ new_blueprint_hash?
│  └─ correction_draft?
└─ overlay
   ├─ recovery?
   ├─ share?
   └─ correction?
~~~

F00 local state不是 durable product truth。

# 26. Browser Persistence

Phase 1 可以 local persistence：

- prompt draft
- unsent clarification draft
- unsent correction draft
- minimal recovery navigation context

預設不 local persistence：

- full Runtime Instance
- sensitive result
- DO_NOT_PERSIST fields
- provider/model raw output
- arbitrary Blueprint internals unless F05 cache需要且符合 policy

Browser persistence使用 versioned key + TTL。

Exact sensitive-field policy由 F07/F12後續補齊；未定前採保守最小保存。

# 27. API / Function Integration

F00直接依賴 F01：

~~~text
POST /api/v1/intents
POST /api/v1/intents/{intent_id}/answers
POST /api/v1/intents/{intent_id}/compile
~~~

F00與 F03使用 local Runtime interfaces：

~~~text
createRuntimeInstance
hydrateInstance
evaluateResult
disposeRuntimeInstance
~~~

F05/F06/F12/F16 的 network/API exact contract尚未完成時，F00只依 semantic interface，不自行發明 endpoint。

# 28. Operation Idempotency UX

Create / answer / compile：

- logical operation開始即生成 Idempotency-Key。
- network retry沿用同 key。
- User明確修改 payload後為新 logical operation → 新 key。
- duplicate button tap不產生新 operation。
- UI可顯示「正在處理」，但不能因重試建立兩個 App。

# 29. Navigation / Back Behavior

## F00-UX-021

Browser Back / in-app Back：

- CLARIFICATION → EDITING：保留 answers draft。
- ASSUMPTION_REVIEW → EDITING：保留 proposal / edits。
- APP → CREATE 只透過 explicit Refine/New，不讓 accidental Back丟 active App。
- COMPARE → APP：預設返回 previous/current safe App，不自動 accept new。
- Blocking operation離開前盡可能保存 prompt draft。

不使用 destructive Back。

# 30. Loading / Skeleton Rules

## F00-UX-022

Loading只用在真的 asynchronous work：

- ANALYZING：composer保留，顯示 operation state。
- BUILDING：可顯示 shell skeleton，不 fake generated content。
- HYDRATING：shell先顯示，Runtime ready後才互動。
- local Runtime action不顯示 global loading。

避免 spinner覆蓋整個產品。

# 31. Cancel Semantics

## F00-UX-023

User可取消：

- ANALYZING request waiting
- BUILDING request waiting where safe
- correction draft / pending compare

Cancel後：

- prompt / intent context保留。
- 已成功 admission的 Blueprint不刪除。
- provider operation無法取消時，idempotency防 duplicate outcome。
- HYDRATING dispose後回 validated App reference / safe creation state。

# 32. Responsive Layout Baseline

Phase 1 mobile-first：

- primary CTA單手可達。
- clarification不要求 horizontal scroll。
- compare窄螢幕可 stacked previous/new。
- Shell chrome不遮 Runtime controls。
- keyboard彈出時 composer action仍可達。
- generated App container有 bounded width策略，但允許 full-width Capability。

# 33. Accessibility Baseline

## F00-UX-024

Required：

- keyboard navigation
- visible focus
- semantic labels
- loading state透過 aria-live適度通知
- field error programmatic association
- modal focus trap / return focus
- color不是唯一狀態指示
- primary touch target至少44 CSS px
- prefers-reduced-motion

F04 / Capability implementation仍需各自驗證 component accessibility。

# 34. Error Seed

| ID | Meaning | Recovery |
|---|---|---|
| F00-ERR-001 | SHELL_BOOT_FAILED | reload / safe home |
| F00-ERR-002 | LOCAL_DRAFT_PERSIST_FAILED | continue without persistence |
| F00-ERR-003 | INVALID_LOCAL_UI_STATE | reset affected overlay |
| F00-ERR-004 | DUPLICATE_SUBMIT_GUARD | ignore duplicate |
| F00-ERR-005 | RUNTIME_MOUNT_FAILED | F12 recovery |
| F00-ERR-006 | UNSUPPORTED_VIEW_STATE | safe home / diagnostics |

F00通常呈現其他 Function error，不重新編碼另一套 technical taxonomy。

# 35. Evidence Seed

正式 Event Envelope由 F07定義。

~~~text
F00-EVT-001 shell_opened
F00-EVT-002 capsule_viewed
F00-EVT-003 capsule_forked
F00-EVT-004 prompt_submitted
F00-EVT-005 clarification_shown
F00-EVT-006 clarification_submitted
F00-EVT-007 assumption_review_shown
F00-EVT-008 assumption_accepted
F00-EVT-009 assumption_edited
F00-EVT-010 app_ready
F00-EVT-011 share_opened
F00-EVT-012 remix_opened
F00-EVT-013 correction_opened
F00-EVT-014 recovery_shown
F00-EVT-015 recovery_action_selected
F00-EVT-016 compare_shown
F00-EVT-017 compare_accept_new
F00-EVT-018 compare_keep_previous
~~~

不要記 every keystroke。

# 36. UX Metrics

~~~text
Time to First Useful App
Capsule → Create conversion
Prompt → Clarification rate
Clarification completion rate
Assumption acceptance/edit rate
Build → App Ready rate
Recovery success rate
Share entry rate
Remix entry rate
Correction entry rate
Correction compare decision rate
~~~

不能把 App Ready 直接當 semantic success。

# 37. Acceptance Criteria

Core Flow：

- F00-AC-001 User可從空白 prompt 或 Capsule開始 Create。
- F00-AC-002 Capsule prefill永遠可編輯。
- F00-AC-003 Clear Intent不增加不必要 confirmation page。
- F00-AC-004 F01需要 clarification時，F00一次只呈現選定的1–3題。
- F00-AC-005 material proposal一定可見且可 Accept/Edit/Reject。
- F00-AC-006 prompt / answers在 recoverable failure後仍保留。
- F00-AC-007 VALIDATED Blueprint可進 F03 hydrate並切到 APP surface。

Runtime / Product Loop：

- F00-AC-008 normal Runtime interaction不觸發 global shell loading。
- F00-AC-009 APP surface可到 Share / Remix / Correction入口。
- F00-AC-010 correction failure不破壞 current App。
- F00-AC-011 Compare可 Accept New / Keep Previous / Adjust Again。
- F00-AC-012 Keep Previous不 mutation old Blueprint。
- F00-AC-013 unsupported intent不 fake success。

Recovery：

- F00-AC-014 consumer不看到 raw 401/500/stack trace。
- F00-AC-015 recoverable failure至少有一個有效 next action。
- F00-AC-016 node-level Runtime failure不強迫離開整個 App。
- F00-AC-017 terminal failure提供 safe exit。

Safety / Privacy：

- F00-AC-018 DO_NOT_PERSIST value不進 local draft storage。
- F00-AC-019 duplicate tap不造成 duplicate logical create/compile。
- F00-AC-020 Shell不直接修改 Runtime Instance Store。
- F00-AC-021 Shell不把 LLM proposal顯示成 User fact。

Accessibility / Responsive：

- F00-AC-022 Phase 1 Core Create flow可全鍵盤操作。
- F00-AC-023 modal關閉後focus回合理觸發點。
- F00-AC-024 mobile width下 clarification / compare無必要 horizontal scroll。
- F00-AC-025 reduced-motion preference被 Shell animation尊重。

Evidence：

- F00-AC-026 Create / clarification / App Ready / recovery / share / remix / correction入口可量測。
- F00-AC-027 telemetry不記 every keystroke。
- F00-AC-028 App Ready不被 telemetry命名為 semantic success。

# 38. Test Mapping Seed

~~~text
F00-AC-001 → TEST-F00-001 create entry
F00-AC-003 → TEST-F00-003 fast path
F00-AC-004 → TEST-F00-004 clarification question cap
F00-AC-005 → TEST-F00-005 visible assumptions
F00-AC-006 → TEST-F00-006 preserve context on failure
F00-AC-007 → TEST-F00-007 validated-to-runtime
F00-AC-008 → TEST-F00-008 no global load on runtime interaction
F00-AC-010 → TEST-F00-010 preserve App on correction failure
F00-AC-011 → TEST-F00-011 compare decisions
F00-AC-013 → TEST-F00-013 unsupported honest UX
F00-AC-014 → TEST-F00-014 no raw engineering errors
F00-AC-019 → TEST-F00-019 duplicate submit guard
F00-AC-020 → TEST-F00-020 shell/runtime boundary
F00-AC-022 → TEST-F00-A11Y-001 keyboard create flow
F00-AC-024 → TEST-F00-RWD-001 mobile clarification/compare
~~~

# 39. Dependencies

Upstream：

- F01 lifecycle / API / clarification / assumptions
- F03 hydration / runtime / result
- F04 coverage status semantics
- Design-to-Delivery

Collaborators：

- F05 Share
- F06 Remix / Refine
- F07 Evidence
- F12 Recovery
- F16 Correction

# 40. Release / Migration

Phase 1 Shell：

~~~text
Discover
+ Prompt Composer
+ Clarification / Assumption
+ Build
+ Runtime Frame
+ Share / Remix / Correct entries
+ Recovery presentation
+ Compare
~~~

No account required before first value。

未來加入 Account / Realtime / Marketplace時，不得破壞：

~~~text
Prompt → Clarify only if needed → Build → Use
~~~

# 41. Open Decisions

目前沒有阻擋 F05/F06/F07/F12/F16 Detailed Design 的 architecture-level open decision。

後續各 Function仍需決定：

1. F05 exact Share modal fields / default share mode。
2. F06 exact Remix vs Refine wording / source context。
3. F07 local draft TTL / Evidence envelope。
4. F12 exact Recovery message catalog / action mapping。
5. F16 exact correction composer / compare semantic explanation payload。
6. Capsule content taxonomy / ranking屬 Product content layer，可迭代，不改 F00 state machine。

# Conclusion

F00 Current Truth：

~~~text
DISCOVER
→ EDIT
→ ANALYZE
→ clarify / review assumptions only when necessary
→ BUILD
→ HYDRATE
→ APP
→ Share / Remix / Correct
→ Compare / Recover without losing context
~~~

> F00 的工作不是替其他 Function 做決策，而是讓所有 Function 對 User 看起來像一個完整、連續、好懂的產品。
