# NodeFF

NodeFF 是一個 No-install、Everyone-is-creator、Sharable/Linkable、Intent Commerce、Fun/Social 的 Intent-to-App Runtime Platform。

## Repository Role

`NFF98/NodeFF` = **Product Design Current Truth**，負責 WHAT / WHY / WHEN。

唯一可修改的 Product Design Current Truth：

```text
working/
```

主要入口：
- Top Architecture：`working/APP-ARCHITECTURE.md`
- Function Portfolio：`working/APP-DETAILED-DESIGN-OVERVIEW.md`
- Shared Data：`working/DATA-MODEL.md`
- Shared API：`working/API-CONVENTIONS.md`
- Execution Admission：`working/EXECUTION-ADMISSION.md`
- Acceptance/Test Conventions：`working/ACCEPTANCE-CONVENTIONS.md`
- Function Details：`working/functions/Fxx-*.md`
- UI/UX：`working/UI-UX/`
- Machine-readable Registries：`working/registries/`

## Build / Delivery Boundary

Approved Product Design 不在 NodeFF 內再複製成 Formal Spec。

```text
NodeFF working/
→ consistency / delta / acceptance / UI audit
→ Human approval
→ Build Freeze
→ NFF98/NFFBuild/build-spec/baselines/BS-*
→ backlog / sprint / Cursor / test / evidence / release
```

`NFF98/NFFBuild` = implementation / delivery authority。

## Retired Structures

- `spec/`：**RETIRED / NO-USE**。Preservation Audit 已確認 Current Working 完整覆蓋舊 Formal Spec；目錄已移除。
- `execution/`：**RETIRED / NO-USE**。Execution 已完整移至 `NFF98/NFFBuild`。

歷史文件若仍出現 `spec/`、Formal Spec、Working → Spec、Spec Promotion、Formal Spec Refresh 等字樣，只代表當時的歷史治理模型，不是 Current Truth。

## Decisions

Architecture / product-impacting decisions 記錄於 `decisions/`。
