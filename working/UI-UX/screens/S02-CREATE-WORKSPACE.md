# S02 — Create Workspace

> Screen ID：S02
>
> 狀態：**WORKING — LOW_FI_REVIEW_IN_PROGRESS**
>
> Phase：Phase 1
>
> Screen-level canonical owner：working/UI-UX/screens/S02-CREATE-WORKSPACE.md
>
> Function behavior sources：working/functions/F00-EXPERIENCE-SHELL.md、working/functions/F01-INTENT-COMPILATION.md
>
> 本文件是 Low-fi review draft，不代表 User 已批准，也不代表 Cursor 可實作。

# 1. User Outcome

S02 的核心任務：

> **讓 User 感覺 NodeFF 正在把他的想法往「可用 App」推進；只有真的缺少關鍵資訊時才打斷他，而且任何回答、假設與失敗都不讓他從頭重來。**

S02 不是 AI chat room，也不是 engineering status console。

# 2. Core UX Principles — Proposed

1. **One Workspace, Changing State**：ANALYZING / CLARIFICATION / ASSUMPTION / BUILDING / HYDRATING 都留在同一 Create Workspace，不為每個 state 跳新頁。
2. **Fast Path First**：Intent 已足夠時，不插入多餘 clarification / assumption；但進入 BUILDING 前仍需要 User 明確按一次「確認建立」。
3. **Interrupt Only for Material Decisions**：只有 material clarification / assumption 才停下來問 User。
4. **Visible Progress, No Fake Precision**：採 stage-based progress，沒有可靠百分比就不顯示假數字。
5. **Preserve Context**：原始 Intent、回答、assumptions、draft 持續保留。
6. **Human Language**：不顯示 Prompt A / Prompt B / validator / registry 等工程術語。

# 3. Entry From S01

流程：S01 Prompt Composer → 建立 App → S02。

進入 S02 後，不顯示新的空白 prompt，而是把原始需求轉成 compact context，例如：

    你的想法
    幫我做一個今晚聚餐投票 App，大家可以選餐廳。   [編輯]

# 4. S02 State Model

    ANALYZING
    ├─ FAST PATH → BUILDING
    ├─ CLARIFICATION_REQUIRED → ANALYZING
    └─ ASSUMPTION_REVIEW → BUILDING

    BUILDING → HYDRATING → APP_READY → S03

任何適用 state 都可進 O03 Recovery Overlay。

READY_TO_BUILD 是可見決策點：若 Intent 已足夠且沒有 material clarification / assumption，S02 顯示最小確認區，User 明確按一次「確認建立」後才進 BUILDING。

# 5. Proposed Desktop Low-fi

    ┌─────────────────────────────────────────────────────┐
    │ NodeFF                                  [取消/返回] │
    │                                                     │
    │ 你的想法                                             │
    │ ┌─────────────────────────────────────────────────┐ │
    │ │ 今晚聚餐投票 App…                        [編輯] │ │
    │ └─────────────────────────────────────────────────┘ │
    │                                                     │
    │ ● 理解想法   ○ 整理成 App   ○ 檢查互動   ○ 準備 App│
    │ ███████────────────  stage-based / no fake %        │
    │                                                     │
    │ ┌─────────────────────────────────────────────────┐ │
    │ │ Dynamic Workspace Body                          │ │
    │ │ Clarification / Assumption / Building / Loading │ │
    │ └─────────────────────────────────────────────────┘ │
    │                                                     │
    │              contextual Primary CTA                 │
    └─────────────────────────────────────────────────────┘

Desktop 預設採 single-focus workspace，不做 permanent sidebar / dashboard。

# 6. Proposed Mobile Low-fi

    ┌────────────────────────────┐
    │ NodeFF              [返回] │
    │ 你的想法            [編輯] │
    │ ┌────────────────────────┐ │
    │ │ 今晚聚餐投票 App…      │ │
    │ └────────────────────────┘ │
    │ ● ━ ○ ━ ○ ━ ○            │
    │ 理解  組合  檢查  準備     │
    │ ┌────────────────────────┐ │
    │ │ Dynamic State Content  │ │
    │ └────────────────────────┘ │
    │ [        Continue        ] │
    └────────────────────────────┘

Mobile 採單欄；Primary CTA 易觸及，但不能遮住表單。

# 7. ANALYZING

User-facing copy 方向：

    正在理解你的想法…
    我們正在整理你要做的 App，有需要你決定的地方才會問你。

不顯示 model name、token usage、Prompt A、JSON 或 policy ID。

# 8. CLARIFICATION_REQUIRED

F01 最多提供 1–3 個 material questions，直接嵌在 Workspace。

範例：

    還差一點資訊
    1. 每個人可以選幾家餐廳？
       ( ) 1 家   ( ) 最多 3 家   ( ) 不限制
    2. 投票結果要即時顯示嗎？
       [是] [否]
                                      [繼續]

required / optional 清楚；答案可修改；Continue 後回 ANALYZING，不開新頁。

# 9. ASSUMPTION_REVIEW

只有 material、可逆但會影響 outcome 的假設才顯示。

    確認幾個設定
    投票截止時間  [今晚 9:00]   建議
    每人最多選    [3 家 ▼]      預設
    結果顯示      [即時]        建議

    [修改]                 [用這些設定繼續]

