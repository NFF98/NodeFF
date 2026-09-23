# NodeFF UI/UX Design System

> 狀態：**WORKING — HIGH-FI DIRECTION A APPROVED / FOUNDATIONS BASELINE**
>
> Phase：Phase 1
>
> Canonical owner：`working/UI-UX/DESIGN-SYSTEM.md`
>
> Approved by User：2026-09-22
>
> Scope：定義 S01–S06 / O01–O05 共用的 High-fi visual foundations、design tokens、interaction states 與 component language。
>
> 本文件擁有 visual / presentation rules，不改寫 Fxx Function behavior、Runtime、Data、API、Error、Security、Evidence 或 Acceptance semantics。
>
> Formal Spec、Backlog / Sprint、Cursor implementation 仍維持 HOLD。

---

# 1. High-fi Direction A

NodeFF Phase 1 採：

> **Clean Creator Canvas + Playful Energy**

核心比例：

~~~text
約 70% Neutral / White Space
約 20% Teal Brand Anchor
約 10% Yellow Energy Accent
~~~

設計目標：

- 乾淨、低干擾。
- 有 Creator / App-making 感，不像 Search page。
- 有 Fun / Social energy，但不做玩具感。
- Generated App 是主角；NodeFF Shell 退到背景。
- 品牌活力集中在 creation moment、progress、capsule、success transition。
- 不用大面積高飽和漸層壓過內容。

---

# 2. Brand Color System

## 2.1 Core Brand Tokens

| Token | Value | Role |
|---|---:|---|
| `--nff-teal-600` | `#0F766E` | Primary brand / CTA / active state |
| `--nff-teal-500` | `#12958A` | Hover / active accent |
| `--nff-aqua-400` | `#2DD4BF` | Progress / creation energy / supporting accent |
| `--nff-yellow-400` | `#F4C84C` | Energy / completion / highlight |
| `--nff-yellow-500` | `#EAB83E` | Yellow hover / stronger accent |
| `--nff-ink-900` | `#102124` | Primary text |
| `--nff-text-600` | `#586865` | Secondary text |
| `--nff-surface-0` | `#FFFFFF` | Main surface |
| `--nff-surface-50` | `#F7FAF9` | Soft canvas / section surface |
| `--nff-border-200` | `#DDE8E6` | Default border |
| `--nff-border-300` | `#C8D9D6` | Stronger divider / control border |

## 2.2 Semantic Tokens

~~~text
--color-bg-canvas            = #FFFFFF
--color-bg-soft              = #F7FAF9
--color-text-primary         = #102124
--color-text-secondary       = #586865
--color-border-default       = #DDE8E6

--color-action-primary       = #0F766E
--color-action-primary-hover = #12958A
--color-action-on-primary    = #FFFFFF

--color-accent-energy        = #F4C84C
--color-accent-creation      = #2DD4BF
~~~

Status colors已由 O03 Recovery High-fi Step 3正式鎖定；以下 shared semantic palette為 cross-screen Current Truth。

## 2.3 Shared Semantic Status Palette — APPROVED

> Approved in O03 Recovery High-fi Step 3：2026-09-23
>
> 這裡是 cross-screen semantic status color 的 canonical token SSOT；個別 Screen / Overlay不得自行建立另一套 Success / Warning / Danger colors。

~~~text
INFO
semantic-info-600    = #2563EB
semantic-info-bg     = #EFF6FF
semantic-info-border = #BFDBFE

SUCCESS
semantic-success-600    = #15803D
semantic-success-bg     = #F0FDF4
semantic-success-border = #BBF7D0

WARNING / DEGRADED
semantic-warning-700    = #B45309
semantic-warning-bg     = #FFFBEB
semantic-warning-border = #FDE68A

DANGER / BLOCKING FAILURE
semantic-danger-700    = #B91C1C
semantic-danger-bg     = #FEF2F2
semantic-danger-border = #FECACA

CRITICAL / SECURITY
semantic-critical-800    = #7F1D1D
semantic-critical-bg     = #FFF1F2
semantic-critical-border = #FDA4AF
~~~

Rules：
- Brand Yellow `#F4C84C` ≠ Warning。
- Brand Teal不得作 Success唯一訊號。
- Recovery Primary Safe Action仍預設使用 Brand Teal；按鈕顏色代表安全 next action，不代表 failure severity。
- Severity不得只靠顏色，必須搭配 icon + copy + structure / action semantics。
- Preserved Context不是完整 Success state；material Lost Context通常使用 Warning treatment。
- Unsupported通常使用 Info / Warning family，不自動升級 Danger。
- Critical / Security不得用大片深紅背景製造恐慌，也不得提供 bypass / fake Retry。


