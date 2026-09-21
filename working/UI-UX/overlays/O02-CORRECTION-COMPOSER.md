# O02 — Correction Composer

> Overlay ID：O02
>
> 狀態：**WORKING — LOW_FI_DIRECTION_APPROVED / HIGH_FI_PENDING**
>
> Phase：Phase 1
>
> Screen-level canonical owner：`working/UI-UX/overlays/O02-CORRECTION-COMPOSER.md`
>
> Function behavior source：F16 Result Correction + F00 Experience Shell。
>
> 本文件是 ④A Low-fi review draft，不代表 User 已批准，也不代表 Cursor 可實作。

# 1. User Outcome

O02 的核心任務：

> **User 發現目前結果 / 規則 / 邏輯不符合預期時，可以直接說「哪裡不對」，NodeFF 保留原 App 與目前結果，開始 correction flow。**

O02 不是一般 Refine Composer。

# 2. Entry / Exit

Entry：

    S03 Result Surface
    → 調整結果 / 邏輯不對 / 結果不是我想要的
    → O02

Exit：

    Cancel
    → 回 S03，同一 App / inputs / result保留

Submit：

    O02
    → F16 correction lifecycle
    → 必要時 clarification / assumption
    → replay / compare
    → S06

# 3. Correction vs Refine Boundary

O02 只處理：

- 結果算錯。
- 規則理解錯。
- 假設錯。
- 邏輯不符合原本意圖。

不處理：

- 加新功能。
- 大幅改 UI。
- 新增 / 刪除 input。
- 改成不同用途。

若 User feedback混入上述功能修改，F16 / F01 可引導轉 S05 Refine，而不是讓 O02 偷偷變成功能編輯器。

# 4. Minimum Information

F16 已固定 Correction Entry minimum：

- current result摘要。
- natural-language correction input。
- optional expected result / rule hint。
- Cancel。
- Continue。

O02 不顯示：
- Blueprint hash。
- Runtime state keys。
- Correction Delta。
- JSON。
- model/provider。
- technical error code。

# 5. Proposed Desktop Low-fi

    ┌──────────────────────────────────────────────────┐
    │ 調整結果                                    [×] │
    │                                                  │
    │ 目前結果                                         │
    │ ┌──────────────────────────────────────────────┐ │
    │ │ $1,200                                       │ │
    │ └──────────────────────────────────────────────┘ │
    │                                                  │
    │ 哪裡不對？                                       │
    │ ┌──────────────────────────────────────────────┐ │
    │ │ 主管應該付兩倍，但現在沒有算進去…           │ │
    │ └──────────────────────────────────────────────┘ │
    │                                                  │
    │ 預期結果或規則（選填）                           │
    │ ┌──────────────────────────────────────────────┐ │
    │ │ 例如：主管權重應為 2x                        │ │
    │ └──────────────────────────────────────────────┘ │
    │                                                  │
    │ [取消]                              [開始修正]   │
    └──────────────────────────────────────────────────┘

Desktop 建議 lightweight dialog / side panel，不跳全頁。

# 6. Proposed Mobile Low-fi

    ╭────────────────────────────╮
    │ 調整結果               [×] │
    │                            │
    │ 目前結果                   │
    │ $1,200                     │
    │                            │
    │ 哪裡不對？                 │
    │ ┌────────────────────────┐ │
    │ │ correction feedback    │ │
    │ └────────────────────────┘ │
    │                            │
    │ 預期結果或規則（選填）     │
    │ ┌────────────────────────┐ │
    │ │ optional hint          │ │
    │ └────────────────────────┘ │
    │                            │
    │ [      開始修正      ]     │
    ╰────────────────────────────╯

Mobile 建議 bottom sheet / full-height sheet，但仍保留目前 App context，不另開獨立 route。

# 7. Current Result Summary

O02 顯示的是 F03 / F16 canonical result summary。

