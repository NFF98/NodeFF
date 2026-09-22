# S03 — App / Runtime

> Screen ID：S03
>
> 狀態：**WORKING — ④A LOW_FI_APPROVED / FUNCTION_DELTA_CLOSED / CROSS_SCREEN_REVIEW_APPROVED / ④B HIGH_FI_APPROVED — WORKING BASELINE**
>
> Phase：Phase 1
>
> Screen-level canonical owner：`working/UI-UX/screens/S03-APP-RUNTIME.md`
>
> Function behavior sources：F00 Experience Shell + F03 Runtime Execution。
>
> 本文件的 ④A Low-fi direction與 Runtime Loading / Timeout Function Delta已完成 User Review；仍不是 Formal Spec或 Cursor implementation authority。

# 1. User Outcome

S03 的核心任務：

> **User 一進來就能直接使用剛生成的 App；NodeFF 本身退到背景，只在需要 Share、Remix、Correct、Revert 或 Recovery 時出現。**

S03 不是 Dashboard，也不是 Builder / Editor。

# 2. Canonical Structure

F00 已定義 APP surface 由兩層組成：

    NFF Shell Chrome
    + Generated App Runtime Frame

Low-fi 原則：

1. **Generated App 是畫面主角**。
2. Shell Chrome 只保留必要產品操作。
3. Shell control 與 App 自己的 controls 必須容易區分。
4. 正常 Runtime interaction 不因 Shell 產生不必要 server calls。
5. 不在 Runtime 畫面顯示 Blueprint / Capability / JSON / technical status。

# 3. Entry / Exit

主要入口：

    S02 APP_READY
    → S03

另一入口：

    S04 Shared App Entry / Restore
    → S03

主要出口 / secondary flow：

    S03 → O01 Share
    S03 → S05 Refine / Remix
    S03 → O02 Correction Composer → S06
    S03 → O03 Recovery
    S03 → O04 Revert Confirmation
    S03 → S01 explicit New / Home

# 4. Proposed Desktop Low-fi

    ┌───────────────────────────────────────────────────────────┐
    │ NodeFF   App Title                         [Share] [•••] │
    ├───────────────────────────────────────────────────────────┤
    │                                                           │
    │                                                           │
    │               GENERATED APP RUNTIME                       │
    │                                                           │
    │      controls / visualization / interactions              │
    │      rendered by F03 from validated Blueprint             │
    │                                                           │
    │                                                           │
    ├───────────────────────────────────────────────────────────┤
    │ Result area — only when canonical result exists           │
    │ Result / summary                                          │
    │ [調整結果]                          [Remix / 修改 App]     │
    └───────────────────────────────────────────────────────────┘

Top shell 原則：
- Generated App 仍是主體，但 Shell Chrome 內的重要功能必須明顯、可快速操作。
- App identity 可用 App Title、App Logo，或 Logo + Title，依 App metadata / available space決定。
- Share 屬高優先功能，預設 visible。
- Remix / Correct / Revert 等功能依重要性與當前 context決定是否 visible。
- 空間不足時，低優先功能才收進 More / overflow（•••）。

原則不是「全部塞 Header」，也不是「全部藏起來」，而是：
> 重要功能先顯示；顯示不了才收進 overflow。

# 5. Proposed Mobile Low-fi

    ┌────────────────────────────┐
    │ ‹  App Title    Share  ••• │
    ├────────────────────────────┤
    │                            │
    │     GENERATED APP          │
    │     RUNTIME FRAME          │
    │                            │
    │     app controls           │
    │     app result/content     │
    │                            │
    ├────────────────────────────┤
    │ Result（有結果時才出現）    │
    │ [調整結果]   [Remix]       │
    └────────────────────────────┘

Mobile 原則：
- App 本體仍優先佔最大可用空間。
- **採 NodeFF permanent bottom navigation**，承接最重要的 Shell actions。
- Bottom navigation 必須精簡，只放高頻／高價值操作。
- Result actions 仍只在需要時出現。
- 若 Generated App 本身需要 bottom controls，必須在 layout 上避免與 NodeFF bottom navigation互相遮擋或搶操作區。

# 6. Runtime App Area

