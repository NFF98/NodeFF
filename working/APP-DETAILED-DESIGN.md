# NodeFF App Detailed Design

> 狀態：Working Design Baseline。本文是 Architecture 與 Implementation 之間的 Function Portfolio：定義 Function 邊界、依賴、1／3／6 個月交付順序與 Acceptance Gate。單一 Function 的 Frontend / Backend / API / Data / Error / Test 細節放在 working/functions/。

# 1. Detailed Design 的目的

Architecture 回答：

> **NFF 是什麼、有哪些系統、邊界在哪裡。**

Detailed Design 必須回答：

> **要做哪些 Function、先做誰、依賴誰、做到什麼才算完成。**

NodeFF 採 **Function-Oriented Design**。

每個 Function 必須從 User Outcome 一路設計到 Runtime / Backend，而不是切成互不相干的 Frontend / Backend 文件。

---

# 2. Function Design Contract

每個 Function 文件都必須包含：

~~~text
Purpose / User Outcome
Scope / Non-Scope
User Flow
Preconditions
Frontend Behavior
Backend / Runtime Behavior
API / Contract
State / Data
Capability Dependencies
Error / Recovery
Security / Permission
Telemetry / Evidence
Acceptance Criteria
Dependencies
Release / Migration
Open Decision Gates
~~~

Cursor 只能實作已經有明確 Contract 與 Acceptance 的 Function。

---

# 3. Function Portfolio

為保留既有引用，F01–F11 編號維持；新增缺少的 cross-cutting Functions。

| ID | Function | 核心結果 | 主要架構 | 目標時程 |
|---|---|---|---|---|
| **F00** | Experience Shell / 靈感精靈 | User 能容易開始、Refine、Remix、Recovery | UX / Cross-layer | 0–1 月 |
| **F01** | Intent Compilation + Model Gateway | Intent → Blueprint Candidate | L1–L2 | 0–1 月 |
| **F02** | Blueprint Validation / Trust Admission | 不可信 Blueprint 不進 Runtime | L3 | 0–1 月 |
| **F03** | Runtime Execution | Blueprint → Interactive App | L4 | 0–1 月 |
| **F04** | Capability Registry / Resolution | Compiler、Validator、Runtime 共用一份能力真相 | L2–L4 | 0–1 月 |
| **F05** | Share / Restore | Link → Recipient 可立即使用 | L1 / L4 | 0–1 月 |
| **F06** | Remix / Refine | Existing App → Semantic Delta → New Blueprint | L2–L4 | 0–1 月 |
| **F07** | Anonymous Identity & Evidence | No-login continuity + PMF evidence | Cross-cutting | 0–1 月 |
| **F08** | Durable Identity / Ownership | Anonymous → Account → Ownership | Cross-cutting | 2–3 月 |
| **F09** | Realtime Room | 多人共享 Instance State | L4 / Infra | 2–3 月，Evidence-gated |
| **F10** | Blueprint Reuse / Retrieval | Trusted Blueprint Family → cheaper / faster compile | L1–L3 | 2–3 月 |
| **F11** | External Capability Execution | AI / API / Heavy Work 受控執行 | Cross-cutting | 4–6 月，必要時提前 Pilot |
| **F12** | Humanized Recovery Orchestration | 技術錯誤 → 可理解、可繼續的 UX | Cross-layer | 0–1 月 |
| **F13** | Entitlement / Metering | Premium / Costly Capability 可控、可量測 | Cross-cutting | 2–6 月 |
| **F14** | Provider Registry / Certification | External Capability 可被信任與版本化 | Platform | 6 月後 |
| **F15** | Transaction / Settlement | Commerce Outcome 可追蹤、對帳、結算 | Platform | 6 月後 |
| **F16** | Result Feedback / Logic Correction | 結果不符 Intent 時保留現況、精準修正、比較與回退 | UX / L2–L4 | 0–1 月 |
| **F17** | Heterogeneous Workflow Orchestration | 多個 Internal / External / Human Steps 能可靠完成同一 Outcome | Platform / External Capability Plane | 6 月後，Evidence-gated |

---

# 4. Function Dependency Map

