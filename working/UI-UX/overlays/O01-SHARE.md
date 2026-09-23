# O01 — Share Overlay

> Overlay ID：O01
>
> 狀態：**WORKING — ④A LOW_FI_APPROVED / ④B HIGH_FI_STEP1–2 APPROVED / STEP3 NEXT**
>
> Phase：Phase 1
>
> Screen-level canonical owner：`working/UI-UX/overlays/O01-SHARE.md`
>
> Function behavior source：F05 Share / Restore + F00 Experience Shell。
>
> ④A Low-fi 已完成 User Review；④B High-fi Step 1 已批准。Formal Spec 與 Cursor implementation 仍維持 HOLD。

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

Cross-screen layering rule：
- O01 active時，underlying S03 Shell controls與 permanent bottom navigation必須 inert / unavailable。
- Runtime context仍保留，但不能穿透 Overlay操作。
- Close後 focus回 Share trigger或合理 safe surface。

# 7. CREATING State

若 Share 尚未建立：

    正在準備分享連結…

Processing presentation統一交 O05：

- 有可靠 checkpoints → Stage label + checkpoint-derived Progress %。
- 沒有可靠 checkpoints → Stage label only。
- 不 fake %，不以時間估算灌高進度。
- 不為了 animation故意拖慢 Share ready。

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

READY 後保留兩種分享方式：

    複製連結
    系統分享

差異：
- **複製連結**：把同一個 public share URL 放入 clipboard，User自行貼到 LINE / Discord / Email / 社群等。
- **系統分享**：呼叫 OS / Browser Share Sheet，少一步貼上，但依裝置 / Browser支援而定。

兩者分享的是同一個 App Link；Copy Link是基本能力，System Share是快捷能力。

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

O01 使用精準 consumer copy：

> **目前這個分享只分享 App 本身，不包含你現在的輸入或結果。**

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

# 16. Confirmed O01 Low-fi Decisions

User 已確認：

1. Desktop 使用 compact Share panel / lightweight dialog；Mobile 使用 bottom sheet，不做 full-screen Share page。
2. READY 後同時保留 **複製連結** 與 **系統分享**：
   - Copy Link = 基本、跨平台分享能力。
   - System Share = 裝置支援時的快捷入口。
3. Privacy copy 固定為：**「目前這個分享只分享 App 本身，不包含你現在的輸入或結果。」**
4. Copy failure 保留有效 URL並允許手動複製 / Retry；Share creation failure提供 Retry + Close；兩者都不離開 S03。
5. Future capability boundary：
   - 分享目前結果 / Runtime snapshot：Phase 1 尚未有正式 Function。
   - 即時共同遊玩 / 共享狀態：由 F09 Realtime Room方向承接，目前為 Deferred，不納入 O01 Phase 1。

# 17. ④B High-fi Contract

> Step 1 approved by User：2026-09-23
>
> Canonical rule：本節是 O01 High-fi 的唯一 canonical contract。後續 Step 2–4 必須在本節續寫，不得另建重複 High-fi summary / shadow copy。
>
> Current status：
> - Step 1 — Structure Lock ✅
> - Step 2 — Geometry + Visual Hierarchy Lock ✅
> - Step 3 — Detailed High-fi Visual Rules Lock — NEXT
> - Step 4 — Final Visual Reference Lock — PENDING

## Step 1 — Structure Lock ✅

### 1. O01 Role / Phase 1 Share Boundary

O01只服務 **「分享這個 App」**。

Phase 1分享的是 immutable App / Blueprint reference。

O01不分享：
- current Runtime inputs；
- current Result；
- Runtime mutable state；
- raw Prompt；
- realtime shared session / Live Room state。

Future Share Result / Runtime Snapshot與Realtime Room需要獨立 Function contract，不得在 O01 High-fi偷偷擴張。

### 2. Entry / Exit

Canonical entry：

~~~text
S03 Share
→ O01
~~~

Canonical exit：

~~~text
O01 Close
→ 原本 S03 Runtime context
~~~

Share success / failure都不導航離開 S03；Close不得清掉 current App / Runtime context。

### 3. Overlay Boundary

O01是 Overlay，不是 Share Page。

- Desktop = compact panel / lightweight dialog。
- Mobile = bottom sheet。
- 不建立 full-screen Share route。
- O01 active時 underlying S03 Shell controls與 permanent bottom navigation必須 inert / unavailable。
- Runtime context仍完整保留，但禁止 click-through。
- Close後 focus回 S03 Share trigger或合理 safe surface。

### 4. Consumer States

O01固定承接以下 consumer states：

~~~text
CREATING
→ READY
   ├─ COPY feedback
   └─ SYSTEM SHARE
→ FAILURE when applicable
~~~

不得把所有狀態壓成單一 ambiguous「分享」button。

