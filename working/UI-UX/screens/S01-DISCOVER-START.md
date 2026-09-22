# S01 — Discover / Start

> Screen ID：S01
>
> 狀態：**WORKING — ④A LOW_FI_APPROVED / ④B HIGH_FI_APPROVED (DIRECTION A)**
>
> Phase：Phase 1
>
> Screen-level canonical owner：`working/UI-UX/screens/S01-DISCOVER-START.md`
>
> Function behavior sources：`working/functions/F00-EXPERIENCE-SHELL.md` + approved `spec/functions/F00-EXPERIENCE-SHELL.md`
>
> 注意：本文件只固定目前已確認的 Screen-level UI/UX。若需要改 F00 behavior contract，必須回 F00 Working Review。

# 1. User Outcome

S01 的核心任務：

> **讓第一次進 NodeFF 的 User，不需要先學 Prompt Engineering，就能很快理解「我可以把現在的想法直接做成 App」，並開始 Create。**

不是讓 User 先理解 NodeFF 的全部功能，也不是把首頁做成傳統搜尋首頁或 App Store。

# 2. Product / UX Direction — Approved

目前已確認：

1. **Prompt-first + Inspiration supporting**。
2. User 可以完全不看 Capsule，直接輸入想法開始。
3. Inspiration Capsules 用來降低空白輸入門檻、示範可能性並支援 Fork / Edit / Run。
4. 首頁資訊保持乾淨、低干擾。
5. 不強迫登入 / 註冊才能取得 First Value。
6. Must not resemble Google / Search UI。
7. S01 的感覺應偏向 **Creator / App-making entry**，不是 Search page。

# 3. Low-fi Information Architecture

S01 目前固定四個核心區塊：

## A. Brand / Value Statement

必要內容：

- NodeFF brand。
- 主訊息：**意圖就是 App**。
- 一句簡短人話，說明「把你的想法／需求直接變成可用 App」。

目的：
- User 第一眼就知道 NodeFF 做什麼。
- 不塞大量產品教育或技術詞。

## B. Prompt Composer

S01 的主要操作核心。

必要能力：

- natural-language input。
- Ghost Text / example hint。
- Primary CTA：**建立 App**。
- prompt draft 可編輯。
- User 不需先選 model / blueprint / capability / technical settings。

Visual rule：

> Composer 應具有 Creator Canvas / Command Surface 感，不使用「中央 Logo + 單一搜尋框」的 Google/Search 首頁語言。

## C. Inspiration Capsules

用途：

- 給 User「原來可以這樣做」的靈感。
- 顯示 outcome / app-like preview，而不是只有 Prompt 文字。
- 可直接 Try / Fork / Prefill 後修改。
- 第一屏只放少量精選內容，避免首頁變成大型 catalog。

## D. Explore More

用途：

- 想看更多的 User 可以繼續 Explore。
- 不讓 Explore 壓過 Create。
- Explore 是 supporting path，不是 S01 primary path。

# 4. Low-fi Desktop Composition

方向：

~~~text
┌────────────────────────────────────────────────┐
│ NodeFF                         minimal controls │
│                                                │
│ 意圖就是 App                                   │
│ 短句：把你的想法直接變成可用 App               │
│                                                │
│ ┌──────────────────────────────┐  ┌──────────┐ │
│ │ Prompt / Creator Surface     │  │ 建立 App →│ │
│ │                              │  └──────────┘ │
│ └──────────────────────────────┘               │
│   optional prompt suggestion chips             │
│                                                │
│ START FROM AN IDEA                             │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│ │ Capsule  │ │ Capsule  │ │ Capsule  │         │
│ │ preview  │ │ preview  │ │ preview  │         │
│ │ Try →    │ │ Try →    │ │ Try →    │         │
│ └──────────┘ └──────────┘ └──────────┘         │
│                                      Explore → │
└────────────────────────────────────────────────┘
~~~

注意：
- Header / 右上角只保留必要 controls。
- 不必要 theme icon、decorative icon、Sign-in pressure、複雜 navigation 不進 Phase 1 首屏 baseline。
- Desktop 可利用較寬空間呈現更強的 Creator feeling，但不增加無必要資訊。

