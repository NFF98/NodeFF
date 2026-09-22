# O05 — Loading / Building / Hydration States

> Overlay / State ID：O05
>
> 狀態：**WORKING — LOW_FI_DIRECTION_APPROVED / FUNCTION_DELTA_CLOSED / CROSS_SCREEN_REVIEW_APPROVED / HIGH_FI_PENDING**
>
> Phase：Phase 1
>
> Screen-level canonical owner：`working/UI-UX/overlays/O05-LOADING-BUILDING-HYDRATION.md`
>
> Function behavior sources：F00 Experience Shell + F01 + F03 + F05 + F06 + F12 + F16。
>
> 本文件的 ④A Low-fi direction與 Runtime Loading / Timeout Function Delta已完成 User Review；仍不是 Formal Spec或 Cursor implementation authority。

# 1. User Outcome

O05 的核心任務：

> **任何需要等待的 operation，以及每個被 F03接受的 S03 Runtime interaction，都要有真實 processing state；User看到的 stage / %不能假造，也不能為了動畫而拖慢完成。**

O05 是跨畫面的共用 loading / progress presentation，不是獨立 route。

# 2. Host Surfaces

O05 可被以下畫面 / Overlay使用：

- S02 Create Workspace。
- S03 App / Runtime（每個被 F03 admitted 的 interaction都有 logical global processing state；極快完成時不強迫 paint loading frame）。
- S04 Shared App Restore。
- S05 Refine / Remix。
- S06 Correction Compare preparation / replay。
- O01 Share creation。
- O02 Correction Composer submit。
- O03 Recovery Retry。
- O04 Revert confirm → previous version hydration。

# 3. Core Rule — Processing Only For Real Work

沿用 F00：

- ANALYZING → 顯示 operation progress。
- BUILDING → 顯示 creation/build progress。
- HYDRATING → 顯示 App準備進度。
- normal local Runtime action被 F03接受後也進入 logical global processing state；Working F00/F03/F12已閉合此 contract。

禁止：
- 把每次 local interaction都強制畫成整頁 spinner；presentation應依 host surface穩定承接。
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

    S02 / S04 / S05 / S06 / O01 / O02 / O03 retry / O04 revert
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

# 8.1 O01 — Share Creation

O01 Share creation也使用同一 processing presentation：

- 有可靠 Share creation checkpoints → Stage + checkpoint-derived %。
- 沒有可靠 checkpoints → 顯示「正在準備分享連結…」等 truthful stage，不顯示 fake %。
- READY立即轉 O01 READY，不為了動畫停留。
- Share failure仍由 F05 / F12 → O03 recovery semantics承接；O05只負責 processing presentation。

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

# 13. S03 Local Runtime Rule — Closed Working Contract

User 已確認：

    click / input / toggle / local calculate
    → global loading / processing state

Presentation rules：
- Runtime interaction被 F03 accepted / admitted、token建立時進 logical global processing state；不是等 commit後才進。
- 有可靠 checkpoints時顯示 Stage + Progress %。
- 無可靠細分時至少顯示 operation stage；不得用時間估算亂灌 %。
- 只有 action成功 commit後才可顯示100%，並立即回正常 S03。
- 不為了讓 loading「看得到」而人工增加不必要等待。
- action在同一 render frame內完成時，完整 loading frame可能不 paint；logical state仍需存在，且不算 UX violation。

**Formal sync note：** 既有 Formal F00仍是舊語意；此 Working Current Truth待 pre-Cursor Formal Spec Refresh一次同步。O05不擁有 operation / commit semantics，仍以 F03為 owner。

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

100% 只在 actual ready / Runtime commit condition成立後顯示。

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

Working Function contract已閉合：
- F03擁有 operation token、deadline guard、atomic discard、stale completion與 integrity判斷。
- F12-POL-011擁有 `F03-ERR-021 → TIMEOUT → APP_CURRENT` recovery。
- F00/O05只呈現 lifecycle與 recovery outcome。

## Runtime interaction watchdog

每次被接受執行的 S03 Runtime interaction建立 operation token：

    STARTED
    → PROCESSING
    → COMMITTED
    or TIMED_OUT
    or FAILED
    or CANCELLED

Timeout分兩層：

### Soft Timeout

當 operation超過 policy-defined soft threshold：

    Progress %停在最後真實 checkpoint
    + 顯示：
      「還在處理，你的 App 和目前內容都還在。」

不亂灌 %。

Soft Timeout是 `PROCESSING` 上的 non-terminal wait condition，不是 operation terminal state。

### Hard Timeout

超過 policy-defined hard threshold：

    close operation token as TIMED_OUT
    → discard uncommitted transaction + staged effects/events
    → keep committed store unchanged
    → late/stale completion cannot commit
    → F03-ERR-021
    → F12-POL-011 TIMEOUT recovery
    → return to safe S03 UX when integrity holds

Default humanized outcome：

    「剛才這個操作處理太久，App 已回到上一個安全狀態。」

Actions依 F12：
- 再試一次（仍有 retry budget時）
- 回到 App / 保留目前狀態
- 稍後再試（budget exhausted時）

如果 timeout造成 integrity uncertainty：
- 不自動回正常 Runtime。
- F03直接產生既有 F03-ERR-018，由 F12-POL-001進 O03 terminal / critical safe-state；不把不安全狀況當成可恢復 TIMEOUT。

Retry：
- 同一 F12 recovery episode可 Retry，但每次 Retry建立新的 F03 operation token。
- closed token永不復用；成功回到 safe continuation後 episode才標 `RECOVERED`。

Browser limitation：
- Phase 1以 monotonic deadline + action-step / recompute / pre-commit guard檢查超時。
- main thread被 trusted synchronous code佔用時，`setTimeout()`不能強制中斷；handler晚回仍會在 pre-commit被拒絕。
- 真正無法返回的 trusted code由 Capability CI / review / resource guard防守；本 Delta不改成 Worker architecture。

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
3. **S03每個被 F03 admitted 的 Runtime interaction都有 logical global processing state。** F00/F03/F12 Material Function Delta已閉合；極快完成不強迫 paint loading frame。
4. 某 checkpoint卡住時，%停在最後真實完成值，不用動畫灌高。
5. Timeout → Recovery → safe S03 / terminal safe-state contract已由 F03 + F12閉合。

# 22. Review Status

> **LOW_FI_DIRECTION_APPROVED — FUNCTION_DELTA_CLOSED — CROSS_SCREEN_REVIEW_APPROVED — HIGH_FI_PENDING**

O05 的 Low-fi presentation direction與 Runtime Function Delta已由 User確認。

下一步是 Cross-Screen Consistency Review；其完成前仍不得進 High-fi。Formal Spec與 Cursor implementation維持 HOLD。
