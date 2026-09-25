# NodeFF Working — Human Navigation

> `working/` = NodeFF 唯一可修改 Product Design Current Truth。

## 先分兩類看

### 1. Common Core
`working/core/`

跨 Phase 共用、不應每一 Phase 重複的核心：
- App / Infra Architecture
- Data invariants
- Business thesis
- Capability contract
- API / Acceptance conventions
- Execution Admission
- Design-to-Delivery governance
- Technical Moat

### 2. Phase / Detailed Modules
- `architecture/evolution/` — 每 Phase architecture additions
- `data-model/` — 每 Phase data contract / delta
- `infrastructure/` — 每 Phase infra activation
- `roadmap/product/` — 每 Phase product / business roadmap
- `roadmap/capability/` — 每 Phase Capability roadmap
- `functions/` — Function detailed design
- `UI-UX/` — Screen / Overlay detailed design
- `registries/` — machine-readable contracts
- `DESIGN-WORKBENCH.md` — temporary discussion only

## Growth Rule

```text
Common Core
+ Phase 1 module
+ Phase 2 delta
+ Phase 3 delta
+ Phase 4+ delta
```

不建立 Phase 2 的整套 Working copy。

Future / deferred Phase file 存在，也不代表 implementation scope。

真正每 Phase frozen copy 在 NFFBuild：`BS-P1-001`, `BS-P2-001`...

## Phase 1 Build Freeze Current Set

Phase 1 Build Freeze 最終 review 使用：
- `core/` shared truth
- `architecture/evolution/PHASE-1.md`
- `data-model/PHASE-1.md`
- `infrastructure/PHASE-1.md`
- `roadmap/product/PHASE-1.md`
- `roadmap/capability/PHASE-1.md`
- Phase 1 Functions / UI-UX / Registries
