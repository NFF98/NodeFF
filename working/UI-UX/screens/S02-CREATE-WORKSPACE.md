# S02 — Create Workspace

> Screen ID：S02
>
> 狀態：**WORKING — LOW_FI_DIRECTION_APPROVED / HIGH_FI_PENDING**
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
2. **Fast Path First**：Intent 已足夠時，ANALYZING 後直接進 BUILDING；不插入 clarification / assumption，也不增加固定「確認建立」步驟。
3. **Interrupt Only for Material Decisions**：只有 material clarification / assumption 才停下來問 User。
4. **Visible Progress, No Fake Precision**：採 stage-based progress，沒有可靠百分比就不顯示假數字。
5. **Preserve Context**：原始 Intent、回答、assumptions、draft 持續保留。
6. **Human Language**：不顯示 Prompt A / Prompt B / validator / registry 等工程術語。

# 3. Entry From S01

流程：S01 Prompt Composer → 建立 App → S02。

進入 S02 後不顯示新的空白 prompt。Fast Path 預設只呈現 creation progress；原始需求不作為常駐主區塊。只有 Clarification / Assumption / Recovery 需要 context 時，才顯示可展開的「查看／修改需求」。

# 4. S02 State Model

    ANALYZING
    ├─ FAST PATH → BUILDING
    ├─ CLARIFICATION_REQUIRED → ANALYZING
    └─ ASSUMPTION_REVIEW → BUILDING

    BUILDING → HYDRATING → APP_READY → S03

任何適用 state 都可進 O03 Recovery Overlay。

READY_TO_BUILD 是內部 transition。若 Intent 已足夠且沒有 material clarification / assumption，S02 直接進 BUILDING，不建立額外確認頁。

# 5. Proposed Desktop Low-fi

    ┌─────────────────────────────────────────────────────┐
    │ NodeFF                                  [取消/返回] │
    │                                                     │
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
    │                            │
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

Fast Path 不要求額外確認；只有 Clarification / Assumption 需要 User decision。

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

# 16. Low-fi Review Result

四個核心 Low-fi 問題已完成 User Review；最終方向見第 19 節。

# 17. Review Status

> **LOW_FI_DIRECTION_APPROVED — HIGH_FI_PENDING**

# 18. Contextual Intent Edit — Approved Low-fi Direction

「修改需求」保留，但**不作為 Fast Path 常駐 UI**。

顯示時機：
- CLARIFICATION_REQUIRED：User 需要回看原始需求時。
- ASSUMPTION_REVIEW：User 發現前提本身要改時。
- RECOVERABLE_FAILURE：User 想修改需求再重試時。

Presentation：
- 預設是一個輕量「查看／修改需求」secondary action。
- 展開後在同一 S02 Workspace 編輯，不跳回 S01。
- Apply 後重新進 F01 semantic analysis。
- 受新 intent 影響的 clarification / assumptions 失效並重新判斷。
- UI 不直接 patch Blueprint。

邊界：
- S02 修改需求 = 生成前修改 creation intent。
- F06 Refine = 已生成 App 後修改。
- F16 Correction = 修正結果／邏輯。
- F03 Runtime input = 操作 App。

# 19. Confirmed S02 Low-fi Decisions

User 已確認：

1. S02 預設是低干擾、近乎隱形的 creation layer；不是 Chat conversation / dashboard。
2. 4-stage visible progress：理解 → 整理 App → 檢查互動 → 準備 App。
3. 只有兩類情況打斷 Fast Path：
   - 缺 material information → 1–3 clarification questions。
   - material assumption → 顯示必要 assumptions 供確認。
4. Clarification / Assumption 留在同一 Workspace，不跳 modal / 新頁。
5. Clear Intent Fast Path 不增加固定「確認建立」頁；直接 BUILDING。
6. 「查看／修改需求」是 contextual secondary action，不是 Fast Path 常駐 UI。
7. BUILDING / HYDRATING 不顯示假百分比。

# 20. Review Status

> **LOW_FI_DIRECTION_APPROVED — HIGH_FI_PENDING**

S02 ④A Low-fi 已完成 User Review。

依 Phase 1 UI/UX 固定流程，S02 ④A Low-fi 已完成；**下一步必須進 S02 ④B High-fi**。S02 High-fi 完成並經 User 確認後，才可進 S03。


## 20.1 Next Step

> **S02 ④B High-fi**：確認顏色、字體、間距、圓角、陰影、動畫、Hover / Loading 效果、品牌風格，以及 Desktop / Mobile 視覺一致性。

S02 High-fi 未經 User 確認前，不進 S03。
