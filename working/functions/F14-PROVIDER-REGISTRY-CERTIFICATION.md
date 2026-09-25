# F14 — Provider Registry / Certification

> 狀態：DEFERRED BASELINE — MIGRATED
>
> 本文件在 SSOT Cleanup 中由 `working/core/APP-DETAILED-DESIGN-OVERVIEW.md` 的既有 Function 級內容搬入。此次搬移 **不改產品架構、不新增功能決策**；只是把既有 Current Truth 放回單一 Function canonical home。
>
> Horizon：6 月後
>
> Delivery 規則：`working/core/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/core/APP-DETAILED-DESIGN-OVERVIEW.md`

# 1. Migrated Current Truth

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

# Status Note

此文件目前是從既有 Portfolio 文件搬出的 Working 內容，**不因搬家自動升格為完整 Function Spec / BUILD_FREEZE_READY**。後續 Detailed Design 仍需依 Design-to-Delivery Contract 補齊缺少的 UI / API / Data / Error / Security / Evidence / Acceptance 等部分。
