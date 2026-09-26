# F09 — Realtime Room

> 狀態：DEFERRED_BASELINE / NOT_BUILD_FREEZE_READY
>
> Activation Gate：日期本身不 unlock；只有 Evidence + Human approval + complete Detailed Design + Build Freeze inclusion 才可進 implementation scope。
>
> Horizon：2–3 月，Evidence-gated
>
> Delivery 規則：`working/common-core/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/detailed-design/APP-DETAILED-DESIGN-OVERVIEW.md`

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


## Relationship To Future Share Modes

> Sync source：O01 Low-fi Review / DESIGN-WORKBENCH。

未來若 appf2支援「共享遊戲 / 多人共同操作 / 同步 mutable App state」，由 F09 Realtime Room 承接，不擴張 F05 static Share/Restore。

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