---

# 3. Gradient Rule

Approved brand gradient direction：

~~~text
Teal
→ Aqua
→ Yellow
~~~

Recommended token：

~~~css
--gradient-brand-energy:
  linear-gradient(
    105deg,
    #0F766E 0%,
    #2DD4BF 58%,
    #F4C84C 100%
  );
~~~

## Allowed

- S01 brand / creator moment。
- Inspiration Capsule accent。
- O05 Progress fill / creation transition。
- small success / completion accent。
- decorative brand stroke / glow。

## Not Allowed

- 大面積 body text background。
- 所有 Primary Button 都用 gradient。
- 整個 S03 Runtime background長期鋪 gradient。
- Error / Warning / Security state只靠 gradient表達。
- 為了「AI感」加入無意義 rainbow / neon。

原則：

> **Gradient 是品牌時刻，不是整個產品的背景。**

---

# 4. Typography

## 4.1 Font Stack

Latin / number：

~~~text
Inter Variable
~~~

Traditional Chinese / CJK preferred：

~~~text
"Noto Sans TC"
→ "PingFang TC"
→ "Microsoft JhengHei"
→ system-ui
→ sans-serif
~~~

Combined CSS direction：

~~~css
font-family:
  Inter,
  "Noto Sans TC",
  "PingFang TC",
  "Microsoft JhengHei",
  system-ui,
  sans-serif;
~~~

不依賴 decorative display font建立品牌辨識。

## 4.2 Type Scale

| Token | Size / Line Height | Weight | Usage |
|---|---|---|---|
| `display-lg` | 44 / 52 | 700 | S01 hero / major creator moment |
| `heading-xl` | 32 / 40 | 700 | Screen title |
| `heading-lg` | 24 / 32 | 650 | Section / dialog title |
| `heading-md` | 20 / 28 | 600 | Card / workspace heading |
| `body-lg` | 16 / 26 | 400–500 | Main body / form |
| `body-md` | 14 / 22 | 400–500 | UI supporting copy |
| `label-md` | 14 / 20 | 600 | Button / control label |
| `caption` | 12 / 18 | 400–500 | Metadata / helper copy |

Rules：

- Consumer UI不使用全大寫作主要層級。
- 技術 metadata 不應靠超小字硬塞。
- Button 文字最低以 `label-md` 為基準。
- 中文 heading避免極端 letter-spacing。
- Number / progress可使用 tabular numerals where supported。

---

# 5. Spacing System

4px base grid：

~~~text
space-1  = 4px
space-2  = 8px
space-3  = 12px
space-4  = 16px
space-6  = 24px
space-8  = 32px
space-12 = 48px
space-16 = 64px
~~~

Usage：

- control internal gap：8–12。
- card internal padding：16–24。
- workspace section gap：24–32。
- screen major section gap：32–64。
- mobile edge padding：16–20。
- desktop content edge / container padding：24–48。

禁止每個 Screen 自創 13px / 19px / 27px 等任意 spacing。

---

# 6. Radius

~~~text
radius-sm   = 8px
radius-md   = 12px
radius-lg   = 16px
radius-xl   = 20px
radius-pill = 999px
~~~

Usage：

- Input / Button：12px。
- Card / Capsule / Result Surface：16px。
- Dialog / Bottom Sheet：20px。
- Tag / Chip：pill。
- Generated App Runtime不強迫套 NodeFF radius；由 Generated App presentation決定。

---

# 7. Elevation / Shadow

NodeFF預設偏 flat。

~~~text
elevation-0
= no shadow

elevation-1
= 0 1px 2px rgba(16,33,36,.06)

elevation-2
= 0 8px 24px rgba(16,33,36,.10)

elevation-3
= 0 16px 40px rgba(16,33,36,.14)
~~~

Usage：

- normal Card：0 / 1。
- hover / selected Capsule：1 / 2。
- floating overlay / dialog：2。
- major modal：2 / 3。
- 不用強 shadow把每張 card都做成浮島。

---

# 8. Motion

## 8.1 Duration Tokens

~~~text
motion-fast   = 120ms
motion-normal = 180ms
motion-slow   = 240ms
~~~

## 8.2 Usage

- Button / hover / control feedback：120ms。
- Dialog / bottom sheet / menu：180ms。
- creation / progress / preview transition：240ms。
- Runtime operation完成不得為 motion故意延遲。

## 8.3 Easing Direction

~~~text
standard:
cubic-bezier(.2,.8,.2,1)

exit:
cubic-bezier(.4,0,1,1)
~~~

## 8.4 Guardrails

