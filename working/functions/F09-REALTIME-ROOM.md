# F09 — Realtime Room

> 狀態：DEFERRED BASELINE — MIGRATED
>
> 本文件在 SSOT Cleanup 中由 `working/core/APP-DETAILED-DESIGN-OVERVIEW.md` 的既有 Function 級內容搬入。此次搬移 **不改產品架構、不新增功能決策**；只是把既有 Current Truth 放回單一 Function canonical home。
>
> Horizon：2–3 月，Evidence-gated
>
> Delivery 規則：`working/core/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/core/APP-DETAILED-DESIGN-OVERVIEW.md`

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

此文件目前是從既有 Portfolio 文件搬出的 Working 內容，**不因搬家自動升格為完整 Function Spec / BUILD_FREEZE_READY**。後續 Detailed Design 仍需依 Design-to-Delivery Contract 補齊缺少的 UI / API / Data / Error / Security / Evidence / Acceptance 等部分。


## Relationship To Future Share Modes

> Sync source：O01 Low-fi Review / DESIGN-WORKBENCH。

未來若 NodeFF支援「共享遊戲 / 多人共同操作 / 同步 mutable App state」，由 F09 Realtime Room 承接，不擴張 F05 static Share/Restore。

Conceptual boundary：

~~~text
F05
= share immutable App definition
→ recipient gets fresh Runtime Instance

F09
= share/join Room
→ presence + mutable shared instance state
~~~

Future result-only sharing不自動等於 F09；若只是分享一份 Result / Snapshot，仍需獨立 Function contract。

F09目前維持 DEFERRED / Evidence-gated，不因此提前進 Phase 1。