~~~mermaid
flowchart TD
    F00[F00 Experience Shell]
    F01[F01 Intent Compilation]
    F02[F02 Validation]
    F03[F03 Runtime]
    F04[F04 Capability Registry]
    F05[F05 Share / Restore]
    F06[F06 Remix / Refine]
    F07[F07 Anonymous Evidence]
    F12[F12 Recovery]
    F16[F16 Result Correction]

    F08[F08 Identity / Ownership]
    F09[F09 Realtime]
    F10[F10 Reuse / Retrieval]
    F13[F13 Entitlement / Metering]

    F11[F11 External Capability]
    F14[F14 Provider Registry]
    F15[F15 Transaction / Settlement]
    F17[F17 Workflow Orchestration]

    F00 --> F01
    F04 --> F01
    F01 --> F02
    F04 --> F02
    F02 --> F03
    F04 --> F03

    F03 --> F05
    F05 --> F06
    F01 --> F06

    F07 --> F01
    F07 --> F05
    F07 --> F06

    F00 --> F16
    F03 --> F16
    F06 --> F16
    F16 --> F01
    F16 --> F02
    F16 --> F07

    F12 --> F00
    F01 --> F12
    F02 --> F12
    F03 --> F12
    F04 --> F12

    F07 --> F08
    F05 --> F08

    F04 --> F10
    F07 --> F10
    F10 --> F01

    F03 --> F09
    F08 --> F09

    F04 --> F11
    F03 --> F11
    F13 --> F11

    F08 --> F13
    F07 --> F13

    F11 --> F14
    F13 --> F14
    F14 --> F15
    F11 --> F17
    F13 --> F17
    F14 --> F17
    F17 --> F15
~~~

設計含義：

> **第 1 個月不是「先做畫面」，而是先建立完整 Core Loop 的最短可信任路徑。**

---

# 5. 0–1 個月：Core Proof Release

第 1 個月的 Release Goal：

> **Intent → Correct App → Use → Share → Recipient Use → Remix，而且任何失敗都有 Humanized Recovery。**

## 必須交付

### F00 — Experience Shell / 靈感精靈

最小能力：

- Inspiration Capsules
- editable prompt
- Ghost Text
- Progressive Refinement entry
- Remix entry
- Recovery presentation
- Result feedback / 「調整結果」entry
- previous vs new result comparison entry

Acceptance：

- User 不必理解 Prompt Engineering
- 從 Capsule 可以直接進 Create
- failure 不清空輸入
- recovery action 明確
- User 可從執行結果直接進入「邏輯不對／調整結果」流程

### F01 — Intent Compilation + Model Gateway

F01 不允許「User Prompt → LLM 直接腦補 → Blueprint」的一步式生成。

正式流程：

~~~text
User Intent
→ Intent Analysis
→ Structured Intent Envelope
→ Clarification Policy
   ├─ READY
   ├─ READY_WITH_VISIBLE_ASSUMPTIONS
   └─ NEEDS_CLARIFICATION
→ Resolved Intent
→ Blueprint Compilation
→ F02 Validation
~~~

分工：
- LLM：理解 Intent、列出 unknown / ambiguity / assumption。
- NFF Clarification Policy：決定直接做、顯示假設、或必須追問。
- F00：把問題與假設用可編輯 UX 呈現。
- LLM 無權自行把關鍵缺口當成不重要。

#### Structured Intent Envelope

第一階段 LLM 只輸出 Intent Envelope，不產 Blueprint。

最低欄位：

~~~text
goal
actors / entities
known_inputs
constraints
requested_output
candidate_rules
missing_fields[]
ambiguities[]
assumptions[]
capability_hints[]
~~~

每個 missing / ambiguity / assumption 至少有：

~~~text
id
semantic_role
description
source
required_for_execution
impact_level
confidence
can_default
proposed_default
alternatives
user_visible
rationale
~~~

source：
- USER_EXPLICIT
- DOMAIN_KNOWN
- NFF_DEFAULT
- LLM_PROPOSED

impact_level：
- LOW
- MEDIUM
- HIGH
- CRITICAL

LLM_PROPOSED 永遠不能偽裝成 USER_EXPLICIT 或 DOMAIN_KNOWN。

#### Clarification Policy

這是 NFF-owned deterministic policy，不是另一個自由 Prompt。

