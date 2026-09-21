# F12 — Humanized Recovery Orchestration

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

統一 Recovery State：

~~~text
status
human_message
preserved_context
next_actions
technical_code
~~~

Acceptance：

- 一般 User 不直接看到裸 401 / 402 / 404 / 500
- user input / intent 盡量保留
- retry 有上限
- unsupported capability 誠實呈現
- component failure 局部隔離
- 每個可預期 failure 至少有一個 next action

# 2. Additional Existing Cross-Function Truth

共同依賴：
- F00
- F01
- F02
- F03
- F04
- F05
- F06
- F11
- F12

要求：

~~~text
technical failure
→ classified failure
→ recovery policy
→ preserved context
→ human UX
~~~

# Status Note

此文件目前是從既有 Portfolio 文件搬出的 Working 內容，**不因搬家自動升格為完整 Function Spec / SPEC_READY**。後續 Detailed Design 仍需依 Design-to-Delivery Contract 補齊缺少的 UI / API / Data / Error / Security / Evidence / Acceptance 等部分。
