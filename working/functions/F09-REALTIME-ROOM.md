# F09 — Realtime Room

> 狀態：DEFERRED BASELINE — MIGRATED
>
> 本文件在 SSOT Cleanup 中由 `working/APP-DETAILED-DESIGN.md` 的既有 Function 級內容搬入。此次搬移 **不改產品架構、不新增功能決策**；只是把既有 Current Truth 放回單一 Function canonical home。
>
> Horizon：2–3 月，Evidence-gated
>
> Delivery 規則：`working/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/APP-DETAILED-DESIGN.md`

# 1. Migrated Current Truth

只有 Social use case 證明需要才做。

模型：

~~~text
Immutable Blueprint
+ Room
+ Presence
+ Mutable Instance State
+ Validated Delta
~~~

Acceptance：

- realtime 不 mutation Blueprint
- disconnected client 有 recovery
- room TTL / persistence 是 policy
- 不把所有 App 強迫 realtime 化

# Status Note

此文件目前是從既有 Portfolio 文件搬出的 Working 內容，**不因搬家自動升格為完整 Function Spec / SPEC_READY**。後續 Detailed Design 仍需依 Design-to-Delivery Contract 補齊缺少的 UI / API / Data / Error / Security / Evidence / Acceptance 等部分。
