# F13 — Entitlement / Metering

> 狀態：DEFERRED_BASELINE / NOT_BUILD_FREEZE_READY
>
> Activation Gate：日期本身不 unlock；只有 Evidence + Human approval + complete Detailed Design + Build Freeze inclusion 才可進 implementation scope。
>
> Horizon：Phase 3+ / evidence-gated（earliest activation after Phase 2 evidence）
>
> Delivery 規則：`working/common-core/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/detailed-design/APP-DETAILED-DESIGN-OVERVIEW.md`

# 1. Migrated Current Truth

## Activation Baseline — Phase 3+

Phase 2 可在 Capability Fabric保留 **non-enforcing** cost / entitlement compatibility metadata，但 **F13 本身不啟用**。

F13 activation至少包含：

- entitlement policy / scope；
- quota / usage record；
- explicit premium boundary；
- usage metering；
- premium enforcement；
- provider cost attribution；
- auditability。

不因 metadata存在就宣稱 premium system已啟用，也不先做完整 marketplace settlement。

Acceptance：

- free / paid capability boundary 可被 Runtime / Gateway 正確 enforce；
- cost-bearing action 不能偷偷執行；
- 使用多少、花多少、誰有權限可重建；
- enforcement / metering failure不可 silently allow paid execution。

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
