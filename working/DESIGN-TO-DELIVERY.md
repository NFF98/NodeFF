# NodeFF Design-to-Delivery Contract

> 狀態：Working Baseline。本文定義 NodeFF 從設計到開發、測試、除錯、Release 與 Evidence 回饋的共同規則。所有 Function（Fxx）都必須遵守本 Contract；未通過對應 Gate 的內容不得跳級進入下一階段。

# 1. Purpose

NodeFF 的設計不能停在文件，也不能讓 Cursor 在實作時自行發明產品或架構決策。

Canonical lifecycle：

~~~text
Discussion
→ Working Design
→ Review
→ Spec
→ Backlog
→ Sprint
→ Cursor Implementation
→ Test
→ Runtime Debug / Evidence
→ Release
→ Production Evidence
→ Design / Spec Improvement
~~~

核心原則：

> 後一階段應由前一階段的已批准內容派生，不重新發明需求。

---

# 2. Current Truth / Source of Truth

NodeFF 區分四種資訊：

~~~text
Discussion
= 思考、比較、未定方案

Working
= 目前最新設計答案，可持續修改

Spec
= 已 Review、可直接開發的正式 Contract

Execution
= 從 Spec 派生出的實作工作與 Sprint
~~~

同一件事在同一層級只能有一個 Current Truth。

例如 Share 曾討論 A / B / C，若目前決定 B：

~~~text
Discussion = A / B / C 都可保留
Working = 只描述目前採 B
Spec = Review 後正式批准 B
Code / Test = 只能實作 B
~~~

Chat / Discussion 不是 implementation source。

---

# 3. Canonical Document Responsibilities

~~~text
working/APP-ARCHITECTURE.md
→ system boundary / top architecture

working/APP-DETAILED-DESIGN.md
→ Function Portfolio / dependency / release scope

working/DATA-MODEL.md
→ shared canonical data model

working/ProjectManagement/CAPABILITY-FABRIC.md
→ capability semantic contract

working/functions/Fxx-*.md
→ single Function end-to-end detailed design

spec/
→ reviewed implementation contracts

execution/
→ backlog / sprint / changelog generated from approved Spec
~~~

不得為 Frontend / Backend / DB 再建立彼此割裂的平行主規格。

---

# 4. Function Design Unit

NodeFF 的基本設計、開發、測試、Debug、Release 追蹤單位是 Function。

每個 Fxx 必須完整串通：

~~~text
User Outcome
→ User Flow
→ UI / UX
→ Frontend State
→ Data / DB
→ API
→ Backend Processing
→ Capability / Runtime
→ Error / Recovery
→ Security / Permission
→ Telemetry / Evidence
→ Acceptance / Test
~~~

若其中任何必要環節未定義，Function 不得標記為 Ready for Spec。

---

# 5. Lifecycle States

每個 Function 使用以下狀態：

~~~text
DRAFT
→ REVIEW
→ WORKING_BASELINE
→ SPEC_READY
→ IN_IMPLEMENTATION
→ IMPLEMENTED
→ TESTED
→ RELEASE_READY
→ RELEASED
→ EVIDENCE_REVIEW
~~~

定義：

- DRAFT：仍有重大未決設計。
- REVIEW：內容已可完整審查。
- WORKING_BASELINE：目前 Working Current Truth。
- SPEC_READY：UX / Data / API / Backend / Runtime / Error / Security / Evidence / Acceptance 全部串通並完成 Review。
- IN_IMPLEMENTATION：已進 Sprint，Cursor 可執行。
- IMPLEMENTED：Code path 已完成，但尚未代表測試或產品成功。
- TESTED：Required Acceptance 對應測試已通過。
- RELEASE_READY：Release Gate 全部通過。
- RELEASED：已正式發佈。
- EVIDENCE_REVIEW：使用 Production Evidence 評估改善。

不得因為 Build 成功直接從 IMPLEMENTED 跳到 RELEASED。

---

# 6. Stable Traceability IDs

所有正式設計項目必須使用穩定 ID。

建議格式：

~~~text
F01-RQ-001    Requirement
F01-UX-001    UX behavior / state
F01-DATA-001  Data contract
F01-API-001   API contract
F01-POL-001   Policy / decision rule
F01-ERR-001   Error class
F01-EVT-001   Telemetry / Evidence event
F01-SEC-001   Security / Permission rule
F01-AC-001    Acceptance criterion
TEST-F01-001  Test case / suite mapping
~~~

