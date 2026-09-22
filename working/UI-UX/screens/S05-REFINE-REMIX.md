# S05 — Refine / Remix Workspace

> Screen ID：S05
>
> 狀態：**WORKING — LOW_FI_DIRECTION_APPROVED / HIGH_FI_PENDING**
>
> Phase：Phase 1
>
> Screen-level canonical owner：`working/UI-UX/screens/S05-REFINE-REMIX.md`
>
> Function behavior sources：F06 Remix / Refine + F00 Experience Shell + F01 Intent Compilation + F03 Runtime。
>
> 本文件是 ④A Low-fi review draft，不代表 User 已批准，也不代表 Cursor 可實作。

# 1. User Outcome

S05 的核心任務：

> **User 不用從頭重做，就能以目前 App 為基礎描述想改什麼；原版始終安全，新版先 Preview，再由 User 決定採用、保留舊版或繼續調整。**

# 2. Refine vs Remix — Same Workspace, Different Meaning

Low-fi 建議共用同一個 S05 Workspace，不做兩套 UI。

Difference 同時用 **relation label + version visual marker** 說清楚：

- **Refine**（internal relation）→ Consumer UI：**修改這個 App**；延續目前 App，做下一版。
- **Remix**（internal relation）→ Consumer UI：**改成我的版本**；以目前 App 為底稿，做衍生版本。
- 原版 / 新版在 Low-fi 先保留不同的 border / accent token 作為版本識別；**實際顏色值屬 ④B High-fi Design System，不在 Low-fi 鎖定。**

原因：
- 兩者底層流程幾乎一致。
- 不需要讓 User 學兩套介面。
- lineage semantics由 F06決定，不靠不同畫面結構。

# 3. Entry

主要入口：

    S03 Current App
    → Refine / Remix
    → S05

S04 Shared App restore完成後，也是先進 S03，再由 S03進 Remix。

進入 S05 必須保留：
- source App reference。
- source App title / logo。
- relation type：Refine / Remix。
- 原 App仍可返回。

# 4. Core Flow

    Source App
    ↓
    Describe Change
    ↓
    ANALYZING
    ├─ CLARIFICATION_REQUIRED
    ├─ ASSUMPTION_REVIEW
    └─ READY
    ↓
    COMPOSING / VALIDATING
    ↓
    PREVIEW_READY
    ↓
    ├─ Use New Version
    ├─ Keep Previous
    └─ Adjust Again

任何 failure：
    source App remains safe

# 5. Proposed Desktop Low-fi — Change Composer

    ┌──────────────────────────────────────────────────────────┐
    │ NodeFF    [App Logo] App Title              [回原 App] │
    ├──────────────────────────────────────────────────────────┤
    │ Refine / Remix                                           │
    │                                                          │
    │ 你想怎麼改這個 App？                                     │
    │ ┌──────────────────────────────────────────────────────┐ │
    │ │ 例如：加一個截止時間，結果改成排名顯示…             │ │
    │ └──────────────────────────────────────────────────────┘ │
    │                                                          │
    │ Source App summary（輕量，可展開）                       │
    │ • 目前 App：餐廳投票                                    │
    │ • 原版會保留                                            │
    │                                                          │
    │ [取消]                                [開始修改]          │
    └──────────────────────────────────────────────────────────┘

原版內容不整頁重複 render在左邊，避免畫面太重。

建議只放：
- App identity。
- 簡短 source summary。
- **「查看原版」button**：User 可回原 App / 原結果確認，再返回 S05，修改草稿不得遺失。

# 6. Proposed Mobile Low-fi — Change Composer

    ┌────────────────────────────┐
    │ ‹ 原 App       App Title  │
    │                            │
    │ Refine / Remix             │
    │                            │
    │ 你想怎麼改這個 App？      │
    │ ┌────────────────────────┐ │
    │ │ change request         │ │
    │ └────────────────────────┘ │
    │                            │
    │ 原版會保留                │
    │                            │
    │ [      開始修改      ]    │
    └────────────────────────────┘

