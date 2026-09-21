# O03 — Recovery Overlay

> Overlay ID：O03
>
> 狀態：**WORKING — LOW_FI_DIRECTION_APPROVED / HIGH_FI_PENDING**
>
> Phase：Phase 1
>
> Screen-level canonical owner：`working/UI-UX/overlays/O03-RECOVERY.md`
>
> Function behavior source：F12 Humanized Recovery + F00 Experience Shell。
>
> 本文件是 ④A Low-fi review draft，不代表 User 已批准，也不代表 Cursor 可實作。

# 1. User Outcome

O03 的核心任務：

> **當某一步失敗時，User 不需要懂技術錯誤；NodeFF 要先保住能保住的內容，再用人話說明發生什麼，最後只提供真正能執行的下一步。**

Recovery 的第一優先不是「顯示錯誤」，而是：

    Preserve Context
    → Explain Clearly
    → Offer Safe Next Action

# 2. Host Surfaces

O03 可套在：

- S02 Create Workspace。
- S03 App / Runtime。
- S05 Refine / Remix Workspace。
- S06 Correction Compare。

O03 不建立獨立產品 route。

# 3. Presentation Levels

依 F12 / F00 固定 mapping：

## A. INFO

Presentation：
- inline notice。

Example：

    沒有偵測到實際修改。
    [修改需求]

不擋主流程。

## B. DEGRADED

Presentation：
- inline / node-level notice。

Example：

    這個區塊暫時無法使用，其他部分仍可繼續。
    [再試一次]

不鎖整個 App。

## C. BLOCKING_RECOVERABLE

Presentation：
- blocking recovery overlay / creation panel。

Example：

    現在暫時無法完成這一步。
    你的需求已保留。

    [再試一次]
    [修改需求]

只阻擋「當前失敗操作」，不破壞 last-known-good App。

## D. TERMINAL / CRITICAL

Presentation：
- terminal safe-state view。

Example：

    這個版本目前無法安全繼續使用。

    [回到安全版本]
    [回首頁]

不提供明知會失敗的 Retry。

# 4. Core Information Hierarchy

任何 User-visible Recovery，資訊順序固定：

1. **現在發生什麼**
2. **哪些內容還在 / 哪些可能遺失**
3. **Primary next action**
4. 最多 2 個 Secondary actions
5. technical details 預設不顯示

Example：

    暫時無法完成這次修改

    原 App 和你的修改內容都還在。

    [再試一次]
    [修改需求]
    [回原 App]

# 5. Context Preservation Copy

如果 context有保留，應明確說：

- 「你的需求已保留」
- 「原 App 還在」
- 「目前結果還在」
- 「分享連結仍有效」

如果 material context遺失，必須明講：

    這次無法保留其中 2 個輸入，
    需要你重新輸入。

不能默默清空。

# 6. Next Action Rules

F12 已固定：

- Primary action最多 1 個。
- visible actions通常 1–3 個。
- 每個 action必須真的能執行。
- Retry不能無限。
- Security / integrity / unsupported 不提供假 Retry。

常見 actions：

    再試一次
    稍後再試
    修改需求
    回原 App
    保留目前版本
    使用較簡單版本
    回首頁
    重新整理

# 7. Retry Budget

Phase 1 同一 recovery episode：

    user-triggered immediate Retry max = 3

第 4 次後：

- transient → 稍後再試 / alternate path。
- terminal → 本來就不顯示 Retry。

UI 不顯示技術 retry counter，例如「attempt 2/3」作為主要文案；可視需要以人話提示：

    再試仍未成功，你可以稍後再試或先回原 App。

# 8. Desktop Low-fi — Blocking Recoverable

    ┌──────────────────────────────────────────────┐
    │ 暫時無法完成這一步                     [×] │
    │                                              │
    │ 你的修改內容和原 App 都還在。               │
    │                                              │
    │ [再試一次]                                   │
    │                                              │
    │ [修改需求]   [回原 App]                      │
    └──────────────────────────────────────────────┘

Desktop：
- centered/lightweight blocking dialog，或 host panel內 blocking state。
- 背後 safe context保持。
- 若 background App仍可安全操作，不應不必要鎖死全部互動。

