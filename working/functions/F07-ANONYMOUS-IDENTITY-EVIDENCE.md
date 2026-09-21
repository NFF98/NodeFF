# F07 — Anonymous Identity & Evidence

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

最小 identity：

- random first-party anonymous_id
- session / intent / blueprint / share linkage

只收 meaningful events：

- compile outcome
- semantic mismatch
- result correction requested
- result correction accepted / rejected / reverted
- capability gap
- share
- open
- use
- remix
- recovery

Acceptance：

- 不使用 fingerprinting
- No Registration ≠ No Evidence
- telemetry 不造成每次 local interaction 都打 server
- privacy-sensitive data 不被無限制收集

# Status Note

此文件目前是從既有 Portfolio 文件搬出的 Working 內容，**不因搬家自動升格為完整 Function Spec / SPEC_READY**。後續 Detailed Design 仍需依 Design-to-Delivery Contract 補齊缺少的 UI / API / Data / Error / Security / Evidence / Acceptance 等部分。
