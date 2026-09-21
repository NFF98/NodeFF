# Phase 1 Screen Inventory

> 狀態：WORKING UI/UX BASELINE
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
| S01 | Discover / Start | 從想法或靈感開始 Create | F00 | **LOW_FI_DIRECTION_APPROVED** |
| S02 | Create Workspace | 分析、補充必要資訊、確認假設並生成 App | F00 + F01 | **LOW_FI_DIRECTION_APPROVED** |
| S03 | App / Runtime | 使用生成 App，進入 Share / Remix / Correct | F00 + F03 | **LOW_FI_DIRECTION_APPROVED** |
| S04 | Shared App Entry / Restore | 從分享連結恢復並立即使用 App | F05 + F00 | **LOW_FI_DIRECTION_APPROVED** |
| S05 | Refine / Remix Workspace | 修改既有 App、Preview child、決定是否採用 | F06 + F00 | **LOW_FI_DIRECTION_APPROVED** |
| S06 | Correction Compare | 比較修正前後並 Accept / Keep / Adjust | F16 + F00 | **LOW_FI_DIRECTION_APPROVED** |

目前 S01–S06 Main Screens 已全部完成 Low-fi 方向確認；下一階段進 O01–O05 Overlay / State Low-fi。

# 3. Overlay / State Inventory

| ID | Overlay / State | Host Screen(s) | Purpose | Main Function |
|---|---|---|---|---|
| O01 | Share Overlay | S03 / restored App | 建立、複製、呼叫 native share | F05 | **LOW_FI_DIRECTION_APPROVED** |
| O02 | Correction Composer | S03 | 收集自然語言 correction feedback | F16 | **LOW_FI_DIRECTION_APPROVED** |
| O03 | Recovery Overlay | S02 / S03 / S05 / S06 | 保留 context，提供 humanized next action | F12 | **LOW_FI_DIRECTION_APPROVED** |
| O04 | Revert Confirmation | S03 | 確認回到 previous/base version | F00 + F16 | **LOW_FI_REVIEW_IN_PROGRESS** |
| O05 | Loading / Building / Hydration States | S02 / S03 / S05 / S06 | 顯示非同步進度與 bounded waiting state | F00 + related Fxx |

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
→ High-fi Design System
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

# 9. Next

下一個 Review：

> **O04 — Revert Confirmation Low-fi**

它將承接：
S03 Previous Version / Revert → confirm target / input restoration semantics → fresh previous Runtime or safe cancel。