# 5. Low-fi Mobile Composition

方向：

~~~text
┌──────────────────────────┐
│ NodeFF        minimal UI │
│                          │
│ 意圖就是 App             │
│ 短句                     │
│                          │
│ ┌──────────────────────┐ │
│ │ Prompt Composer      │ │
│ │                      │ │
│ └──────────────────────┘ │
│ [      建立 App →      ] │
│ suggestion chips         │
│                          │
│ 試試這些靈感             │
│ ┌──────────────────────┐ │
│ │ Capsule / Preview    │ │
│ └──────────────────────┘ │
│ ┌──────────────────────┐ │
│ │ Capsule / Preview    │ │
│ └──────────────────────┘ │
│               Explore → │
└──────────────────────────┘
~~~

Mobile rule：
- Prompt Composer + Create CTA 必須容易找到。
- Capsule 採垂直 stack / swipe-friendly presentation，避免必要 horizontal scroll。
- 不因小螢幕增加額外 navigation clutter。

# 6. Primary Interactions

## S01-ACT-001 — Direct Create

~~~text
User types intent
→ Create
→ enter S02 Create Workspace
~~~

Behavior semantics 由 F00 / F01 擁有；S01 只負責 initiation presentation。

## S01-ACT-002 — Start from Capsule

~~~text
User selects Capsule
→ prefill editable prompt / creation context
→ User can edit
→ Create
→ S02
~~~

Capsule metadata 不可偷偷變成 User Explicit fact；此語意仍由 F00/F01 contract控制。

## S01-ACT-003 — Explore

~~~text
User selects Explore
→ expanded inspiration discovery
~~~

Phase 1 是否採同頁展開或獨立 surface，留待後續 Screen review；不可因此阻塞 primary Create path。

# 7. S01 States

目前 Low-fi 需要涵蓋：

- EMPTY / INITIAL。
- USER_TYPING。
- CAPSULE_PREFILLED。
- LOCAL_INPUT_INVALID（例如空內容 / client-required constraint）。
- READY_TO_SUBMIT。

真正的 ANALYZING / CLARIFICATION / ASSUMPTION / BUILDING / HYDRATING 主要由 S02 承接，不讓 S01 同時承載整個 creation lifecycle。

# 8. Navigation / Header Guardrail

Phase 1 S01 Header：

- 必須乾淨。
- NodeFF brand 必須可辨識。
- 非必要 controls 不出現在首屏。
- 不因「以後可能需要」就提前放 Docs / Community / Settings / model picker。
- Registration 不得阻擋 First Value。

右上不必要圖案與裝飾已被明確排除。

# 9. Visual Direction — High-fi Input

High-fi 尚未批准，但目前方向已確立：

### Color
- Tiffany Blue → Yellow 作為色彩探索方向。
- Blue/green side 偏 creation / calm / brand anchor。
- Yellow 偏 energy / completion / accent。
- 正式 HEX、gradient stop、contrast 尚未決定。
- 最終必須形成 NodeFF 自己的 palette，而不是複製 Tiffany brand identity。

### Style
- Clean。
- Playful enough to support Fun / Social。
- Creator-oriented。
- 不像 Google / Search。
- 不過度裝飾。
- 不在首屏放沒有直接作用的 icon / chrome。

# 10. Relationship to Visible Generation Progress

User 已確認「可視化生成進度」是重要 UX。

S01 本身只負責 submit entry；主要 progress presentation 放在 **S02 Create Workspace**。

候選 stage language：

~~~text
理解你的想法…
整理成 App…
確認可以安全執行…
準備你的 App…
完成
~~~

原則：
- 不只 generic spinner。
- 不暴露 Prompt A / Prompt B / Validator 等工程語言。
- 沒有可靠 percentage 時不顯示假的精確百分比。
- 優先 stage-based progress + bounded animation。

# 11. Accessibility / Responsive Baseline

Low-fi baseline：

