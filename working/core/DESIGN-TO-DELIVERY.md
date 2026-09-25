# NodeFF Design-to-Delivery Contract

> 狀態：CURRENT GOVERNANCE。
>
> `spec/` / Formal Spec / Working → Spec / Spec Promotion / Formal Spec Refresh 模型已 **RETIRED / NO-USE**。
>
> Current flow：**NodeFF Working → Human-approved Build Freeze → NFFBuild immutable BS-* → Delivery**。

# 1. Purpose

NodeFF 的設計不能停在 Chat，也不能讓 Cursor 在實作時自行發明產品或架構決策。

Canonical lifecycle：

```text
Discussion
→ NodeFF Working Design
→ Review / Consistency / Delta / Acceptance / UI Audit
→ Human approval
→ Build Freeze
→ NFFBuild Locked Build Spec
→ Backlog
→ Sprint
→ Cursor Implementation
→ Test / Evidence
→ Release
→ Production Evidence
→ NodeFF Working Improvement
```

核心原則：

> 後一階段由前一階段的已批准內容派生，不重新發明需求。

# 2. Current Truth / Source of Truth

```text
Discussion
= 思考、比較、未定方案

NodeFF Working
= 唯一可修改 Product Design Current Truth

NFFBuild Locked BS-*
= 某一 approved Working commit 的 immutable implementation snapshot

NFFBuild Delivery
= Backlog / Sprint / Code / Test / Evidence / Release
```

不存在 NodeFF 內部第二份 Formal Spec Current Truth。

# 3. Canonical Document Responsibilities

```text
working/core/APP-ARCHITECTURE.md
→ system boundary / top architecture

working/core/APP-DETAILED-DESIGN-OVERVIEW.md
→ Function Portfolio / dependency / phase / release scope

working/core/DATA-MODEL.md
→ shared canonical data model

working/core/API-CONVENTIONS.md
→ shared public API transport / control contract

working/core/EXECUTION-ADMISSION.md
→ fresh Blueprint trust / compatibility execution gate

working/core/ACCEPTANCE-CONVENTIONS.md
→ shared Acceptance → Test conventions

working/registries/
→ machine-readable Recovery / Evidence / Acceptance contracts

working/core/CAPABILITY-FABRIC.md
→ capability semantic contract

working/functions/Fxx-*.md
→ single Function end-to-end detailed Product Design truth

working/UI-UX/
→ screen composition / visual hierarchy / responsive / presentation truth

NFF98/NFFBuild/build-spec/baselines/BS-*
→ Human-approved immutable implementation snapshot

NFF98/NFFBuild/delivery/
→ backlog / sprint / evidence execution

NFF98/NFFBuild/releases/
→ release execution
```

UI/UX 文件不得自行改寫 Function behavior semantics。需要改 Product behavior / state semantics / API / Data / Runtime 時，必須先回對應 Working canonical owner。

# 4. Function Design Unit

每個 Fxx 應完整串通：

```text
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
```

缺少 implementation 必需 contract 時，不得進 Build Freeze。

# 5. Working Maturity

建議使用：

```text
DRAFT
→ REVIEW
→ WORKING_BASELINE
→ BUILD_FREEZE_READY
```

舊 `SPEC_READY` 名稱只代表歷史治理狀態；**NO-USE 作為現行 authority gate**。

`BUILD_FREEZE_READY` 代表：
- required product semantics 已閉合；
- Acceptance/Test mapping 已足夠；
- blocking open decisions = 0；
- 可以進 Human Build Freeze Review。

它不等於 implemented / tested / released。

# 6. Stable Traceability IDs

正式設計項目使用 stable IDs，例如：

```text
F01-RQ-001
F01-UX-001
F01-DATA-001
F01-API-001
F01-POL-001
F01-ERR-001
F01-EVT-001
F01-SEC-001
F01-AC-001
TEST-F01-001
```

ID 不重用。淘汰時標記 deprecated / superseded，不重編造成 traceability 斷裂。

# 7. Build Freeze Gate

進入 Build Freeze 前必須確認：

```text
Scope / Non-Scope
User Flow
UI / UX
Frontend State
Data / DB
API / Contract
Backend / Runtime
Capability dependency
Error / Recovery
Security / Permission
Telemetry / Evidence
Acceptance / Test
Dependency / Compatibility
Open Decisions = 無 blocker
Phase Boundary
```

規則：

1. Working 是唯一可修改 Current Truth。
2. Build Freeze 只能固定已 Review 的 Working，不重新改寫需求。
3. **沒有 User 明確批准，不得建立或啟用 NFFBuild BS-*。**
4. Freeze 必須記 exact NodeFF source commit。
5. Freeze inventory 必須列出 included Function / Shared / UI-UX / Registry files。
6. NFFBuild baseline merge 後 immutable。
7. 後續 semantic change 必須回 NodeFF Working，再建立新 baseline；不得改舊 baseline。

# 8. Build Spec → Backlog / Sprint

NFFBuild Backlog / Sprint 必須由 active Locked Build Spec 派生。

每個 work item 至少可追蹤：

```text
Build Spec ID
Function ID
Requirement / Contract ID(s)
Acceptance ID(s)
Test ID(s)
Dependency
Implementation scope
```

不得讓 Cursor 從 Chat 或未批准 Working delta 建正式 implementation task。

# 9. Acceptance → Executable Test

Acceptance 是 Test 的來源。

每個 Critical Acceptance 必須有 automated test，或明確標記 manual / runtime evidence test 並說明原因。