- prefers-reduced-motion 必須有 fallback。
- 不做持續 pulse來假裝 progress。
- 不用 bounce表達 serious recovery / confirmation。
- O05百分比只隨真實 checkpoint前進。

---

# 9. Responsive Foundations

Phase 1 layout bands：

~~~text
Mobile
< 640px

Compact / Tablet
640–1023px

Desktop
1024–1439px

Wide
≥ 1440px
~~~

這是 Design System基準，不代表所有 component只能依 viewport breakpoint切換；可在後續 component High-fi 使用 container-aware adaptation。

## Common Rules

Mobile：
- edge padding 16–20px。
- touch target ≥ 44 CSS px。
- primary decision CTA不可被 keyboard / bottom safe area遮擋。
- sheet / overlay尊重 safe-area inset。

Desktop：
- 不因空間大就增加不必要 sidebar。
- Screen max-width依工作類型決定；S03 Runtime允許更寬。
- long-form decision / compare避免過寬 line length。

---

# 10. Icon Language

Phase 1使用單一 outline icon language：

- default 20px。
- stroke約 1.75–2px。
- round caps / joins preferred。
- icon永遠搭配 accessible name。
- 高風險 /重要 decision不可只顯 icon、不顯文字。
- 不混用多套 icon family造成 stroke / geometry不一致。
- Emoji只可作內容 / playful copy，不取代系統 icon contract。

---

# 11. Component State Contract

所有共用元件至少必須定義：

~~~text
DEFAULT
HOVER
FOCUS_VISIBLE
ACTIVE / PRESSED
DISABLED
LOADING where applicable
ERROR / INVALID where applicable
SELECTED where applicable
~~~

不得只畫 Default。

---

# 12. Button System

## 12.1 Primary

用途：

- 建立 App
- 開始修改
- 使用新版
- 使用修正版
- recovery primary action

Visual：

~~~text
background = Teal 600
text = White
radius = 12
min-height = 44
~~~

States：

- Hover → Teal 500。
- Pressed → darker visual compression，不縮到影響 layout。
- Focus → visible focus ring，不只用 shadow。
- Disabled → neutral surface + readable muted text；不得只降 opacity到不可讀。
- Loading → 保留 label width / geometry；spinner不是唯一狀態資訊。

## 12.2 Secondary

- neutral / white surface。
- border default。
- primary text。
- hover用 soft teal surface。

## 12.3 Ghost

- 無 permanent fill。
- 適合「查看原版」「Explore」「取消」等低優先操作。

## 12.4 Destructive

不得使用 brand yellow代替 danger。

真正 destructive / critical色彩在 Recovery / Confirmation component review建立 semantic token。

---

# 13. Input / Composer

Visual baseline：

- white / soft surface。
- border default。
- radius 12。
- focus使用 Teal focus treatment。
- error必須有 icon/text programmatic association，不只紅框。
- placeholder / ghost text對比必須可讀但不與真實輸入混淆。

S01 Prompt Composer可比一般 TextInput更有 creator-surface感，但仍沿用同一 focus / error / disabled semantics。

---

# 14. Capsule Card

Capsule 是 S01 的品牌核心元件。

Baseline：

- radius 16。
- neutral surface為主。
- 可有小範圍 Teal / Aqua / Yellow accent。
- outcome / app-like preview優先，不做純 prompt text card。
- selected / hover可提升 elevation，但不做大型霓虹 glow。
- CTA wording用「試試看 / 立即試試」等 Consumer copy，High-fi S01 review再定 final copy。

Capsule不使用大量不同彩虹色分類；品牌一致性優先。

---

# 15. App Identity / Shell Chrome

App identity可呈現：

~~~text
Logo
Title
or Logo + Title
~~~

Shell Chrome：

- clean / low density。
- Generated App佔主體。
- S03 permanent bottom navigation只屬 Runtime。
- Shell control使用 NodeFF system tokens。
- Generated App內部 controls不得被強制重畫成 NodeFF元件。

原則：

> **NodeFF owns the shell; creators own the App presentation.**

---

# 16. Progress — O05 Step 3 Synced

> Shared Progress visual rule approved in O05 High-fi Step 3：2026-09-23。
>
> O05是 Progress / Stage presentation owner；Source Function仍擁有 checkpoint / ready / commit truth。

## 16.1 Presentation Modes

只有兩種合法模式：
~~~text
DETERMINATE
→ Stage label + checkpoint-derived Progress %

INDETERMINATE
→ Stage label + bounded activity indicator
~~~

沒有可靠 checkpoints時不得顯示空 rail或假百分比。

## 16.2 Determinate Track / Fill

