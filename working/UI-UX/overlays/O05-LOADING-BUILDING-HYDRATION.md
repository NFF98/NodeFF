# O05 — Loading / Building / Hydration States

> Overlay / State ID：O05
>
> 狀態：**WORKING — LOW_FI_DIRECTION_APPROVED / FUNCTION_DELTA_PENDING / HIGH_FI_PENDING**
>
> Phase：Phase 1
>
> Screen-level canonical owner：`working/UI-UX/overlays/O05-LOADING-BUILDING-HYDRATION.md`
>
> Function behavior sources：F00 Experience Shell + F01 + F03 + F05 + F06 + F12 + F16。
>
> 本文件是 ④A Low-fi review draft，不代表 User 已批准，也不代表 Cursor 可實作。

# 1. User Outcome

O05 的核心任務：

> **任何真正需要等待的 asynchronous work，都要讓 User知道「現在在做什麼、做到哪裡、能不能取消、完成後會去哪裡」，但不能用假進度欺騙 User。**

O05 是跨畫面的共用 loading / progress presentation，不是獨立 route。

# 2. Host Surfaces

O05 可被以下畫面 / Overlay使用：

- S02 Create Workspace。
- S03 App / Runtime（只在真的 async shell/runtime transition；一般 local interaction不用 global loading）。
- S04 Shared App Restore。
- S05 Refine / Remix。
- S06 Correction Compare preparation / replay。
- O02 Correction Composer submit。
- O03 Recovery Retry。
- O04 Revert confirm → previous version hydration。

# 3. Core Rule — Loading Only For Real Async Work

沿用 F00：

- ANALYZING → 顯示 operation progress。
- BUILDING → 顯示 creation/build progress。
- HYDRATING → 顯示 App準備進度。
- **User-approved UI delta：normal local Runtime action 也進入 global loading state。此點目前與 formal F00/F03 contract衝突，待 Function Delta Review。**

禁止：
- 每按一個 local button就整頁 spinner。
- spinner蓋掉整個產品。
- fake generated content skeleton。
- 為了讓動畫好看而故意延遲完成。

# 4. Progress Model

O05 建議統一採：

> **Stage label + Checkpoint-derived Progress %**

百分比代表：
- 已完成多少個「可驗證 work checkpoints」。

百分比不代表：
- 還剩幾秒。
- LLM多久會回。
- network多久會好。

例如 4 個 major checkpoints：

    0%   operation started
    25%  checkpoint 1 complete
    50%  checkpoint 2 complete
    75%  checkpoint 3 complete
    100% ready

若單一 checkpoint內等待很久：
- % 可以停在目前完成值。
- 顯示現在正在做什麼。
- **不平滑亂跑假進度。**

# 5. Why % Can Still Be Honest

Progress % 不是「時間進度」，而是「工作完成度」。

Example：

    50%
    正在檢查互動…

意思是：
> 目前定義的 restore/build/correction work已有一半 checkpoints完成。

不是：
> 還剩一半時間。

這可以同時滿足：
- User需要看到 %。
- NodeFF不提供假 precision。

# 6. Proposed Cross-Screen Consistency Delta

目前既有 Low-fi有一個差異：

- S02：已核准 stage-based / no fake %。
- S04：已核准 checkpoint-derived Loading %。
- O02：已核准 checkpoint-derived Progress %。

O05 建議統一後：

    S02 / S04 / S05 / S06 / O02 / O03 retry / O04 revert
    → 能定義可靠 checkpoints時
    → Stage + %

因此如果 User批准 O05，本文件將構成 **presentation-only Low-fi consistency delta**：
- S02 不再是「完全不顯示 %」。
- 改為「不顯示假 %；有可靠 checkpoints時顯示 checkpoint-derived %」。

這不修改 F01 / F03 Function semantics。

# 7. S02 — Create / Build Progress

Proposed 4 stages：

1. 理解你的想法
2. 整理成 App
3. 確認互動可以執行
4. 準備你的 App

Presentation：

    50%
    確認互動可以執行…

Rules：
- clarification / assumption等待 User時，progress停住。
- User回答後繼續。
- READY直接進 S03，不增加完成確認頁。

# 8. S04 — Shared App Restore

已核准：

    App Logo / Title
    Loading %
    人話 stage

Example：

    67%
    正在準備 App…

不為了 animation拖慢 entry。

# 9. S05 — Refine / Remix

Proposed stages：

1. 理解修改
2. 更新 App
3. 檢查互動
4. 準備新版

Presentation：

    50%
    正在檢查新版互動…

原版始終安全。

# 10. O02 / F16 Correction

已核准處理中顯示 %。

Recommended checkpoints可跨：

1. capture before
2. understand correction
3. compose / validate child
4. replay / compare ready

Consumer copy不顯示 technical names。

Example：

    75%
    正在用相同輸入比較結果…

# 11. O03 Recovery Retry

User按 Retry後：

- 若 target Function有 checkpoints → 使用同一 Progress %。
- 若只是單一 external wait、沒有可驗證中間 checkpoint：
  - 顯示目前狀態文字。
  - % 停在上一個真實 checkpoint。
  - 不 fake smooth movement。

# 12. O04 Revert

Confirm「回到原版」後：

Possible checkpoints：

1. confirm target still safe
2. prepare previous Blueprint
3. initialize fresh Runtime
4. restore eligible inputs / ready

Example：

    75%
    正在恢復原版…

完成後直接回 S03 previous/base App。