ID 一旦進 Spec 不應重編號；被淘汰時標記 deprecated / superseded，不重用舊 ID。

---

# 7. Working → Spec Gate

Function 只有在以下項目全部完成時才可由 Working 升格為 Spec：

~~~text
Scope / Non-Scope
User Flow
UI / UX
Frontend State
Data / DB read-write
API / Contract
Backend / Runtime processing
Capability dependency
Error / Recovery
Security / Permission
Telemetry / Evidence
Acceptance Criteria
Dependency / Compatibility
Open Decisions = 無 blocker
~~~

升格規則：

1. Working 是可修改 Current Truth。
2. Spec 是批准後的 implementation contract。
3. 升格不是重新改寫需求，而是固定已 Review 的 Working。
4. Spec 變更必須留下可追蹤 change。
5. Cursor 不得以 Chat 討論覆蓋 Spec。

---

# 8. Spec → Backlog / Sprint

Backlog 與 Sprint 必須由 Spec 派生。

每個 execution item 至少要能指回：

~~~text
Function ID
Requirement ID(s)
Acceptance ID(s)
Dependency
Implementation scope
Test expectation
~~~

不得建立無 Spec / 無 Acceptance 的 implementation task，除非明確標記為 spike / experiment，且不得被當成正式 product behavior。

---

# 9. Acceptance → Executable Test

Acceptance 是 Test 的來源，不是 Release 前才補的文字。

例如：

~~~text
F02-AC-007
Unknown capability must never enter Runtime.
~~~

至少對應：

~~~text
TEST-F02-007-A
unknown capability ID → validation rejected

TEST-F02-007-B
unsupported capability version → rejected / incompatible
~~~

每個 Critical Acceptance 必須有 automated test 或明確記錄為 manual / runtime evidence test，且說明原因。

規則：

> Test 驗證 Spec，不重新發明需求。

---

# 10. Executable Policy / Decision Table

Deterministic product policy 必須同時具備：

~~~text
Human-readable rule
+ stable Policy ID
+ machine-executable implementation
+ mapped tests
+ telemetry evidence where relevant
~~~

例如 F01 Clarification Policy：

~~~text
F01-POL-CP-001
Required execution value missing + no safe default
→ NEEDS_CLARIFICATION
~~~

應對應：

~~~text
implementation rule
→ TEST-F01-CP-001-*
→ telemetry policy_rule_id = F01-POL-CP-001
~~~

LLM 不得覆蓋 deterministic policy result。

---

# 11. Runtime Debug Traceability

Runtime failure 不應只有 stack trace。

可觀測資料在可行時至少應能指向：

~~~text
request / session
Function
Blueprint hash / revision
Capability ID / version
Runtime stage
Error Class
Recovery Policy
related Requirement / Acceptance when applicable
~~~

例如：

~~~text
function_id = F03
capability_id = game.timer@1
runtime_stage = EFFECT
error_code = F03-ERR-012
recovery_policy = F12-POL-004
~~~

Stack trace 是工程資訊，不是 Consumer UX。

---

# 12. Error / Recovery Contract

每個預期 failure 必須：

1. 有 stable Error ID / class。
2. 指明 retryable / terminal。
3. 指明哪些 context 必須保留。
4. 對應 Humanized Recovery。
5. 至少提供一個有效 next action，除非確實無法繼續。
6. 需要時產生 telemetry evidence。

一般 User 不直接看到裸工程錯誤碼。

---

# 13. Evidence Contract

Telemetry 不是附加功能。

每個 Function 在 Design 階段就必須定義哪些 Evidence 用來回答：

~~~text
Did it work technically?
Did it match user intent?
Did recovery work?
Was the function useful?
What did it cost?
Should we improve / expand / stop?
~~~

Evidence event 必須可追蹤到 Function；必要時追蹤 Requirement / Policy / Capability。

不得為方便 Debug 無限制收集敏感資料。

---

# 14. Release Gate

Function / Release 只有在所有 Required Gate 通過時才能 Release：

~~~text
Required Spec approved
+ Required implementation complete
+ Acceptance tests pass
+ security / permission checks pass
+ compatibility / migration checks pass
+ runtime smoke tests pass
+ Humanized Recovery verified
+ required telemetry exists
+ known blockers = 0
~~~

