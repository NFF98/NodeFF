# S04 — Shared App Entry / Restore

> Screen ID：S04
>
> 狀態：**WORKING — ④A LOW_FI_APPROVED / ④B HIGH_FI_STEP1_APPROVED / STEP 2–4 PENDING**
>
> Phase：Phase 1
>
> Screen-level canonical owner：`working/UI-UX/screens/S04-SHARED-APP-ENTRY.md`
>
> Function behavior sources：F05 Share / Restore + F00 Experience Shell + F03 Runtime。
>
> 本文件的 ④A Low-fi 與 ④B High-fi Step 1 已完成 User Review；Step 2–4 尚未完成，因此仍不可交付 Cursor 實作。

# 1. User Outcome

S04 的核心任務：

> **Recipient 點開分享連結後，不用安裝、不用登入、不用重新生成，盡快直接進入可使用的同一個 App。**

因此 S04 不應變成 Landing Page、Creator Profile、Share Preview Page 或登入牆。

# 2. Core UX Direction — Proposed

S04 預設是一個 **transitional entry surface**，不是長時間停留的正式產品頁。

正常成功路徑：

    /share/{share_id}
    → S04 short restore transition
    → S03 App / Runtime

若 restore 足夠快，S04 可以只短暫出現，甚至幾乎感覺不到。

只有兩類情況需要讓 S04 明顯存在：

1. Restore 尚在進行，需要避免白畫面。
2. Share / Blueprint / Trust / Compatibility / Hydration 發生錯誤，需要 humanized recovery。

# 3. Important Product Truth

Recipient 取得的是：

    same immutable Blueprint
    + fresh Runtime Instance

不是：

    Creator 當時的輸入
    Creator 當時的結果
    Creator 當時的 Runtime state

UI 不應暗示「接續 Creator 當時的進度」。

# 4. Normal Restore Flow

F05 internal states：

    OPEN_ROUTE
    → RESOLVING_SHARE
    → FETCHING_BLUEPRINT
    → CHECKING_TRUST
    → HYDRATING
    → READY

Consumer 不顯示這些工程狀態名稱。

User-facing restore UI 固定顯示：
- App Logo / App Title（可取得時）。
- Loading progress %。
- 簡短人話狀態。

Proposed consumer stages：

    正在打開這個 App…
    ↓
    正在確認可以安全使用…
    ↓
    正在準備 App…
    ↓
    S03

Loading % 必須表示「已完成的 restore work」，不是預估剩餘時間。

# 5. Proposed Desktop Low-fi

    ┌──────────────────────────────────────────────┐
    │ NodeFF                                       │
    │                                              │
    │                                              │
    │              [ App Logo ]                    │
    │               App Title                      │
    │                                              │
    │            正在打開這個 App…                 │
    │                  42%                         │
    │            ████████────────                  │
    │                                              │
    │        不需要登入，也不需要安裝              │
    │                                              │
    └──────────────────────────────────────────────┘

正常情況不顯示額外 CTA。

若 Blueprint metadata 已安全取得，可在不延遲 READY 的前提下顯示：

    App Logo / App Title

但不得為了做漂亮 preview 而延後進 S03。

# 6. Proposed Mobile Low-fi

    ┌──────────────────────────┐
    │ NodeFF                   │
    │                          │
    │      [ App Logo ]        │
    │       App Title          │
    │                          │
    │   正在打開這個 App…      │
    │          42%             │
    │     ███████──────        │
    │                          │
    │ 不需要登入，也不需要安裝 │
    └──────────────────────────┘

Mobile 不顯示 navigation / bottom navigation，因為還沒有進入真正 S03 Runtime。

READY 後再由 S03 接管 Header / Bottom Navigation。

Cross-screen rule：
- permanent NodeFF bottom navigation只屬於 S03 Runtime。
- S04 restore期間不預先顯示 S03 Shell navigation，也不讓 User在 restore中誤進其他 Shell flow。

# 7. Progress Behavior

S04 progress 是 restore progress，不是 AI generation progress。

Rules：
- 不使用 S02 的「理解 / 組 App」copy。
- 不顯示 LLM / Compile / Validation engineering terminology。
- **顯示 Loading %。**
- 百分比只能根據已完成的 restore checkpoints / hydration work推進，不能假裝預測剩餘秒數。
- 不為了動畫而故意延長 loading。
- 當 metadata 已取得時，同時顯示 App Logo / Title。

Low-fi progress checkpoints：

1. Share resolved。
2. Blueprint fetched / trust checked。
3. Runtime hydration completed。

UI 可以把這些 checkpoint 映射成連續 Loading %，但不把 internal technical names直接顯示給 User。

# 8. No Login / No Install

First Value 前：

- 不要求 Sign in。
- 不要求註冊。
- 不要求下載 App。
- 不要求 Creator 授權。
- 不要求重新輸入 Prompt。

