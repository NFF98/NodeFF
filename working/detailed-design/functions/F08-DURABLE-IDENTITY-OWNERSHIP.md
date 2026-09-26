# F08 — Durable Identity / Ownership

> 狀態：DEFERRED_BASELINE / NOT_BUILD_FREEZE_READY
>
> Activation Gate：日期本身不 unlock；只有 Evidence + Human approval + complete Detailed Design + Build Freeze inclusion 才可進 implementation scope。
>
> Horizon：2–3 月
>
> Delivery 規則：`working/common-core/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/detailed-design/APP-DETAILED-DESIGN-OVERVIEW.md`

# 1. Migrated Current Truth

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

# 2. Additional Existing Cross-Function Truth

共同依賴：
- F05
- F06
- F07
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