Track：
~~~text
surface = #F7FAF9
border  = #DDE8E6
radius  = pill
~~~

Normal fill：
~~~text
Teal #0F766E
→ Aqua #2DD4BF
~~~

Rules：
- fill只隨真實 checkpoint completion前進。
- checkpoint不變時保持最後真實值。
- 不使用 elapsed time / timer / provider latency灌 progress。
- 0–99%正常 processing不使用 Warning / Danger semantic colors。

## 16.3 Yellow Completion Boundary

Brand Yellow `#F4C84C`：
- **只在 actual 100% / ready / committed後**允許作小面積 completion accent。
- 0–99%不提前使用 Yellow暗示「快完成」。
- Long Wait / Soft Timeout不使用 Yellow。
- Brand Yellow不是 Warning。

Completion accent可為 very small cap / spark / highlight；不得變成大面積 yellow success surface。

## 16.4 Completion Flourish

`duration = 180–240ms max`

Rules：
- 可使用 small Yellow accent + check / completion mark。
- 不得延遲 target transition。
- target立即 ready時 flourish可以不 paint。
- 不新增 O05-specific Success Card。
- Runtime operation完成不得為 motion故意延遲。

## 16.5 Stage / Number

Stage：
- Ink `#102124`。
- 依 host採 `heading-md` / `body-lg`。
- Consumer human language only。
- 不顯示 Function ID / checkpoint ID / engineering enum。

Percentage：
- Ink `#102124`。
- tabular numerals where supported。
- 不顯示 ETA / remaining seconds。
- Workspace / Restore可較 prominent；S03 / Overlay較 compact。

## 16.6 Indeterminate Activity

- Stage label + small bounded activity indicator。
- 不顯示空 rail。
- 不使用 fake shimmer progress / fake fill。
- indicator只代表 operation active，不代表 work增加。
- reduced-motion可改 static activity mark。

## 16.7 Long Wait / Soft Timeout

- 保持 Teal / Aqua visual language。
- 最後真實 %不變。
- support copy使用 secondary text `#586865`。
- 可搭 neutral / Info icon。
- 不切 Warning Yellow / Danger Red。
- failure / hard timeout正式交 F12 / O03後，才使用 shared semantic status palette。

## 16.8 Motion

~~~text
micro feedback           = 120ms
state / label transition = 180ms
progress transition      ≤ 240ms
completion flourish      = 180–240ms max
~~~

禁止 fake smooth crawl、continuous pulse、infinite shimmer、bounce、red blink，以及在兩個真 checkpoint間自行補 intermediate progress。

## 16.9 Host Visual Adaptation

Workspace：可有較完整 creator-energy presentation。

S04 Restore：更安靜、快速，不增加多餘 flourish。

S03 Runtime：White / Soft Neutral compact surface、radius16、default border、elevation1 baseline；Generated App保持主角。

Overlay：保留原 dialog / sheet visual identity；progress只承接 action region；O03 Retry / O04 Revert不得使用 Danger progress。

## 16.10 Accessibility

Determinate：semantic progressbar + truthful `aria-valuenow/min/max`。

Indeterminate：不偽造 `aria-valuenow`；Stage / status text提供 activity語意。

Required：
- progress不只靠 motion或顏色。
- Stage / completion / Long Wait使用適度 live announcement。
- prefers-reduced-motion有 fallback。
- Cancel / controls touch target ≥44px。
- focus transition不得丟失。

Progress visual goal：

> **讓 User感覺作品正在形成，而不是看 deployment console / file downloader。**

---

# 17. Version / Compare Visual Language

S05 / S06版本區分：

- 文字 label永遠存在。
- Before / Source使用 neutral treatment。
- New / After可使用 Teal / Aqua selected accent。
- Yellow可用於 small “new / changed / highlight” energy marker。
- 不靠單一顏色表達版本差異。
- Compare layout優先 clarity，不追求裝飾對稱。

---

# 18. Overlay / Bottom Sheet

Desktop：

- lightweight dialog / panel。
- radius 20。
- elevation 2。
- overlay max width依內容類型限制。
- 背景 context仍可辨識但 inert when blocking。

Mobile：

- bottom sheet / full-height sheet依內容量與 severity。
- top drag handle只在真的支援 gesture dismiss時顯示。
- primary CTA容易觸及。
- safe-area aware。

O01 / O02 / blocking O03 / O04 active時：
- underlying S03 Shell controls inert。
- close後 focus回 trigger / safe surface。

---

# 19. Focus

Global focus direction：

- focus ring必須 visible。
- 不只靠 browser default，也不完全移除 outline。
- Teal focus treatment需在 white / soft surface都有足夠辨識。
- focus不造成 layout shift。
- keyboard navigation order跟 visual hierarchy一致。