- Primary CTA 可透過 keyboard 操作。
- Composer 有清楚 label / accessible name。
- Capsule action 不只靠顏色辨識。
- Mobile 不應要求必要 horizontal scrolling。
- High-fi palette 必須再做 contrast 檢查。
- Motion 在 High-fi 階段定義 reduced-motion fallback。

# 12. Explicitly Not in S01 Phase 1 Baseline

目前不在首屏 baseline：

- 強制 Sign in / Sign up。
- Dashboard。
- 完整 My Apps workspace / Dashboard（但 S01 navigation 可顯示「我的 App · Soon」placeholder；見第 15 節）。
- 複雜分類 Sidebar。
- Model picker。
- Blueprint / Registry / Runtime technical controls。
- 大量 navigation。
- 不必要 decorative header icons。
- 大型 App Store-like catalog。

這些若未來有 Evidence，需要重新 Review，不因長期可能性提前加入。

# 12.1 High-fi Direction A Input — Approved

S01 ④B High-fi 必須套用 `working/UI-UX/DESIGN-SYSTEM.md` Direction A：

- Teal為主品牌 anchor。
- Yellow只作 energy accent。
- Teal → Aqua → Yellow gradient只用於 brand / creation moments，不整頁鋪滿。
- 保持大量 neutral / white space。
- Hero / Prompt Composer為首屏視覺主角。
- Inspiration Capsules為 supporting creation path，不得壓過 Create。
- Header維持極簡，不因效果圖示意新增 Phase 1 Low-fi未批准的 navigation。
- High-fi visual reference已由 User確認「可以」；但效果圖不是 pixel-spec，個別 S01 composition仍以本文件既有 Low-fi為基準。

# 13. ④B High-fi Decisions — Resolved

S01 的 ④B High-fi 已於 2026-09-22 完成 User Review。

本 Screen 使用：
- `working/UI-UX/DESIGN-SYSTEM.md` 的 Direction A tokens / visual language；
- 第 15 節 approved structure / geometry；
- 第 16 節 approved visual reference。

未來若需改動已批准 layout / navigation / component presentation，必須重新進 S01 Working Review。

# 14. Review Status

已由 User 確認：

- S01 ④A Low-fi direction。
- High-fi Direction A。
- Desktop / Mobile structure。
- Header navigation。
- Hero presentation。
- long-form Creator Composer geometry / auto-grow rule。
- single Create CTA。
- Inspiration text category navigation。
- 作品展示卡 presentation。
- Footer social icons。
- Mobile bottom navigation。
- 「我的 App」Soon placeholder。
- S01 Desktop + Mobile final visual reference。

因此 S01 現在狀態：

> **④B HIGH_FI_APPROVED — WORKING BASELINE**

此 approval 是 UI/UX Working approval；不代表 Formal Spec promotion，也不代表 Cursor implementation 可開始。

# 15. ④B High-fi Structure v2 — Approved

User approved on 2026-09-22.

## 15.1 Desktop Header

Approved structure：

~~~text
NodeFF Logo | 首頁 | 探索靈感 | 我的 App
~~~

Rules：

- 必須包含「首頁」。
- Profile 暫不出現。
- 「我的 App」Phase 1 先保留 placeholder，不假裝已有完整功能。
- 不放 Search / Login / Notification / Docs / Community / Model Picker。
- 首頁 active state採文字 + Teal indicator，不用大色塊。

## 15.2 Hero

- 主標：**意圖就是 App**。
- 副標暫不放文字，保留空間 / breathing room。
- Hero保持 compact，不浪費首屏。
- Teal為主視覺；Yellow只作小面積 energy accent。

## 15.3 Creator Composer

Creator Composer 是 S01 唯一 Primary Create entry。

Approved geometry：

- Desktop initial height：約 180–220px。
- Mobile initial height：約 160–180px。
- 支援 multi-line long-form intent。
- auto-grow 到約 320–360px 後才內部 scroll。
- Primary CTA只有一顆：**建立 App**。
- 不在 Header / Mobile bottom nav 重複 Create。
- suggestion chips只作 supporting prefill，不搶 CTA。

## 15.4 Inspiration Display

「靈感膠囊」High-fi display改採 **作品展示卡 / App Preview Card**：

