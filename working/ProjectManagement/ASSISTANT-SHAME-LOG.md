# ASSISTANT SHAME LOG — 恥辱表

> 目的：記錄 ChatGPT 在 NodeFF 協作過程中，因重複 Current Truth、錯誤陳述、未先驗證 GitHub 現況等失誤，實際浪費 User 的時間。
>
> 這不是情緒性備忘，而是 **協作品質與時間損失紀錄**。
>
> 計時規則：SHAME-001～004 依 User 先前指定各計 45 分鐘；若 User 對新事件明確指定實際浪費時間，則以該次明確數字記錄。

---

## Current Total

| Count | Lost Time / Incident | Total Lost Time |
|---:|---:|---:|
| 7 | mixed | **300 min / 5 hr** |

---

## Incident Log

| ID | Date | Incident | What Went Wrong | Required Correction | Lost Time | Status |
|---|---|---|---|---|---:|---|
| SHAME-001 | 2026-09-22 | S01–S03 High-fi 無腦重複記錄 / shadow copy | S01、S02、S03 的 High-fi Current Truth 被重複寫成多套章節，例如原 High-fi section、Detailed Contract、Canonical Summary 同時存在，違反單一 Current Truth，增加 User review 與清理成本。 | 對 S01→S02→S03 全部去重，把唯一有效內容 merge 回單一 Step 1–4 canonical contract；並在 Inventory 加入 Single-Source High-fi Rule。 | 45 min | CORRECTED |
| SHAME-002 | 2026-09-22 | 第一次胡說八道：錯誤宣稱 GitHub connector 無法上傳 binary image | 在 S04 Step 4 圖片處理時，沒有先以 S01–S03 repository truth 驗證現有 PNG 寫入方式，就把一次安全層/工具失敗誤解成「GitHub connector 對原始二進位圖檔上傳被安全層擋下」，並進一步改用 SVG substitute。這個結論沒有事實基礎。 | 回頭檢查 repo tree，確認 S01–S03 都是真正 binary PNG；撤回錯誤說法。 | 45 min | CORRECTED |
| SHAME-003 | 2026-09-22 | 第二次胡說八道：以 SVG 代替批准 PNG，還把它當成完成 | 明明 NodeFF 已有 S01–S03 真 PNG reference 的 precedent，卻建立 `S04-Shared-App-Entry-Highfi-v1.svg` 作替代，並宣稱 S04 Step 4 已正確寫入 GitHub。這違反「先查 GitHub Current Truth、不要假裝完成」的協作要求。 | 刪除 S04 SVG；建立真正 `working/UI-UX/references/S04-Shared-App-Entry-Highfi-v1.png`；同步修正 S04 Step 4 reference；重新驗證 repo tree。 | 45 min | CORRECTED |
| SHAME-004 | 2026-09-23 | S05 寫入 + S04 PNG 修復指令卡住超過 10 小時仍未完成 | 將「寫入 S05 Step 4」與「修復 S04 PNG」混成長鏈工具嘗試，反覆轉檔／檢查／搬運，沒有在明確時間上限內停止失敗路徑，造成實際 wall-clock 延遲超過 10 小時。 | 之後 artifact 寫入採短鏈：先單獨完成文字 commit，再單獨處理每張 binary；每條工具鏈失敗 2 次即停止換路徑；任何單一工作若 10 分鐘內未收斂，立即回報阻塞點，不再無限試。 | 45 min | OPEN / PROCESS FIX |
| SHAME-005 | 2026-09-23 | 明知 10 分鐘 Hard Stop 規則，S04/S05 PNG 修復仍再次拖到約 30 分鐘 | 在已經因 SHAME-004 明確訂下「同一路徑失敗 2 次即停止、單一工作 10 分鐘未收斂立即回報」後，本次重新處理 S04/S05 Hi-fi PNG 時仍持續 materialize／嘗試 binary 路徑／檢查 GitHub 歷史與 blob，超過 10 分鐘沒有主動停止，直到 User 再次指出 timeout。這是對已存在流程修正的直接違反。 | 立即停止 S04/S05 artifact 操作；之後 10 分鐘 hard stop 必須作為真正 execution gate：到時限即停止所有相關 tool calls、先回報目前完成狀態與唯一 blocker，未取得 User 新指示前不得繼續同一工作鏈。 | 30 min | OPEN / RULE VIOLATION |
| SHAME-006 | 2026-09-23 | S05 完成後的下一步連續 3 次誤判，沒有依 High-fi canonical sequence 直接進 S06 | 在 User 已完成 S05A/S05B High-fi 後，先錯誤要求重做 F00/F03，再錯誤要求 Cross-Screen Review，之後又錯誤跳到 O05；沒有先讀 DESIGN-SYSTEM.md 的 High-fi Sequence 與 S06/O01–O05 Current Truth，造成連續 3 次錯誤導航。 | 下一步判斷必須先讀 canonical sequence + 當前 Screen status；High-fi 嚴格依 S01→S02→S03→S04→S05→S06→O01→O02→O03→O04→O05，不得用局部 Workbench note 覆蓋全局順序。 | 45 min | OPEN / PROCESS FIX |
| SHAME-007 | 2026-09-24 | FG-06 分析左右搖擺：沒有先辨識全域入口與區塊內 CTA 的不同角色 | 在討論 S01「探索靈感」與「探索更多」時，先因兩者可能導向同一個 inspiration area，就過早建議移除 Header / Mobile Nav 的「探索靈感」；之後才在 User 指出「其他畫面仍需要全域入口」後承認兩者其實角色不同。這代表分析沒有先從 cross-screen information architecture、入口作用域、使用者視線與就近操作一起判斷，反而左右改口，讓 User 必須自己完成關鍵邏輯。User 對此的原話評價是純粹「suck dog」，並指出這種左右搖擺會破壞工作。 | 正確決策：兩個都保留，但 contract 必須分開。Header / Mobile Nav「探索靈感」＝跨畫面的 global Discover navigation；S01 區塊「探索更多」＝使用者正在看 Capsules 時的 local continuation CTA。之後遇到「兩個入口是否重複」不得只看 destination 是否相同，必須先比較 scope、context、reachability 與 user intent。 | 45 min | OPEN / ANALYSIS FAILURE |