Generated App area 完全由 F03 render tree呈現。

S03 Shell：
- 不直接 mutation App state。
- 不把 Generated App 的 button / input 包成 NodeFF control。
- 不替 Runtime 猜 result。
- 不攔截正常 local interaction。

User 應感覺：

> 「我現在正在用這個 App。」

而不是：

> 「我還在 NodeFF 的生成工具裡。」

# 7. Shell Chrome — Proposed Priority

## Always Accessible

- App identity：Title / Logo / Logo + Title。
- Share。
- 其他高優先功能依當前 screen width / device context保持 visible。
- Mobile 由 bottom navigation承接核心 NodeFF actions。
- **S03 是 Phase 1 唯一 permanent NodeFF bottom navigation host。**
- 進入 S05 Refine / Remix 或 S06 Correction Compare 時，不把 S03 bottom navigation 帶入 focused workspace。
- O01 / O02 / blocking O03 / O04 active 時，underlying S03 Shell controls與 bottom navigation 必須 inert；Overlay close後再恢復。

## Contextual

- Correct / 調整結果：只有 canonical result exists 時。
- Previous Version / Revert：只有 current session correction eligible 時。
- Recovery notice：只有 failure / degraded state 時。

Low-fi 建議：
- Share 作 visible action。
- 重要功能能顯示就顯示；只有空間不足或低頻 action才收進 overflow。
- Correct 與 Result 放在一起，避免與 Remix 混淆。
- Remix 明確代表「修改 App 本身」。
- Revert 為 contextual action，只在 eligible 時出現；位置可依空間與重要性決定。

# 8. Result Surface

若 F03 canonical `result.outputs` 有 AVAILABLE output：

S03 可顯示 result area。

    ┌──────────────────────────────┐
    │ 結果                         │
    │ 目前推薦：A 餐廳             │
    │                              │
    │ [調整結果]        [分享]      │
    └──────────────────────────────┘

Rules：
- Result 不從 DOM 猜。
- ERROR output 不顯示 fake value。
- 沒有 result contract 的 App，不硬塞 Result 卡。
- Generated App 如果自己已自然呈現 result，Shell result summary可以省略，避免重複。

# 9. Share Entry — O01

Share 不離開 S03 主 context。

    Share
    → O01 Share Overlay

Share pending / success / failure 都保留 App。

O01 詳細 presentation 見 `working/UI-UX/overlays/O01-SHARE.md`。

# 10. Remix / Refine Entry — S05

User 想改的是「這個 App 本身」：

    S03
    → Remix / 修改這個 App
    → S05

原 App 必須可返回。
Runtime input mutation不等於 Refine。

# 11. Correct Result Entry — O02 → S06

只有 result存在時，才顯示：

    調整結果
    邏輯不對
    結果不是我想要的

Flow：

    S03
    → O02 Correction Composer
    → correcting
    → S06 Compare

Correct不是一般 App editing，所以不和 Remix 混成同一個 CTA。

# 12. Previous Version / Revert — O04

只有 active Blueprint 是同 session accepted correction，且 base仍可執行時才出現。

建議位置：
- Desktop：overflow / secondary menu。
- Mobile：overflow。

不常駐 primary action，避免一般使用流程增加噪音。

# 13. Recovery / Partial Failure

F03 node-level failure：

    failed subtree
    → safe fallback
    → rest of App stays usable

S03 不應整頁 white screen。

Recoverable：
- 保留 App。
- O03 / inline notice 說明問題。
- next actions 1–3 個。

Fatal：
- 不 render half-trusted App。
- 進 Blocking Recovery。

# 14. Empty / Loading / Transition

S03 本身不承接長時間 BUILDING；那屬 S02/O05。

S03 可有：
- very short app mounting transition。
- capability-local loading。
- result pending state（若 Blueprint contract本身定義）。

但不能重新顯示「正在理解你的需求」。

## O05 Runtime Loading Function Contract

User 已在 O05 Low-fi 明確要求：

> **S03 normal local Runtime interaction 也要顯示 global loading。**

Working F00/F03/F12已閉合此 Material Delta；既有 Formal Spec暫時保留舊語意，待 pre-Cursor Formal Spec Refresh一次同步。

