# F15 — Transaction / Settlement

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

- transaction lifecycle
- idempotency
- payment result
- durable transaction log
- reconciliation
- revenue share
- settlement audit

Acceptance：

> Money path 必須可追蹤、可重放、可對帳，不依賴前端 state 當真實來源。

F14 / F15 / F17 都不改寫 F01–F06 的核心 Intent → Blueprint → Runtime 流程。

F15 只擁有 transaction / settlement truth；若 transaction path需要 heterogeneous multi-step orchestration，F15只引用 F17 validated outcome，F17 flow / retry / compensation semantics仍由 `F17-WORKFLOW-ORCHESTRATION.md` 單獨擁有。

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