# 9. Mobile Low-fi — Blocking Recoverable

    ╭────────────────────────────╮
    │ 暫時無法完成這一步         │
    │                            │
    │ 原 App 和修改內容都還在。 │
    │                            │
    │ [      再試一次      ]     │
    │ [      修改需求      ]     │
    │ [      回原 App      ]     │
    ╰────────────────────────────╯

Mobile：
- bottom sheet / full-height recovery sheet視嚴重度。
- Primary CTA單手可達。
- 不讓 User在錯誤狀態迷路。

# 10. Inline / Node-level Recovery

對 DEGRADED / PARTIAL_COMPONENT_FAILURE：

    ┌─────────────────────────────┐
    │ ⚠ 這個區塊暫時無法使用     │
    │ 其他部分仍可繼續            │
    │ [再試一次]                  │
    └─────────────────────────────┘

Rules：
- 不跳 blocking overlay。
- 不把整個 S03 Runtime變成 error page。
- node恢復後 notice移除。
- 其他 node照常使用。

# 11. Terminal Safe State

Terminal / Critical 不應還留一堆不安全操作。

Example：

    目前無法安全開啟這個版本

    我們保留了可用的 App reference，
    但這個版本不能繼續執行。

    [回到安全版本]
    [回首頁]

Rules：
- 不提供 silent bypass。
- 不重新 compile incompatible Blueprint。
- 不自動降級 security。
- technical trace只留 diagnostics。

# 12. Close Behavior

不是所有 Recovery 都可以直接 [×]。

Rules：

- INFO / DEGRADED：可 dismiss，前提是不會造成誤解。
- BLOCKING_RECOVERABLE：若 Close 等於安全地回到 host surface，可提供 Close。
- TERMINAL / CRITICAL：若 Close沒有明確 safe surface，不提供單純 [×]；必須選安全出口。
- 關閉不能造成 context silent loss。

# 13. Retry / Recovery Progress

User按「再試一次」後，如果進入實際 async operation：

- Recovery Overlay可轉成 recovery-in-progress state。
- **進度呈現交 O05 Loading / Building / Hydration 共用規則。**
- 若有可靠 work checkpoints可顯示 %。
- 沒有可靠 progress source不得 fake %。

O03 本身不另外發明第二套 loading規則。

# 14. Unsupported Is Not Error Retry

UNSUPPORTED：

    這個版本目前還做不到其中一部分。

Primary：
    修改需求

Secondary：
    使用較簡單版本

不顯示：
    再試一次

除非底層其實是 transient dependency，不是 capability unsupported。

# 15. Security / Integrity

Security / integrity問題：

- Fail closed。
- 停止 affected execution path。
- 保留安全 context。
- Consumer不看 raw security code。
- 不顯示「仍然執行」之類 bypass CTA。

# 16. Accessibility

- blocking recovery focus移到 heading / Primary action。
- Close後 focus回合理 trigger / safe surface。
- inline notice使用適度 aria-live。
- severity不只靠顏色。
- CTA至少44 CSS px。
- keyboard可完整操作。
- technical code不作 screen reader主要資訊。

# 17. Confirmed O03 Low-fi Decisions

User 已確認並固定：

1. **小問題**：使用 inline notice，User 可繼續使用 App。
2. **局部元件壞掉**：只在該 component 顯示 Recovery，不鎖整個 App。
3. **目前操作做不下去，但 App 還安全**：才使用 blocking Recovery Overlay。
4. **真的不能安全繼續**：才進 terminal safe-state。
5. Recovery 資訊順序固定為：**發生什麼 → 保留/遺失什麼 → 1 個 Primary + 最多 2 個 Secondary CTA**。
6. 同一 recovery episode 最多 3 次 immediate User Retry；第 4 次改成稍後再試或其他安全路徑，不提供無限 Retry。

# 18. Review Status

> **LOW_FI_DIRECTION_APPROVED — HIGH_FI_PENDING**

O03 ④A Low-fi 已完成 User Review。

依固定流程，下一步進 O04 — Revert Confirmation ④A Low-fi。