Low-fi presentation contract：
- 每次被 F03 accepted / admitted 的 Runtime interaction都建立 operation token並進入 logical global processing state；不是等到 commit後才開始。
- 若有可驗證 checkpoints，使用 Stage + checkpoint-derived Progress %。
- 不用時間預估製造假百分比。
- 只有 commit成立後才可顯示100%。
- 不為了動畫故意延遲操作完成。
- 極快、同一 render frame內完成的 interaction可能看不到完整 loading frame，這不算 violation。
- Soft Timeout停在最後真實 checkpoint；Hard Timeout由 F03 discard未提交 transaction並交 F12回 safe S03或 terminal safe-state。

# 15. Desktop / Mobile Responsive Rules

Desktop：
- Runtime frame優先寬度與可用空間。
- Shell actions 不做大型 sidebar。
- Result area可以在 Runtime下方或 contextually adjacent，但不得擠壓 App 核心操作。

Mobile：
- compact top chrome + permanent bottom navigation。
- Generated App 仍優先取得最大內容空間。
- bottom navigation只放高頻／高價值 Shell actions。
- overflow收納低頻 actions。
- 若 Generated App 自己有 bottom controls，必須預留安全區與避免重疊。
- shell overlay不能破壞 App current state。

# 16. Accessibility Baseline

- Shell control與 Generated App controls都有可辨識 accessible name。
- focus進入 S03後，優先落在 App主要內容 / heading。
- Overlay close後 focus回到觸發入口。
- node failure fallback可被 assistive technology感知。
- Result change / correction success使用非破壞性 live announcement when appropriate。
- Mobile touch targets維持可操作尺寸。

# 17. Confirmed S03 Low-fi Decisions

User 已確認：

1. **Generated App 佔畫面絕對主體**；NodeFF Shell Chrome保持極簡，但 Share等重要功能必須明顯。
2. App identity 可以是 **App Title、Logo，或 Logo + Title**。Header / Shell 的重要功能能顯示就顯示；空間不足時才收進 `•••`。
3. **Correct 與 Remix 不混在一起**：
   - Correct = 調整結果 / 邏輯。
   - Remix = 修改 App 本身。
4. **Mobile 採 permanent bottom navigation**，但仍要把最大可用空間留給 Generated App。
5. Generated App若自己有 bottom controls，NodeFF bottom navigation必須避免遮擋與操作衝突。

# 18. Review Status

> **LOW_FI_DIRECTION_APPROVED — HIGH_FI_PENDING**

S03 ④A Low-fi與 Runtime Function Delta已完成 User Review。

依固定流程，下一步進 `Cross-Screen Consistency Review → High-fi Design System → ④B High-fi`。Formal Spec與 Cursor implementation仍維持 HOLD。


---

# 19. ④B High-fi Structure + Function Handoff Contract

Approved by User：2026-09-22

本節鎖定 S03 ④B High-fi 的結構、geometry 與 UI ↔ Function handoff。後續視覺與完整圖不得自行改寫 Function semantics。

## 19.1 Desktop / Mobile Structure

Desktop：
- Header約 64–72px。
- 左：NodeFF Logo + App Identity。
- 右：`修改這個 App`、`分享`、`•••`。
- NodeFF Logo = explicit Home / New App escape hatch，回 S01 Discover / Start。
- 不搬入 S01 的完整 navigation。
- Generated App Runtime Frame為絕對主角。
- Runtime max-width約 1200–1280px；頁面左右保留 24–40px breathing room。
- Generated App內容區至少佔首屏約 70vh；內容更長時自然延伸。
- Result / NodeFF Action Surface僅在有 canonical result且需要 NodeFF-level action時出現。
- Result Surface與 Runtime Frame同寬，在內容流內，不做右側 sidebar。

Mobile：
- Header約 56–64px。
- Header只保留 NodeFF Logo / App Identity / `•••`。
- Share / Modify不塞入 header。
- permanent bottom navigation固定：
  `App / 修改 / 分享`。