~~~text
CP-001 必要執行值缺失，且沒有安全明確 default
→ NEEDS_CLARIFICATION

CP-002 有兩個以上合理 interpretation，且會造成 HIGH / CRITICAL 結果差異
→ NEEDS_CLARIFICATION

CP-003 涉及金額、權限、外部成本或不可逆行為，關鍵規則不是 User Explicit
→ NEEDS_CLARIFICATION

CP-004 有安全、可逆 default，但會影響業務結果
→ READY_WITH_VISIBLE_ASSUMPTIONS

CP-005 只影響畫面或 cosmetic，不影響核心結果
→ READY

CP-006 資訊完整且沒有 material ambiguity
→ READY
~~~

規則：
- 一次最多問 1–3 個最高資訊價值問題。
- 問題必須直接對應 blocker / material ambiguity。
- 已回答問題不得重問，除非上游條件改變。
- Policy rule 有 stable ID 與 version，可測試、可 telemetry、可擴充。
- Domain-specific required fields 可由 Domain Policy Pack 擴充，但不能繞過 Core Policy。

#### Question Priority

~~~text
Execution Blocker
> Safety / Money / Permission
> High Outcome Divergence
> Core Business Rule
> Secondary Preference
> Cosmetic
~~~

同層優先問「回答一次可以消除最多下游不確定性」的問題。

#### Visible Assumptions

NFF 必須區分：

~~~text
FACT
= User 明講或可信資料源提供

DEFAULT
= NFF 版本化預設

PROPOSAL
= LLM 建議

UNKNOWN
= 目前不能可靠決定
~~~

UI 不得把 PROPOSAL 顯示成 FACT。

公司分帳例：

~~~text
User:
「公司 50 人，有老闆、經理、員工，聚餐幫我分帳」

解析：
total_people = 50
roles = owner / manager / employee
bill_total = UNKNOWN
role_counts = UNKNOWN
weight_rule = PROPOSAL(3:2:1)

UI:
總金額 [_____]
老闆 [1]  經理 [5]  員工 [44]
建議權重：老闆 [3] : 經理 [2] : 員工 [1]
「這是建議值，可直接修改」
~~~

確認後才形成 Resolved Intent。

#### LLM Prompt Contract

不採單一 mega-prompt，採兩個版本化 Prompt。

**Prompt A — Intent Analyst**

輸入：
- raw user intent
- conversation / correction context
- relevant Inspiration Capsule metadata
- capability semantic catalog
- domain policy metadata

硬指令：
1. Preserve user-stated facts exactly.
2. Separate facts, unknowns, defaults and proposals.
3. Never invent a required business value.
4. Identify ambiguities that materially change outcome.
5. Propose defaults only when safe and reversible.
6. Mark proposal provenance and impact.
7. Output Structured Intent Envelope only.
8. Do not generate Blueprint yet.

**Prompt B — Blueprint Composer**

只有 Clarification Gate 通過後才執行。

輸入：
- resolved_intent
- accepted_visible_assumptions
- capability_registry_snapshot
- LegoSpec schema
- security/resource policy
- existing_blueprint when refining

硬指令：
1. Treat resolved_intent as semantic source of truth.
2. Do not introduce new business assumptions.
3. Use only registered capabilities/operators.
4. Preserve invariants and requested totals.
5. Output Blueprint Candidate only.
6. Never output arbitrary JavaScript.

Prompt 必須帶：
- prompt_version
- schema_version
- registry_version
- model_adapter
- evaluation_fixture_version

因此 Prompt 可回放、A/B、Regression Test，不是散落字串。

#### Fast Path

Clarification Gate 每次都執行，但 User 不一定每次被問。

~~~text
Clear Intent
→ READY
→ immediately compile

Minor material assumption
→ READY_WITH_VISIBLE_ASSUMPTIONS
→ show/edit assumption
→ compile

Critical missing information
→ NEEDS_CLARIFICATION
→ ask blocker
→ merge answer
→ re-run policy
→ compile
~~~

Model Gateway 最小要求：

- NFF-owned interface
- 至少一個 production adapter
- provider config 不進 LegoSpec
- timeout / provider failure 可分類
- future provider switch 不改 F02 / F03 contract

Acceptance：

