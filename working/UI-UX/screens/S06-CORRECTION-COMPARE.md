# S06 — Correction Compare

> Screen ID：S06
>
> 狀態：**WORKING — LOW_FI_REVIEW_IN_PROGRESS**
>
> Phase：Phase 1
>
> Screen-level canonical owner：`working/UI-UX/screens/S06-CORRECTION-COMPARE.md`
>
> Function behavior sources：F16 Result Correction + F00 Experience Shell + F03 Runtime。
>
> 本文件是 ④A Low-fi review draft，不代表 User 已批准，也不代表 Cursor 可實作。

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
    │ NodeFF   App Title                         [回目前 App]     │
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
    │ ‹ App Title               │
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

S06 可提供：

    查看原版 App
    查看修正版 App

但兩者不是決策。

Rules：
- 查看不等於 Accept / Reject。
- 返回 S06後 compare context必須保留。
- 若開 full Runtime preview，應明確標示目前查看哪一版。

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

# 19. Proposed Low-fi Decisions To Confirm

本輪主要確認 4 件事：

1. **Desktop 是否預設 side-by-side「修正前 / 修正後」，Mobile 改 stacked compare？**
2. **S06 頂部是否保留「你剛剛說哪裡不對」摘要，下面才顯示 Before / After？**
3. **三個主要 CTA 是否固定為：保留原版 / 再調整 / 使用修正版？**
4. **LIMITED_COMPARISON 是否一定要明顯告訴 User「這次只能有限比較」，不能假裝修正前後完全可比？**

# 20. Review Status

> **LOW_FI_REVIEW_IN_PROGRESS**

本文件僅做 S06 ④A Low-fi。

S06確認後，Main Screens S01–S06 Low-fi完成；接著進 O01–O05 Overlay / State Low-fi。全部 Low-fi完成後，再做 Cross-Screen Review → High-fi Design System → ④B High-fi。