User-facing source labels只用：已提供 / 預設 / 建議 / 尚未決定。

# 10. BUILDING / Visible Generation Progress

Proposed 4 stages：

1. 理解你的想法
2. 整理成 App
3. 確認互動可以執行
4. 準備你的 App

規則：
- stage-based bar / stepper。
- Active stage 有 bounded motion。
- 不顯示假百分比。
- validation-driven recompose 保持在同一 BUILDING surface。
- 若需要 User decision，才回 Clarification / Assumption。

# 11. HYDRATING

Blueprint validated 後顯示短暫：

    正在打開你的 App…

保留 progress visual continuity；不再顯示 Compiler 類 copy。READY 後直接進 S03，不增加「完成」中介頁。

# 12. Recovery

Recoverable failure 使用 O03，不離開 S02：

    目前沒完成，但你的內容還在。
    [再試一次] [修改需求]

必須保留 original intent、answers、accepted assumptions 與 safe progress context。

# 13. CTA Mapping

| State | Primary CTA |
|---|---|
| ANALYZING | none / Cancel secondary |
| CLARIFICATION_REQUIRED | Continue |
| ASSUMPTION_REVIEW | 用這些設定繼續 |
| BUILDING | none |
| HYDRATING | none |
| RECOVERABLE_FAILURE | Retry / context-specific action |

Fast Path 仍要求 User 明確按一次「確認建立」，作為開始實際生成前的最後確認。

# 14. Visual Guardrails

- Clean / low distraction。
- Must not resemble Google/Search UI。
- Tiffany Blue → Yellow 只作未來 High-fi direction。
- progress 要像「創作正在形成」，不能像下載器或 deployment console。
- 不堆滿 technical badges / status chips。

# 15. Accessibility / Responsive

- Stepper 不只靠顏色表示 state。
- Active stage有 text / icon / aria-current equivalent。
- Motion支援 reduced-motion。
- Question具有 label / error association。
- Keyboard可完成 clarification / assumption。
- Mobile CTA不可遮住最後一題。

# 16. Low-fi Review Questions

本輪請確認四件事：

1. S02 維持單一 focused workspace，而不是 chat conversation / dashboard？
2. Progress 採 4 stages：理解 → 整理成 App → 檢查互動 → 準備 App？
3. Clarification / Assumption 都嵌在同一 Workspace，不跳 modal / 新頁？
4. Fast Path 資訊足夠時自動繼續，不多一個「確認建立」按鈕？

# 17. Review Status

> **LOW_FI_REVIEW_IN_PROGRESS**

尚未 User approve；批准後才更新 Screen Inventory 為 LOW_FI_DIRECTION_APPROVED。

# 18. Edit Intent UI / Function Contract — Proposed

此項尚未 User approve。

「你的想法 [編輯]」不是單純把原句改字，而是讓 User 在 S02 建立前，能修正 creation intent。

## 18.1 Proposed UI

Compact mode：

    你的想法
    幫我做一個今晚聚餐投票 App，大家可以選餐廳。
    [編輯]

按「編輯」後，不跳頁，原區塊展開成 editable composer：

    ┌────────────────────────────────────┐
    │ 幫我做一個今晚聚餐投票 App，       │
    │ 每人最多選三家，晚上九點截止。     │
    └────────────────────────────────────┘
    [取消]                    [套用修改]

目的：
- 保留 S02 creation context。
- 不把 User 送回 S01。
- 讓 User 在真正 BUILDING 前修正需求。
- 不把 Clarification / Assumption 與 raw intent edit 混成同一種 UI。

## 18.2 Function Behavior

按「編輯」只改 raw creation intent，不直接修改 Blueprint。

Canonical behavior：

    current intent context
    → User edits raw intent
    → Apply
    → create semantic re-analysis on same creation flow
    → invalidate stale clarification / assumptions when affected
    → re-run F01 clarification policy
    → return one of:
       CLARIFICATION_REQUIRED
       ASSUMPTION_REVIEW
       READY_TO_BUILD

Rules：
1. Edit 後不沿用已失效的分析結果。
2. 與新 intent 無衝突的回答可保留；有衝突的答案 / assumption 必須失效或重新確認。
3. 不允許 UI 直接 patch Blueprint。
4. 若已進 BUILDING，是否允許 Edit 需依 cancel semantics；Phase 1 baseline 建議 BUILDING 中不直接 hot-edit。
5. 套用修改後，progress 回到「理解想法」階段。

## 18.3 Proposed Boundary

S02 的「編輯」是 **修改這次要建立的 App 意圖**。

不是：
- 修改已生成 App（那是 F06 Refine / Remix）。
- 修正結果錯誤（那是 F16 Correction）。
- 修改 Runtime input（那是 F03 App Runtime interaction）。

# 19. Confirmed S02 Decisions

目前 User 已確認：

1. 4-stage visible progress：理解 → 整理 App → 檢查互動 → 準備 App。
2. Clarification / Assumption 直接嵌在同一 Workspace，不跳 Modal / 新頁。
3. Fast Path 在進入 BUILDING 前，必須有一次明確「確認建立」。

尚未確認：

- S02 是否採 single focused workspace 作為整體 layout。
- 「你的想法 [編輯]」的 exact UI / edit behavior。