- output 只能是受控 Blueprint Candidate
- unsupported intent 不 fake success
- provider failure 有 bounded recovery
- semantic mismatch 可被 evidence 捕捉

### F02 — Blueprint Validation

驗證至少包括：

- schema
- state references
- capability existence
- bindings
- rules
- permissions
- resource bounds
- version / compatibility
- degradation metadata

Acceptance：

> Invalid / unsafe / incompatible Blueprint 100% 不得進 Runtime。

注意：這不等於 Semantic Correctness 100%。

### F03 — Runtime Execution

負責：

- hydration
- state
- action
- rule
- view
- effect
- local component isolation

Acceptance：

- normal deterministic interaction = 0 LLM
- arbitrary JS impossible by design
- single component failure 不造成整頁 White Screen
- Blueprint / Instance 分離

### F04 — Capability Registry / Resolution

Phase 1 採：

> **Canonical versioned source → generated compiler metadata + validator schema + runtime registration**

Acceptance：

- Compiler / Validator / Runtime 不得有三份手寫 registry
- unknown capability 被拒絕
- registry version 被 Blueprint / validation 流程識別
- Capability Coverage 可得到 Full / Partial / External / Unsupported

### F05 — Share / Restore

Acceptance：

- recipient 不需安裝
- First Value 前不要求 account
- valid Blueprint 可 restore
- sensitive data 不預設放 portable URL
- share error 有 recovery UX

### F06 — Remix / Refine

~~~text
Existing Blueprint
+ User Semantic Change
→ Delta / Recompile
→ Full Validation
→ New Immutable Blueprint
~~~

Acceptance：

- original Blueprint 不被 mutation
- Runtime state change 不等於 semantic revision
- Remix lineage 可追蹤
- refinement failure 保留原 App / Intent

### F16 — Result Feedback / Logic Correction

這個 Function 處理：

> **App 技術上能跑，但 User 認為邏輯、假設或結果明顯不符合原 Intent。**

主流程：

~~~text
Current Blueprint
+ Current Instance Inputs
+ Current Result
→ User Correction Feedback
→ Preserve Current Version
→ Correction Intent
→ Semantic Delta
→ Full Validation
→ New Immutable Blueprint Revision
→ Re-run with preserved inputs
→ Compare Old / New Result
→ Accept / Continue Correcting / Revert
~~~

Frontend 最小行為：

- Result 畫面提供「調整結果／邏輯不對」入口
- User 可用自然語言指出問題
- 原本 Inputs / Result 不消失
- 新舊 Result 可比較
- 可返回上一版
- 不把 semantic mismatch 顯示成 technical error

Backend / Compiler responsibility：

- 將 feedback 正規化為 Correction Intent
- 以 existing Blueprint 為 base
- 優先產生最小 Semantic Delta
- 不允許直接 mutation 原 Blueprint
- 新 revision 必須完整走 F02 Validation
- correction failure 時保留原 Blueprint 可繼續使用

State / Data：

~~~text
base_blueprint_id
base_revision
instance_input_snapshot
result_snapshot_before
correction_intent
semantic_delta
new_blueprint_id
result_snapshot_after
correction_outcome
~~~

Acceptance：

1. User 不需重新輸入原本資料即可修改邏輯。
2. 原 Blueprint 永遠可回復。
3. 修改只針對 User 指出的語意範圍，但新 Blueprint 仍完整驗證。
4. 新舊 Result 可比較。
5. correction 失敗不破壞目前可用版本。
6. semantic mismatch / correction / accept / revert 都形成 Evidence。
7. 「有結果」不得被當成「結果正確」的證明。

### F07 — Anonymous Identity & Evidence

最小 identity：

- random first-party anonymous_id
- session / intent / blueprint / share linkage

只收 meaningful events：

- compile outcome
- semantic mismatch
- result correction requested
- result correction accepted / rejected / reverted
- capability gap
- share
- open
- use
- remix
- recovery

Acceptance：

- 不使用 fingerprinting
- No Registration ≠ No Evidence
- telemetry 不造成每次 local interaction 都打 server
- privacy-sensitive data 不被無限制收集

### F12 — Humanized Recovery Orchestration

統一 Recovery State：

~~~text
status
human_message
preserved_context
next_actions
technical_code
~~~

