# NodeFF Shadow Truth Audit — 2026-09-25

> **AUDIT EVIDENCE ONLY / NO CURRENT AUTHORITY**
>
> Purpose：證明 `DESIGN-WORKBENCH.md`、`DECISION-CANDIDATES.md`、`OPEN-QUESTIONS.md` 不承載未被 canonical Working 吸收的已批准 Product Truth；只留下真正 unresolved / evidence-gated items。

## Audit Baseline

- Repository：NFF98/NodeFF
- Branch：main
- Audited HEAD：3eda549759fa36c59bc016245eb2a01877bf4c77
- Current Product Design Truth：`working/`
- Delivery boundary：NodeFF Working → Human-approved Build Freeze → NFFBuild locked BS-*

## 1. DESIGN-WORKBENCH — Section → Canonical Owner Proof

| Audit Group | Workbench Content | Result | Canonical Owner / Proof |
|---|---|---|---|
| WB-01 | Anonymous-first + Evidence + future Identity | SYNCED | `working/ProjectManagement/BUSINESS-PLAN.md`; `working/DATA-MODEL.md`; F07; F08 |
| WB-02 | Idea / Need → App; Wedge is not product boundary; 「意圖就是 App」 | SYNCED | `working/APP-ARCHITECTURE.md`; `working/ProjectManagement/BUSINESS-PLAN.md` |
| WB-03 | Architecture document responsibility restructuring | SYNCED | APP-ARCHITECTURE / APP-DETAILED-DESIGN-OVERVIEW / INFRA-ARCHITECTURE / CAPABILITY-FABRIC / functions |
| WB-04 | PENDING-FUNC-001 Capability Card expansion | SYNCED | `working/ProjectManagement/CAPABILITY-FABRIC.md`; APP-DETAILED-DESIGN-OVERVIEW |
| WB-05 | PENDING-FUNC-002 Infrastructure baseline | SYNCED | `working/INFRA-ARCHITECTURE.md`; APP-DETAILED-DESIGN-OVERVIEW |
| WB-06 | PENDING-FUNC-003 Experience Shell / Model Gateway / Capability Gap / Recovery | SYNCED | APP-ARCHITECTURE; F01/F02/F03/F04/F12 |
| WB-07 | S01 UI/UX review notes / brand / progress presentation | SYNCED / HISTORICAL | `working/UI-UX/screens/S01-DISCOVER-START.md`; DESIGN-SYSTEM; O05 |
| WB-08 | Future Share Modes Boundary | SYNCED | INFRA-ARCHITECTURE §9; F05; F09 |
| WB-09 | Runtime Global Loading + Timeout | SYNCED | F00; F03; F12; O05; recovery/evidence/acceptance registries |
| WB-10 | 2026-09-21 / 2026-09-22 session closeout and next-step notes | HISTORICAL | No product authority; superseded by current Working |
| WB-11 | PENDING-FUNC-004 F01 Creation Progress | SYNCED / CLOSED | F01; F00; O05; acceptance-test registry |
| WB-12 | LLM Proposal ≠ READY Truth / bounded retry / deterministic validation / independent READY | SYNCED | APP-ARCHITECTURE guardrails; F02 deterministic validation; F03 READY + timeout + commit guards; F12 bounded retry/recovery |
| WB-13 | Mid-term Layer 4 exact split: 4A UI / 4B Logic / 4C Data / 4D Capability Runtime | PARTIAL ORPHAN | General L4 expansion exists in APP-ARCHITECTURE, but exact 4A–4D partition is not canonical elsewhere |
| WB-14 | Mid-term Layer 3 exact split: 3A UI / 3B Logic / 3C Data / 3D Capability / 3E Runtime Safety + “No Runtime Capability Without Contract Coverage” | PARTIAL ORPHAN | Phase 1 validation coverage exists in F02, but exact future 3A–3E architecture and invariant are not canonical elsewhere |

### Workbench Gate

- Approved / closed content with canonical owner: PASS
- Historical session material identifiable: PASS
- Unique unresolved Product Truth: **2 partial-orphan architecture groups (WB-13, WB-14)**
- Therefore Workbench cannot yet be fully archived/deleted until WB-13 / WB-14 are either:
  1. absorbed into canonical Architecture; or
  2. explicitly demoted to non-approved discussion.

## 2. DECISION-CANDIDATES

### DC-001 — Rule Representation

**RESOLVED / STALE AS OPEN DECISION**

Canonical proof:
- F02 explicitly uses pure Expression AST.
- F02 forbids free-form expression string.
- F03 implements pure typed Expression / Rule VM.

