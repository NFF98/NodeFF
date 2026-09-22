# S02 — Create Workspace

> Screen ID：S02
>
> 狀態：**WORKING — ④A LOW_FI_APPROVED / ④B HIGH_FI_APPROVED (DIRECTION A)**
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

> **④A LOW_FI_APPROVED — ④B HIGH_FI_APPROVED**

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

S02 ④A Low-fi 與 ④B High-fi 均已完成 User Review。


## 20.1 Next Step

> **S03 — App / Runtime ④B High-fi**。

S02 High-fi 已定稿並進入 Working baseline。


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


---

# 22. ④B Final High-fi Visual Reference — Approved

Approved by User：2026-09-22

Repository reference：

![S02 Create Workspace High-fi v1](../references/S02-Create-Workspace-Highfi-v1.png)

Canonical image path：

`working/UI-UX/references/S02-Create-Workspace-Highfi-v1.png`

## 22.1 Approved Screen Rules Represented by the Reference

Desktop：
- Header = NodeFF + `← 回到建立 App`。
- 不顯示一般 navigation / Share / Profile。
- Creation Progress 為主視覺。
- 4-stage stepper = 理解想法 / 整理 App / 檢查互動 / 準備 App。
- 有 reliable checkpoints 時顯示 checkpoint-derived Progress %。
- `查看需求` 為 secondary expandable action。
- Clarification 顯示在同一 Dynamic Workspace Body。
- 每輪最多 3 個最高優先 material questions。
- Continue 後重新分析；若仍需要，再進下一輪。
- 不顯示 round number。
- Completion 在同一 Workspace transition 為 `你的 App 已完成` + `開啟 App`。

Mobile：
- 無 permanent bottom navigation。
- Header保留 NodeFF + `回到建立 App`。
- compact 4-stage indicator。
- progress / stage 與 Dynamic Workspace 垂直排列。
- Clarification choices 單欄。
- Primary CTA full-width。
- 不顯示 S01 / S02 / S03 等 internal ID。

## 22.2 Reference Boundary

此圖片是 **approved S02 High-fi visual reference**。

實作優先順序：

1. 本文件文字 contract；
2. `working/UI-UX/DESIGN-SYSTEM.md`；
3. approved visual reference。

若圖片生成細節與文字 contract衝突，以文字 contract為準。圖片中的示例 question copy / choice content 只代表 presentation pattern，不自動成為 F01 product semantics。

F01 Creation Progress checkpoint backend gap仍由：

`working/DESIGN-WORKBENCH.md → PENDING-FUNC-004`

追蹤，待獨立 Function Delta Review閉合後再升 Formal Spec。

S02 ④B 已完成。

Next：

> **S03 — App / Runtime ④B High-fi：先鎖結構 → 再鎖視覺 → 最後出完整圖。**


---

# 23. ④B Detailed High-fi Implementation Contract — Approved

Approved by User：2026-09-22

本節把 S02 已批准的 ④B 討論補成 Cursor 可執行的 visual / state contract；Function semantics仍由 F00 / F01 / O05擁有。

## 23.1 Screen Attention Hierarchy

固定順序：

~~~text
Creation Progress
> Current Dynamic Workspace task
> Contextual intent access
> Shell chrome
~~~

- S02不是聊天介面、Dashboard、deployment console或 technical builder。
- 正常 Fast Path需安靜；只有 Clarification / Assumption / Recovery 才提高 surface prominence。
- 大量 white / neutral space保持 focused creation感。

## 23.2 Header Geometry / Treatment

- Desktop約 `64–72px`；Mobile約 `60px`。
- 內容：NodeFF + `← 回到建立 App`。
- Header使用 white / soft neutral、subtle divider；不使用大面積 gradient或重陰影。
- 不顯示首頁 / 探索 / 我的 App / Share / Profile / permanent bottom nav。
- Back control是 secondary chrome，不得比 Creation Progress更醒目。

## 23.3 Progress Component

Desktop主內容 max-width約 `760–840px`。

4 stages：

~~~text
理解想法 → 整理 App → 檢查互動 → 準備 App
~~~

