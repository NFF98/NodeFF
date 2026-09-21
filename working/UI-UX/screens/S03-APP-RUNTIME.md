# S03 — App / Runtime

> Screen ID：S03
>
> 狀態：**WORKING — LOW_FI_REVIEW_IN_PROGRESS**
>
> Phase：Phase 1
>
> Screen-level canonical owner：`working/UI-UX/screens/S03-APP-RUNTIME.md`
>
> Function behavior sources：F00 Experience Shell + F03 Runtime Execution。
>
> 本文件是 ④A Low-fi review draft，不代表 User 已批准，也不代表 Cursor 可實作。

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

未來另一入口：

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

Top shell建議只讓：
- NodeFF / Home
- App title
- Share
- More / overflow

Overflow 可承接：
- New / Home
- Remix / Refine
- Previous Version / Revert（eligible 時）
- 其他非 primary shell actions

理由：F00 要求這些 actions「可達」，不代表全部必須常駐在 header。

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
- App 本體優先佔高度。
- Shell 不做 permanent bottom nav。
- Result actions 只有需要時出現。
- 若 generated App 本身需要 bottom controls，NodeFF shell 不可搶同一區域造成衝突。

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

- App title。
- Home / New。
- Share。
- Remix / Refine。

## Contextual

- Correct / 調整結果：只有 canonical result exists 時。
- Previous Version / Revert：只有 current session correction eligible 時。
- Recovery notice：只有 failure / degraded state 時。

Low-fi 建議：
- Share 作 visible action。
- Remix 可在 result/action area或 overflow，依 screen width調整。
- Correct 與 Result 放在一起，比放 header 更符合 User 心智。
- Revert 放 overflow，避免一般 User 沒有 correction history 時看到無意義入口。

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

O01 詳細畫面之後獨立做 Low-fi。

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

# 15. Desktop / Mobile Responsive Rules

Desktop：
- Runtime frame優先寬度與可用空間。
- Shell actions 不做大型 sidebar。
- Result area可以在 Runtime下方或 contextually adjacent，但不得擠壓 App 核心操作。

Mobile：
- compact top chrome。
- generated App 先於 NodeFF secondary actions。
- overflow收納低頻 actions。
- 不固定一排過多 shell buttons。
- shell overlay不能破壞 App current state。

# 16. Accessibility Baseline

- Shell control與 Generated App controls都有可辨識 accessible name。
- focus進入 S03後，優先落在 App主要內容 / heading。
- Overlay close後 focus回到觸發入口。
- node failure fallback可被 assistive technology感知。
- Result change / correction success使用非破壞性 live announcement when appropriate。
- Mobile touch targets維持可操作尺寸。

# 17. Proposed Low-fi Decisions To Confirm

本輪主要確認 4 件事：

1. **Generated App 是否應佔 S03 絕對主體，NodeFF Shell只留極簡 top chrome？**
2. **Header 是否採 App Title + Share + overflow；Remix / Correct / Revert依 context放在 result area或 overflow，而不是全部塞 Header？**
3. **Correct 是否只在有 canonical Result 時出現，並靠近 Result；Remix 永遠是「改 App」的另一條路？**
4. **Mobile 是否不做 NodeFF permanent bottom navigation，把最大空間留給 Generated App？**

# 18. Review Status

> **LOW_FI_REVIEW_IN_PROGRESS**

本文件僅做 S03 ④A Low-fi。

依固定流程，S03 Low-fi確認後繼續 S04 / S05 / S06 與 O01–O05 Low-fi；所有 Low-fi完成後才統一進 High-fi Design System。
