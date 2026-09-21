# O01 — Share Overlay

> Overlay ID：O01
>
> 狀態：**WORKING — LOW_FI_REVIEW_IN_PROGRESS**
>
> Phase：Phase 1
>
> Screen-level canonical owner：`working/UI-UX/overlays/O01-SHARE.md`
>
> Function behavior source：F05 Share / Restore + F00 Experience Shell。
>
> 本文件是 ④A Low-fi review draft，不代表 User 已批准，也不代表 Cursor 可實作。

# 1. User Outcome

O01 的核心任務：

> **User 在不離開目前 App、不打斷 Runtime 的情況下，快速取得可分享連結，複製或呼叫系統分享。**

# 2. Entry / Exit

Entry：

    S03 Share CTA
    → O01

Exit：

    Close
    → 回 S03，同一 Runtime context保留

Share success / failure都不導航離開 S03。

# 3. Function Truth

F05 已固定：

    CLOSED
    → CREATING
    → READY
       ├─ COPY_SUCCESS
       └─ SHARE_SHEET_OPEN
    → FAILED

Rules：
- Share failure不破壞 current App。
- pending不 lock Runtime normal interaction。
- duplicate tap不建立 duplicate logical share。
- copy failure只影響 copy action，不讓 share本身失效。
- Native Share是 convenience，不是 dependency。

# 4. Presentation Direction

O01 不採全頁。

Low-fi 建議：
- Desktop：compact anchored panel / lightweight dialog。
- Mobile：bottom sheet。
- 都可隨時 Close。
- 不使用阻斷整個 App 的 full-screen loading。

目的：
> Share 是高頻輕操作，不該讓 User 覺得離開 App。

# 5. Desktop Low-fi

    ┌────────────────────────────────────────┐
    │ 分享這個 App                      [×] │
    │                                        │
    │ [ App Logo ]  App Title               │
    │                                        │
    │ 分享連結                               │
    │ ┌────────────────────────────────────┐ │
    │ │ nodeff.../share/xxxxx              │ │
    │ └────────────────────────────────────┘ │
    │                                        │
    │ [複製連結]          [系統分享]         │
    │                                        │
    │ 收到連結的人可直接開啟使用             │
    └────────────────────────────────────────┘

# 6. Mobile Low-fi

    ╭────────────────────────────╮
    │ 分享這個 App           [×] │
    │                            │
    │ [Logo] App Title           │
    │                            │
    │ nodeff.../share/xxxxx      │
    │                            │
    │ [      複製連結      ]     │
    │ [      系統分享      ]     │
    │                            │
    │ 收到連結即可直接使用       │
    ╰────────────────────────────╯

Bottom sheet不遮掉整個 Runtime；關閉後回到原位置。

# 7. CREATING State

若 Share 尚未建立：

    正在準備分享連結…

Rules：
- Create CTA duplicate tap disabled / coalesced。
- App仍保留。
- 不顯示 content hash / internal ID。
- User可關閉 O01；背景 share operation依 existing lifecycle繼續或安全收束，不影響 App。

# 8. READY State

成功後主要資訊：

- App Logo / Title。
- public share URL。
- Copy Link。
- Native Share（supported時）。
- Close。

Primary action建議：

    複製連結

Secondary：

    系統分享

理由：
- Copy是跨平台穩定能力。
- Native Share有裝置/瀏覽器差異。

# 9. Copy Success

按 Copy後：

    已複製

應是短暫 inline feedback，不另開新 Overlay。

不能：
- 關閉整個 O01才顯示成功。
- 把 copy success當成 share creation success的唯一判定。

# 10. Copy Failure

如果 clipboard失敗：

    無法自動複製
    你仍可以選取上方連結手動複製

    [再試一次]

Share URL仍有效。

# 11. Native Share

若 Web Share API supported：

    系統分享

呼叫 OS / browser share sheet。

若不 supported：
- 不顯示 disabled dead button。
- 只保留 Copy Link。

Native Share cancel不是 error。

# 12. Create Failure

若 Share creation失敗：

    暫時無法建立分享連結
    你的 App 不受影響

    [再試一次]
    [關閉]

不離開 S03，不清 Runtime state。

# 13. Privacy Copy

O01 可用簡短 consumer copy：

> 分享的是這個 App，不會分享你目前輸入的內容或結果。

這對 NodeFF 很重要，因為 F05 明確規定 Share只指向 Blueprint，不含 Runtime input / Result。

不顯示：
- anonymous ID
- Blueprint hash
- raw Prompt
- Result snapshot
- provider/model data

# 14. Re-open Behavior

若同一 logical Share 已 READY 且 UI仍持有有效 share URL：
- 再開 O01 直接顯示 READY。
- 不因 UI reopen 重複觸發 create。

若沒有現成 READY context：
- 依 F05正常 create lifecycle。

這是 UI operation reuse，不改 F05 durable semantics。

# 15. Accessibility

- Overlay有明確 accessible title。
- Desktop dialog/panel與Mobile bottom sheet focus管理清楚。
- Close後 focus回 S03 Share trigger。
- Copy success用 polite live announcement。
- URL可 keyboard select/copy。
- Native Share不可用時不留下不可操作控制。
- Touch target至少44 CSS px。

# 16. Proposed Low-fi Decisions To Confirm

本輪確認 4 件事：

1. **Desktop 用 compact Share panel/dialog、Mobile 用 bottom sheet，不做 full-screen Share page？**
2. READY 後是否以 **「複製連結」為 Primary CTA，「系統分享」為 Secondary CTA**？
3. 是否顯示一句 privacy copy：**「分享的是 App，不會分享你目前輸入的內容或結果」**？
4. Copy failure時是否保留有效 URL並提供手動複製 / Retry；Share create failure則顯示 Retry + Close，且兩者都不離開 S03？

# 17. Review Status

> **LOW_FI_REVIEW_IN_PROGRESS**

O01確認後進 O02 — Correction Composer ④A Low-fi。