~~~text
App 使用畫面預覽
↓
App 名稱
↓
一句 outcome
↓
試試看 →
~~~

Desktop：

- 3 cards / row。
- Preview約佔 card視覺面積 60%。
- 不放 author / like / comment / rating / overflow menu。

Mobile：

- 單欄。
- Preview保持足夠高度，不縮成小 thumbnail。

## 15.5 Inspiration Category Navigation

放在「靈感精靈」作品區上方：

~~~text
全部 | 生產力 | 生活 | 學習 | 工具
~~~

Rules：

- 純文字 Navigation Bar。
- 不使用 category icon grid。
- active category = Teal text + underline。
- Mobile可水平文字 tabs scroll。

## 15.6 Explore

- 「探索更多 →」為 secondary / ghost action。
- 放在靈感區，不進 Header。
- 不搶 Creator Composer Primary CTA。

## 15.7 Footer

- 可放 NodeFF 官方 social icons。
- 不放 App Share button。
- Share App仍只屬 S03 Runtime / O01 Share。
- Footer保持低視覺權重。

## 15.8 Mobile Bottom Navigation

Approved：

~~~text
首頁 | 探索靈感 | 我的 App
~~~

Rules：

- 不放 Create。
- 不放 Profile。
- 「我的 App」Phase 1 placeholder顯示 **Soon**，並採 disabled / unavailable visual state。
- Create仍只由 S01 Creator Composer提供。

## 15.9 High-fi Layout Rule

後續 S01 High-fi圖不得自行新增未批准元素。

若圖中出現：

- 額外 Create button
- Profile
- hamburger
- category icon grid
- App Store-like metadata
- 額外 promotional banner
- Key UI Elements / design-system展示區

皆視為 mockup錯誤，不構成 Working Current Truth。

Next：

> **S01 Desktop + Mobile Layout Wireframe High-fi Review**


---

# 16. ④B Final High-fi Visual Reference — Approved

Approved by User：2026-09-22

![S01 Discover Start High-fi v1](../references/S01-Discover-Start-Highfi-v1.png)

Canonical image path：

`working/UI-UX/references/S01-Discover-Start-Highfi-v1.png`

Desktop：
- Header = NodeFF Logo / 首頁 / 探索靈感 / 我的 App · Soon。
- Profile 暫不出現。
- Hero 只保留「意圖就是 App」；副標位置保留 breathing room。
- Creator Composer 為唯一 Create entry。
- Composer 支援大量 multi-line 輸入與 auto-grow。
- 靈感精靈使用文字 category navigation。
- Inspiration 採 3 cards / row 的作品展示卡。
- Footer 可使用 NodeFF 官方 social icons。

Mobile：
- Header 不放 hamburger / Profile。
- Creator Composer 仍是唯一 Create entry。
- Inspiration cards 單欄。
- Bottom Navigation = 首頁 / 探索靈感 / 我的 App · Soon。
- Bottom Navigation 不放 Create。
- 「我的 App」為 Soon placeholder。

Reference boundary：

此圖片是 approved S01 High-fi visual reference，但 implementation 時仍以本文件文字規則 + `DESIGN-SYSTEM.md` tokens 為準。若圖片生成誤差與文字 contract 衝突，文字 contract 優先。

S01 ④B 已完成。

Next：

> **S02 — Create Workspace ④B High-fi：先鎖結構 → 再鎖視覺 → 最後出完整圖。**


---

# 17. ④B Detailed High-fi Implementation Contract — Approved

Approved by User：2026-09-22

本節把 S01 已批准的 High-fi 討論收斂成 Cursor 可執行的 visual / responsive contract；不新增 Function behavior。若本節與 approved image 的生成誤差衝突，以本節 + 第 15 節 + `DESIGN-SYSTEM.md` 為準。

## 17.1 Canvas / Brand Balance

- 整體採 Direction A：**Clean Creator Canvas + Playful Energy**。
- Neutral / White 為主要 canvas；Teal 是主品牌與 active / creation anchor；Yellow只作小面積 energy accent。
- 預設視覺平衡遵循 Design System 約 `70% Neutral / 20% Teal / ≤10% Yellow`，不是機械 pixel quota。
- 不使用大面積 gradient、霓虹 glow、重陰影或高飽和彩虹分類。
- S01 首屏的 attention hierarchy：
  `Creator Composer > Hero message > Inspiration previews > Explore / Footer chrome`。

