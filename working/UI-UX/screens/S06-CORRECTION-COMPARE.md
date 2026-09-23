# S06 — Correction Compare

> Screen ID：S06
>
> 狀態：**WORKING — ④A LOW_FI_APPROVED / ④B HIGH_FI_STEP1 APPROVED / STEP2 NEXT**
>
> Phase：Phase 1
>
> Screen-level canonical owner：`working/UI-UX/screens/S06-CORRECTION-COMPARE.md`
>
> Function behavior sources：F16 Result Correction + F00 Experience Shell + F03 Runtime。
>
> ④A Low-fi 已完成 User Review；④B High-fi Step 1 已批准。Formal Spec 與 Cursor implementation 仍維持 HOLD。

# 1. User Outcome

S06 的核心任務：

> **當 User 認為結果 / 規則 / 邏輯不對時，NodeFF 讓他用相同可重播 inputs 比較修正前後結果，清楚知道改了什麼，再自己決定要不要採用新版。**

S06 不是一般 Refine Preview，也不是技術 diff viewer。

# 2. Entry

Canonical flow：

    S03 Result
    → O02 Correction Composer
    → correction generation / replay
    → S06 Compare

只有 F16 correction 進 S06。

一般新增功能 / 改 UI / 改用途：
    → S05 Refine / Remix
    不進 S06。

# 3. Core Information Hierarchy

S06 必須依序讓 User看到：

1. **你剛剛說哪裡不對**
2. **修正前結果**
3. **修正後結果**
4. **這次改了什麼**
5. **比較可信度 / 限制**
6. **決策 CTA**

Default 不顯示：
- JSON diff
- AST diff
- state key diff
- model reasoning
- internal correction delta IDs

# 4. Proposed Desktop Low-fi

    ┌──────────────────────────────────────────────────────────────┐
    │ NodeFF   App Title                                            │
    ├──────────────────────────────────────────────────────────────┤
    │ 你說：主管應該付兩倍，但現在沒有                            │
    │                                                              │
    │ ┌────────────────────────┐  ┌────────────────────────┐       │
    │ │ 修正前                 │  │ 修正後                 │       │
    │ │                        │  │                        │       │
    │ │ 結果：$1,200           │  │ 結果：$1,450           │       │
    │ │                        │  │                        │       │
    │ └────────────────────────┘  └────────────────────────┘       │
    │                                                              │
    │ 這次改了什麼                                                 │
    │ • 主管權重改成 2x                                            │
    │ • 其他規則維持不變                                           │
    │                                                              │
    │ 比較品質：可直接比較 / 有限制                                │
    │                                                              │
    │ [保留原版]          [再調整]             [使用修正版]        │
    └──────────────────────────────────────────────────────────────┘

Desktop 預設 side-by-side，因為核心任務就是比較。

# 5. Proposed Mobile Low-fi

Mobile 不強迫左右並排。

    ┌────────────────────────────┐
    │ App Title                 │
    │                            │
    │ 你說：主管應該付兩倍…      │
    │                            │
    │ ┌────────────────────────┐ │
    │ │ 修正前                 │ │
    │ │ 結果：$1,200           │ │
    │ └────────────────────────┘ │
    │                            │
    │        ↓                   │
    │                            │
    │ ┌────────────────────────┐ │
    │ │ 修正後                 │ │
    │ │ 結果：$1,450           │ │
    │ └────────────────────────┘ │
    │                            │
    │ 這次改了什麼              │
    │ 比較品質                  │
    │                            │
    │ [保留原版]                │
    │ [再調整] [使用修正版]      │
    └────────────────────────────┘

Mobile 原則：
- stacked compare。
- Before / After label永遠清楚。
- CTA不遮比較內容。

# 6. Version Visual Distinction

沿用 S05 的版本辨識原則：

- 修正前 / 修正後需有不同 border / accent token。
- 必須有文字 label，不可只靠顏色。
- 實際色值留到 ④B High-fi Design System 決定。

# 7. What User Said Was Wrong

S06 最上方保留簡短 correction statement：

    你說：
    「主管應該付兩倍，但現在沒有」

目的：
- 讓 User知道系統修的是哪一件事。
- 避免只看到兩個不同數字，卻不知道差異對應什麼。

若 feedback 很長，預設摘要 + 展開查看原文。

# 8. Previous Result / New Result

Before / After 必須來自 F16 + F03 canonical result。

Rules：
- 不從 DOM 抓數字。
- unavailable output要標示 unavailable / error，不 fake default。
- SENSITIVE / DO_NOT_PERSIST值依 policy處理。
- 若 result有多個 output，優先顯示 material outputs，其他可展開。

# 9. What Changed

User-facing summary只回答：

> **「為了修正你指出的問題，這次改了什麼？」**