- `App`只代表 current active destination，不自行加入 reset / scroll-to-top 等未定義行為。
- Runtime內容左右 padding約 16px。
- bottom navigation約 64–72px + safe area。
- Generated App如有自己的 bottom controls，Runtime必須預留安全區避免重疊。
- Result Surface在內容流中，不 floating於 bottom nav上方。

## 19.2 Visual Hierarchy

固定優先順序：

~~~text
Generated App
> App Title / Identity
> Primary NodeFF actions
> Result correction actions
> NodeFF brand chrome
> Overflow actions
~~~

S03 不採中央窄欄 SaaS Dashboard版型；Runtime需有較大橫向自由度。

## 19.3 UI ↔ Function Handoff — Mandatory

### 1. Generated App Interaction → F03

- Generated App內 click / input / toggle / local calculate皆由 F03 Runtime處理。
- S03 Shell不得直接 mutation Runtime state。
- Shell只訂閱 F03 operation lifecycle / checkpoint projection。
- 同一 Instance遵循 F03 single-writer / FIFO / atomic commit。
- UI不得以 presentation state決定 commit。

### 2. Share → F05 → O01

- `分享`呼叫 F05 Share flow並呈現在 O01。
- Share不離開 S03主 context。
- current Runtime Instance保留。
- Share只分享 Blueprint durable reference，不包含目前 Runtime inputs / result。
- Share failure不得破壞 current App。

### 3. 修改 → F06 → S05

- `修改` / `修改這個 App`進 F06 Refine / Remix flow。
- 不得原地 mutation既有 immutable Blueprint。
- 變更完成後產生 new immutable Blueprint + lineage + fresh Runtime Instance。
- original App必須可返回。
- Runtime input change不等於 Refine。

### 4. 調整結果 → F16 → O02 → S06

- `調整結果`只在 F03 canonical `evaluateResult()` / `result.outputs`存在 `AVAILABLE` output時可顯示。
- UI不得從 DOM或畫面文字猜 result。
- Entry → O02 Correction Composer → F16 correcting → S06 Compare。
- Correct = outcome / logic correction；不得和 Modify App混為同一 semantic action。

### 5. 回到修正前版本 → F16 / F00 → O04

- 只有 current active Blueprint為 same-session accepted correction child，且 previous/base仍 trusted + compatible時才提供。
- 預設放 `•••` contextual menu，不常駐 primary。
- O04負責確認 target與 input restoration truth。
- UI不得自行推定版本可 revert。

### 6. NodeFF Logo → F00 → S01 / New App

- NodeFF Logo是明確 global escape hatch。
- 進 S01 Discover / Start，讓 User建立新的 App。
- 不依賴 Browser Back，避免 accidental Back丟 active App。
- Mobile `•••`可提供文字備援 `回到首頁 / 建立新的 App`，但不搬入整套 S01 navigation。

## 19.4 Runtime Processing Presentation

F03 每個 accepted / admitted Runtime interaction都建立 operation token並進 logical `GLOBAL_PROCESSING`。

High-fi presentation：
- 極快、同一 render frame完成 → 不強迫 paint loading frame。
- 可見 processing優先使用 Runtime Frame頂部的 subtle progress rail + stage label。
- reliable checkpoints → Stage + checkpoint-derived %。
- no reliable checkpoints → Stage only。
- 不 fake %。
- 不用 elapsed time灌進度。
- 不為了動畫延遲真正完成。
- normal processing不 blanket-disable整個 App；只依 Function truth限制受影響 interaction。
- Soft Timeout提升 processing presence但保留 last true checkpoint。
- Hard Timeout → F03 discard uncommitted transaction → F12 / O03 recovery。

## 19.5 Function-driven Eligibility

以下 UI visibility必須由 Function truth驅動，不由 Screen猜測：

- `調整結果`：canonical AVAILABLE result。
- `回到修正前版本`：revert eligibility。
- Share state：F05 state。
- Processing stage / %：F03 / O05 lifecycle projection。
- Recovery severity / next actions：F12 / O03。
- Modify / Remix semantic flow：F06。

S03 Screen只擁有 presentation，不成為第二份 Function truth。


---

# 20. ④B Detailed High-fi Visual Rules — Approved

Approved by User：2026-09-22