Release Scope 由 APP-DETAILED-DESIGN.md 定義，不以「Code 已完成」取代 Release Gate。

---

# 15. Post-Release Evidence Loop

Release 不是終點。

~~~text
Production Evidence
→ Detect mismatch / failure / friction
→ Trace to Function / Policy / Capability
→ Working Design Delta
→ Review
→ Spec Change when approved
→ Implementation / Test / Release
~~~

Evidence 可以改變設計，但不得直接繞過 Working / Spec 修改 Production contract。

---

# 16. Change Control

設計變更分三類：

## Minor
不改 user outcome / public contract / data compatibility。

→ 可直接更新 Working，保留 change trace。

## Material
改變 UX flow、API、Data、Runtime semantics、Acceptance、Security、Compatibility。

→ 必須重新 Review 受影響 Function / Shared Contract。

## Architecture-impacting
改變 Top Architecture、system boundary、Capability trust boundary、Blueprint model、Infra truth boundary。

→ 必須先指出衝突 / 缺口，不可在 Function 文件中偷偷改方向。

---

# 17. Cursor Contract

Cursor 的責任：

~~~text
Read approved Spec
→ implement exactly defined scope
→ preserve contracts
→ write / update mapped tests
→ report deviations / blockers
→ update execution records
~~~

Cursor 不負責：

- 發明產品行為
- 改 Top Architecture
- 自創 API / DB contract
- 用實作方便性覆蓋 Acceptance
- 把 unresolved design 當成 coding choice

若 Spec 有矛盾或缺口，應回到 Design，而不是在 Code 中默默決策。

---

# 18. Software Engineering Guardrails

NodeFF Detailed Design 與 Delivery 從 Day 1 遵守：

- Requirement traceability
- Contract-first design
- Versioned schema / policy
- Explicit acceptance
- Backward compatibility awareness
- Security by design
- Observability by design
- Testability
- Failure / recovery design
- Deterministic policy where required
- Change control
- No arbitrary generated code
- No hidden product decision in implementation

---

# 19. Phase 1 Application

0–1 月 Core Release 的 Functions：

~~~text
F00
F01
F02
F03
F04
F05
F06
F07
F12
F16
~~~

全部遵守本 Contract。

中長期 Function 可以保留 compatibility metadata，但不得因本 Contract 提前進入 Implementation。

---

# 20. Definition of Done

一個 Function 的 Definition of Done 不是「頁面會跑」。

最低標準：

~~~text
Spec approved
+ Implementation mapped to Spec
+ Required tests mapped to Acceptance
+ Error / Recovery verified
+ Security verified
+ Evidence instrumentation verified
+ Release Gate passed
+ Production Evidence can be traced back
~~~

因此：

> Build Success ≠ Function Success。
>
> Runtime Success ≠ Semantic Success。
>
> Release ≠ Learning Complete。

# 21. CT Commit / Revert Rule

每一次會改變 GitHub Current Truth 的更新，都必須有一個可辨識、可回退的 commit point。

每次更新後，對 User 的說明至少包含：

~~~text
Commit
→ 哪個 commit

Changed
→ 改了什麼

Why
→ 為什麼改

Impact
→ 影響哪些 Current Truth / Function / downstream work

Revert
→ 如果方向不對，要回到哪個 commit / 哪個變更前狀態
~~~

規則：

1. commit message 必須是人可以理解的 change summary，不使用無意義訊息。
2. 一個 commit 優先只承載一個 coherent design change。
3. Material / Architecture-impacting change 不與無關 cleanup 混在同一 commit。
4. User Review 後若方向不對，可依 commit boundary revert / forward-fix。
5. Revert 不代表刪除討論歷史；只代表 Current Truth 回到先前 approved state。
6. 每次 GitHub Working 更新後，ChatGPT 必須提供白話 commit 說明與 rollback point。

---

# 22. Detailed Design All-Picture Completion Matrix

此 Matrix 是 0–1 月 Detailed Design 的進度總覽。它追蹤「Current Working Baseline 是否已建立」，不等於已升格 Spec / Implemented / Released。

## 22.1 Established Baselines

