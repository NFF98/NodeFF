# F11 — External Capability Execution

> 狀態：DEFERRED_BASELINE / NOT_BUILD_FREEZE_READY
>
> Activation Gate：日期本身不 unlock；只有 Evidence + Human approval + complete Detailed Design + Build Freeze inclusion 才可進 implementation scope。
>
> Horizon：4–6 月
>
> Delivery 規則：`working/common-core/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/detailed-design/APP-DETAILED-DESIGN-OVERVIEW.md`

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
