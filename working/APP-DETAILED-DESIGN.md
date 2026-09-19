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

    F08[F08 Identity / Ownership]
    F09[F09 Realtime]
    F10[F10 Reuse / Retrieval]
    F13[F13 Entitlement / Metering]

    F11[F11 External Capability]
    F14[F14 Provider Registry]
    F15[F15 Transaction / Settlement]

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

Acceptance：

- User 不必理解 Prompt Engineering
- 從 Capsule 可以直接進 Create
- failure 不清空輸入
- recovery action 明確

### F01 — Intent Compilation + Model Gateway

負責：

~~~text
Intent
→ semantic understanding
→ capability coverage
→ capability selection
→ composition
→ Blueprint Candidate
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

### F07 — Anonymous Identity & Evidence

最小 identity：

- random first-party anonymous_id
- session / intent / blueprint / share linkage

只收 meaningful events：

- compile outcome
- semantic mismatch
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

這些 Function 不改寫 F01–F06 的核心 Intent → Blueprint → Runtime 流程。

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
F00 + F01 + F02 + F03 + F04 + F05 + F06 + F07 + F12
~~~

Outcome：

> Intent → Correct App → Use → Share → Remix → Recover

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
F14 + F15
+ provider / commerce expansion
~~~

Outcome：

> Intent Commerce / Capability Network 持續擴張

---

# 13. Design → Development Flow

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
6. Capability Gap 是 Evidence，不是用 heuristic 假裝解決。
7. Phase 1 優先完成完整 Core Loop，不追求大量 Capability。
8. 第 2–3 個月才把 Anonymous Value 升成 Durable Identity。
9. 第 4–6 個月才把 External / Paid Capability 提升為正式 execution path。
10. 6 個月後才持續建 Provider / Transaction Network。
11. 日期不自動解鎖功能；Evidence Gate 才解鎖。
12. 所有新 Function 必須證明不破壞 Intent → Blueprint → Runtime 核心。

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
Intent Commerce / Capability Network 持續擴張
~~~

> **先把核心循環做成可信任產品，再把它變成可累積資產，最後才把它擴張成平台。**
