# F15 — Transaction / Settlement

> 狀態：DEFERRED BASELINE — MIGRATED
>
> 本文件在 SSOT Cleanup 中由 `working/APP-DETAILED-DESIGN.md` 的既有 Function 級內容搬入。此次搬移 **不改產品架構、不新增功能決策**；只是把既有 Current Truth 放回單一 Function canonical home。
>
> Horizon：6 月後
>
> Delivery 規則：`working/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/APP-DETAILED-DESIGN.md`

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

F17 只在 Blueprint / Capability Plan 明確需要外部多步執行時加入：

~~~text
Runtime / Capability Action
→ F17 Orchestration
→ External / Async Steps
→ Validated Outcome
→ Runtime / Durable State
~~~

# Status Note

此文件目前是從既有 Portfolio 文件搬出的 Working 內容，**不因搬家自動升格為完整 Function Spec / SPEC_READY**。後續 Detailed Design 仍需依 Design-to-Delivery Contract 補齊缺少的 UI / API / Data / Error / Security / Evidence / Acceptance 等部分。