來源：
- Resolved Correction Intent。
- Correction Delta。
- deterministic semantic diff metadata。

Low-fi presentation：

    這次改了什麼
    • 主管分攤權重：1x → 2x
    • 其他分攤規則維持不變

不顯示 technical JSON path。

# 10. Comparison Quality

F16 已定義：

- DETERMINISTIC_REPLAY
- SEEDED_REPLAY
- TIME_CONTEXT_REPLAY
- LIMITED_COMPARISON

Consumer不直接看 enum。

Proposed user-facing mapping：

## Fully Comparable

    使用相同輸入重新計算
    這次結果可以直接比較

## Limited Comparison

    這次比較有部分限制
    隨機 / 時間狀態無法完全重現，因此數值差異不一定全部來自這次修正

Rules：
- LIMITED 必須 visible。
- 不可以把不可 apples-to-apples 的比較包裝成「已修正正確」。

# 11. Use Corrected Version

Primary CTA：

    使用修正版

Effect：
- child corrected Blueprint / Runtime becomes active。
- correction outcome = ACCEPTED。
- 回 S03。
- base Blueprint保留。

User心智：
> 「這個修正比較符合我要的，就用它。」

# 12. Keep Previous

CTA：

    保留原版

Effect：
- correction outcome = REJECTED。
- base App保持 active。
- child仍保留為 immutable artifact。
- 回 S03 base App。

# 13. Adjust Again

CTA：

    再調整

F16 default：
- 保留 current comparison。
- prefill previous feedback + latest change summary。
- base = latest generated child。
- replay inputs重新驗證。

UI 顯示：

    你正在繼續調整：目前這個修正版

Secondary option：

    從原版重新修正

# 14. Return / View App

S06 不提供獨立的「回目前 App」Decision CTA，避免 User無法判斷這代表暫時離開、Reject correction，或 Accept目前版本。

S06 可提供：

    查看原版 App
    查看修正版 App

但兩者只是 Preview，不是決策。

Rules：
- 查看不等於 Accept / Reject。
- Preview結束後回 S06，compare context必須保留。
- 若開 full Runtime preview，應明確標示目前查看哪一版。
- 真正離開 Compare 的產品決策只使用：**保留原版 / 再調整 / 使用修正版**。
- S06 是 focused decision workspace，不繼承 S03 permanent bottom navigation。
- 此規則不新增 F16 outcome；完全沿用既有 ACCEPT / KEEP_PREVIOUS / ADJUST_AGAIN semantics。

# 15. Loading / Replay State

進 S06前可能有：
- CHILD_READY
- REPLAYING
- COMPARE_READY

User-facing不顯示 technical state。

Proposed：

    正在套用相同輸入…
    正在比較修正前後結果…

如果有可靠 progress source可以顯示 progress；沒有就 stage-based，不 fake %。

# 16. Failure / Recovery

任何 technical failure：
- 不破壞 base App。
- 保留 correction draft / before context。
- 交 O03 / F12。

Examples：

## Replay Failed

    目前無法完整比較，但原版還在。

    [再試一次]
    [保留原版]

## Limited Replay

不是 error：

    這次只能做有限比較。

    [查看限制]
    [保留原版]
    [再調整]

# 17. Revert Boundary

S06 是「尚未接受修正版前」的 Compare。

Revert 是：

    User 已接受修正版
    → 回 S03
    → Previous Version / Revert
    → O04

因此 S06 不放 Revert CTA。

S06 只放：
- 使用修正版
- 保留原版
- 再調整

# 18. Accessibility / Responsive

- Before / After 不只靠顏色。
- Desktop side-by-side 在窄寬時自動變 stacked。
- screen reader順序固定：issue → previous → new → changes → quality → actions。
- Result change可用 aria-live適度宣布。
- CTA wording明確，不使用模糊「Done」。
- focus從 O02進 S06後落在 Compare heading。

# 19. Confirmed S06 Low-fi Decisions

User 已確認：

1. Desktop 預設採 **side-by-side 修正前 / 修正後**；Mobile 採上下 stacked compare。
2. S06 頂部保留 **「你剛剛說哪裡不對」** 摘要，下面再顯示 Before / After。
3. 三個主要 CTA 固定為：**保留原版 / 再調整 / 使用修正版**。
4. 若 comparison_mode = LIMITED_COMPARISON，必須明確告知 User「這次只能有限比較」，不可暗示兩邊完全 apples-to-apples。

# 20. ④B High-fi Contract

> Step 1 approved by User：2026-09-23
>
> Canonical rule：本節是 S06 High-fi 的唯一 canonical contract。後續 Step 2–4 必須在本節續寫，不得另建重複 High-fi summary / shadow copy。
>
> Current status：
> - Step 1 — Structure Lock ✅
> - Step 2 — Geometry + Visual Hierarchy Lock — NEXT
> - Step 3 — Detailed High-fi Visual Rules Lock — PENDING
> - Step 4 — Final Visual Reference Lock — PENDING

