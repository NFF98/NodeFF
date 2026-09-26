# appf2 Working Registries

> **CURRENT AUTHORITY：appf2 Working machine-readable Product Design contracts**

本目錄維護：
- `recovery-registry.json`
- `evidence-event-registry.json`
- `acceptance-test-registry.json`

## Ownership Rules

1. Registry 必須對應 canonical Working Function / Shared contracts。
2. Registry 不得自行發明 Product semantics。
3. Stable ID 不重用；superseded / deprecated 必須保留 traceability。
4. Phase / deferred content 不因出現在 registry 自動成為 Build Freeze scope。
5. Build Freeze 時，只投影 Human-approved scope 與 source commit 到 `NFF98/appf2-build/build-spec/baselines/BS-*`。

## Registry Boundaries

### Acceptance Registry

Design-owned：
- Acceptance ID / Function ID；
- criterion / expected observable；
- stable Test ID mapping；
- proof scope；
- active / superseded lifecycle；
- required-for-Build-Freeze truth。

Build-owned，不得放在 Design registry：
- fixture strategy；
- test file / implementation location；
- runner / framework；
- CI job；
- execution result / evidence artifact placement。

### Evidence Registry

擁有 event identity、allowed properties、privacy / retention semantics與 metric meaning；collector / pipeline / storage implementation由 Build決定。

### Recovery Registry

擁有 source error → recovery policy mapping、severity、retryability、consumer action semantics；UI presentation仍由 F00 / O03等 UI owner承接，implementation mechanics由 Build決定。

## Validation

Build Freeze 前至少驗證：
- IDs unique；
- Function ↔ Registry 無 orphan；
- owner path存在；
- deprecated / superseded traceability完整；
- forbidden raw payload boundary未被放寬。
