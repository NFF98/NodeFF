# F10 — Blueprint Reuse / Retrieval

> 狀態：DEFERRED BASELINE — MIGRATED
>
> 本文件在 SSOT Cleanup 中由 `working/common-core/APP-DETAILED-DESIGN-OVERVIEW.md` 的既有 Function 級內容搬入。此次搬移 **不改產品架構、不新增功能決策**；只是把既有 Current Truth 放回單一 Function canonical home。
>
> Horizon：2–3 月
>
> Delivery 規則：`working/common-core/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/common-core/APP-DETAILED-DESIGN-OVERVIEW.md`

# 1. Migrated Current Truth

優先順序：

~~~text
Exact / structured reuse
→ trusted family reuse
→ semantic retrieval only when evidence exists
~~~

Acceptance：

- reused Blueprint 必須重新做 compatibility / trust check
- retrieval 不可繞過 validation
- reuse correctness 可量測
- fresh compile vs reuse cost 可比較

# Status Note

此文件目前是從既有 Portfolio 文件搬出的 Working 內容，**不因搬家自動升格為完整 Function Spec / BUILD_FREEZE_READY**。後續 Detailed Design 仍需依 Design-to-Delivery Contract 補齊缺少的 UI / API / Data / Error / Security / Evidence / Acceptance 等部分。