### 5. CREATING

CREATING只呈現：
- App identity（可取得時）；
- `正在準備分享連結…`；
- O05 processing presentation；
- Close。

Rules：
- 不顯示 fake URL。
- 不顯示 content hash / internal ID。
- 不要求第二個「建立連結」確認步驟。
- duplicate create gesture依 F05去重 / coalesce。
- User可Close；operation依既有 lifecycle安全繼續或收束，不影響 App。

### 6. READY

READY是 O01核心狀態。

固定資訊順序：

~~~text
分享這個 App
→ App Logo / Title
→ Share URL
→ 複製連結
→ 系統分享（supported only）
→ Privacy copy
→ Close
~~~

Share URL是同一 public App Link；O01不得顯示 raw Blueprint hash等 internal metadata。

### 7. Copy Link / System Share

`複製連結`是 Phase 1基本、跨平台能力，READY時必須存在。

`系統分享`是 convenience capability，只在裝置 / Browser支援時顯示。

Native Share不支援時：
- 不顯示 disabled dead button；
- 保留 Copy Link即可。

兩者分享的是同一 App Link，不建立兩種 Share semantics。

### 8. Privacy Copy — Always Visible

READY主體內固定可見：

> **目前這個分享只分享 App 本身，不包含你現在的輸入或結果。**

**Privacy copy always visible = YES.**

Rules：
- 不收進 tooltip / info icon / hidden disclosure。
- 不降級成難以注意的 legal footer。
- 此文字是 Phase 1 Share trust boundary的正式 consumer message。

### 9. Copy Success

`複製連結`成功後：

~~~text
已複製
~~~

只做短暫 inline feedback / polite live announcement。

不得：
- 關閉 O01才顯示成功；
- 開第二個 Overlay；
- 把 copy success誤當成 share creation的唯一成功判定。

### 10. Copy Failure

Copy failure只影響 clipboard action，不讓已READY的 Share失效。

必須保留：
- 有效 Share URL；
- 手動選取 / 複製能力；
- Retry when eligible。

不得把整個 O01轉成 Share creation failure state。

### 11. Share Creation Failure

Share creation failure才進 O01真正 recovery state：

~~~text
暫時無法建立分享連結
你的 App 不受影響

[再試一次]
[關閉]
~~~

Retry eligibility與 recovery semantics仍由 F05 / F12 truth決定；O01不得自行發明。

### 12. Re-open Behavior

若同一 logical Share已有有效 READY context：

~~~text
re-open O01
→ READY directly
~~~

不得重新 create、不得重播 fake loading、不得建立 duplicate logical share。

若沒有有效 READY context，才依 F05正常 create lifecycle。

### 13. Native Share Cancel

User關閉 / cancel OS或Browser Share Sheet不是 Error。

Canonical return：

~~~text
System Share cancelled
→ O01 READY
~~~

不得顯示「分享失敗」。

### 14. Step 1 Locked Decisions

1. O01 Phase 1只分享 App / immutable Blueprint reference。
2. O01是 Overlay，不是獨立 Share Page。
3. Entry = S03 Share → O01；Close回同一 S03 Runtime context。
4. O01 consumer states固定為 CREATING / READY / COPY or SYSTEM SHARE feedback / FAILURE。
5. CREATING不顯示 fake URL / hash / second confirmation。
6. READY固定呈現 App identity → URL → Copy → supported System Share → Privacy copy → Close。
7. Copy Link是基本能力；System Share只在supported時顯示。
8. **Privacy copy always visible = YES**。
9. Copy success只做 inline feedback，不換頁、不關 Overlay。
10. Copy failure保留有效 URL與手動複製，不升級成 Share failure。
11. Share creation failure提供 Retry + Close，且明確告知 App不受影響。
12. Re-open READY不得重新 create。
13. Native Share cancel不是 Error。
14. O01不新增 Share Result / Runtime Snapshot / Live Room等 Phase 1外能力。

> Step 1：**APPROVED / LOCKED**。下一步：Step 2 — Geometry + Visual Hierarchy Lock。

## Step 2 — Geometry + Visual Hierarchy Lock ✅

> Approved by User：2026-09-23
>
> Step 2：**APPROVED / LOCKED**
>
> Scope：鎖定 O01 Desktop / Mobile overlay geometry、state body placement、URL / action hierarchy、Privacy copy位置與不同 state 的版面穩定性。不得改寫 Step 1 Function / state semantics；color / border / shadow / motion留給 Step 3。

### 1. Desktop Overlay Geometry

Desktop採 **centered lightweight dialog**，不採 anchored popover。

Recommended width：
~~~text
480–560px
max-width：約 560px
~~~

原因：O01需同時承接 URL、Privacy copy、Copy / System Share、Creating / Failure state；centered dialog可提供穩定結構，又不會像完整頁面。

