# F17 — Heterogeneous Workflow Orchestration

> 狀態：DEFERRED_BASELINE / NOT_BUILD_FREEZE_READY
>
> Activation Gate：日期本身不 unlock；只有 Evidence + Human approval + complete Detailed Design + Build Freeze inclusion 才可進 implementation scope。
>
> Horizon：6 月後，Evidence-gated
>
> Delivery 規則：`working/common-core/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/detailed-design/APP-DETAILED-DESIGN-OVERVIEW.md`

# 1. Migrated Current Truth

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

appf2-owned Orchestration Contract 至少必須描述：

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

# Status Note

此文件是 intentional deferred baseline，不是 Phase 1 / current Build Freeze input。

啟用前必須補齊與 Review：
- UI / UX（若有 User-facing surface）；
- API / Interface；
- Data / lifecycle；
- Error / Recovery / timeout / retry；
- Security / Permission / Privacy；
- Evidence / observability；
- Acceptance / expected observable；
- compatibility / versioning；
- unresolved decisions = 0 blockers。

缺少的 Product Design 不得由 appf2-build / Cursor自行補決策。
