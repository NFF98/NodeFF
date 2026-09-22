# Phase 1 Screen Inventory

> 狀態：WORKING UI/UX — LOW-FI + CROSS-SCREEN APPROVED / HIGH-FI DIRECTION A APPROVED / S01–S03 ④B HIGH-FI APPROVED / S04 ④B NEXT
>
> 目的：管理 Phase 1 的 Screen / Surface 地圖、Screen-level UX Review 狀態與畫面之間的關係。
>
> **Canonical Boundary：**
> - 本目錄擁有 Screen composition、visual hierarchy、responsive behavior、presentation mapping、Low-fi / High-fi UI decision。
> - `working/functions/Fxx-*.md` 仍擁有 Function behavior、state semantics、API、Data、Runtime、Error、Security、Evidence 與 Acceptance。
> - Screen 文件不得自行發明新的 Function behavior；若畫面設計需要改產品行為，必須回到相關 Fxx Working Design Review。
> - 目前文件仍屬 Working，不是 Cursor implementation authority。

# 1. Phase 1 Screen Model

Phase 1 目前採 **6 個主要 Screen / Surface + 5 類 Overlay / State**。

原則：

> Screen 是 User 的主要工作空間；Overlay / State 是在不離開主要工作空間的情況下，暫時完成一件事或呈現狀態。

# 2. Main Screens

| ID | Screen / Surface | Primary User Outcome | Main Function Sources | Screen Design Status |
|---|---|---|---|---|
| S01 | Discover / Start | 從想法或靈感開始 Create | F00 | **④A LOW_FI_APPROVED / ④B HIGH_FI_APPROVED** |
| S02 | Create Workspace | 分析、補充必要資訊、確認假設並生成 App | F00 + F01 | **④A LOW_FI_APPROVED / ④B HIGH_FI_APPROVED** |
| S03 | App / Runtime | 使用生成 App，進入 Share / Remix / Correct | F00 + F03 | **④A LOW_FI_APPROVED / FUNCTION_DELTA_CLOSED / ④B HIGH_FI_APPROVED** |
| S04 | Shared App Entry / Restore | 從分享連結恢復並立即使用 App | F05 + F00 | **LOW_FI_DIRECTION_APPROVED** |
| S05 | Refine / Remix Workspace | 修改既有 App、Preview child、決定是否採用 | F06 + F00 | **LOW_FI_DIRECTION_APPROVED** |
| S06 | Correction Compare | 比較修正前後並 Accept / Keep / Adjust | F16 + F00 | **LOW_FI_DIRECTION_APPROVED** |

目前 S01–S06 Main Screens 與 O01–O05 Overlay / State 的 ④A Low-fi direction均已完成 User Review；S03/O05 的 Runtime Global Loading + Timeout F00/F03/F12 Function Delta也已閉合。Cross-Screen Consistency Review 已於 2026-09-22 完成；下一個 gate 是 High-fi Design System → ④B High-fi。

# 3. Overlay / State Inventory

| ID | Overlay / State | Host Screen(s) | Purpose | Main Function |
|---|---|---|---|---|
| O01 | Share Overlay | S03 / restored App | 建立、複製、呼叫 native share | F05 | **LOW_FI_DIRECTION_APPROVED** |
| O02 | Correction Composer | S03 | 收集自然語言 correction feedback | F16 | **LOW_FI_DIRECTION_APPROVED** |
| O03 | Recovery Overlay | S02 / S03 / S05 / S06 | 保留 context，提供 humanized next action | F12 | **LOW_FI_DIRECTION_APPROVED** |
| O04 | Revert Confirmation | S03 | 確認回到 previous/base version | F00 + F16 | **LOW_FI_DIRECTION_APPROVED** |
| O05 | Loading / Building / Hydration States | S02 / S03 / S04 / S05 / S06 / O02 / O03 / O04 | 顯示非同步進度與 bounded waiting state | F00 + related Fxx | **LOW_FI_DIRECTION_APPROVED — FUNCTION_DELTA_CLOSED** |

Overlay / State 預設不建立獨立 route，也不應讓 User 無故失去目前 App / draft / comparison context。

# 4. Phase 1 Primary Flow

~~~text
S01 Discover / Start
↓
S02 Create Workspace
↓
S03 App / Runtime
├─ O01 Share
├─ O02 Correct → S06 Correction Compare
├─ S05 Refine / Remix
└─ O03 Recovery