## Step 1 — Structure Lock ✅

### 1. S06 Role

S06 只服務 **F16 Result Correction**。

Canonical entry：

~~~text
S03 Result
→ O02 Correction Composer
→ correction generation / replay
→ S06 Correction Compare
~~~

新增功能、改 UI、改用途仍走 S05，不進 S06。

S06 是 **Compare Decision Workspace**，不是 Editor、Builder、一般 Refine Preview或 technical diff viewer。

### 2. Canonical Information Order

S06 固定依序呈現：

~~~text
App context
→ 你剛剛說哪裡不對
→ 修正前 / 修正後
→ 這次改了什麼
→ 比較可信度 / 限制
→ Decision actions
~~~

若 correction feedback 過長，可顯示摘要並提供展開原文；不可移除 correction context。

### 3. Before / After Result Surfaces

修正前與修正後都必須來自 F16 + F03 canonical result，且必須有明確文字 label，不可只靠顏色。

Consumer UI不顯示 JSON / AST diff、state key diff、model reasoning、internal correction delta ID、technical Blueprint path。

Unavailable / protected outputs依 Function / policy truth呈現，不 fake default。

### 4. What Changed

「這次改了什麼」只呈現 consumer semantic summary；來源仍是 Resolved Correction Intent / Correction Delta / deterministic semantic diff metadata，UI不得自行推論改動。

### 5. Comparison Quality Is First-class Structure

Comparison quality / limitation不得藏進 technical detail。

若為 LIMITED_COMPARISON：
- 必須明確顯示「這次只能有限比較」；
- 必須說明數值差異不一定全部來自本次修正；
- 不得包裝成「系統已證明修正正確」。

F16允許在限制已明確揭露時仍由 User自行決定是否採用修正版；S06不得自行把 LIMITED等同於失敗。

### 6. Decision Actions

S06只有三個產品決策：**保留原版 / 再調整 / 使用修正版**；Primary = **使用修正版**。

- 保留原版 → correction outcome = REJECTED → 回 S03 base App。
- 再調整 → 繼續 correction lifecycle；Phase 1 default base = latest generated child。
- 使用修正版 → correction outcome = ACCEPTED → corrected child becomes active → 回 S03。

再調整仍保留 secondary option：**從原版重新修正**；使用 original pre-correction Blueprint作 base。

### 7. Preview Is Not A Decision

可以提供 **查看原版 App / 查看修正版 App**，但只能是 Preview action。

- 查看不等於 Accept / Reject。
- Preview返回後保留同一 compare context。
- 若進 full Runtime preview，必須明確標示目前查看版本。
- 不增加第四個「回目前 App」Decision CTA。

### 8. Revert Boundary

S06不提供 Revert。接受修正版後若 User要回前版，由 **S03 → O04 Revert Confirmation** 承接。

### 9. Focused Workspace / Shell Boundary

S06不繼承 S03 permanent bottom navigation；不得把「目前 App / 修改 / 分享」帶進 S06 decision workspace。

### 10. Loading / Recovery Ownership

- correction generation / replay / comparison processing presentation → O05。
- technical failure / retry / preserved context → O03 + F12。
- S06只呈現 compare-ready content與 consumer decision。

### 11. Step 1 Locked Decisions

1. S06只服務 F16 Correction。
2. S06定位為 Compare Decision Workspace，不是 Editor / technical diff viewer。
3. Information order固定為 App context → issue → Before/After → changed summary → quality/limits → decisions。
4. Before / After都是 canonical Result surface，且明確文字標示。
5. What Changed只用 consumer semantic summary。
6. Comparison Quality / LIMITED_COMPARISON是正式可見結構。
7. 三個唯一產品決策為保留原版 / 再調整 / 使用修正版，Primary = 使用修正版。
8. Adjust Again預設以 latest generated child繼續；可 secondary選擇從原版重新修正。
9. 查看原版 / 修正版只屬 Preview，不是 decision。
10. S06不放 Revert；接受後若要回前版由 S03 → O04承接。
11. S06不繼承 S03 permanent bottom navigation。
12. Processing交 O05；Failure / Recovery交 O03 + F12。

> Step 1：**APPROVED / LOCKED**。下一步：Step 2 — Geometry + Visual Hierarchy Lock。

# 21. Review Status

> **④A LOW_FI_APPROVED / ④B HIGH_FI_STEP1 APPROVED — STEP2 NEXT**

S06 ④A Low-fi與④B Step 1已完成 User Review。

下一步：**S06 ④B Step 2 — Geometry + Visual Hierarchy Lock**。

Formal Spec、Backlog / Sprint、Cursor implementation維持 HOLD。
