# O05 — Loading / Building / Hydration States

> Overlay / State ID：O05
>
> 狀態：**WORKING — ④A LOW_FI_APPROVED / FUNCTION_DELTA_CLOSED / CROSS_SCREEN_REVIEW_APPROVED / ④B HIGH_FI_STEP1 APPROVED / STEP2 NEXT**
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

# 22. ④B High-fi Contract

> Step 1 approved by User：2026-09-23
>
> Canonical rule：本節是 O05 High-fi 的唯一 canonical contract。後續 Step 2–4 必須在本節續寫，不得另建重複 High-fi summary / shadow copy。
>
> Current status：
> - Step 1 — Structure Lock ✅
> - Step 2 — Geometry + Visual Hierarchy Lock — NEXT
> - Step 3 — Detailed High-fi Visual Rules Lock — PENDING
> - Step 4 — Final Visual Reference Lock — PENDING

## Step 1 — Structure Lock ✅

### 1. O05 Role — Shared Processing Presentation System

O05正式鎖定為 **Shared Processing Presentation System**，不是單一 Loading Overlay，也不是獨立 route。

它可被以下 host surface共用：
- S02 Create Workspace。
- S03 App / Runtime。
- S04 Shared App Restore。
- S05 Refine / Remix。
- S06 Correction Compare preparation / replay。
- O01 Share creation。
- O02 Correction Composer submit。
- O03 Recovery Retry。
- O04 Revert confirm。

### 2. Only Two Legal Progress Presentation Modes

O05 Consumer presentation只允許兩種 mode：

~~~text
DETERMINATE
→ Stage label + checkpoint-derived Progress %

INDETERMINATE
→ Stage label only
~~~

不得存在第三種「時間估算型」或平滑動畫灌高的假百分比。

### 3. Source Function Owns Progress Truth

是否能顯示百分比，不由 O05決定。

只有當 Source Function已提供可靠、finite、ordered checkpoint plan時，O05才可呈現 checkpoint-derived %。

O05只負責 consumer projection，不擁有：
- checkpoint定義。
- checkpoint completion truth。
- operation commit truth。
- retryability。
- cancelability。

### 4. O05 Must Not Invent Checkpoints

O05不得為了 UI想顯示 25 / 50 / 75 / 100，自行反推或補出 backend checkpoints。

如果 Source Function沒有可靠 checkpoint contract：
~~~text
Stage label only
~~~

不得 fake precision。

### 5. Progress Percentage Meaning

Progress %只代表：

> **已完成多少可驗證 work checkpoints。**

Canonical formula：
~~~text
progress_percent
= completed_checkpoints / planned_checkpoints × 100
~~~

它不代表：
- 剩餘時間。
- LLM ETA。
- network ETA。
- provider latency prediction。

### 6. 100% Completion Rule

`100%` 只可在 owner Function的 actual committed / ready condition成立後呈現。

以下不得自行等同 100%：
- commit_ready。
- validation passed。
- response received。
- last internal step started。

若 Function尚未 actual ready / committed，O05不得先跑到100%再等待。

### 7. Stage and Percentage May Advance Independently

Stage change與 % change不必一對一。

Rules：
- 同一 stage可完成多個 checkpoint。
- 某個 stage可長時間停在同一真實 %。
- 不因畫面看起來沒動，就人工增加 progress。
- checkpoint completion必須 monotonic。

### 8. Canonical Processing Information Structure

所有 O05 processing presentation固定依序：

~~~text
Operation / App context
→ Stage label
→ Progress indicator（only when determinate）
→ truthful support copy
→ Cancel（only when Source Function says safe）
~~~

不得讓 spinner成為唯一資訊。

### 9. Long Wait / Soft Timeout

Long Wait / Soft Timeout是 `PROCESSING` 上的 non-terminal wait condition，不是 Error。

此時：
- 保持最後真實 checkpoint %。
- 顯示現在仍在處理。
- 可顯示「你的內容都還在」等 truthful preservation copy。
- 不自行顯示 Retry。
- 不切 O03。

### 10. Failure / Hard Timeout Boundary

Failure / Hard Timeout不由 O05處理。

Canonical transition：
~~~text
O05 processing
→ Source Function failure / timeout truth
→ F12
→ O03 Recovery
~~~

O05不得：
- 自己發明 error modal。
- 無限 spinner。
- 清空 host surface。

### 11. Cancel Ownership

Cancel是否存在，必須由 Source Function授權。

Rules：
- safe cancel → O05可顯示 Cancel。
- not cancellable → 不顯示 Cancel。
- 不用 disabled Cancel假裝有能力。
- O05不得自行判斷 operation是否安全可取消。