Acceptance：

- 一般 User 不直接看到裸 401 / 402 / 404 / 500
- user input / intent 盡量保留
- retry 有上限
- unsupported capability 誠實呈現
- component failure 局部隔離
- 每個可預期 failure 至少有一個 next action

---

# 6. 1 個月 Release Gate

只有以下 Core Loop 同時成立，第 2–3 個月項目才應升級：

~~~text
Create works
+ Semantic quality measurable
+ Runtime stable
+ Share works
+ Recipient uses
+ Remix works
+ Wrong result / logic can be corrected without restarting
+ Old / new result can be compared or reverted
+ Failure recoverable
+ Evidence collected
~~~

不能因為「程式 build 成功」就視為 Phase 1 完成。

---

# 7. 第 2–3 個月：PMF Deepening

目標：

> **把一次性的成功 App 變成可以 Reuse、Own、Save、Publish 的資產。**

## F08 — Durable Identity / Ownership

~~~text
anonymous_id
→ authenticate
→ ownership claim
→ user_id
~~~

Acceptance：

- existing anonymous artifacts 可安全 claim
- public share 不等於 ownership
- account 不阻擋 First Value
- ownership / permission 與 Blueprint content 分離

## F10 — Blueprint Reuse / Retrieval

優先順序：

~~~text
Exact / structured reuse
→ trusted family reuse
→ semantic retrieval only when evidence exists
~~~

Acceptance：

- reused Blueprint 必須重新做 compatibility / trust check
- retrieval 不可繞過 validation
- reuse correctness 可量測
- fresh compile vs reuse cost 可比較

## F09 — Realtime Room

只有 Social use case 證明需要才做。

模型：

~~~text
Immutable Blueprint
+ Room
+ Presence
+ Mutable Instance State
+ Validated Delta
~~~

Acceptance：

- realtime 不 mutation Blueprint
- disconnected client 有 recovery
- room TTL / persistence 是 policy
- 不把所有 App 強迫 realtime 化

## F13 — Entitlement / Metering，Basic

第 2–3 個月只做必要底座：

- capability cost class
- entitlement metadata
- quota / usage record
- explicit premium boundary

不做完整 marketplace settlement。

Acceptance：

- free / paid capability boundary 可被 Runtime / Gateway 正確 enforce
- cost-bearing action 不能偷偷執行

---

# 8. 第 4–6 個月：Scale Readiness

這段的目標不是做更多 Feature，而是確認 NFF 能安全承接高價值、高成本能力。

## F11 — External Capability Execution

~~~text
Runtime Action
→ Capability Gateway
→ Policy / Entitlement
→ External Provider / Worker
→ Result Validation
→ State Update
~~~

適用：

- runtime AI
- search / data
- media generation
- heavy compute
- external workflow

Acceptance：

- provider secret 不進 Browser
- provider output 視為 untrusted
- timeout / retry / idempotency policy 明確
- cost / latency 被 telemetry
- failure 可回到 Humanized Recovery

## F13 — Entitlement / Metering，Production

增加：

- usage metering
- quota
- premium enforcement
- provider cost attribution
- auditability

Acceptance：

> 使用多少、花多少、誰有權限，必須可重建。

## Scale Readiness Hardening

F01–F12 同時要強化：

- versioning
- compatibility
- recovery quality
- model routing
- trusted reuse
- capability maturity
- failure quarantine
- cost observability

---

# 9. 6 個月後：Platform Expansion

前提是 External / Paid Capability Pilot 已有真實供需 Evidence。

## F14 — Provider Registry / Certification

負責：

- provider identity
- version
- capability contract
- certification
- SLA metadata
- privacy / residency
- trust status

Acceptance：

- third-party provider 不能繞過 Capability Contract
- certification / revocation 可管理
- provider version 可追蹤

## F17 — Heterogeneous Workflow Orchestration

目的：

> **把一個需要多個異質 Capability 的 Intent，變成可追蹤、可恢復、可驗證的 Outcome。**

適用場景：
- 多個 External API 串接
- 長時間 async job
- 跨 Provider workflow
- 需要 retry / timeout / compensation
- 需要人工核准或 Human-in-the-loop
- 部分步驟失敗後仍需安全復原

Canonical flow：