規則：

> Test 驗證 frozen Build Spec，不重新發明 Product Truth。

# 10. Executable Policy

Deterministic policy 應具有：

```text
Human-readable rule
+ stable Policy ID
+ machine-executable implementation
+ mapped tests
+ telemetry evidence where relevant
```

LLM 不得覆蓋 deterministic policy result。

# 11. Runtime Debug Traceability

Runtime failure 在可行時應能追蹤：

```text
request / session
Build Spec
Sprint / Task
Function
Blueprint hash / revision
Capability ID / version
Runtime stage
Error Class
Recovery Policy
Acceptance / Test
```

Stack trace 是工程資訊，不是 Consumer UX。

# 12. Error / Recovery Contract

預期 failure 應：
1. 有 stable Error ID / class。
2. 指明 retryable / terminal。
3. 指明 preserve context。
4. 對應 Humanized Recovery。
5. 有有效 next action，除非確實無法繼續。
6. 需要時產生 telemetry evidence。

# 13. Evidence Contract

每個 Function 在 Working Design 階段就應定義 Evidence，用來回答：

```text
Did it work technically?
Did it match user intent?
Did recovery work?
Was the function useful?
What did it cost?
Should we improve / expand / stop?
```

不得為 Debug 無限制收集敏感資料。

# 14. Release Gate

Release authority 在 `NFF98/NFFBuild`。

Release 至少要求：

```text
Locked Build Spec
+ required implementation complete
+ Acceptance tests pass
+ security / permission checks pass
+ compatibility checks pass
+ runtime smoke tests pass
+ Humanized Recovery verified
+ required evidence exists
+ known blockers = 0
+ required User release approval
```

Build Success ≠ Release。

# 15. Production Evidence Loop

```text
Production Evidence
→ detect mismatch / failure / friction
→ trace to Function / Policy / Capability
→ NodeFF Working Delta
→ Human review / approval
→ new Build Freeze / Rebaseline when implementation truth changes
→ NFFBuild delivery
```

Evidence 不得直接改 Production contract。

# 16. Change Control / Design Delta

### Minor
不改 user outcome / public contract / data compatibility。

→ 更新 canonical Working，保留 change trace。

### Material
改 UX flow、API、Data、Runtime semantics、Acceptance、Security、Compatibility。

→ Review affected Working owners；Human approval 後才能進下一次 Build Freeze。

### Architecture-impacting
改 Top Architecture、system boundary、Capability trust boundary、Blueprint model、Infra truth boundary。

→ 必須先在 NodeFF Working 解決，不可在 NFFBuild / Cursor 偷做。

若 implementation 發現 Material issue：

```text
NFFBuild Finding
→ NodeFF Working
→ Human approval
→ new BS-* Rebaseline
→ rebind backlog / sprint
```

# 17. Cursor Contract

Cursor：

```text
Read active NFFBuild Locked Build Spec
→ work only on active Sprint task
→ preserve contracts
→ write/update mapped tests
→ record evidence
→ report Finding / blocker
```

Cursor 不得：
- 發明產品行為
- 改 Top Architecture
- 自創 API / DB contract
- 用實作方便性覆蓋 Acceptance
- 直接修改 locked Build Spec
- 由 raw demand 建 Product Truth

# 18. Software Engineering Guardrails

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

# 19. Per-Phase Application

Design-to-Delivery governance 本身跨 Phase 共用，不為 Phase 2 / 3 複製另一份流程。

每次 Build Freeze 必須從 Product Roadmap 與 Function Portfolio 明確選定該次 Phase scope。

Current Phase 1 / NOW BUILD：

```text
F00 F01 F02 F03 F04 F05 F06 F07 F12 F16
```

Canonical Phase scope：
- Product / Business：`working/ProjectManagement/roadmap/PHASE-1.md`
- Architecture：`working/architecture/evolution/PHASE-1.md`
- Infrastructure：`working/infrastructure/PHASE-1.md`
- Data：`working/data-model/PHASE-1.md`
- Capability：`working/ProjectManagement/capability-roadmap/PHASE-1.md`
- Function portfolio：`working/core/APP-DETAILED-DESIGN-OVERVIEW.md`

中長期 module 可以先存在作 deferred design，但 **未經 Evidence Gate + Human approval + Build Freeze inclusion 就不是 implementation scope**。

# 20. Definition of Done

一個 Function 的完成不是「頁面會跑」。

```text
Approved Build Spec
+ implementation mapped
+ Acceptance/Test passed
+ Error / Recovery verified
+ Security verified
+ Evidence verified
+ Release Gate passed
+ Production Evidence可回溯
```

# 21. Commit / Revert Rule

每次改變 GitHub Current Truth 的更新，都要有可辨識、可回退 commit。

回報至少包含：

```text
Commit
Changed
Why
Impact
Revert
```

Material / Architecture-impacting change 不與無關 cleanup 混在同一 commit。

# 22. Retired Governance Notice

以下模型已 **RETIRED / NO-USE**：

```text
Working → Formal Spec → NodeFF Backlog / Sprint
spec/functions/
spec/shared/
Formal Spec Refresh
Spec Promotion
```

歷史 Audit / Re-Audit / Closure Report 可以保留上述文字作歷史證據，但不得作 Current Governance。

Current model only：

```text
NodeFF Working
→ Human-approved Build Freeze
→ NFFBuild immutable BS-*
→ NFFBuild Delivery
```