本節是 S03 的 Detailed High-fi contract。它與第 19 節 UI ↔ Function handoff共同構成 Cursor 未來實作時的 Working visual authority；不得只依 mockup猜 behavior。

## 20.1 Core Visual Principle

S03 是 User 真正「使用 App」的關鍵 surface。

固定 attention hierarchy：

~~~text
Generated App
> App Identity
> Primary NodeFF actions
> Result-specific correction action
> NodeFF brand chrome
> Overflow actions
~~~

目標：
- Generated App取得約 80–90% attention。
- NodeFF存在但退到背景。
- User感覺是「我正在用 App」，不是「我在 NodeFF Dashboard裡操作一個 widget」。

禁止：
- sidebar / inspector。
- dashboard card sea。
- technical console / JSON / Blueprint badges。
- 把 Generated App包成一個小 preview card。
- 讓 NodeFF shell比 App內 primary action更搶眼。

## 20.2 Shell vs Generated App Boundary

NodeFF Shell：
- 使用固定 Direction A system tokens。
- white / very-soft neutral surface。
- subtle divider；不使用厚陰影、glassmorphism或大面積 brand gradient。
- Shell controls與 Generated App controls要視覺可區分。

Generated App：
- 可以有自己的 app presentation / visual personality。
- 不強制重畫成 NodeFF元件。
- Runtime Canvas不預設再包一層巨大 white card。
- F00只擁有 shell；F03 render tree擁有 App area。

Design System principle：

> **NodeFF owns the shell; creators own the App presentation.**

## 20.3 Desktop Header

Geometry：
- 約 `64–72px`高。
- single row。
- left = `NodeFF Logo → App Identity`。
- right = `修改這個 App / 分享 / •••`。

Left：
- NodeFF Logo低視覺重量，但明確可點。
- Logo → F00 → S01 / New App。
- App Logo + App Title為主要 identity。
- App Title約 `18–20px semibold`。
- title過長使用 single-line ellipsis，不撐高 Header。
- NodeFF與App identity之間可用 subtle divider / spacing區隔。

Right actions：
- `分享`：compact Teal primary shell action。
- `修改這個 App`：secondary / outline / ghost treatment。
- `•••`：icon-only overflow，touch/click target仍 ≥44px。
- `修改這個 App`與`分享`需 visible；Revert等低頻 contextual action進 overflow。
- Shell action visual weight不得高於 Generated App真正的 primary CTA。

NodeFF Logo hover / focus可提供 accessible tooltip：`回到首頁`。

## 20.4 Runtime Canvas Geometry

Desktop：
- max-width約 `1200–1280px`。
- viewport左右 breathing room約 `24–40px`。
- initial usable App area至少約 `70vh`，但不是固定高度。
- 內容長時自然 document scroll。
- full-width Capability可依 contract突破一般內容欄，但仍受 viewport safe-area / overflow control。
- 不做中央窄欄 SaaS form版型。

Mobile：
- Runtime全寬。
- content horizontal padding約 `16px`，但 Generated App可依 component contract使用 edge-to-edge presentation。
- 需預留 permanent bottom nav + safe area。
- Generated App若自己有 bottom controls，必須再加入足夠 spacing，兩層 controls不可互相遮擋。

## 20.5 Result Surface / Correct Placement

Result Surface不是常駐空白區。

Visibility：
- 只有 F03 canonical `evaluateResult()` / `result.outputs`存在 `AVAILABLE` output且需要 NodeFF-level result action時出現。
- UI不能從 DOM、screen text或視覺 pattern猜 result。

Placement：
- 與 Runtime Frame同寬。
- 位於 normal content flow。
- 不做右側 sidebar。
- 不 floating覆蓋 App。

Duplication rule：
- Generated App已清楚呈現 result → NodeFF不重複抄一次 result value。
- Result Surface只提供必要 result-specific action。

**Approved semantic / visual separation：**
- `修改這個 App`固定在 Header / Mobile bottom navigation → F06。
- `調整結果`只在 canonical result附近 → F16。
- Result Surface **不再重複放「修改這個 App」**。

因此「改 App」與「改結果」在語意與視覺位置都天然分流。