Visual states：
- completed：Teal check + completed label。
- current：Teal active marker；可使用 restrained bounded pulse / flow。
- future：neutral gray。
- %約 `36–44px`。
- progress rail約 `8px`。
- reliable checkpoints → Stage + checkpoint-derived %。
- no reliable checkpoints → Stage only；numeric %與 numeric bar均省略。
- Yellow只在接近 completion / ready作小面積 energy accent，不作 warning。
- 100%只在 actual ready condition成立後。

## 23.4 Dynamic Workspace Surface

正常 processing：
- surface可近乎隱形；Progress是主要視覺。
- 不用 chat bubble、avatar、assistant transcript。

Clarification：
- 使用同一 Dynamic Workspace surface。
- heading方向：`還差一點資訊`。
- 當前每輪最多 3 個 material questions。
- choice優先用大面積 selectable row / pill；單欄優先，避免密集 grid。
- selected state使用 Teal border / light soft surface + icon/label，不只靠色彩。
- 回答送出後上一輪收起 / 替換，只留下可展開 `已提供的資訊`摘要。
- 不顯示「第1輪」「第2輪」等 engine language。

Assumption Review：
- 與 Clarification共用 surface family。
- 每項呈現 `設定名稱 | 目前值 | 已提供/預設/建議/尚未決定`。
- metadata tag使用 neutral treatment；Yellow不是 warning。
- Primary：`用這些設定繼續`。
- Secondary：`修改需求`。

## 23.5 Original Intent Access

- Fast Path不常駐巨大 Prompt card。
- 預設使用輕量 `查看需求` disclosure。
- Clarification / Assumption / Recovery時可升為 `查看／修改需求`。
- 展開後可讀完整 long-form intent。
- 編輯仍在 S02內完成；Apply後由 Function重新分析。
- disclosure open/close不應造成大幅 layout jump。

## 23.6 Processing / Waiting

- 不用 full-screen spinner覆蓋 S02。
- stage / progress只能反映真實 operation。
- checkpoint停住時視覺停在最後真實值，不做 fake smooth percentage。
- bounded animation只表示「仍在工作」，不代表進度。
- Soft/Hard timeout semantics依 O05 / F00 / source Function，不由視覺自行判斷。

## 23.7 Completion Transition

完成後，同一 Progress surface自然轉為：

~~~text
100%
你的 App 已完成
[開啟 App →]
~~~

- 不建立額外 Success Page。
- completion accent可使用 Teal → Aqua → 少量 Yellow。
- check / completion motion約 `180–240ms`。
- reduced-motion時改為直接 state change。
- Primary CTA只有 `開啟 App`。
- User-facing UI不顯示 internal `S03`。

## 23.8 Mobile Composition

順序固定：

~~~text
Header
→ compact stage indicator
→ current stage
→ % / Stage-only
→ Dynamic Workspace
→ contextual CTA
~~~

- compact indicator方向：`✓ 理解   ● 整理   ○ 檢查   ○ 準備`。
- 不硬塞四個完整長標籤。
- Clarification單欄；Primary CTA可 full-width。
- keyboard / viewport resize時，Primary CTA不得遮最後一題。
- 不顯示 S01 bottom navigation。
- 唯一離開入口為 `回到建立 App`。

## 23.9 Component States / Accessibility

- Button、choice、disclosure、progress、input皆需 Default / Hover / Focus / Pressed / Disabled / Loading where applicable。
- touch target ≥44 CSS px。
- focus ring visible且不造成 layout shift。
- progress不只靠 motion；current/completed需文字 / icon / semantics。
- loading status使用適度 aria-live，不連續洗屏。
- clarification question / error與 control做 programmatic association。

## 23.10 Cursor Guardrails

Cursor不得自行：
- 加 chat transcript / AI avatar；
- 加 technical validation logs；
- 加 fake percentage；
- 加 general navigation；
- 加 Share / Profile；
- 加 permanent bottom nav；
- 加第二個 Create CTA；
- 把 Clarification固定成一次問完所有問題；
- 把 Completion改成獨立頁。

S02 implementation authority順序：

1. 本文件文字 contract；
2. `working/UI-UX/DESIGN-SYSTEM.md`；
3. approved visual reference；
4. 其他示意圖。

S02 High-fi細節視為 Working Current Truth；Formal Spec仍待 pre-Cursor refresh。
