# F08 — Durable Identity / Ownership

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
- F08
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

此文件目前是從既有 Portfolio 文件搬出的 Working 內容，**不因搬家自動升格為完整 Function Spec / BUILD_FREEZE_READY**。後續 Detailed Design 仍需依 Design-to-Delivery Contract 補齊缺少的 UI / API / Data / Error / Security / Evidence / Acceptance 等部分。