## 20.6 Runtime Processing / Global Loading

F03 accepted / admitted interaction建立 operation token後，S03進 logical `GLOBAL_PROCESSING`；但 High-fi presentation必須克制。

Presentation：
- 極快、同一 browser render frame完成 → 不強迫 paint loading。
- 肉眼可見 processing優先使用 **Runtime Canvas頂部 subtle progress rail + stage copy**。
- rail約 `3–4px`。
- reliable checkpoints → Stage + checkpoint-derived %。
- no reliable checkpoints → Stage only。
- 不 fake %。
- 不以 elapsed time平滑灌進度。
- 不為 animation故意延遲 completion。
- operation commit成立後才可到100%。

Interaction rule：
- normal processing不 blanket-disable整個 App。
- 只有 Function truth要求不可重入/受影響的 control才 disabled / pending。
- F03仍維持 single-writer / FIFO / atomic commit；presentation state不能決定 Runtime commit。

Soft Timeout：
- 保留 last true checkpoint。
- processing presence可提高一級。
- human copy例如：`還在處理，內容會保留`。
- 不跳 fake error。

Hard Timeout：
- F03 discard uncommitted transaction。
- 交 F12 / O03 humanized recovery。

## 20.7 Mobile Header

約 `56–64px`。

固定：
- NodeFF Logo。
- App Identity / Title。
- `•••`。

Rules：
- 不塞 `分享` / `修改`到 top header；由 bottom navigation承接。
- NodeFF Logo → S01 / New App。
- `•••`提供 contextual低頻 action。
- `•••`可包含文字備援：`回到首頁 / 建立新的 App`。
- 不搬入 S01的首頁 / 探索 / 我的 App完整 navigation。
- title過長 ellipsis。

## 20.8 Mobile Permanent Bottom Navigation

固定三項：

~~~text
App | 修改 | 分享
~~~

Geometry：
- 約 `64–72px + safe area`。
- fixed bottom。
- icon + text。
- touch target ≥44px。

State：
- `App` = current active destination。
- active `App`使用 Teal icon + text / active indicator。
- `修改`、`分享`預設 neutral。
- 不做中央大 FAB。
- 不用大面積 Yellow fill。
- `App`不得自行發明 tap-to-reset / scroll-to-top等未定義 behavior。

Function mapping：
- `修改` → F06 → S05。
- `分享` → F05 → O01。
- `調整結果`不放 permanent nav，因為它是 result-conditional。

## 20.9 Contextual Overlay Visual Family

原則：
> Overlay是在目前 App上完成一件事，不是跳去另一個產品。

O01 Share：
- Desktop約 `420–480px` lightweight dialog / anchored panel。
- Mobile bottom sheet。
- Runtime context仍可辨識。
- Share pending不變成 full-screen loading。

O02 Correction：
- 使用同一 overlay family，但內容聚焦「哪裡需要調整」。
- 由 canonical result context進入。

O04 Revert：
- 使用 confirmation family。
- destructive / consequential action不能用品牌 Yellow當 danger。

O03 Recovery：
- INFO / DEGRADED → inline / node-level。
- BLOCKING_RECOVERABLE → dialog / sheet。
- TERMINAL → safe-state presentation。

Layering：
- O01 / O02 / blocking O03 / O04 active時，underlying Shell + bottom nav inert。
- close後 focus回 trigger / safe surface。
- inline node-level recovery不鎖整頁。

## 20.10 Brand / Color Management

S03沿用 Direction A，但比 S01/S02更克制：

~~~text
Neutral / White ≈ 70%+
Teal family      ≈ 20%
Yellow           ≤ 10%
~~~

實際 S03 Yellow可低於10%。

用途：
- Neutral：canvas、shell、secondary UI。
- Teal：Share、active bottom nav、focus、processing rail、interactive active states。
- Aqua：Teal過渡 / restrained progress support。
- Yellow：small new / completion / energy marker。

Yellow不得：
- 當一般 warning。
- 鋪滿 Header / bottom nav / Runtime。
- 取代 danger semantic color。

不能只靠顏色表達 status / current / error。

## 20.11 Motion