## 17.2 Header

Desktop：
- Header保持單列、低密度、低視覺重量。
- 內容固定：`NodeFF Logo | 首頁 | 探索靈感 | 我的 App`。
- active item使用 Teal text / indicator；不使用大型 filled tab。
- `我的 App`若仍為 Phase 1 placeholder，必須以 `Soon` / unavailable treatment 明示，不可假裝可操作。
- 不加入 Profile / Search / Notification / Login / hamburger / Docs / model selector。

Mobile：
- 不使用 hamburger。
- Header只保留必要 brand / page chrome；主要 navigation由底部 nav承接。
- 任何 icon/control touch target需 ≥44 CSS px。

## 17.3 Hero

- 主標固定：**意圖就是 App**。
- 目前不顯示副標，但保留 breathing room，不把 Composer緊貼標題。
- Hero不做大型 marketing banner，不放插畫牆或 promotion。
- Teal可作文字 / small accent；Yellow不得成為整塊 Hero背景。

## 17.4 Creator Composer

- S01唯一 Primary Create entry。
- Desktop initial height：約 `180–220px`。
- Mobile initial height：約 `160–180px`。
- multi-line + auto-grow；約 `320–360px` 後才進 internal scroll。
- Composer surface使用 white / soft neutral、12–16px radius family、subtle border / elevation。
- Focus使用 Teal focus treatment；不能只靠 shadow。
- Placeholder / ghost text 必須明顯弱於真實 user input，但仍可讀。
- suggestion chips是 supporting prefill；不可比 `建立 App`更搶眼。
- Primary CTA只有 `建立 App`；不在 Header或 bottom nav複製另一個 Create。
- Disabled / loading / invalid 狀態沿用 Design System component state contract，不用 opacity-only 表達。

## 17.5 Inspiration Preview Cards

- High-fi採 **App Preview / 作品展示卡**，不是 Prompt card、social feed或 App Store listing。
- Desktop固定以 3 cards / row 作主要組合。
- preview visual約佔 card視覺面積 60%。
- card資訊順序：Preview → App 名稱 → 一句 outcome → `試試看 →`。
- 不顯示 author / likes / comments / ratings / featured badge / overflow noise。
- hover可小幅提升 elevation或 border emphasis；不得用大型 glow / scale跳動。
- Mobile單欄，preview不可縮成小 thumbnail。

## 17.6 Category Navigation / Explore

- Category navigation位於 Inspiration cards上方。
- 使用文字 tabs：`全部 | 生產力 | 生活 | 學習 | 工具`。
- active = Teal text + underline / indicator。
- Mobile可水平 scroll，但不改成 icon grid。
- `探索更多 →`為 secondary / ghost action，只存在 Inspiration區，不進 Header。

## 17.7 Footer

- Footer保持低視覺重量。
- 可放 NodeFF官方 social icons。
- Footer不是 App Share surface，不放「分享這個 App」。
- footer controls需使用同一 icon family與 visible focus。

## 17.8 Mobile Bottom Navigation

固定三項：

~~~text
首頁 | 探索靈感 | 我的 App
~~~

- `首頁`為 current active destination。
- `我的 App`以 `Soon` + unavailable/disabled visual state呈現。
- 不放 Create / Profile。
- 固定在底部時需 safe-area aware，不遮內容。
- active / disabled不能只靠顏色；文字 / icon / status需同時可辨識。

## 17.9 Motion / Accessibility

- Hover約 120ms、一般 transition約 180ms；不用持續 decorative motion搶 Composer注意力。
- prefers-reduced-motion時，移除不必要 slide / pulse，保留 state change。
- keyboard focus順序依：Header → Composer → Create → Inspiration → Explore → Footer。
- body / control contrast、focus、touch target、disabled semantics需通過 Design System accessibility gate。

## 17.10 Cursor Guardrails

