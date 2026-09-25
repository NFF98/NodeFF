# F13 — Entitlement / Metering

> 狀態：DEFERRED BASELINE — MIGRATED
>
> 本文件在 SSOT Cleanup 中由 `working/common-core/APP-DETAILED-DESIGN-OVERVIEW.md` 的既有 Function 級內容搬入。此次搬移 **不改產品架構、不新增功能決策**；只是把既有 Current Truth 放回單一 Function canonical home。
>
> Horizon：2–6 月
>
> Delivery 規則：`working/common-core/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/common-core/APP-DETAILED-DESIGN-OVERVIEW.md`

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

此文件目前是從既有 Portfolio 文件搬出的 Working 內容，**不因搬家自動升格為完整 Function Spec / BUILD_FREEZE_READY**。後續 Detailed Design 仍需依 Design-to-Delivery Contract 補齊缺少的 UI / API / Data / Error / Security / Evidence / Acceptance 等部分。
