# appf2 Detailed Design

> Canonical role：implementation-facing **Product Design truth**。這裡定義 What / Why / When / observable correctness；不定義 Cursor / CI / Sprint / Release execution mechanics。

## Canonical Owners

~~~text
APP-DETAILED-DESIGN-OVERVIEW.md
→ Function portfolio / dependency / phase / release scope

data-model/DATA-MODEL-DETAILED.md
→ detailed durable/browser data contracts across phases

infrastructure/INFRASTRUCTURE-DETAILED.md
→ detailed infrastructure activation across phases

functions/Fxx-*.md
→ one end-to-end canonical Function design per Function

UI-UX/
→ screen / overlay / responsive / presentation truth

registries/
→ machine-readable Acceptance / Evidence / Recovery Product contracts
~~~

## Phase Rule

Phase 是 applicability / activation metadata，不是 folder boundary。

同一 canonical file 可以包含 future Phase section；只有 Evidence + Human approval + Build Freeze inclusion 才成為 implementation scope。

## Build Boundary

Detailed Design 可以指定：
- Product behavior；
- API / Data / Runtime contract；
- UI state / presentation；
- Error / Recovery；
- Security / Privacy；
- Evidence semantics；
- Acceptance / expected observable。

Detailed Design 不指定：
- Cursor task mechanics；
- test file placement / fixture implementation；
- CI job；
- Sprint lifecycle；
- release / deploy procedure。

上述 Build execution authority 位於 `NFF98/appf2-build`。

## Review Rule

Working Content Quality Review = **Cleanup + Completeness**，canonical rule：
`working/common-core/DESIGN-TO-DELIVERY.md#23-working-content-quality-review--build-freeze-migration-rule`。
