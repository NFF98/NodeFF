# O04 — Revert Confirmation

> Overlay ID：O04
>
> 狀態：**WORKING — LOW_FI_DIRECTION_APPROVED / HIGH_FI_PENDING**
>
> Phase：Phase 1
>
> Screen-level canonical owner：`working/UI-UX/overlays/O04-REVERT-CONFIRMATION.md`
>
> Function behavior source：F00 Experience Shell + F16 Result Correction。
>
> 本文件是 ④A Low-fi review draft，不代表 User 已批准，也不代表 Cursor 可實作。

# 1. User Outcome

O04 的核心任務：

> **User 已接受某次修正版後，如果想回到修正前版本，可以清楚知道會回哪一版、輸入會不會一起恢復，而且修正版不會被刪除。**

# 2. Entry Preconditions

O04 只在以下條件成立時可進：

    current active Blueprint
    = same-session previously ACCEPTED correction child

並且：

    previous/base Blueprint
    still trusted + compatible

若 previous/base 已 REVOKED / INCOMPATIBLE：

- 不顯示可執行 Revert CTA。
- 交 O03 / F12 說明不能安全返回。

# 3. Entry

S03：

    Previous Version
    / 回到修正前版本
    → O04

O04 不是版本歷史頁。

Phase 1 不承諾：
- account-level history。
- cross-device完整版本列表。
- 任意多版本 timeline。

# 4. Core Message

主訊息固定要讓 User知道兩件事：

1. 會回到修正前版本。
2. 目前修正版不會被刪除。

Low-fi：

    回到修正前版本？

    目前修正版不會被刪除。

# 5. Version Target

O04 必須顯示 target identity，避免 User不知道「回到哪一版」。

可顯示：
- App Logo / Title。
- 「修正前版本」label。
- 若有簡短 result summary，可顯示 previous result摘要。

不顯示：
- Blueprint hash。
- lineage ID。
- correction_id。
- internal version enum。

# 6. Input Restoration — Three Cases

## Case A — Before Snapshot Available

如果 same-session correction前 snapshot仍在 memory且 compatible：

    會恢復：
    ✓ 修正前版本
    ✓ 修正前輸入

這是 default。

## Case B — Only Current Inputs Can Be Safely Mapped

如果原 snapshot不存在，但 current inputs可安全映射：

    回到修正前版本
    [ ] 保留目前輸入

Toggle default = OFF。

只有 User explicit opt-in才帶 current compatible inputs。

## Case C — No Safe Input Snapshot

如果沒有安全可恢復的 input snapshot：

    會回到修正前版本，
    但目前輸入不會恢復。

    App 將從原版初始狀態開始。

這件事必須在 Confirm 前說清楚。

# 7. Desktop Low-fi

    ┌──────────────────────────────────────────────┐
    │ 回到修正前版本？                       [×] │
    │                                              │
    │ [App Logo] App Title                         │
    │ 修正前版本                                   │
    │                                              │
    │ 目前修正版不會被刪除。                       │
    │                                              │
    │ 輸入狀態                                     │
    │ ✓ 將恢復修正前的輸入                         │
    │                                              │
    │ [取消]                         [回到原版]     │
    └──────────────────────────────────────────────┘

# 8. Mobile Low-fi

    ╭────────────────────────────╮
    │ 回到修正前版本？       [×] │
    │                            │
    │ [Logo] App Title           │
    │ 修正前版本                 │
    │                            │
    │ 修正版不會被刪除           │
    │                            │
    │ ✓ 恢復修正前輸入           │
    │                            │
    │ [取消]                     │
    │ [      回到原版      ]     │
    ╰────────────────────────────╯

Mobile 可用 bottom sheet / confirmation sheet。

# 9. CTA Semantics

Primary：

    回到原版

Secondary：

    取消

不建議寫：
- Delete New Version
- Undo Forever
- Restore Data

因為這些都會造成錯誤心智。

# 10. Successful Revert

Confirm 後：

    fresh ExecutionAdmission for base
    → fresh F03 Runtime Instance
    → APP on base Blueprint

結果：

- active App切回 base。
- correction outcome = REVERTED。
- 修正版 child不刪除。
- lineage不刪除。
- 回 S03，不回 S06 Compare。

# 11. Failure

若 confirm 後發現 target不能安全執行：

    無法安全回到這個版本
    目前修正版仍保持可用

    [保留目前版本]
    [回到 App]

交 O03 / F12。

不能：
- force execute unsafe base。
- silent downgrade trust。
- 重新 compile old Blueprint來假裝 revert成功。

# 12. Close / Cancel

Cancel / Close：

- 保持 current corrected App active。
- 不修改 correction outcome。
- 不 mutation任何 Blueprint。
- focus回 S03 Previous Version / Revert trigger。

# 13. Accessibility

- confirmation heading明確。
- target version不只靠顏色識別。
- input restoration狀態可被 screen reader讀取。
- destructive-looking action wording清楚。
- Primary / Cancel keyboard可達。
- Mobile touch target至少44 CSS px。
- Confirm後進度由 O05共用 loading規則承接。

# 14. Confirmed O04 Low-fi Decisions

User 已確認：

1. O04 固定先說 **「回到修正前版本？」**，並明確補一句 **「目前修正版不會被刪除」**。
2. Confirm 前明確顯示輸入恢復狀態：可恢復 / 可選擇保留目前輸入 / 無法恢復。
3. CTA 固定為 **取消 + 回到原版**，不使用 Delete / Undo Forever 等容易誤解的 wording。
4. 若 previous/base 已不安全或 incompatible，不提供可執行 Revert；改由 O03 / F12 說明並保留目前修正版。
5. 「目前修正版不會被刪除」對應 F16 既有 Function truth：成功 Revert 後 child Blueprint 與 CORRECT lineage 都保留，只是 active App 切回 previous/base。

# 15. Review Status

> **LOW_FI_DIRECTION_APPROVED — HIGH_FI_PENDING**

O04 ④A Low-fi 已完成 User Review。

依固定流程，下一步進 O05 — Loading / Building / Hydration States ④A Low-fi。