### 2. Desktop Vertical Structure

固定順序：
~~~text
Title + Close
→ App Identity
→ State Body
→ Actions
→ Privacy Copy
~~~

READY / CREATING / FAILURE都沿用同一外框與主要區塊位置，避免 state transition時整個 dialog大幅跳動。

### 3. App Identity Scale

App Identity只作 context，不是主視覺。

Recommended：
- Logo：約 40–48px。
- App Title：約 16–20px。

不得做大型 hero / identity card。

### 4. Share URL Geometry

READY時 Share URL是第一操作焦點。

Rules：
- 佔主要內容寬度。
- 單行顯示。
- 可 keyboard select / manual copy。
- overflow安全處理。
- 不做大型 textarea。
- Desktop field高度約 44–48px。

### 5. Desktop READY Actions

Desktop READY actions預設同列：
~~~text
[複製連結]    [系統分享]
Primary        Secondary
~~~

`複製連結` = Primary。
`系統分享` = Secondary，只有 supported時存在。

若 System Share不支援：
- 不保留空槽。
- 不顯示 disabled placeholder。
- Copy自然成為唯一主要 action。

### 6. Privacy Copy Placement

Privacy copy固定放在 actions下方、overlay主體底部。

Rules：
- Always visible。
- 視覺優先低於 URL / actions。
- 仍屬主體內容，不縮成難以注意的 legal footer / tiny caption。
- line length保持易讀。

### 7. CREATING Layout Stability

CREATING不改 dialog外框 geometry。

App Identity保留；原 READY URL / action所在 State Body位置改呈現：
~~~text
正在準備分享連結…
+ O05 processing presentation
~~~

READY後只替換 State Body，不重建另一套 layout。

### 8. FAILURE Layout Stability

Share creation failure同樣在原 State Body位置替換：
~~~text
暫時無法建立分享連結
你的 App 不受影響

[再試一次]
[關閉]
~~~

不另開第二個 modal，不轉成 full-screen error。

### 9. Copy Feedback Locality

Copy success / failure只影響 URL + Copy action附近。

`已複製`放在 Copy action附近。

Copy failure message放在 URL field下方，保留有效 URL與其餘 READY layout。

不得因 clipboard feedback重排整個 Overlay。

### 10. Mobile Bottom Sheet Geometry

Mobile採 bottom sheet：
- full available width。
- horizontal padding約 16–20px。
- top radius = 20px。
- 預設由內容決定高度，不強制 full-height。
- 小螢幕 /內容增加時可延伸。

### 11. Mobile Action Order

Mobile固定：
~~~text
[複製連結]
[系統分享]  supported only
Privacy copy
Close
~~~

Rules：
- 主要 actions直向堆疊。
- 接近 full-width。
- min-height ≥ 44px。
- safe-area aware。
- Close使用明確 close control；Step 2不預設增加額外大型 Cancel button。

### 12. Visual Hierarchy

READY：
~~~text
Share URL / Primary Copy Action
> Overlay Title
> App Identity
> Secondary System Share
> Privacy Copy
> underlying NodeFF / Runtime context
~~~

CREATING：
~~~text
Processing state
> Overlay Title
> App Identity
~~~

FAILURE：
~~~text
Failure message + Recovery action
> Overlay Title
> App Identity
~~~

### 13. Step 2 Locked Decisions

1. Desktop = centered lightweight dialog，不用 anchored popover。
2. Desktop width約 480–560px，max-width約 560px。
3. 固定結構：Title + Close → App Identity → State Body → Actions → Privacy Copy。
4. App Identity保持 context scale：Logo約40–48px，Title約16–20px。
5. READY的Share URL是第一操作焦點。
6. `複製連結` = Primary；`系統分享` = Secondary。
7. Unsupported System Share不留 disabled placeholder / empty slot。
8. Privacy copy固定在 actions下方且 always visible。
9. CREATING / FAILURE原地替換 State Body，不另建另一套 Overlay geometry。
10. Copy success / failure維持 local feedback，不推倒 READY layout。
11. Mobile = bottom sheet，actions直向堆疊。
12. Mobile order = 複製連結 → 系統分享（supported only）→ Privacy copy → Close。

> Step 2：**APPROVED / LOCKED**。下一步：Step 3 — Detailed High-fi Visual Rules Lock。

# 18. Review Status

> **④A LOW_FI_APPROVED / ④B HIGH_FI_STEP1–2 APPROVED — STEP3 NEXT**

O01 ④A Low-fi與④B Step 1–2已完成 User Review。

下一步：**O01 ④B Step 3 — Detailed High-fi Visual Rules Lock**。

Formal Spec、Backlog / Sprint、Cursor implementation維持 HOLD。
