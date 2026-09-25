# F11 — External Capability Execution

> 狀態：DEFERRED BASELINE — MIGRATED
>
> 本文件在 SSOT Cleanup 中由 `working/core/APP-DETAILED-DESIGN-OVERVIEW.md` 的既有 Function 級內容搬入。此次搬移 **不改產品架構、不新增功能決策**；只是把既有 Current Truth 放回單一 Function canonical home。
>
> Horizon：4–6 月
>
> Delivery 規則：`working/core/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/core/APP-DETAILED-DESIGN-OVERVIEW.md`

# 1. Migrated Current Truth

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

# Status Note

此文件目前是從既有 Portfolio 文件搬出的 Working 內容，**不因搬家自動升格為完整 Function Spec / BUILD_FREEZE_READY**。後續 Detailed Design 仍需依 Design-to-Delivery Contract 補齊缺少的 UI / API / Data / Error / Security / Evidence / Acceptance 等部分。
