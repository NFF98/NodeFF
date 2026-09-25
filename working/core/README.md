# NodeFF Common Core

> `working/core/` = **跨 Phase 共用、長期沿用的 Current Truth**。
>
> 這裡放 Phase 1 / 2 / 3 / 4 都共同遵守的核心，不放某一 Phase 的詳細新增內容。

## Core Documents

- `APP-ARCHITECTURE.md` — 系統架構、核心責任、跨 Phase guardrails
- `APP-DETAILED-DESIGN-OVERVIEW.md` — Function portfolio / dependency / release index
- `DATA-MODEL.md` — shared data invariants / phase module index
- `INFRA-ARCHITECTURE.md` — shared infrastructure principles / boundaries
- `BUSINESS-PLAN.md` — shared business thesis / KPI / strategic guardrails
- `CAPABILITY-FABRIC.md` — shared Capability contract / maturity / coverage / registry rules
- `TECHNICAL-MOAT.md` — long-term technical moat thesis
- `API-CONVENTIONS.md` — shared API contract conventions
- `ACCEPTANCE-CONVENTIONS.md` — shared acceptance / test conventions
- `EXECUTION-ADMISSION.md` — shared fresh execution admission contract
- `DESIGN-TO-DELIVERY.md` — cross-Phase design → Build Freeze → NFFBuild governance

## Not Core

Phase-specific roadmap / evolution / infra / data additions、Functions、UI-UX、Registries、Workbench、historical evidence 都不放進此目錄。

## Growth Rule

```text
Common Core
+ Phase 1 module
+ Phase 2 delta
+ Phase 3 delta
+ Phase 4+ delta
```

後一 Phase 不複製 Common Core；只新增該 Phase 的 delta / activation / migration。NFFBuild 才建立每次 immutable Build Spec snapshot。