Mobile 不做 split-pane；保留明顯的「查看原版」入口，返回 S05 時保留 change draft。

Cross-screen navigation rule：
- S05 是 focused modification workspace，不繼承 S03 permanent bottom navigation。
- 返回 / 查看原版 / decision CTA由 S05自身承接，避免修改中誤觸 S03 Shell actions。

# 7. Change Composer Rules

Minimum UI：
- source App title / logo。
- relation label。
- natural-language change input。
- Cancel。
- Continue / 開始修改。

Optional：
- current assumptions / relevant inputs，只在真的跟 change有關時顯示。
- 不預設 carry Runtime inputs。

User不用看：
- source hash
- lineage
- semantic delta
- JSON
- model/provider

# 8. Clarification / Assumption

S05 沿用 S02 同樣原則：

> **只有真的需要 User decision 才打斷。**

Clarification：
- 1–3 material questions。
- 直接嵌在同一 Workspace。
- 原 change request保留。

Assumption Review：
- 只顯示 material assumptions。
- Accept / Edit / Reject。
- 不顯示 raw provenance enum。

# 9. Change Progress

S05 建議沿用 NodeFF creation progress語言，但改成 change context。

Low-fi proposed stages：

1. 理解修改
2. 更新 App
3. 檢查互動
4. 準備新版

Rules：
- 共用 O05：有可靠 checkpoints時顯示 **Stage label + checkpoint-derived Progress %**。
- 沒有可靠 checkpoints時只顯示 Stage label，不 fake %。
- % 代表 work completion，不代表剩餘時間。
- 不為了讓 progress看得到而延遲真正完成。
- 不顯示 Prompt / Validation engineering terminology。
- source App始終保持安全。

# 10. Preview Ready — Core S05 State

F06 已明確要求：

    source App remains safe
    + child fresh Runtime Instance
    → PREVIEW_READY

Low-fi 建議 Preview 狀態直接成為 S05 後半段主要畫面。

Desktop：

    ┌──────────────────────────────────────────────────────────┐
    │ App Title — 新版預覽                        [返回原版]   │
    ├──────────────────────────────────────────────────────────┤
    │                                                          │
    │                  NEW APP PREVIEW                         │
    │                  fresh Runtime                          │
    │                                                          │
    ├──────────────────────────────────────────────────────────┤
    │ 這是新版，原版仍保留                                    │
    │ [查看原版]                                               │
    │                                                          │
    │ [保留原版]      [再調整]             [使用新版]          │
    └──────────────────────────────────────────────────────────┘

Mobile：

    ┌────────────────────────────┐
    │ 新版預覽          原版     │
    ├────────────────────────────┤
    │                            │
    │      NEW APP PREVIEW       │
    │                            │
    ├────────────────────────────┤
    │ 原版仍保留                │
    │ [查看原版]                │
    │ [保留原版]                │
    │ [再調整] [使用新版]        │
    └────────────────────────────┘

# 11. Preview Comparison Philosophy

S05 不是 S06 Correction Compare。

所以預設不做：
- old/new result逐項比較。
- technical diff。
- correction explanation。

S05只需要：
- 明確告訴 User現在看到的是新版。
- 原版安全存在。
- 可以回原版。
- 可以再調整。

若未來 High-fi需要 side-by-side preview，再根據實際 screen size決定，不在 Low-fi先鎖。

# 11.1 View Original

S05 必須讓 User 隨時確認 source App / 原版結果。

Flow：

    S05
    → 查看原版
    → source App / source result
    → 返回修改
    → S05 current draft / preview context preserved

Rules：
- 「查看原版」不是「保留原版」決策。
- 查看原版不改 active child / source selection。
- 不清空 change draft。
- Preview 已存在時，返回 S05 後仍回到同一 preview context。
- Mobile / Desktop 都必須可達。

# 12. Use New Version

Primary CTA：

    使用新版

結果：
- child Blueprint / Runtime becomes active。
- 回 S03。
- source仍存在。
- lineage保留。

User心智：
> 「好，就用這個版本。」