Shared recipient：
S04 Shared App Entry / Restore
↓
S03 App / Runtime
↓
可進 S05 Remix
~~~

# 5. UI/UX Design Process — Mandatory

Phase 1 UI/UX 必須固定走以下 6 步，不得跳步、混步或提前升格：

1. **抽出現有 UX**：從 F00 / F05 / F06 / F12 / F16 等既有 Function contracts 整理所有畫面、狀態與互動。
2. **建 Screen Inventory**：列出 S01、S02…每個 Screen / Overlay 的目的、入口、出口與主要 Function source。
3. **補缺口**：找出 Spec / Function 已有 behavior，但尚未有具體畫面承接的位置。
4. **分兩大階段確認**：先完成所有 Screen / Overlay 的 ④A Low-fi，再統一進 ④B High-fi。
   - **④A Low-fi**：逐頁確認版面、資訊層級、CTA、流程、states、Desktop / Mobile；**不討論顏色與品牌視覺**。
   - **④B High-fi**：全部 Low-fi 完成並做 Cross-Screen Review 後，才統一確認顏色、字體、間距、圓角、陰影、動畫、Hover / Loading 效果、品牌風格、Desktop / Mobile 視覺一致性與 Design System。
5. **User 批准後**：才整理成 UI/UX Working Design baseline。
6. **最後再問 User 是否升 Spec**：沒有 User 明確批准，不得 promotion 到 formal Spec。

硬規則：
- 單一 Screen 的 Low-fi 未確認，不得把該 Screen 標為 LOW_FI_DIRECTION_APPROVED。
- **所有 S01–S06 / O01–O05 Low-fi 未完成前，不得開始任何 Screen 的 ④B High-fi。**
- High-fi 未確認，不得標記完整 UI/UX Working Baseline。
- Working UI/UX 未完成 Cross-Screen Review，不得詢問 Spec promotion。
- 顏色 / 效果 / 風格屬於 **④B High-fi**，不得在 ④A Low-fi 當成 approval blocker。
- Screen-level visual design 不得自行改寫 Function behavior semantics。

## 5.1 ④B High-fi Mandatory Step Gates

每一個 Screen / Overlay 的 ④B High-fi 必須逐層鎖定並**當下寫回對應 Working 文件 + Git commit**；只在 Chat 中口頭確認不算完成。

固定流程：

~~~text
Step 1 — Structure Lock
→ Step 2 — Geometry + Visual Hierarchy Lock
→ Step 3 — Detailed High-fi Visual Rules Lock
→ Step 4 — Final Visual Reference Lock
→ Working Baseline
~~~

### Step 1 — Structure Lock

至少鎖定：
- screen regions / sections；
- navigation / header / footer / bottom nav；
- primary / secondary CTA placement；
- conditional surfaces；
- overlay relationship；
- Function handoff入口；
- 哪些 element 明確不存在。

### Step 2 — Geometry + Visual Hierarchy Lock

至少鎖定：
- Header / nav / panel / content主要尺寸範圍；
- max-width / padding / gap / content flow；
- Desktop / Mobile composition；
- attention hierarchy；
- fixed / sticky / scroll behavior；
- safe-area / keyboard / bottom-control collision rule；
- responsive collapse / stacking。

### Step 3 — Detailed High-fi Visual Rules Lock

至少鎖定：
- Design System token套用；
- color / border / accent / surface usage；
- typography hierarchy；
- radius / elevation；
- component states；
- hover / focus / pressed / disabled / loading；
- progress / motion / reduced-motion；
- overlay visual family；
- accessibility；
- Cursor visual guardrails；
- UI ↔ Function eligibility / state truth不得由 Screen猜測。

### Step 4 — Final Visual Reference Lock

必須：
1. User明確批准 final Desktop / Mobile visual；
2. Approved PNG存入 `working/UI-UX/references/`；
3. Screen / Overlay文件 embed canonical image path；
4. 明文記錄 image boundary：圖片不覆蓋文字 contract / Fxx Function truth；
5. 更新 Screen Inventory status；
6. 有 commit可追溯。

### Optional Step 4.5 — Additional Layer Detail