若未來要做 account CTA，只能在 S03 使用 App 後再討論，不屬 S04 Phase 1 baseline。

# 9. App Identity

若在 Blueprint fetch 後已取得安全 metadata：

顯示：
- App Logo。
- App Title。
- Loading progress %。

不顯示：
- Creator anonymous ID。
- raw Prompt。
- Blueprint hash。
- model/provider。
- Runtime inputs/results。

App identity 是輔助，不是 blocking dependency。

# 10. Error / Recovery States

S04 必須承接 F05 / F12 的 humanized failure。

## A. Link Not Found

    這個分享連結找不到了。

    [回到 NodeFF]
    [建立自己的 App]

不 Retry 無意義 permanent 404。

## B. Expired / Revoked

    這個分享 App 已經無法使用。

    [回到 NodeFF]

不假裝重新生成舊 App。

## C. Temporary Blueprint / Network Failure

    暫時打不開，但分享連結還在。

    [再試一次]
    [回到 NodeFF]

保留原 share route / reference。

## D. Incompatible / Unsafe To Run

    這個 App 目前無法安全開啟。

    [重新整理再試]
    [回到 NodeFF]

不 silently reinterpret、不偷偷 recompile。

## E. Hydration Recoverable

依 F12 / F03：
- 若 core App仍可安全使用 → 進 S03 + inline Recovery。
- 若不能安全 READY → 留 S04 blocking recovery。

# 11. Back / Close Behavior

Recipient 從外部 link 進來時：

- Browser Back → 回前一個外部頁面，正常。
- S04 不需要自創 Back stack。
- 不在 restore 中要求 User 選擇是否繼續，除非有 material recovery decision。

# 12. Transition To S03

READY 後：

    S04
    → S03

Transition 原則：
- 不增加「App 已準備好，按繼續」頁。
- 不要求再按一次 Enter / Open。
- S03 建立 fresh Runtime Instance。
- S03 接管 App identity、Share、Remix、Correct、bottom navigation等 Shell。

# 13. Share → Remix

Recipient 在 S04 不直接 Remix。

先：

    S04 → S03

User 實際看到 / 使用 App後，再從 S03 進：

    Remix → S05

這避免 Recipient 還沒看到 App，就被推去 Creator flow。

# 14. Accessibility Baseline

- Restore status透過 aria-live適度通知。
- Progress不能只靠顏色。
- 長 loading需有可理解文字。
- Error primary action可 keyboard / assistive tech操作。
- reduced-motion preference被尊重。
- 進 S03後 focus移到 App主要內容，而不是留在消失的 loading UI。

# 15. Confirmed S04 Low-fi Decisions

User 已確認：

1. **S04 採幾乎隱形的過渡層**；成功時自動進 S03，不建立 Share Landing Page。
2. Restore 過程顯示 **Loading progress %**。
3. S04 顯示 **App Logo / App Title + Loading %**；不顯示 Login、Creator資料、Prompt、Result Preview。
4. 永久失效的 Share 不重新生成舊 App；只有暫時性錯誤才提供 Retry，其餘提供 Home / Create New 等安全出口。
5. Loading % 必須由已完成 restore work推進，不代表預估剩餘時間。

# 16. Review Status

> **④A LOW_FI_APPROVED / ④B HIGH_FI_STEP1_APPROVED / STEP 2–4 PENDING**

S04 ④A Low-fi 已完成 User Review；④B High-fi Step 1 Structure Lock 已完成。下一步為 S04 Step 2 — Geometry + Visual Hierarchy Lock。


---

# 17. ④B High-fi Contract

> Step 1 approved by User：2026-09-22
>
> Canonical rule：本節是 S04 High-fi 的唯一 canonical contract。後續 Step 2–4 必須在本節內續寫，不得另建重複 High-fi summary / shadow copy。
>
> Current status：
> - Step 1 — Structure Lock ✅
> - Step 2 — Geometry + Visual Hierarchy Lock ⏳
> - Step 3 — Detailed High-fi Visual Rules Lock ⏳
> - Step 4 — Final Visual Reference Lock ⏳

## Step 1 — Structure Lock ✅

### 1. S04 Role

S04 是 **Shared App Entry / Restore transitional surface**。

它的任務只有：

~~~text
外部分享連結
→ 安全恢復同一 immutable Blueprint
→ 建立 fresh Runtime Instance
→ READY
→ S03 App / Runtime
~~~

S04 不是：
- Share Landing Page；
- Creator Profile；
- App Preview Page；
- Login / Sign-up wall；
- Builder / Editor；
- 第二個 Runtime surface。

### 2. Minimal Entry Chrome

Desktop / Mobile 一致：

