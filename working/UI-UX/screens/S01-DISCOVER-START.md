# S01 — Discover / Start

> Screen ID：S01
>
> 狀態：**WORKING — LOW_FI_DIRECTION_APPROVED / HIGH_FI_PENDING**
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
- My Apps。
- 複雜分類 Sidebar。
- Model picker。
- Blueprint / Registry / Runtime technical controls。
- 大量 navigation。
- 不必要 decorative header icons。
- 大型 App Store-like catalog。

這些若未來有 Evidence，需要重新 Review，不因長期可能性提前加入。

# 13. Open High-fi Decisions

仍待後續：

1. 正式 NodeFF color tokens / HEX。
2. Gradient 是否為大面積 background、CTA accent 或動態生成效果。
3. Typography system。
4. Radius / shadow / elevation。
5. Capsule High-fi visual language。
6. Composer 的 final geometry / motion。
7. Header 最終保留 controls。
8. Ghost Text 的正式 copy / rotation rules。
9. Explore 最終 presentation。
10. Desktop / Mobile breakpoint 與 exact spacing token。

# 14. Review Status

已由 User 確認：

- S01 核心內容方向。
- Prompt-first + Capsules supporting。
- Must not resemble Google/Search UI。
- 畫面乾淨。
- 移除右上不必要圖案／控制。
- Tiffany Blue → Yellow 作 High-fi color direction input。
- visible generation progress 應納入 NodeFF，但主要在 S02 設計。

尚未確認：

- High-fi visual design。
- Design tokens。
- exact component styling。
- final responsive pixel-level layout。

因此 S01 目前狀態：

> **LOW_FI_DIRECTION_APPROVED — HIGH_FI_PENDING**

不代表 Spec change approved，也不代表 Cursor 可開始 implementation。