# 13. Keep Previous

CTA：

    保留原版

結果：
- source remains active。
- 回 S03 source App。
- child artifact不需要刪除。

Consumer不需要知道 immutable hash / lineage。

# 14. Adjust Again

CTA：

    再調整

F06 default：
- base = latest preview child。

UI 必須顯示清楚：

    你正在調整：剛剛的新版本

並提供 secondary option：

    從原版重新調整

避免 User搞不清楚 change是疊在哪一版上。

# 15. Runtime Input Carryover

一般 Refine / Remix：

> **不自動帶現在 Runtime輸入到新版。**

Low-fi不需要每次跳警告。

只有在 User可能誤解時，用簡短 copy：

    新版會從自己的初始狀態開始。

不顯示 privacy/security工程說明。

# 16. Failure / Recovery

任何 failure 都必須保證：

    原 App 還在

Examples：

## Analysis / Compose Failure

    這次修改沒有完成，原版沒有受影響。

    [再試一次]
    [修改需求]
    [回原 App]

## Unsupported Change

    這個修改目前還做不到。

    [簡化修改]
    [回原 App]

## Child Hydration Failure

    新版已產生，但目前無法打開預覽。

    [再試一次]
    [保留原版]

詳細 recovery由 O03 / F12承接。

# 17. Back / Cancel

任何 S05 state：
- Cancel / Back預設回 source App。
- 不丟 change draft when recoverable。
- Preview時 Back不能默認採用新版。
- Adjust Again可回 Preview，不破壞 child。

# 18. Accessibility / Responsive

- relation label不能只靠顏色。
- Composer有明確 label。
- Preview CTA順序與 keyboard focus合理。
- Mobile CTA不遮 Generated App preview。
- preview ready透過非破壞性 live announcement。
- 返回原版 / 使用新版 wording明確，避免 ambiguous「Done」。

# 19. Confirmed S05 Low-fi Decisions

User 已確認：

1. **Refine / Remix 共用同一個 S05 Workspace**。
2. Refine / Remix 必須同時用 **relation label + version visual marker** 區分。
3. 原版 / 新版的 border / accent 需要可辨識；實際顏色留到 ④B High-fi Design System 決定。
4. Change Composer 只顯示 App identity + 修改需求 +「原版會保留」，不把原 App整頁並排。
5. 必須提供 **「查看原版」button**，讓 User 回原 App / 原結果確認後再回 S05，且 change draft / preview context 不遺失。
6. 新版完成直接進 Preview，三個主要決策 CTA：**保留原版 / 再調整 / 使用新版**。
7. 「再調整」預設基於最新 Preview child，並提供「從原版重新調整」secondary option。

# 19.1 ④B Version Color Management

User confirmed during ④B review：

- **Refine / Remix 共用同一個 S05 Workspace**；不做兩套 UI。
- relation semantics 必須透過 **relation label** 明確顯示，不能只靠顏色。
- version visual marker 同時採 **border / accent color management**：
  - **Source / Original / Before**：Neutral treatment；使用 neutral border / surface，代表原版與來源。
  - **Candidate / New / After**：Teal / Aqua treatment；使用 Teal / Aqua border / accent，代表新版／目前候選版本。
  - **Yellow**：只作 small `NEW` / changed / energy marker；不得作整個新版 surface 的主色或把新版誤表達成 warning。
- 原版與新版的區分必須同時依賴：
  1. relation label；
  2. version label（原版／新版等 consumer copy）；
  3. border / accent visual marker。
- Accessibility：版本關係不得只靠顏色辨識。
- 這套 version color language 與 `working/UI-UX/DESIGN-SYSTEM.md` 的 Version / Compare Visual Language 一致。

# 20. Review Status

> **LOW_FI_DIRECTION_APPROVED — HIGH_FI_PENDING**

S05 ④A Low-fi 已完成 User Review。

依固定流程，下一步進 S06 ④A Low-fi；所有 S01–S06 / O01–O05 Low-fi完成後，再進 Cross-Screen Review → High-fi Design System → ④B High-fi。
