# appf2 Working — Human Navigation

> `working/` = appf2 唯一可修改的 Product Design Current Truth。
>
> 結構狀態：**STRUCTURE_READY / CONTENT_REVIEW_PENDING**
>
> 目前只代表目錄與 semantic ownership 結構已定案；內容仍需進行 Quality Review / Dedup / Consistency Audit。尚未達到 Build Freeze。

## Canonical Structure

```text
working/
├─ README.md
├─ DESIGN-WORKBENCH.md
│
├─ common-core/
│  ├─ APP-ARCHITECTURE.md
│  ├─ BUSINESS-PLAN.md
│  ├─ CAPABILITY-FABRIC.md
│  ├─ DATA-MODEL.md
│  ├─ INFRA-ARCHITECTURE.md
│  ├─ TECHNICAL-MOAT.md
│  ├─ API-CONVENTIONS.md
│  ├─ ACCEPTANCE-CONVENTIONS.md
│  ├─ EXECUTION-ADMISSION.md
│  └─ DESIGN-TO-DELIVERY.md
│
└─ detailed-design/
   ├─ README.md
   ├─ APP-DETAILED-DESIGN-OVERVIEW.md
   ├─ data-model/
   │  └─ DATA-MODEL-DETAILED.md
   ├─ infrastructure/
   │  └─ INFRASTRUCTURE-DETAILED.md
   ├─ functions/
   ├─ UI-UX/
   └─ registries/
```

## Ownership Rule

### Common Core

`working/common-core/` 放跨 Phase 共用、長期沿用的原則、邊界與 shared contract。

Common Core 不因 Phase 1 / 2 / 3 / 4 複製。

### Detailed Design

`working/detailed-design/` 放 implementation-facing 的詳細設計。

Functions、UI/UX、Registries 依 semantic owner 維持單一 canonical truth，不按 Phase 複製。

Data Model / Infrastructure 的詳細內容也以單一 detailed owner 管理；Phase 只作為 scope / applicability / activation metadata，不自動形成 folder boundary。

### Design Workbench

`working/DESIGN-WORKBENCH.md` 只作為尚未決定、尚未有 canonical owner、或 evidence-gated 的暫存討論區。

它不是 Product Design SSOT，也不是 Build Spec source。

## Build Boundary

```text
appf2 Working
→ Content Quality Review / Dedup
→ Cross-file Consistency / Acceptance / UI Audit
→ Human approval
→ Build Freeze
→ appf2-build immutable BS-*
→ Backlog / Sprint / Cursor / Test / Evidence / Release
```

appf2-build 負責 implementation / delivery governance；appf2 不重複維護 Cursor execution rules。

## Current Next Step

1. 逐檔 Content Quality Review。
2. Dedup：同一 semantic truth 只能留在一個 canonical owner。
3. 修正 cross-reference / ownership / consistency。
4. 確認 Phase 1 Build Freeze set。
5. User 批准後才建立 appf2-build locked baseline。

> **Structure Ready ≠ Content Ready ≠ Build Freeze Ready。**
