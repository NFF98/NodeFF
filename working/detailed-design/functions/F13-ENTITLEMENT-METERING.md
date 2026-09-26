# F13 — Entitlement / Metering

> 狀態：DEFERRED_BASELINE / NOT_BUILD_FREEZE_READY
>
> Activation Gate：日期本身不 unlock；只有 Evidence + Human approval + complete Detailed Design + Build Freeze inclusion 才可進 implementation scope。
>
> Horizon：2–6 月
>
> Delivery 規則：`working/common-core/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/detailed-design/APP-DETAILED-DESIGN-OVERVIEW.md`

# 1. Migrated Current Truth

## Basic — 2–3 月

第 2–3 個月只做必要底座：

- capability cost class
- entitlement metadata
- quota / usage record
- explicit premium boundary

不做完整 marketplace settlement。

Acceptance：

- free / paid capability boundary 可被 Runtime / Gateway 正確 enforce
- cost-bearing action 不能偷偷執行

## Production — 4–6 月

增加：

- usage metering
- quota
- premium enforcement
- provider cost attribution
- auditability

Acceptance：

> 使用多少、花多少、誰有權限，必須可重建。

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