- Hover：約 `120ms`。
- 一般 UI transition：約 `180ms`。
- completion / recovery transition：約 `240ms`內。
- Runtime operation完成不做煙火 / confetti。
- 可使用 progress rail收束 + content update。
- 不使用持續 pulse吸走 App注意力。
- prefers-reduced-motion：移除不必要 slide / pulse / animated progress flourish，保留狀態改變。

## 20.12 Interaction / Component States

S03 Shell components至少需：

~~~text
DEFAULT
HOVER
FOCUS_VISIBLE
PRESSED
DISABLED where applicable
LOADING where applicable
ACTIVE / SELECTED where applicable
~~~

- focus ring visible。
- disabled仍需可讀。
- icon-only overflow有 accessible name。
- loading不能只靠 spinner。
- selected / active不能只靠顏色。

Generated App component states由 Capability / F03 contract擁有，不由 S03 Shell覆寫。

## 20.13 Accessibility

- Shell / Runtime focus order符合 visual hierarchy。
- initial focus進 App主要 heading/content，不先跳 bottom nav。
- overlay focus trap / restore明確。
- aria-live只適度通知 operation / result change，不連續洗屏。
- mobile touch target ≥44 CSS px。
- bottom nav safe-area aware。
- color不是唯一 state indicator。
- node failure fallback可被 assistive technology感知。
- Runtime content不能被 fixed nav遮住。

## 20.14 Cursor Guardrails

Cursor不得自行：
- 把 Runtime變 Dashboard。
- 新增 sidebar / inspector。
- 從 DOM猜 canonical result。
- 在 Result Surface重複放「修改這個 App」。
- 把 `調整結果`常駐在沒有 canonical result的 App。
- 把每個 local click變 full-screen spinner。
- 為了 loading animation故意延遲 operation。
- 把 Header塞入 S01完整 navigation。
- 在 mobile top header重複 Share / Modify。
- 讓 bottom nav遮住 Generated App controls。
- 讓 mockup sample content變成 Function requirement。

S03 implementation authority順序：

1. 本文件第 19–20 節文字 contract；
2. `working/UI-UX/DESIGN-SYSTEM.md`；
3. approved S03 visual reference；
4. 其他示意圖。

若 visual reference與文字 contract衝突，文字 contract優先。

# 21. S03 ④B Approval Status

User 已於 2026-09-22 確認 S03 Desktop + Mobile final High-fi visual。

因此 S03 現在狀態：

> **④B HIGH_FI_APPROVED — WORKING BASELINE**

Formal Spec、Backlog / Sprint與 Cursor implementation仍維持 HOLD，直到 pre-Cursor Formal Spec Refresh。


---

# 22. ④B High-fi Step 1–4 Canonical Lock — Approved

Approved by User：2026-09-22

本節是 S03 High-fi 的 **Step 1 → Step 4 canonical index**。S03是 User 真正使用 App 的關鍵 surface，因此 UI contract必須與 F00 / F03 / F05 / F06 / F12 / F16 handoff一起讀取。

## Step 1 — Structure Lock ✅

Desktop：
- Header左：NodeFF Logo + App Identity。
- Header右：`修改這個 App / 分享 / •••`。
- NodeFF Logo = explicit Home / New App escape hatch → S01。
- 不搬入 S01完整 navigation。
- Generated App Runtime Frame = 絕對主角。
- Result Surface只在 canonical result存在且需要 NodeFF-level result action時出現。
- `修改這個 App`固定由 Header承接。
- `調整結果`只在 result附近出現。
- Revert等低頻 contextual action進 `•••`。

Mobile：
- Header：NodeFF Logo / App Identity / `•••`。
- permanent bottom navigation：`App | 修改 | 分享`。
- `App`只代表 current destination，不自行新增 reset / scroll-top behavior。
- `調整結果`不進 permanent nav。
- `•••`可提供 `回到首頁 / 建立新的 App`文字備援。

Function handoff：
- Runtime interaction → F03。
- Share → F05 → O01。
- Modify → F06 → S05。
- Correct Result → F16 → O02 → S06。
- Revert → F16/F00 → O04。
- Home/New → F00 → S01。

