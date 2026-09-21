# F06 — Remix / Refine

> 狀態：DRAFT — MIGRATED CURRENT TRUTH
>
> 本文件在 SSOT Cleanup 中由 `working/APP-DETAILED-DESIGN.md` 的既有 Function 級內容搬入。此次搬移 **不改產品架構、不新增功能決策**；只是把既有 Current Truth 放回單一 Function canonical home。
>
> Horizon：0–1 月
>
> Delivery 規則：`working/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/APP-DETAILED-DESIGN.md`

# 1. Migrated Current Truth

~~~text
Existing Blueprint
+ User Semantic Change
→ Delta / Recompile
→ Full Validation
→ New Immutable Blueprint
~~~

Acceptance：

- original Blueprint 不被 mutation
- Runtime state change 不等於 semantic revision
- Remix lineage 可追蹤
- refinement failure 保留原 App / Intent

# Status Note

此文件目前是從既有 Portfolio 文件搬出的 Working 內容，**不因搬家自動升格為完整 Function Spec / SPEC_READY**。後續 Detailed Design 仍需依 Design-to-Delivery Contract 補齊缺少的 UI / API / Data / Error / Security / Evidence / Acceptance 等部分。