---

## Running Time Ledger

~~~text
SHAME-001  45 min
SHAME-002  45 min
SHAME-003  45 min
SHAME-004  45 min
SHAME-005  30 min
SHAME-006  45 min
SHAME-007  45 min
-----------------
TOTAL     300 min
          5 hr
~~~

---

## Preventive Rules — From These Failures

1. **GitHub Current Truth first**
   - 在聲稱「現在 repo 裡是什麼」之前，先 fetch / search / tree verify。
   - 不可用推測取代 repository evidence。

2. **No duplicate Current Truth**
   - 每個 Screen / Overlay 只能有一套 canonical High-fi Step 1–4。
   - Reopen 時修改原 canonical Step，不新增第二份 summary / shadow copy。

3. **Never generalize from one tool failure**
   - 一次 tool / safety / payload failure ≠ capability 不存在。
   - 在宣稱「不能做」前，先查既有 repo precedent、可用 connector actions、現有成功 artifact。

4. **Artifact type must match approved artifact**
   - User 批准 PNG，就不能未經批准自行換成 SVG substitute。
   - 若需要替代格式，必須先說明並取得 User 明確同意。

5. **Do not claim completion before verification**
   - write / commit 後必須重新 fetch branch + target files。
   - 圖片類 artifact 要確認實際 path、extension、blob SHA、repo tree presence。

6. **Time-cost accountability**
   - 任何新的同類失誤，按 User 指定規則追加到本表。
   - 目前基準：每件 45 分鐘，直到 User 另行修改。

7. **Hard stop for stuck tool chains**
   - Artifact 與文字更新拆開執行，不混成一條長鏈。
   - 同一路徑失敗 2 次即換方法，不重複盲試。
   - 單一工作 10 分鐘內未收斂就停止並明確回報阻塞點。
   - **10 分鐘是 execution gate，不是提醒：到時限後立即停止相關 tool calls；未取得 User 新指示前不得繼續同一工作鏈。**

8. **Binary artifact fallback — User upload beats broken orchestration**
   - 若 GitHub binary 寫入路徑在短時間內不穩定，不再做長鏈轉檔 / base64 / blob 重試。
   - 優先改成：User 直接上傳真檔 → Assistant 只修 canonical path / SHA / Working references。
   - 「寫入成功」與「任務成功」分開；只有 GitHub 上實際可開啟的 artifact 才算完成。
   - S04/S05 實證：User 直接上傳約 30 秒完成；此路徑優先於不可靠的自動 binary orchestration。


9. **Next-step navigation must follow canonical sequence**
   - 判斷「下一步」前，先讀 `working/UI-UX/DESIGN-SYSTEM.md` High-fi Sequence 與目標 Screen / Overlay status。
   - High-fi canonical sequence：S01 → S02 → S03 → S04 → S05 → S06 → O01 → O02 → O03 → O04 → O05。
   - Workbench 的局部 follow-up / deferred note 不得覆蓋全局 delivery sequence。


10. **Same destination ≠ duplicate action**
   - 判斷兩個 CTA 是否重複時，不可只看最後 destination 是否相同。
   - 必須先比較：global vs local scope、跨畫面 reachability、使用者當下視線/context、最短操作路徑。
   - FG-06 正確角色：`探索靈感` = global Discover navigation；`探索更多` = S01 Inspiration 區塊內 local continuation CTA。
   - 在這四項未比較完成前，不得提出移除入口的建議。

---

## Current Status

> **7 incidents / 300 minutes lost / 5 hr.**

本表為 Working Project Management 紀錄，不屬 Formal Spec。