## Step 2 — Geometry + Visual Hierarchy Lock ✅

Desktop：
- Header約 `64–72px`。
- Runtime max-width約 `1200–1280px`。
- viewport左右 breathing room約 `24–40px`。
- initial usable Runtime area至少約 `70vh`，但不是固定 height。
- content長時自然 scroll。
- Result Surface與 Runtime同寬、在 normal flow，不做右 sidebar。

Mobile：
- Header約 `56–64px`。
- Runtime horizontal padding約 `16px`，Capability可依 contract edge-to-edge。
- bottom nav約 `64–72px + safe area`。
- Generated App若有自己的 bottom controls，需額外預留 spacing。

固定 attention hierarchy：

~~~text
Generated App
> App Identity
> Primary NodeFF actions
> Result-specific correction
> NodeFF brand chrome
> Overflow
~~~

Generated App取得約 80–90% attention；S03不做中央窄欄 SaaS Dashboard。

## Step 3 — Detailed High-fi Visual Rules Lock ✅

Shell：
- white / very-soft neutral。
- subtle divider；不做 glassmorphism、重陰影、大面積 gradient。
- NodeFF Shell與 Generated App controls視覺可辨，但 Shell不得搶 App。

Header：
- App Title約 `18–20px semibold`；過長 ellipsis。
- Share = compact Teal primary shell action。
- Modify = secondary / outline / ghost。
- overflow icon target ≥44px。
- Shell action視覺權重不得高於 App內 primary CTA。

Result：
- 不從 DOM猜 result。
- App已清楚呈現 result時，NodeFF不重複抄 value。
- Result Surface只保留必要 `調整結果`。
- 「改 App」與「改結果」在 visual placement與 Function semantics都分流。

Runtime processing：
- accepted/admitted interaction建立 operation token後有 logical processing state。
- 肉眼可見時用 Runtime頂部約 `3–4px` subtle progress rail + stage。
- reliable checkpoints → Stage + %；否則 Stage only。
- 極快 operation不強迫 paint loading。
- 不 full-screen spinner、不 fake smooth %、不為動畫拖慢 operation。
- 不 blanket-disable整個 App；只依 Function truth限制 affected controls。
- Soft Timeout保留 last true checkpoint；Hard Timeout → F12/O03 recovery。

Mobile bottom nav：
- active App = Teal icon + text / indicator。
- Modify / Share neutral。
- 不做中央大 FAB。
- 不用大面積 Yellow。

Color：
- S03約 `70%+ Neutral / ~20% Teal / ≤10% Yellow`，實際 Yellow可更少。
- Teal = action / active / focus / processing。
- Yellow只作 small energy / completion marker，不當 warning或 danger。

Motion：
- Hover ~120ms。
- general transition ~180ms。
- completion / recovery ≤240ms。
- 不做 confetti / fireworks。
- reduced-motion移除 pulse / slide等非必要效果。

Overlay：
- O01 Desktop約 `420–480px` lightweight dialog / anchored panel；Mobile bottom sheet。
- O01 / O02 / blocking O03 / O04 active時 underlying Shell + bottom nav inert。
- close後 focus restore。
- inline node recovery不鎖整頁。

Accessibility：
- initial focus進 App主要內容，不先落 bottom nav。
- touch target ≥44 CSS px。
- fixed nav不得遮 Runtime。
- state不能只靠顏色。

## Step 4 — Final Visual Reference Lock ✅

User 已確認 S03 Desktop + Mobile final High-fi review board。

Canonical intended repository path：

`working/UI-UX/references/S03-App-Runtime-Highfi-v1.png`

Approved-image boundary：
- 圖片鎖定 layout / visual hierarchy / component language / color use / Desktop-Mobile relationship。
- mockup sample restaurant content、sample labels、sample imagery與 annotation examples不自動成為 Function requirements。
- Step 1–3文字 contract + Fxx Function truth永遠優先於圖片生成誤差。

S03 High-fi Step 1–4：**CLOSED / WORKING BASELINE**。

> Repository binary reference must exist at the canonical path before the pre-Cursor Formal Spec Refresh can mark UI artifact packaging as VERIFIED.
