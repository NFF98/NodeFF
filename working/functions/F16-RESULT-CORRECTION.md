# F16 — Result Feedback / Logic Correction

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

這個 Function 處理：

> **App 技術上能跑，但 User 認為邏輯、假設或結果明顯不符合原 Intent。**

主流程：

~~~text
Current Blueprint
+ Current Instance Inputs
+ Current Result
→ User Correction Feedback
→ Preserve Current Version
→ Correction Intent
→ Semantic Delta
→ Full Validation
→ New Immutable Blueprint Revision
→ Re-run with preserved inputs
→ Compare Old / New Result
→ Accept / Continue Correcting / Revert
~~~

Frontend 最小行為：

- Result 畫面提供「調整結果／邏輯不對」入口
- User 可用自然語言指出問題
- 原本 Inputs / Result 不消失
- 新舊 Result 可比較
- 可返回上一版
- 不把 semantic mismatch 顯示成 technical error

Backend / Compiler responsibility：

- 將 feedback 正規化為 Correction Intent
- 以 existing Blueprint 為 base
- 優先產生最小 Semantic Delta
- 不允許直接 mutation 原 Blueprint
- 新 revision 必須完整走 F02 Validation
- correction failure 時保留原 Blueprint 可繼續使用

State / Data：

~~~text
base_blueprint_id
base_revision
instance_input_snapshot
result_snapshot_before
correction_intent
semantic_delta
new_blueprint_id
result_snapshot_after
correction_outcome
~~~

Acceptance：

1. User 不需重新輸入原本資料即可修改邏輯。
2. 原 Blueprint 永遠可回復。
3. 修改只針對 User 指出的語意範圍，但新 Blueprint 仍完整驗證。
4. 新舊 Result 可比較。
5. correction 失敗不破壞目前可用版本。
6. semantic mismatch / correction / accept / revert 都形成 Evidence。
7. 「有結果」不得被當成「結果正確」的證明。

# 2. Additional Existing Cross-Function Truth

共同依賴：
- F00
- F01
- F02
- F03
- F06
- F07
- F16

要求：

~~~text
executed result
→ user semantic feedback
→ preserved inputs / old revision
→ correction intent
→ semantic delta
→ full revalidation
→ new immutable revision
→ old/new result comparison
→ accept / refine again / revert
~~~

原則：

- Runtime success 不代表 semantic success。
- correction 不直接修改 Runtime code。
- original Blueprint / result 必須可保留。
- correction outcome 必須成為 Compiler / Reuse / Capability Evidence。

# Status Note

此文件目前是從既有 Portfolio 文件搬出的 Working 內容，**不因搬家自動升格為完整 Function Spec / SPEC_READY**。後續 Detailed Design 仍需依 Design-to-Delivery Contract 補齊缺少的 UI / API / Data / Error / Security / Evidence / Acceptance 等部分。
