# appf2 Working — Human Navigation

> `working/` = appf2 唯一可修改的 Product Design Current Truth。
>
> 狀態：**STRUCTURE_READY / CONTENT_REVIEW_COMPLETE / FINAL_AUDIT_COMPLETE / HUMAN_APPROVAL_PENDING**
>
> 2026-09-26 已完成 STEP 2 Working Content Quality Review 與 Final Audit。Final Audit 已完成 Cross-file Consistency、Acceptance Mapping、UI/UX Consistency、Registry Integrity 與 Phase 1 Build Freeze Inventory；目前沒有已知 Phase 1 Build Freeze blocker。尚未 Human-approved Build Freeze。

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

## Final Audit Result — 2026-09-26

Final Audit 結論：**PASS / HUMAN APPROVAL REQUIRED BEFORE BUILD FREEZE**。

已驗證：
- 53 / 53 Working text / JSON：0 stale path、0 retired pending lifecycle、0 duplicate heading。
- Phase 1 Functions：`F00 F01 F02 F03 F04 F05 F06 F07 F12 F16` 全部維持 `BUILD_FREEZE_READY / STEP2_REVIEWED`。
- Acceptance Registry：285 entries；284 ACTIVE + 1 SUPERSEDED；Acceptance ID / Test ID unique；proof scope合法。
- Phase 1 Function ↔ Acceptance / Event / Error Registry：0 missing / 0 orphan。
- Recovery Registry：所有引用的 `F12-POL-*` 都有 canonical definition。
- UI/UX：S01–S06 + O01–O05 cross-screen truth一致；11 / 11 approved PNG SHA unchanged。
- Phase scope：Phase 2 = F08/F09/F10 + evidence-unlocked Creator / PMF work；F11/F13/F14/F15/F17 = Phase 3+ deferred / evidence-gated。
- 日期本身不 unlock任何 deferred Function。

Final Audit 修正的 material / structural findings：
1. F13 entitlement / metering 從舊 2–6 月混合 scope 完整收回 Phase 3+。
2. Business / Capability appendix 與 Detailed Overview 的 stale canonical references修正。
3. S06 舊 execution-boundary wording收斂回 Human-approved Build Freeze boundary。

## Phase 1 Build Freeze Candidate Inventory

Build Freeze **不是複製全部 Working**。目前 candidate 共 **47 個 source artifacts**：

### Include / Project into locked Build Spec

- Shared implementation truth（7）：`APP-ARCHITECTURE.md`、`CAPABILITY-FABRIC.md`、`DATA-MODEL.md`、`INFRA-ARCHITECTURE.md`、`API-CONVENTIONS.md`、`ACCEPTANCE-CONVENTIONS.md`、`EXECUTION-ADMISSION.md`。
- Scope owner（1）：`working/detailed-design/APP-DETAILED-DESIGN-OVERVIEW.md` 的 Phase 1 scope。
- Detailed Data / Infrastructure（2）：只投影 Phase 1 section，不把 future Phase sections帶入 implementation。
- Phase 1 Functions（10）：`F00 F01 F02 F03 F04 F05 F06 F07 F12 F16`。
- UI/UX（24）：13 個 textual contracts + 11 個 approved reference PNG。
- Machine-readable registries（3）：Acceptance / Evidence / Recovery。

### Reference-only / Do Not Copy as Build Spec Truth

- `working/common-core/BUSINESS-PLAN.md`
- `working/common-core/TECHNICAL-MOAT.md`
- `working/common-core/DESIGN-TO-DELIVERY.md`
- `working/README.md`
- `working/DESIGN-WORKBENCH.md`
- Deferred Functions：`F08 F09 F10 F11 F13 F14 F15 F17`
- Data / Infrastructure 的 Phase 2 / 3 / 4+ sections

這些可供 provenance / strategy / future design參考，但不得因同 repo存在就自動進 Phase 1 implementation baseline。

## Current Next Step

只剩 Human Gate：

1. User Review Final Audit result。
2. User 明確批准 **Phase 1 Build Freeze**。
3. 才把上述 approved Phase 1 truth投影為 `NFF98/appf2-build` 第一個 immutable `BS-*` baseline。
4. Build Freeze 後才進 Backlog → Sprint → Cursor → Test → Evidence → Release。

> **Final Audit Complete ≠ Build Freeze。沒有 Human approval，不建立 appf2-build baseline。**
