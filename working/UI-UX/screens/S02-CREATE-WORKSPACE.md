# S02 — Create Workspace

> Screen ID：S02
>
> 狀態：**WORKING — ④A LOW_FI_APPROVED / ④B HIGH_FI_REVIEW_IN_PROGRESS**
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
4. **Visible Progress, No Fake Precision**：採 stage-based progress；有可靠 work checkpoints 時顯示 checkpoint-derived Progress %，沒有可靠 checkpoints 就不假造百分比。
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
    │ ███████────────────  checkpoint-derived % when valid │
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
- 有可靠 work checkpoints時顯示 checkpoint-derived Progress %；沒有可靠 checkpoints時不顯示假百分比。
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
7. BUILDING / HYDRATING 採「有可靠 checkpoints就顯示 %；沒有就不假造」；百分比代表 work completion，不代表剩餘時間。

# 20. Review Status

> **LOW_FI_DIRECTION_APPROVED — HIGH_FI_PENDING**

S02 ④A Low-fi 已完成 User Review。

依 Phase 1 UI/UX 固定流程，S02 ④A Low-fi 已完成。**下一步進 S03 ④A Low-fi**；等 S01–S06 / O01–O05 全部 Low-fi 完成並 Cross-Screen Review 後，才統一進 ④B High-fi。


## 20.1 Next Step

> **S03 ④A Low-fi**。

S02 的 High-fi 方向先保留於 `working/DESIGN-WORKBENCH.md`，待全部 Low-fi 與 Cross-Screen Review 完成後統一進 Design System / ④B High-fi。


---

# 21. ④B High-fi Structure / Geometry / Visual Rules — Approved for Final Mockup

Approved by User：2026-09-22

本節是 S02 final High-fi mockup 的文字 contract。完整圖不得自行新增未批准元素；若圖片與本文衝突，以本文為準。

## 21.1 Workspace Header

User-facing：

~~~text
NodeFF
← 回到建立 App
~~~

Rules：
- 不顯示 S01 / S02 / S03 等 internal Screen ID。
- 不放 Share / Profile / 首頁 / 探索靈感 / 我的 App 等一般 navigation。
- S02 是 focused creation workspace。
- Desktop header約 64–72px；Mobile約 60px。
- Mobile同樣不顯示 permanent bottom navigation。

## 21.2 Original Intent / Draft

- 原始 Intent 必須被保留。
- Fast Path不以大型 Prompt card常駐。
- 預設只顯示輕量 secondary action：`查看需求`。
- Clarification / Assumption / Recovery 時可變為：`查看／修改需求`。
- 展開後可完整閱讀 long-form intent。
- 需要修改時留在同一 S02 Workspace，不返回首頁重填。

## 21.3 Creation Progress — Primary Visual

4-stage consumer progression：

~~~text
理解想法
→ 整理 App
→ 檢查互動
→ 準備 App
~~~

Presentation rules：

~~~text
reliable checkpoints
→ Stage + checkpoint-derived Progress %

no reliable checkpoints
→ Stage only
~~~

- 不存在「沒有 reliable checkpoints但顯示 %」的模式。
- %代表 work completion，不代表 time remaining。
- checkpoint停住時，%停在最後真實完成值。
- 不以 elapsed time / animation timer灌高百分比。
- 100%只在 target ready condition成立後。
- F01 creation checkpoint backend contract另記於 `working/DESIGN-WORKBENCH.md` 的 `PENDING-FUNC-004`。

Desktop：
- primary content max-width約 760–840px。
- 4-stage stepper置於主要內容上方。
- %約 36–44px。
- progress bar約 8px高。

Visual：
- completed = Teal check。
- active = Teal + restrained bounded pulse / flow。
- pending = neutral gray。
- Yellow只在 approaching completion / ready作小面積 energy accent。

## 21.4 Clarification / Assumption Dynamic Workspace

S02只保留一個 Dynamic Workspace Body。

Clarification：
- 標題方向：`還差一點資訊`。
- 每輪最多 3 個最高優先 material questions。
- User回答後：
  `merge answers → re-analyze → 若仍需要則下一輪最多3題`。
- 持續多輪直到所有 required / material unknowns resolved。
- 不是把初始問題機械切成 3 題一組全部問完；每輪重算 priority / necessity。
- 上一輪完成後收起 / 替換，只留下可展開的「已提供的資訊」摘要。
- 畫面永遠只顯示當前最多 3 題。
- 不顯示「第1輪 / 第2輪」等系統批次語言。
- 能用 direct choices時優先使用 selectable rows / pills；不做密集表單。

Assumption：
- 與 Clarification共用同一 surface language。
- 每項顯示：
  `設定名稱 | 目前值 | 已提供/預設/建議/尚未決定`。
- neutral tags，不把 Yellow當 warning。
- Primary CTA：`用這些設定繼續`。
- Secondary：`修改需求`。

## 21.5 Processing State

正常 processing 時保持低干擾：
- 不做 Dashboard。
- 不做 AI chat bubbles。
- 不堆 technical badges / logs。
- Dynamic Workspace Body可以近乎隱形；Progress是視覺主角。
- Clarification / Assumption / Recovery出現時，才形成較明確的 card/surface。

## 21.6 Completion / Handoff

當完成條件成立：

~~~text
100%
你的 App 已完成
[開啟 App →]
~~~

Rules：
- User不看到 S03。
- Completion不建立額外 Success Page。
- 原本 S02 Progress surface自然 transition到 completion state。
- completion可使用 Teal → Aqua → 少量 Yellow accent。
- check animation約 180–240ms。
- Primary CTA只有：`開啟 App`。

## 21.7 Mobile High-fi

Mobile不做另一套產品，只垂直化：

~~~text
Header
→ compact 4-stage indicator
→ current stage label
→ checkpoint-derived % / Stage-only presentation
→ Dynamic Workspace Body
→ contextual primary CTA
~~~

Compact stage example：

~~~text
✓ 理解   ● 整理   ○ 檢查   ○ 準備
正在整理成 App…
~~~

Rules：
- 不硬塞四個完整長標籤。
- Clarification questions單欄。
- Primary CTA full-width且不遮住最後一題。
- 無 S01 bottom nav。
- 唯一離開入口是「回到建立 App」。

## 21.8 Direction A Application

- white / neutral background為主。
- Teal是 creation / progress主色。
- Aqua作過渡。
- Yellow只作 completion / energy accent。
- 不鋪大面積 gradient。
- 保持大量 breathing room。
- 整體感受：quiet, focused, creator-oriented。

## 21.9 Final Mockup Gate

以上結構、geometry、visual hierarchy已由 User確認。

下一步只做：

> **S02 Desktop + Mobile Final High-fi Mockup**

Mockup不得自行新增：
- general navigation
- Share
- Profile
- bottom navigation
- extra Create CTA
- chat transcript
- technical status console
- fake percentage
- unrelated promo / dashboard card

User確認 final mockup後，需像 S01一樣：
1. 把圖片存入 `working/UI-UX/references/`；
2. 在本文件 embed approved image；
3. 將 S02標成 `④B HIGH_FI_APPROVED`；
4. 更新 Phase 1 Screen Inventory；
5. 最終 pre-Cursor Formal Spec Refresh時，文字規格 + approved visual reference一起升格給 Cursor。