| Area | Status | Canonical Location | Role |
|---|---|---|---|
| Top Architecture | ✅ STABLE_BASELINE | `working/APP-ARCHITECTURE.md` | system boundary |
| Product Boundary | ✅ STABLE_BASELINE | `working/ProjectManagement/BUSINESS-PLAN.md` + Architecture | product / evidence boundary |
| Function Portfolio | ✅ STABLE_BASELINE | `working/APP-DETAILED-DESIGN.md` | Fxx scope / dependency |
| Release Scope | ✅ STABLE_BASELINE | `working/APP-DETAILED-DESIGN.md` | 0–1 / 3 / 6 month scope |
| Infra Boundary | ✅ STABLE_BASELINE | `working/INFRA-ARCHITECTURE.md` | Browser / Edge / Postgres / External |
| Capability Philosophy | ✅ STABLE_BASELINE | `working/ProjectManagement/CAPABILITY-FABRIC.md` | capability boundary / maturity |
| Design-to-Delivery | ✅ STABLE_BASELINE | `working/DESIGN-TO-DELIVERY.md` | Working → Spec → Test → Release rules |

## 22.2 Detailed Design Gaps

| Area | Status | Canonical Location | Main Dependency |
|---|---|---|---|
| Canonical Data Model | ✅ WORKING_BASELINE | `working/DATA-MODEL.md` | Architecture + Infra + Delivery Contract |
| Executable Blueprint | ✅ WORKING_BASELINE | `working/functions/F02-BLUEPRINT-VALIDATION.md` canonical Blueprint section | Data Model + F04 Registry |
| Concrete Registry | ✅ WORKING_BASELINE | `working/functions/F04-CAPABILITY-REGISTRY.md` | Capability Fabric + Data Model |
| API Contracts | 🟡 DRAFT | Phase 1 core public/API boundaries established in F01 + F05 + F06 + F07 + F16; F12 uses internal recovery interfaces; deferred Fxx pending | Data Model + Function flow |
| UX State Machines | 🟡 DRAFT | Phase 1 core UX baselines established across F00 + F05 + F06 + F12 + F16; deferred Fxx UX pending | Function flow + Error / Recovery |
| Runtime Semantics | ✅ WORKING_BASELINE | `working/functions/F03-RUNTIME-EXECUTION.md` | Blueprint + Registry |
| Error Taxonomy | ✅ WORKING_BASELINE | F12 shared recovery taxonomy + Phase 1 core F00–F07/F16 source error mappings | Runtime / API / UX |
| Evidence Schema | ✅ WORKING_BASELINE | `working/functions/F07-ANONYMOUS-IDENTITY-EVIDENCE.md` common envelope / ingestion / privacy / retention; each Fxx owns event meaning | Data Model + Function Acceptance |
| Function Specs | 🟡 DRAFT | `working/functions/Fxx-*.md` | all required shared contracts |
| Executable Acceptance | ❌ NOT_STARTED | each Fxx Acceptance + mapped tests | Function contracts + Delivery Contract |

## 22.3 Dependency Order

~~~text
Canonical Data Model
        ↓
Concrete Registry
        ↓
Executable Blueprint
        ↓
Runtime Semantics
        ↓
F01 Compilation / API
        ↓
F00 UX State Machine
        ↓
Share / Remix / Identity-Evidence / Recovery / Correction
        ↓
Complete Function Specs
        ↓
Executable Acceptance
        ↓
Working → Spec Gate
~~~

這不是禁止平行設計；而是避免 downstream 文件自行發明 upstream contract。

## 22.4 Status Meaning

~~~text
❌ NOT_STARTED
= 尚未建立 canonical Working design

🟡 DRAFT
= 已開始，但仍有 blocker / major open decision

✅ WORKING_BASELINE
= 已建立目前 Current Truth，可供 downstream design 引用，但尚未代表 Spec

✅ SPEC_READY
= Function / shared contract 已完成 Review，可升格正式 Spec
~~~

任何 status change 都必須伴隨對應 GitHub commit，並依 §21 提供白話 change / impact / revert 說明。

---

# Conclusion

NodeFF 的 Delivery 原則只有一句：

> **每個產品決策都能一路追到 Code / Test / Runtime Evidence；每個 Production 問題也能一路追回答案與設計。**

這份文件是 Working 階段的共同 Delivery Contract。未來所有 Function 詳細設計、Spec 升格、Execution、Test、Debug、Release 都以此為共同規則。