~~~text
Resolved Intent
→ Capability Graph
→ Step Plan
→ Execute Step
→ Validate Result
→ Persist Workflow State
→ Next Step
   ├─ success → continue
   ├─ retryable failure → bounded retry
   ├─ compensatable failure → compensation
   ├─ approval required → human step
   └─ terminal failure → Humanized Recovery
→ Final Validated Outcome
~~~

NFF-owned Orchestration Contract 至少必須描述：

~~~text
workflow_id
workflow_version
steps[]
dependencies
input / output contract
provider / capability reference
timeout_policy
retry_policy
idempotency_key_policy
compensation_action
approval_requirement
status
evidence
~~~

架構規則：
- Temporal、n8n、Queue/Worker 等只能是 execution backend / adapter。
- Vendor workflow DSL 不得成為 Blueprint / Capability 核心語意。
- 每一步 External Output 都視為 untrusted，必須重新驗證。
- Workflow state 是 durable execution truth，不等於 Blueprint 或 Browser Instance。
- 只有真實需求證明需要 multi-step / long-running execution 時才啟用 F17。

Acceptance：
- 任一步驟失敗可定位到 step / provider / attempt。
- retry 有上限且具 idempotency。
- 可補償步驟能安全 rollback / compensate。
- User 可看到 meaningful progress，而不是裸 job state。
- Workflow 失敗不得破壞已完成且不可逆的 durable truth。
- provider / workflow reliability 可 telemetry。
- orchestration backend 可替換，不改 Blueprint / Capability Contract。

## F15 — Transaction / Settlement

負責：

- transaction lifecycle
- idempotency
- payment result
- durable transaction log
- reconciliation
- revenue share
- settlement audit

Acceptance：

> Money path 必須可追蹤、可重放、可對帳，不依賴前端 state 當真實來源。

F14 / F15 / F17 都不改寫 F01–F06 的核心 Intent → Blueprint → Runtime 流程。

F17 只在 Blueprint / Capability Plan 明確需要外部多步執行時加入：

~~~text
Runtime / Capability Action
→ F17 Orchestration
→ External / Async Steps
→ Validated Outcome
→ Runtime / Durable State
~~~

---

# 10. Cross-Function Contracts

有幾個 Contract 不能由單一 Function 私自定義。

## Blueprint Contract

共同依賴：
- F01
- F02
- F03
- F04
- F05
- F06
- F10
- F11

要求：
- immutable canonical form
- schema version
- registry version
- compatibility
- capability references
- support / degradation metadata

## Result Quality / Logic Correction Contract

共同依賴：
- F00
- F01
- F02
- F03
- F06
- F07
- F16

要求：

~~~text
executed result
→ user semantic feedback
→ preserved inputs / old revision
→ correction intent
→ semantic delta
→ full revalidation
→ new immutable revision
→ old/new result comparison
→ accept / refine again / revert
~~~

原則：

- Runtime success 不代表 semantic success。
- correction 不直接修改 Runtime code。
- original Blueprint / result 必須可保留。
- correction outcome 必須成為 Compiler / Reuse / Capability Evidence。

## Recovery Contract

共同依賴：
- F00
- F01
- F02
- F03
- F04
- F05
- F06
- F11
- F12

要求：

~~~text
technical failure
→ classified failure
→ recovery policy
→ preserved context
→ human UX
~~~

## Identity / Ownership Contract

共同依賴：
- F05
- F06
- F07
- F08
- F09
- F10
- F13

要求：
- anonymous use
- account claim
- ownership
- permission
- entitlement
- share access

## Capability Contract

共同依賴：
- F01
- F02
- F03
- F04
- F11
- F13
- F14
- F17

詳細來源：

- working/ProjectManagement/CAPABILITY-FABRIC.md

---

# 11. Acceptance 層級

NodeFF 不允許只用「頁面可以 render」當完成。

每個 Function 至少有四層 Acceptance：

## A. Technical
- code path works
- contract valid
- tests pass

## B. Safety / Reliability
- invalid input bounded
- permission correct
- recovery works
- no forbidden execution path

## C. Semantic / Product
- outcome 符合 user intent
- unsupported case 誠實
- UX 可理解
- User 能指出「結果／邏輯不對」
- correction 後可比較新舊結果並回退
- runtime success 不得被當成 semantic success