- 只保留必要的 NodeFF brand / entry chrome。
- 不顯示 S01完整 navigation。
- 不顯示「首頁 / 探索靈感 / 我的 App / 修改 / 分享 / Profile」。
- 不顯示 hamburger。
- 不顯示 S03 permanent bottom navigation。

S03 navigation只能在 Runtime真正 READY並完成 S04 → S03 handoff後出現。

### 3. App Identity

若安全 metadata 已取得，可顯示：

~~~text
App Logo
App Title
~~~

Rules：
- App identity是 contextual aid，不是 blocking dependency。
- 不得為了等待 Logo / Title而延遲 READY。
- 不顯示 Creator anonymous ID、raw Prompt、Blueprint hash、provider/model、Creator inputs/results。

### 4. Restore Status Surface

Normal restore body固定只需要：

~~~text
App Identity（when available）
↓
Human-readable restore stage
↓
Progress presentation
↓
「不需要登入，也不需要安裝」
~~~

Progress presentation只鎖位置與存在條件，不在 S04自行定義完整 cross-flow checkpoint contract。

Canonical presentation boundary：

~~~text
reliable restore checkpoints
→ Stage + checkpoint-derived %

no reliable restore checkpoints
→ Stage only
~~~

詳細 cross-flow progress model留待 O05 High-fi / Processing Review統一處理。

S04不得：
- 用 elapsed time推算進度；
- fake smooth %；
- 顯示 LLM / Compiler / Validator等工程語言；
- 為了 loading animation故意延遲 READY。

### 5. Success Path — Direct to S03

Desktop / Mobile一致：

~~~text
restore READY
→ immediately enter S03
~~~

成功後：
- 不顯示「開啟 App」中繼按鈕；
- 不顯示「完成，按繼續」頁；
- 不要求 User再次確認；
- S03立即接管 App identity、Runtime、Share、Modify、Correct與 Mobile bottom navigation。

### 6. Failure / Recovery Path — Must Always Have Home Escape

Desktop / Mobile一致。

只要 S04 無法進入正常 READY，UI必須提供 **可返回 NodeFF 首頁 S01 的安全出口**，讓 User離開失敗 share flow並可重新建立自己的 App。

Canonical safe exit：

~~~text
[回到首頁]
→ S01 Discover / Start
→ User 可重新建立 App
~~~

若 source Function truth判定該錯誤可 retry，可另外顯示：

~~~text
[再試一次]
[回到首頁]
~~~

Rules：
- `回到首頁`在失敗狀態不得被移除。
- Desktop / Mobile recovery capability一致；只能因版面不同改排列，不得改可用出口。
- UI不得自行判定 retryable。
- permanent not-found / revoked / expired不可假裝 Retry能恢復。
- incompatible / unsafe不得偷偷 recompile或 reinterpret舊 App。
- 若未來加入「建立自己的 App」快捷 CTA，其 destination仍是 S01 Create entry，不建立另一套 creation flow。

### 7. No App Preview / Creator Runtime Carry-over

S04不預先 render：
- App screenshot preview；
- Creator當時的 inputs；
- Creator當時的 result；
- Creator Runtime state；
- fake Generated App skeleton。

Recipient得到：

~~~text
same immutable Blueprint
+ fresh Runtime Instance
~~~

不是 Creator session continuation。

### 8. Mobile Structure

Mobile與 Desktop採相同 semantic structure：

~~~text
NodeFF brand
↓
App Identity（when available）
↓
Restore Status / Recovery
~~~

Mobile restore期間沒有 permanent bottom navigation。

只有進入 S03後才出現：

~~~text
App | 修改 | 分享
~~~

Clarification：
- `App = current S03 Runtime destination, not S01.`
- 此處引用 S03 已批准的 Mobile nav wording；S04 不另外定義或改名。
- 若未來 S03 將 `App` 改成 `使用` / `目前 App` 或其他更直覺 consumer label，必須先 reopen S03 Step 1，再同步回 S04。

### 9. Function Handoff Boundary

Canonical handoff：

~~~text
/share/{share_id}
→ F05 resolve Share
→ immutable Blueprint reference
→ trust / compatibility truth
→ F03 fresh Runtime hydration
→ READY
→ S03
~~~

S04 presentation不得：
- 重新 compile Blueprint；
- restore Creator inputs / results；
- mutation immutable Blueprint；
- 自己決定 READY；
- 自己發明 checkpoint；
- 自己推進 progress；
- silently reinterpret incompatible content。

### Step 1 Lock Summary

S04 High-fi Structure Lock：

> **成功就直接消失進 S03；失敗就留在同一 S04 recovery surface，而且 Desktop / Mobile 都一定有「回到首頁」的安全出口，讓 User 可回 S01重新建立 App。**

Step 1：**APPROVED / CLOSED**。

Next：

> **S04 Step 2 — Geometry + Visual Hierarchy Lock**
