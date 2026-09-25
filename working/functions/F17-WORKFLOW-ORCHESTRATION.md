# F17 — Heterogeneous Workflow Orchestration

> 狀態：DEFERRED BASELINE — MIGRATED
>
> 本文件在 SSOT Cleanup 中由 `working/APP-DETAILED-DESIGN-OVERVIEW.md` 的既有 Function 級內容搬入。此次搬移 **不改產品架構、不新增功能決策**；只是把既有 Current Truth 放回單一 Function canonical home。
>
> Horizon：6 月後，Evidence-gated
>
> Delivery 規則：`working/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/APP-DETAILED-DESIGN-OVERVIEW.md`

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

# Status Note

此文件目前是從既有 Portfolio 文件搬出的 Working 內容，**不因搬家自動升格為完整 Function Spec / BUILD_FREEZE_READY**。後續 Detailed Design 仍需依 Design-to-Delivery Contract 補齊缺少的 UI / API / Data / Error / Security / Evidence / Acceptance 等部分。
