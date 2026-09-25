# NodeFF Project Management

> 狀態：Working Project / Phase Governance。

本目錄管理 **WHY / WHEN / Phase boundary / evidence-gated roadmap**，不管理 Cursor backlog / sprint / implementation evidence。

## Canonical Files

- `BUSINESS-PLAN.md` — shared business model / principles / KPI / strategic guardrails
- `CAPABILITY-FABRIC.md` — shared Capability semantic / maturity / registry contract
- `roadmap/` — Product / Business phase-specific evolution
- `capability-roadmap/` — Capability phase-specific evolution
- `DECISION-CANDIDATES.md` — only unresolved human decision gates
- `OPEN-QUESTIONS.md` — only evidence-gated unknowns

## Phase Structure

```text
Shared Core
├─ BUSINESS-PLAN.md
└─ CAPABILITY-FABRIC.md

Phase Growth
├─ roadmap/PHASE-1..4+
└─ capability-roadmap/PHASE-1..4+
```

Rule：
- 不為 Phase 2 複製整套 ProjectManagement。
- shared 原則只寫一次。
- Phase file 只寫該階段的 target / scope / gate / new activation。
- Calendar 不自動解鎖 Phase；Evidence + Human approval 才能解鎖。
- Backlog / Sprint / Cursor / Test Evidence / Release execution 永遠由 `NFF98/NFFBuild` 承接。