Conclusion：remove from active Decision Gates.

### DC-002 — Capability Registry Source Format

**RESOLVED / STALE AS OPEN DECISION**

Canonical proof:
- F04 defines One Canonical Registry Source.
- Canonical source is versioned code artifact (`capability-definition.ts`, registry + generator).
- Deterministic generated outputs include compiler catalog, validator registry, runtime registry and compatibility manifest.
- CAPABILITY-FABRIC independently confirms “Versioned canonical source → generated artifacts”.

Conclusion：remove from active Decision Gates.

### Decision Gate Result

**Active unresolved decisions in current DECISION-CANDIDATES = 0**

The file may remain as an empty decision-gate template or be removed after governance cleanup.

## 3. OPEN-QUESTIONS

### OQ-001 — Phase 1 strongest Use Case Wedge

**KEEP OPEN / EVIDENCE-GATED**

Business Plan deliberately treats current categories as wedges, not product boundary. Real usage evidence is required.

### OQ-002 — Phase 1 Capability Set size

**NARROW, NOT DELETE**

Already resolved:
- high composition density over raw capability count;
- Phase 1 candidate capability families;
- Build ≠ Validated;
- core capabilities should progress to TESTED / VALIDATED based on evidence.

Still open:
- exact release subset / which candidate capabilities earn sufficient evidence for release.

Recommended rewritten question:
> Which Phase 1 candidate capabilities should enter the release set after TESTED / VALIDATED evidence, and what evidence threshold is sufficient?

### OQ-003 — Is Realtime required in Phase 1?

**RESOLVED / DELETE FROM OPEN QUESTIONS**

Proof:
- F09 = 2–3 month, DEFERRED / Evidence-gated.
- INFRA-ARCHITECTURE explicitly says Realtime is not a Phase 1 dependency.

### OQ-004 — Portable Snapshot vs Durable Reference switching threshold

**RESOLVED FOR PHASE 1 / DELETE FROM OPEN QUESTIONS**

Proof:
- INFRA-ARCHITECTURE: Production default = Mode B / DURABLE_REFERENCE.
- Mode A = optional experiment, not Release 1 blocker.
- Mode C = deferred to F09.

Future tuning can be evidence-driven without remaining a Phase 1 design blocker.

### OQ-005 — When is Semantic Reuse worth investing in?

**KEEP OPEN / EVIDENCE-GATED**

Current architecture intentionally waits for repetition rate, compilation cost, mismatch and reuse-correctness evidence before pgvector / richer semantic reuse.

### OQ-006 — Anonymous Evidence retention / privacy policy

**NARROW, NOT DELETE**

Already resolved:
- raw product event retention = 90 days;
- raw intent / result value retention = 30 days;
- local draft = 7 days;
- debug raw payload max 7 days;
- explicit deletion/anonymization policy required;
- anonymous ID is not authorization or ownership proof.

Still open:
- user-facing notice / consent boundary;
- explicit privacy reset UX;
- research-use governance / secondary-use policy;
- jurisdiction-driven policy changes if required.

Recommended rewritten question:
> What user-facing notice / consent / privacy-reset and secondary-use governance is required for Phase 1 anonymous evidence?

## 4. Final Shadow Truth Gate

```text
Workbench approved truth with owner         PASS
Workbench historical-only sections          IDENTIFIED
Workbench unresolved orphan truth           2 groups

Decision Candidates stale decisions         2
Decision Candidates real open decisions     0

Open Questions real evidence-gated          OQ-001, OQ-005
Open Questions to narrow                     OQ-002, OQ-006
Open Questions resolved                      OQ-003, OQ-004
```

## 5. Human Decisions Still Required

Only two Product Architecture decisions require explicit human disposition before Workbench can be fully cleaned:

### HD-01 — Mid-term Layer 4 exact architecture

Choose one:
- **ABSORB** exact 4A UI / 4B Logic / 4C Data / 4D Capability Runtime split into canonical APP-ARCHITECTURE as future architecture; or
- **DEMOTE** this exact split to discussion and retain only the broader canonical L4 Universal Runtime evolution.

### HD-02 — Mid-term Layer 3 exact architecture

Choose one:
- **ABSORB** exact 3A UI / 3B Logic / 3C Data / 3D Capability / 3E Runtime Safety validation split + “No Runtime Capability Without Contract Coverage” into canonical APP-ARCHITECTURE; or
- **DEMOTE** the exact split to discussion and retain only existing F02 / architecture validation principles.

Everything else can be mechanically cleaned after HD-01 / HD-02 without further product decision.
