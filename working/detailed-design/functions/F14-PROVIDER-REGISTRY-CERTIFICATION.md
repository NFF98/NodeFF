# F14 — Provider Registry / Certification

> 狀態：DEFERRED_BASELINE / NOT_BUILD_FREEZE_READY
>
> Activation Gate：日期本身不 unlock；只有 Evidence + Human approval + complete Detailed Design + Build Freeze inclusion 才可進 implementation scope。
>
> Horizon：6 月後
>
> Delivery 規則：`working/common-core/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/detailed-design/APP-DETAILED-DESIGN-OVERVIEW.md`

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