### 12. Completion Transition

一旦 owner Function actual ready / committed：
~~~text
100%（if determinate）
→ immediately target surface
~~~

Rules：
- 不為動畫刻意停留。
- 不額外增加「完成，請繼續」頁。
- 只有 Function明確需要 User decision時才停。

### 13. S03 Runtime Fast Path

每個被 F03 admitted 的 Runtime interaction都有 logical `GLOBAL_PROCESSING`。

但若 operation在同一 browser render frame內完成：
- loading frame可能完全不 paint。
- logical lifecycle仍成立。
- 這不是 UX violation。
- **不得人工延長 operation只為讓 O05被看見。**

### 14. Preserve Host Context

O05不是「白畫面 + spinner」系統。

Processing時應盡量保持 host context穩定，例如：
- Create保留 creation context。
- Runtime保留 safe App context。
- Correction / Revert保留原 surface geometry。

只有 Function安全語意需要時才可切更強 blocking presentation。

### 15. User Decision Is Not Processing

Clarification / Assumption Review等 User decision狀態，不得被當作 processing繼續跑。

例如 F01：
~~~text
ANALYZING
→ NEEDS_CLARIFICATION
→ waiting for User
→ User answers
→ subsequent processing
~~~

等待 User回答時：
- progress停止 / 離開 processing presentation。
- 不繼續灌 %。
- 不顯示假 loading。

### 16. Retry Starts a New Operation

Retry不是延續舊 progress。

任何 Retry：
- 由 Source Function建立新的 operation identity。
- 使用新的 checkpoint plan / lifecycle truth。
- O05重新 projection。

不得從失敗前的 `75%` 接著跑到 `100%`。

### 17. F01 Creation Progress Delta Boundary

`SD-20260922-002 — F01 Creation Progress Checkpoint Contract` 在本 Step 1後 **仍保持 OPEN**。

O05 Step 1只鎖 Consumer progress interface，不得藉此宣稱 F01 backend / Function contract已閉合。

F01後續 Function Delta Review仍必須獨立完成：
- canonical checkpoint schema。
- planned / completed checkpoints。
- checkpoint plan freeze / legal recalculation。
- clarification round對 checkpoint plan的影響。
- F01 → F00 / S02 progress projection interface。
- F01 / F03 Runtime-prepared handoff ownership。
- cancel / retry / failure lifecycle。
- Acceptance / Test。

Cursor不得從 O05 UI mockup反推 F01 backend semantics。

### 18. Step 1 Locked Decisions

1. **O05 = Shared Processing Presentation System，不是單一 Overlay。**
2. **只允許兩種合法 progress mode：reliable checkpoints → Stage + %；otherwise Stage only。**
3. Source Function擁有 checkpoint / completion truth；O05只做 presentation projection。
4. **O05永遠不得自行產生 checkpoint或假百分比。**
5. %代表 work checkpoint completion，不代表時間。
6. 100%只在 actual committed / ready後。
7. Stage與 %可不同步；不得為了動感人工灌高。
8. Processing資訊順序固定為 Context → Stage → Progress(if determinate) → support copy → Cancel(if safe)。
9. Long Wait / Soft Timeout仍屬 PROCESSING，不是 Error。
10. Failure / Hard Timeout交 F12 → O03。
11. Cancel是否顯示由 Source Function決定。
12. Completion立即進 target surface，不加多餘完成頁。
13. S03極快 operation可不 paint loading frame，禁止人工延長。
14. O05盡量保留 host context，不做白畫面 spinner系統。
15. Clarification / User Decision不是 Processing。
16. Retry建立新 operation，不延續舊 progress。
17. **SD-20260922-002仍保持 OPEN；O05 Step 1不得假裝 F01 Function Delta已閉合。**

> Step 1：**APPROVED / LOCKED**。下一步：Step 2 — Geometry + Visual Hierarchy Lock。

# 23. Review Status

> **④A LOW_FI_APPROVED / FUNCTION_DELTA_CLOSED / CROSS_SCREEN_REVIEW_APPROVED / ④B HIGH_FI_STEP1 APPROVED — STEP2 NEXT**

O05 的 Low-fi presentation direction、Runtime Function Delta、Cross-Screen Review與④B Step 1已由 User確認。

下一步：**O05 ④B Step 2 — Geometry + Visual Hierarchy Lock**。

`SD-20260922-002 — F01 Creation Progress Checkpoint Contract` 仍保持 **OPEN**，後續另做 Function Delta closure，不混入 O05 UI規格。

Formal Spec與 Cursor implementation維持 HOLD。
