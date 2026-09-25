# NodeFF Working — Human Navigation

> `working/` = NodeFF 唯一可修改 Product Design Current Truth。

## 先讀這 6 個入口

1. `APP-ARCHITECTURE.md` — NFF 是什麼、系統怎麼分工
2. `APP-DETAILED-DESIGN-OVERVIEW.md` — Functions / dependency / release scope
3. `ProjectManagement/BUSINESS-PLAN.md` — 商業核心 / KPI / guardrails
4. `ProjectManagement/CAPABILITY-FABRIC.md` — NFF 能做什麼
5. `DESIGN-TO-DELIVERY.md` — 怎麼從設計進 Build Freeze / NFFBuild
6. `ProjectManagement/roadmap/PHASE-1.md` — 現在 Phase 1 要證明什麼

## Shared Core vs Phase Growth

```text
Shared / long-lived truth
├─ APP-ARCHITECTURE.md
├─ DATA-MODEL.md
├─ INFRA-ARCHITECTURE.md
├─ BUSINESS-PLAN.md
└─ CAPABILITY-FABRIC.md

Phase-specific growth
├─ architecture/evolution/PHASE-*.md
├─ data-model/PHASE-*.md
├─ infrastructure/PHASE-*.md
├─ ProjectManagement/roadmap/PHASE-*.md
└─ ProjectManagement/capability-roadmap/PHASE-*.md
```

## Growth Rule

- 同一語意只有一個 owner。
- 不建立「Phase 2 完整複製版」。
- Phase 2 只寫相對 shared core / Phase 1 的新增與改變。
- Deferred phase file 可以存在，但不等於 implementation scope。
- 真正每 Phase frozen copy 在 NFFBuild：`BS-P1-001`, `BS-P2-001`...。

## Phase 1 Build Freeze Current Set

Phase 1 Build Freeze 最終 review 會使用：

- shared core canonical Working
- `architecture/evolution/PHASE-1.md`
- `data-model/PHASE-1.md`
- `infrastructure/PHASE-1.md`
- `ProjectManagement/roadmap/PHASE-1.md`
- `ProjectManagement/capability-roadmap/PHASE-1.md`
- Phase 1 Functions / UI-UX / Registries

UI-UX / Functions / Registries 仍留到最後做 quality / tidy / consistency review。
