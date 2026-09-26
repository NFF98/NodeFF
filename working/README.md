# appf2 Working — Human Navigation

> `working/` = appf2 唯一可修改的 Product Design Current Truth。
>
> 狀態：**STRUCTURE_READY / CONTENT_REVIEW_COMPLETE / FINAL_AUDIT_PENDING**
>
> 2026-09-26 已完成 STEP 2 Working Content Quality Review：Cleanup + Completeness。已處理 stale authority/path、retired governance、Design↔Build ownership、phase consolidation、registry metadata、closed delta reconciliation 與可直接判定的內容缺口；尚未 Human-approved Build Freeze。

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

STEP 2 已完成；下一個 gate 不再重做內容清理，而是 Final Audit / Build Freeze sequence：

1. Cross-file consistency re-audit。
2. Acceptance mapping audit。
3. UI/UX consistency audit。
4. Registry integrity audit。
5. 確認 Phase 1 Build Freeze inventory。
6. User 明確批准後才建立 appf2-build locked baseline。

Working Review / migration 規則：`working/common-core/DESIGN-TO-DELIVERY.md#23-working-content-quality-review--build-freeze-migration-rule`。

> **Structure Ready ≠ Content Ready ≠ Build Freeze Ready。**