若 Step 4後發現 Cursor仍需要額外一層細節，例如：
- component anatomy；
- complex state matrix；
- interaction timeline；
- overlay stacking；
- animation frame / timing；
- data-to-UI mapping；
- capability-specific responsive contract；

則新增：

~~~text
Step 4.5 — <Layer Name> Lock
~~~

Rules：
- Step 4.5不是偷改已批准 Step 1–4。
- 若它改變既有 Structure / Geometry / Visual Rule / Function semantics，必須 reopen對應 Step，而不是只追加 4.5。
- 若涉及 Function behavior，回相關 Fxx Working Delta Review。
- Step 4.5同樣必須 User批准 + Git commit。

### Hard Gate

> **沒有 Step 1–4（以及需要時的 Step 4.5）GitHub Current Truth，不得把該 Screen / Overlay交給 Cursor實作。**

每一 Step 的 approved內容必須落在該 Screen / Overlay canonical Working文件；不能只依 chat history或只依 final mockup。

每個 Screen 的 Low-fi 至少確認：

1. User 到這裡要完成什麼。
2. 主要資訊區塊與 visual hierarchy。
3. Primary / Secondary CTA。
4. Loading / Empty / Error / Recovery / Disabled state。
5. Desktop / Mobile responsive behavior。
6. Overlay / modal / navigation relationship。
7. Accessibility baseline。
8. 與 Fxx Contract 是否一致。

# 6. Visual Design Sequence

Phase 1 採 **Low-fi 全貌優先**：先把所有 Screen / Overlay 的骨架與互動關係走完，再統一建立 High-fi Design System，避免前面頁面因後續共用元件 / Overlay / Navigation 發現而反覆重做。

~~~text
S01–S06 + O01–O05 ④A Low-fi
→ Cross-Screen consistency review
→ High-fi Design System — Direction A Foundations APPROVED
→ S01–S06 + O01–O05 ④B High-fi
→ Final Review
~~~

目前 High-fi 方向已有 Working note：

- 主色探索：Tiffany Blue → Yellow direction。
- 必須形成 NodeFF 自己的 brand system，不複製其他品牌識別。
- 介面優先乾淨、低干擾。
- Must not resemble Google / Search UI。
- 生成流程應探索 visible stage-based progress，而非只有 generic spinner。

詳細 Working discussion：`working/DESIGN-WORKBENCH.md`。

# 7. Canonical Ownership Guardrail

若 Screen 文件與 Function 文件發生衝突：

- Layout / visual / responsive presentation → 本 UI/UX Screen 文件先作 Working owner。
- Product behavior / state semantics / API / Data / Runtime / Error / Security → Fxx 文件為 owner。
- 若 visual decision 需要新增或改變 behavior，必須先建立 Fxx delta 並 Review，不能只靠 Screen 文件偷改產品行為。

# 7.1 Cross-Screen Consistency Baseline — Approved

2026-09-22 Cross-Screen Consistency Review 已確認以下共用 Low-fi 規則：

## Navigation Scope

- **S01 Discover / Start 與 S03 App / Runtime 都可使用 NodeFF permanent bottom navigation，但 navigation scope 不同。**
- S01 Mobile bottom navigation固定為：`首頁 / 探索靈感 / 我的 App · Soon`，不放 Create / Profile；Create只由 S01 Creator Composer提供。
- S03 App / Runtime bottom navigation仍依 Runtime scope管理，不因 S01 navigation而新增重複 Create入口。
- S04 Restore 尚未進入 Runtime，不顯示 permanent bottom navigation；READY 後才由 S03 接管。
- S05 Refine / Remix 與 S06 Correction Compare 是 focused decision workspace，不繼承 S03 permanent bottom navigation。
- S05 / S06 使用自己的 Back / View / Decision CTA，不把 S03 shell navigation 帶進決策流程。

## Overlay Layering

- O01 / O02 / blocking O03 / O04 active 時，underlying S03 Shell controls 與 bottom navigation 必須 inert / unavailable。
- Overlay close 後 focus 回合理 trigger / safe surface。
- O03 inline / node-level Recovery 不是 blocking overlay，不需停用整個 S03。
- Overlay 不得清掉 App、draft、inputs、comparison 等 host context。

## Shared Processing Presentation

所有真實 async / bounded waiting presentation 共用 O05：

~~~text
reliable checkpoints
→ Stage label + checkpoint-derived Progress %