# 13. S03 Local Runtime Rule — User-approved Delta

User 已確認：

    click / input / toggle / local calculate
    → global loading / processing state

Presentation rules：
- Runtime action開始時進 global processing state。
- 有可靠 checkpoints時顯示 Stage + Progress %。
- 無可靠細分時至少顯示 operation stage；不得用時間估算亂灌 %。
- action成功 commit後立即回正常 S03。
- 不為了讓 loading「看得到」而人工增加不必要等待。

**Important：此決策與目前 formal F00「normal Runtime interaction不觸發 global shell loading」衝突，因此需要 F00/F03 Material Function Delta；O05 不得單獨改寫正式 Function truth。**

Node/component單獨 async仍可有 component-local detail，但不取消全域 processing feedback。

# 14. Loading Layout — Desktop

    ┌────────────────────────────────────────────┐
    │                                            │
    │              App / Operation              │
    │                                            │
    │                   50%                     │
    │          ██████████──────────              │
    │                                            │
    │         正在確認互動可以執行…             │
    │                                            │
    │              [取消 where safe]            │
    │                                            │
    └────────────────────────────────────────────┘

不要求 full-screen；依 host surface內嵌。

# 15. Loading Layout — Mobile

    ┌────────────────────────────┐
    │                            │
    │            50%             │
    │      ████████────────      │
    │                            │
    │   正在確認互動可以執行…    │
    │                            │
    │       取消 where safe      │
    │                            │
    └────────────────────────────┘

Primary content保持穩定，不讓 layout不停跳。

# 16. Progress Completion

100% 只在 actual ready condition成立時顯示。

Rules：
- 不先跑到100%再等 backend。
- Ready後快速 transition到 target surface。
- 不另外加「完成，按繼續」頁，除非 Function明確需要 User decision。

# 17. Long Wait

如果同一 checkpoint等待較久：

顯示：

    50%
    還在處理這一步，你的內容都還在。

可安全 cancel時：

    [取消]

可 retry不是 loading state本身決定；由 source Function / F12決定。

# 18. Runtime Timeout → Normal UX Return

現有 Function 狀態：
- F12 已有 TIMEOUT recovery class、bounded Retry / Retry Later / safe surface。
- F00 已有 Create / Analyze 類 operation timeout。
- **F03 尚未有完整的 normal Runtime action timeout → recovery → return-to-normal-S03 UX contract。**

因此新增 Working Design requirement：

## Runtime interaction watchdog

每次 S03 Runtime interaction建立 operation token：

    STARTED
    → PROCESSING
    → COMMITTED
    or TIMED_OUT
    or FAILED

Timeout分兩層：

### Soft Timeout

當 operation超過 policy-defined soft threshold：

    Progress %停在最後真實 checkpoint
    + 顯示：
      「還在處理，你的 App 和目前內容都還在。」

不亂灌 %。

### Hard Timeout

超過 policy-defined hard threshold：

    mark operation timed out
    → stop / abandon affected processing where safe
    → discard uncommitted transaction
    → preserve last committed Runtime state
    → ignore stale late completion for that operation token
    → F12 TIMEOUT recovery
    → return to safe S03 UX

Default humanized outcome：

    「剛才這個操作處理太久，App 已回到上一個安全狀態。」

Actions依 F12：
- 再試一次（仍有 retry budget時）
- 回到 App / 保留目前狀態
- 稍後再試（budget exhausted時）

如果 timeout造成 integrity uncertainty：
- 不自動回正常 Runtime。
- 升級 O03 terminal / critical safe-state。

Exact soft/hard timeout數值由 F03/F12 Function policy決定，不在 UI Low-fi硬編秒數。

# 19. Failure Transition

Loading失敗：

    O05
    → O03 Recovery

不能：
- spinner無限轉。
- 直接清空畫面。
- 自己發明另一套 error modal。

# 20. Accessibility

- progressbar提供 aria-valuenow / label。
- stage change透過 aria-live適度通知。
- 不只靠 animation表達進度。
- prefers-reduced-motion respected。
- keyboard可達 Cancel when safe。
- 100%後 focus移到 target main content。
- 長等待文案清楚，不用只有 spinner。

# 21. Confirmed O05 Low-fi Decisions

User 已確認：

1. O05 統一採 **Stage label + checkpoint-derived Progress %**；%代表工作完成度，不代表剩餘時間。
2. S02「no fake %」細化為：**有可靠 checkpoints就顯示 %；沒有就不假造**，與 S04 / O02一致。
3. **S03 normal local Runtime interaction也要顯示 global loading / processing state。** 此點為 F00/F03 Material Function Delta，尚待 Function Review。
4. 某 checkpoint卡住時，%停在最後真實完成值，不用動畫灌高。
5. 必須有 Timeout → Recovery → 正常 UX return設計；F12已有 TIMEOUT骨架，但 F03 normal Runtime action缺完整 contract，已記錄為 Function Gap。

# 22. Review Status

> **LOW_FI_DIRECTION_APPROVED — FUNCTION_DELTA_PENDING — HIGH_FI_PENDING**

O05 的 Low-fi presentation direction已由 User確認。

但因 S03 global loading + Runtime action timeout涉及正式 F00/F03 behavior change，在 Function Delta閉合前，Phase 1 UI/UX Low-fi Gate **不得宣告完全閉合**，也不得進 High-fi。

下一步應先完成 F00/F03 Working Function Delta Review，再做 Cross-Screen Consistency Review。
