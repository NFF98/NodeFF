# NodeFF Design Workbench

> 狀態：ACTIVE DISCUSSION BUFFER — **NOT SSOT**
>
> 用途：只暫存「尚未批准、尚未有 canonical owner」的產品／商業／架構討論。
>
> Current Product Design Truth 永遠在對應的 canonical `working/` 文件；本檔不得成為 shadow truth。

## Current Active Discussion

**NONE**

目前沒有尚未歸屬 canonical owner 的 Active Design Discussion。

## 使用規則

1. 新議題只有在「尚未決定」時才可暫存在這裡。
2. 一旦 User 批准，必須立即吸收到正確 canonical owner。
3. 已同步內容不得繼續完整保留在 Workbench。
4. Session closeout、過往 review notes、已關閉 delta 不放這裡；需要保存則進 `archive/`。
5. Build Freeze 前，本檔必須維持：
   - approved unique truth = 0
   - closed-but-unsynced item = 0
   - active orphan decision = 0
6. Workbench 不得直接成為 NFFBuild Build Spec source。

## Latest Cleanup

2026-09-25 Shadow Truth Audit 已確認：
- Anonymous-first / Identity / Evidence：已進 Business Plan / Data Model / F07 / F08。
- Intent → App / Wedge boundary：已進 App Architecture / Business Plan。
- Capability / Infra / Experience Shell / Recovery：已進 canonical Working。
- UI/UX、Runtime Timeout、Creation Progress：已進對應 UI / Function / Registry。
- LLM Proposal ≠ READY Truth：已由 Architecture + F02 + F03 + F12 覆蓋。
- 中期 L3 3A–3E 與 L4 4A–4D：經 User 批准後已吸收到 `working/core/APP-ARCHITECTURE.md`，明確標為中期方向，不是 Phase 1 implementation scope。

完整歷史內容：
- `archive/ProjectManagement/DESIGN-WORKBENCH-HISTORY-2026-09-25.md`
- `archive/ProjectManagement/SHADOW-TRUTH-AUDIT-2026-09-25.md`