Rules：
- 不從 DOM 猜。
- 多個 outputs 時只顯示主要 / material result，其他可展開。
- output ERROR 不 fake value。
- protected / sensitive result依 F16 privacy policy處理。
- 目的只是讓 User確認「我正在修哪個結果」。

# 8. Main Input — 哪裡不對？

Primary field：

> **哪裡不對？**

User可用自然語言，例如：

- 主管應該付兩倍。
- 這個總額不對。
- 你把週末也算進工作日了。
- 這個排名規則跟我原本說的不一樣。

這是 correction semantic source。

# 9. Optional Expected Result / Rule Hint

Secondary field：

> **預期結果或規則（選填）**

可以填：
- 明確預期數值。
- 正確規則。
- 正確假設。
- 判斷方式。

例如：

    正確結果應該是 1450
    主管權重 = 2x

Rules：
- User沒填也能 Continue。
- LLM / System不能自己把 expected result填成 User fact。
- 如果 correction feedback已很清楚，不要求重複輸入。

# 10. Submit Behavior

Primary CTA：

    開始修正

Submit後：

    CAPTURING_BEFORE
    → ANALYZING
    → ...

Consumer不顯示 internal state names。

Low-fi copy可用：

    正在確認目前結果…
    正在理解你指出的問題…
    正在準備修正版…

處理中固定顯示 **Progress %**。

Rules：
- 百分比必須對應已完成的 correction checkpoints / work，不假裝預測剩餘秒數。
- clarification等待 User input時暫停進度，不假裝持續增加。
- 進入 child compose / validation / replay時可持續更新。
- 不為了動畫故意延長 operation。

O02本身在 submit後可：
- 保持 sheet/panel並轉 progress state，或
- 收合為 bounded progress state。

不能立即把原 App清掉。

# 11. Clarification After Submit

若 F16 / F01發現 correction仍有 material ambiguity：

- 沿用 S02 / S05同一 clarification presentation。
- 最多 1–3 material questions。
- 保留 correction draft。
- 不要求 User重打目前結果。

# 12. Cancel / Close

EDITING 狀態：
- Close / Cancel → 回 S03。
- 原 App / current inputs / current result保持。
- correction draft可依 F00 draft policy保留。

Submit後若 operation仍在進行：
- 可安全 cancel時允許取消。
- 不能安全 cancel時，不假裝已中止；依 F00 operation semantics處理。
- 不破壞 base App。

# 13. Failure

任何 correction technical failure：

    修正沒有完成
    原本的 App 和結果都還在

    [再試一次]
    [修改說明]
    [回原 App]

詳細由 O03 / F12承接。

# 14. Accessibility

- Field有明確 label。
- Current Result summary可被 assistive tech讀取。
- Optional欄位明確標示「選填」。
- Error與field programmatic association。
- Mobile keyboard開啟時 CTA仍可達。
- Close後 focus回 S03 correction trigger。
- submit progress透過 aria-live適度通知。

# 15. Confirmed O02 Low-fi Decisions

User 已確認：

1. Desktop 使用 lightweight dialog / side panel；Mobile 使用 bottom sheet / full-height sheet，不做獨立頁。
2. O02 固定顯示：**目前結果摘要 +「哪裡不對？」+「預期結果或規則（選填）」**。
3. Primary CTA 固定為 **「開始修正」**；Submit 後先進 progress / clarification，最後才進 S06 Compare。
4. Correction 處理中必須顯示 **Progress %**；百分比依真實已完成 work / checkpoints 推進，不做假時間預估。
5. 若 User其實是在加功能 / 改 UI / 改用途，由系統引導轉 S05 Refine，不把 O02 擴張成通用修改器。

# 16. Review Status

> **LOW_FI_DIRECTION_APPROVED — HIGH_FI_PENDING**

O02 ④A Low-fi 已完成 User Review。

依固定流程，下一步進 O03 — Recovery Overlay ④A Low-fi。