High-fi component implementation前再確定 exact ring thickness / offset token。

---

# 20. Brand Usage Ratio

Default composition target：

~~~text
Neutral / White Space ≈ 70%
Teal family          ≈ 20%
Yellow energy        ≈ 10%
~~~

這不是機械式 pixel quota，而是品牌平衡原則。

若一個 Screen看起來「整頁都在發光」：
→ Yellow / gradient使用過量。

若一個 Screen看起來像一般 enterprise SaaS：
→ creation accent / playful energy不足。

---

# 21. Phase 1 Component Inventory

High-fi至少共用以下 components：

1. Button
2. TextInput / TextArea / Composer
3. Select / Choice / Toggle presentation
4. Tag / Chip
5. Inspiration Capsule Card
6. App Identity
7. Shell Header
8. S03 Bottom Navigation
9. Progress / Stage
10. Result Surface
11. Version Card
12. Compare Card
13. Dialog
14. Bottom Sheet
15. Inline Notice
16. Recovery Surface
17. Empty / Loading / Disabled presentation

逐頁 High-fi不得重新發明同名 component。

---

# 22. Accessibility Gate

High-fi design不得通過，若：

- body / control文字對比不足。
- touch target < 44 CSS px（無合理例外）。
- focus state缺失。
- version / status只靠顏色。
- progress只靠 motion。
- selected / disabled無 programmatic state。
- reduced-motion沒有 fallback。
- overlay focus trap / restore沒有設計。
- mobile keyboard會遮主要 CTA。

---

# 23. What Is Approved vs Still Open

## Approved — Direction A Foundations

- Teal做主品牌色。
- Yellow做 energy accent。
- Teal → Aqua → Yellow 作有限品牌漸層。
- 70 / 20 / 10 balance direction。
- Clean Creator Canvas + Playful Energy。
- Inter + CJK system / Noto Sans TC direction。
- 4px spacing grid。
- 12 / 16 / 20px main radius hierarchy。
- low-elevation / mostly-flat UI。
- restrained motion。
- S03 Runtime chrome低干擾。
- NodeFF Shell與Generated App presentation分離。

## Still Open — To Resolve in ④B

- exact focus ring token。
- exact button heights beyond minimum。
- exact Capsule imagery / illustration language。
- exact Header geometry。
- exact S03 bottom navigation item visual styling。
- final breakpoint tuning per Screen / component。
- dark mode（Phase 1目前未承諾）。

---

# 24. High-fi Sequence

~~~text
Direction A Foundations — APPROVED
→ Core Component High-fi
→ S01 ④B High-fi
→ S02 ④B High-fi
→ S03 ④B High-fi
→ S04 ④B High-fi
→ S05 ④B High-fi
→ S06 ④B High-fi
→ O01–O05 ④B High-fi
→ Final Cross-Screen High-fi Review
~~~

下一步：

> **S01 — Discover / Start ④B High-fi Review**

在 S01 review中優先定：

1. Header geometry。
2. Hero typography / hierarchy。
3. Prompt Composer final geometry。
4. Inspiration Capsule visual language。
5. gradient / yellow實際使用比例。
6. Desktop / Mobile final composition。
7. Ghost Text / suggestion chip visual。
8. Explore presentation。


---

# 25. Visual Direction Validation — Approved 2026-09-22

User 已透過 High-fi Direction A 效果圖確認整體視覺方向可接受。

Approved visual impression：

- **Teal / Green family = 主品牌 anchor。**
- **Yellow = energy / completion / playful accent。**
- Gradient方向維持 **Teal → Aqua → Yellow**。
- 整體仍採 **70% Neutral + 20% Teal + 10% Yellow** 的視覺平衡。
- 感覺應是 **Clean Creator Canvas + Playful Energy**。
- UI要乾淨、明亮、有創作感，但不變成高飽和玩具感或 generic AI SaaS。
- Generated App仍是主角；NodeFF brand chrome不得壓過 App內容。

Visual reference status：

> **APPROVED AS DESIGN DIRECTION REFERENCE — NOT PIXEL-SPEC**

效果圖用來確認品牌氣質、色彩比例、component language、density與整體視覺感受；其中示意 screen / navigation / sample content 不自動成為產品行為或 screen composition Current Truth。

個別 Screen仍必須以：
- 已批准 Low-fi composition；
- Cross-Screen Consistency Baseline；
- 本 Design System；
- 對應 Fxx Function truth

共同進行 ④B High-fi Review。

Next：

> **S01 — Discover / Start ④B High-fi**