no reliable checkpoints
→ Stage label only
~~~

Rules：

- % 代表完成工作比例，不代表剩餘時間。
- 不 fake %。
- 不為了讓 loading 看得到而延遲真正完成。
- O01 Share creation 也納入 O05 共用 presentation。
- failure transition 仍交 source Function + O03 / F12，不由 O05 自創 recovery semantics。

## Consumer-facing Terminology

Consumer UI 優先使用：

~~~text
建立 App
修改這個 App
改成我的版本
調整結果
使用新版
使用修正版
查看原版
保留原版
~~~

Refine / Remix / Correction 可繼續作內部 Function / Working 文件術語，但一般 Consumer 不需要先理解這些英文概念。

## S06 Exit Semantics

S06 Compare 不提供模糊的「回目前 App」獨立決策出口。

- 查看原版 App / 查看修正版 App = Preview，不是 Accept / Reject。
- 保留原版 = Reject correction。
- 使用修正版 = Accept correction。
- 再調整 = 繼續 correction lifecycle。

因此不新增新的 F16 outcome / Function behavior。

---

# 8. Spec Promotion Note

舊 `spec/08-UI.md` 已淘汰，不再作 UI/UX 正式入口。

目前已記錄未來 UI/UX formal promotion target：

~~~text
spec/ui-ux/
├─ PHASE1-SCREEN-INVENTORY.md
├─ DESIGN-SYSTEM.md
├─ screens/
│  └─ Sxx-*.md
└─ overlays/
   └─ Oxx-*.md
~~~

**注意：以上 formal structure 現在尚未建立。**

只有在 S01–S06 / O01–O05 Low-fi + High-fi + Cross-Screen Review 完成，且 User 明確答覆「同意升格」後，才建立 / promotion。

需要改 product behavior 的 UI decision，仍必須同步回相關 Fxx Working → Review → Spec；UI/UX Spec不得成為第二份 Function behavior truth。

未取得 User 明確批准前，不升格、不啟動 Cursor implementation。

# 9.1 Formal Spec Freeze / Pre-Cursor Refresh

User 已確認目前策略：

- 現階段 **不更新 Formal Spec**。
- 先完成：
  1. F00/F03/F12 Runtime Loading + Timeout Working Function Delta Review（**完成：2026-09-22**）；
  2. Cross-Screen Consistency Review（**完成：2026-09-22**）；
  3. High-fi Design System / ④B High-fi（**IN PROGRESS — S01–S03 APPROVED / S04 NEXT**）；
  4. Cursor Build / Operating Model討論。
- **正式 Cursor 開發前**，再做一次短期 Formal Spec Refresh，把最後批准的 Working truth一次同步到 implementation contract。
- 在該 refresh前，Cursor implementation維持 HOLD。

# 9. Next

下一個 Review：

> **S04 — Shared App Entry / Restore ④B High-fi — NEXT**

已完成 ④B High-fi Working baseline：

- S01 — Discover / Start：**Step 1–4 CLOSED**
  - reference：`working/UI-UX/references/S01-Discover-Start-Highfi-v1.png`
- S02 — Create Workspace：**Step 1–4 CLOSED**
  - reference：`working/UI-UX/references/S02-Create-Workspace-Highfi-v1.png`
- S03 — App / Runtime：**Step 1–4 CLOSED / ARTIFACT VERIFIED**
  - text contract：`working/UI-UX/screens/S03-APP-RUNTIME.md`
  - approved reference：`working/UI-UX/references/S03-App-Runtime-Highfi-v1.png`
  - PNG blob SHA：`bfc2f2a3e8f7baa8539685cf681ab088e90c4082`。

後續 S04–S06、O01–O05 全部固定使用第 5.1 節流程：

> **Step 1 鎖結構 → Step 2 鎖 Geometry + Visual Hierarchy → Step 3 鎖 Detailed High-fi Visual Rules → Step 4 鎖圖 → 必要時 Step 4.5 鎖其他 Layer Detail。**

每一步都必須在 User批准後**立即更新對應 Working文件並 commit**，不得等整頁做完才補，也不得只留在 Chat。

Formal Spec、Backlog / Sprint 與 Cursor implementation仍維持 HOLD；待全部 ④B完成、Cursor Build / Operating Model Review完成後，再執行 pre-Cursor Formal Spec Refresh。