## D. Evidence / Economics
- telemetry exists
- success / failure 可量測
- cost 可追蹤
- 能判斷是否值得繼續投資

因此：

> **Build Success ≠ Function Success。**

---

# 12. Release Management

Release 應以 User Outcome，而不是技術 layer 命名。

## Release 1 — Core Loop，0–1 月

~~~text
F00 + F01 + F02 + F03 + F04 + F05 + F06 + F07 + F12 + F16
~~~

Outcome：

> Intent → Correct App → Use → Share → Remix → Correct Result → Recover

## Release 2 — Durable Value，2–3 月

~~~text
F08 + F10
+ F09 if proven
+ F13 Basic
+ hardening of Release 1
~~~

Outcome：

> Reuse → Identity → Ownership → Creator Value

## Release 3 — Scale Readiness，4–6 月

~~~text
F11
+ F13 Production
+ reliability / compatibility / cost hardening
~~~

Outcome：

> External / Paid Capability 可以安全接入

## Continuous Platform Releases，6 月後

~~~text
F14 + F15 + F17
+ provider / commerce / orchestration expansion
~~~

Outcome：

> Intent Commerce / Capability Network / Heterogeneous Orchestration 持續擴張

---

# 13. Design → Development Flow

Canonical lifecycle、Traceability ID、Working → Spec Gate、Acceptance → Test、Runtime Debug 與 Release Gate 的共同規則，以：

- `working/DESIGN-TO-DELIVERY.md`

為唯一 Working Contract。本文件只保留 Function Portfolio、Dependency、Acceptance 層級與 Release Scope，不重複定義 Delivery 規則。


~~~text
Architecture
→ Function Scope
→ Contract
→ Acceptance
→ Dependency Check
→ execution/BACKLOG
→ execution/SPRINT
→ Cursor Implementation
→ Automated / Manual Test
→ Evidence
→ Release
→ CHANGELOG
~~~

只有在以下條件完成後 Function 才應進 Sprint：

1. Scope / Non-Scope 清楚
2. upstream contracts 已知
3. acceptance 可測
4. error / recovery 已設計
5. security / permission 已設計
6. telemetry 已定義
7. phase / dependency 已確認

---

# 14. Detailed Design Guardrails

1. Function 是 User Outcome，不是單純 technical module。
2. Frontend / Backend / Runtime 必須在同一 Function flow 裡一起設計。
3. Architecture 決定邊界，Cursor 不發明新架構。
4. 所有跨 Function Contract 只能有 canonical source。
5. Error / Recovery 是功能本身，不是最後補上的例外。
6. Result Correction 是核心 UX，不是把錯誤 Prompt 叫 User 從頭重做。
7. Runtime Success 不等於 Semantic / Product Success。
8. Capability Gap 是 Evidence，不是用 heuristic 假裝解決。
9. Phase 1 優先完成完整 Core Loop，不追求大量 Capability。
10. 第 2–3 個月才把 Anonymous Value 升成 Durable Identity。
11. 第 4–6 個月才把 External / Paid Capability 提升為正式 execution path。
12. 6 個月後才持續建 Provider / Transaction / Orchestration Network。
13. Workflow engine vendor 只能是 Adapter，不得成為 NFF semantic contract。
14. Multi-step external workflow 必須有 timeout / retry / idempotency / compensation policy。
15. 日期不自動解鎖功能；Evidence Gate 才解鎖。
16. 所有新 Function 必須證明不破壞 Intent → Blueprint → Runtime 核心。

# 結論

APP-DETAILED-DESIGN 的核心不是列出「未來要做什麼」，而是控制：

~~~text
先做什麼
→ 為什麼
→ 依賴什麼
→ 做到什麼算成功
→ 什麼證據才能進下一階段
~~~

NodeFF 的 Function Delivery 順序因此固定為：

~~~text
0–1 月
Core Loop

2–3 月
Reuse / Identity / Creator Value

4–6 月
Scale Readiness / External Paid Capability

6 月後
Intent Commerce / Capability Network / Orchestration 持續擴張
~~~

> **先把核心循環做成可信任產品，再把它變成可累積資產，最後才把它擴張成平台。**
