# appf2

appf2 是一個 No-install、Everyone-is-creator、Sharable/Linkable、Intent Commerce、Fun/Social 的 Intent-to-App Runtime Platform。

## Repository Role

`NFF98/appf2-design` = **Product Design Current Truth**，負責 WHAT / WHY / WHEN。

唯一可修改的 Product Design Current Truth：

```text
working/
```

主要入口：
- Top Architecture：`working/common-core/APP-ARCHITECTURE.md`
- Function Portfolio：`working/common-core/APP-DETAILED-DESIGN-OVERVIEW.md`
- Shared Data Invariants / Index：`working/common-core/DATA-MODEL.md`
- Phase Data Modules：`working/detailed-design/data-model/`
- Architecture Evolution：`working/common-core/APP-ARCHITECTURE.md#preserved-architecture-evolution-content`
- Infrastructure Phase Modules：`working/detailed-design/infrastructure/`
- Shared API：`working/common-core/API-CONVENTIONS.md`
- Execution Admission：`working/common-core/EXECUTION-ADMISSION.md`
- Acceptance/Test Conventions：`working/common-core/ACCEPTANCE-CONVENTIONS.md`
- Function Details：`working/detailed-design/functions/Fxx-*.md`
- UI/UX：`working/detailed-design/UI-UX/`
- Machine-readable Registries：`working/detailed-design/registries/`
- Product Roadmap：`working/common-core/BUSINESS-PLAN.md#preserved-product-roadmap-content`
- Capability Roadmap：`working/common-core/CAPABILITY-FABRIC.md#preserved-capability-roadmap-content`

## Build / Delivery Boundary

Approved Product Design 不在 appf2 內再複製成 Formal Spec。

```text
appf2 working/
→ consistency / delta / acceptance / UI audit
→ Human approval
→ Build Freeze
→ NFF98/appf2-build/build-spec/baselines/BS-*
→ backlog / sprint / Cursor / test / evidence / release
```

`NFF98/appf2-build` = implementation / delivery authority。

## Retired Structures

- `spec/`：**RETIRED / NO-USE**。Preservation Audit 已確認 Current Working 完整覆蓋舊 Formal Spec；目錄已移除。
- `execution/`：**RETIRED / NO-USE**。Execution 已完整移至 `NFF98/appf2-build`。

歷史文件若仍出現 `spec/`、Formal Spec、Working → Spec、Spec Promotion、Formal Spec Refresh 等字樣，只代表當時的歷史治理模型，不是 Current Truth。

## Archive

`archive/` 只保存歷史治理、討論與協作證據；**永遠不是 Current Truth、Build Freeze input 或 Cursor implementation authority**。



## Working Growth Rule

appf2 不為 Phase 2 / 3 / 4 複製一整套 Working 文件。

- shared / long-lived truth 留在 root canonical owner；
- phase-specific additions 放在對應 `PHASE-*.md` module；
- 後一 Phase 只寫 delta / new activation，不複製前一 Phase 全文；
- appf2-build 才建立每次 immutable `BS-Px-nnn` snapshot。