Cursor不得自行新增：
- 第二個 Create入口；
- Profile / hamburger / Search；
- promo banner；
- category icon grid；
- social metrics；
- App Store metadata；
- 大型 design-system說明區；
- 未批准的 secondary hero copy。

S01 implementation authority順序：

1. 本文件文字 contract；
2. `working/UI-UX/DESIGN-SYSTEM.md`；
3. approved visual reference；
4. 其他示意圖。

S01 的 High-fi細節視為 Working Current Truth；Formal Spec仍待 pre-Cursor refresh。


---

# 18. ④B High-fi Step 1–4 Canonical Lock — Approved

Approved by User：2026-09-22

本節是 S01 High-fi 的 **Step 1 → Step 4 canonical index**。Cursor / pre-Cursor refresh 不得只看最終圖片；必須同時讀取每一層已鎖定的文字 contract。

## Step 1 — Structure Lock ✅

鎖定內容：
- Desktop Header：`NodeFF Logo | 首頁 | 探索靈感 | 我的 App`。
- Hero主訊息：**意圖就是 App**；副標暫不顯示，但保留 breathing room。
- Creator Composer = S01 唯一 Primary Create entry。
- Inspiration採 **App Preview / 作品展示卡**，不是 Prompt card / social feed / App Store listing。
- Inspiration上方使用文字 category navigation。
- Explore保持 supporting path，不進 Header。
- Footer可放 NodeFF官方 social icons，但不放 App Share。
- Mobile bottom navigation固定：`首頁 | 探索靈感 | 我的 App · Soon`。
- Mobile不放 Create / Profile / hamburger。
- 「我的 App」Phase 1是明確 Soon / unavailable placeholder。

Structure authority：
- 第 15 節 approved structure；
- 第 17 節 detailed implementation contract。

## Step 2 — Geometry + Visual Hierarchy Lock ✅

Desktop：
- Creator Composer initial height：約 `180–220px`。
- Composer auto-grow到約 `320–360px`後才 internal scroll。
- Inspiration = 3 cards / row。
- Preview visual約佔 card面積 60%。
- Hero compact；Composer是首屏視覺主角。
- attention hierarchy：
  `Creator Composer > Hero > Inspiration > Explore / Footer`。

Mobile：
- Composer initial height：約 `160–180px`。
- Inspiration單欄。
- category文字 tabs可水平 scroll。
- bottom nav fixed + safe-area aware。
- 內容不得被 bottom nav遮住。

Geometry不得因 mockup自行新增 sidebar、promo strip、第二個 Create入口或 App Store metadata。

## Step 3 — Detailed High-fi Visual Rules Lock ✅

- Direction A：**Clean Creator Canvas + Playful Energy**。
- brand balance：約 `70% Neutral / 20% Teal / ≤10% Yellow`。
- Teal = brand / creation / active anchor。
- Yellow = small energy accent，不作大面積背景。
- Composer focus = visible Teal focus treatment。
- Inspiration cards採 restrained elevation / border emphasis；不做 neon glow。
- active category = Teal text + underline / indicator。
- Hover約 120ms；一般 transition約 180ms。
- prefers-reduced-motion移除不必要 motion。
- touch target ≥44 CSS px。
- active / disabled / selected不可只靠顏色。
- keyboard focus順序依 visual hierarchy。
- Cursor不得新增 Profile / Search / Notification / extra Create / promo banner / social metrics / category icon grid。

Detailed visual authority：
- 第 17 節；
- `working/UI-UX/DESIGN-SYSTEM.md`。

## Step 4 — Final Visual Reference Lock ✅

Approved reference：

![S01 Discover Start High-fi v1](../references/S01-Discover-Start-Highfi-v1.png)

Canonical path：

`working/UI-UX/references/S01-Discover-Start-Highfi-v1.png`

Rules：
- final image只用來鎖定 composition / density / visual impression。
- 圖片若與 Step 1–3文字 contract衝突，**文字 contract優先**。
- sample content / decorative props不自動成為 Function requirement。

S01 High-fi Step 1–4：**CLOSED / WORKING BASELINE**。
