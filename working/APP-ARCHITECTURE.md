# NodeFF Application Architecture — Working Brain

> Status: WORKING / NOT OFFICIAL SSOT
>
> Purpose: Consolidated application architecture for NodeFF. This file replaces prior accumulated working notes. It is the current architecture brain for discussion and future promotion into official `spec/` only after explicit Founder approval.

---

## 1. Product Identity

NodeFF is an **Intent-to-Interactive-App Protocol and Runtime**.

A user expresses an intent in natural language. NodeFF compiles that intent into a controlled declarative Blueprint, validates it, and executes it in a trusted Universal Player.

NodeFF is **not**:
- an AI code generator;
- a platform that deploys one application per generated Micro-App;
- a general arbitrary-JavaScript runtime;
- a native-app replacement for every use case.

Core model:

```text
Intent
  ↓
Semantic Compiler
  ↓
Validated Blueprint / LegoSpec
  ↓
Universal Player
  ↓
Interactive Micro-App
```

Deployment principle:

> **NFF deploys the Runtime, not every generated App.**

---

## 2. Primary Product Loop

```text
Intent
 → Compile
 → Validate
 → Execute
 → Interact
 → Share
 → Remix / Refine
 → Reuse
```

A successful existing Blueprint should require **0 LLM calls merely to open, run, share, or replay normal deterministic interaction**.

LLM is primarily a **compile-time semantic component**, not the normal interaction runtime.

---

## 3. Four-Layer Architecture

### Layer 1 — Ingestion & Routing

Responsibilities:
- receive natural-language intent;
- safety/policy/tier gate;
- normalization;
- exact/canonical-intent cache lookup;
- route to compiler or reusable Blueprint;
- enforce request-level limits.

Layer 1 does **not** invent semantic logic.

### Layer 2 — Semantic Compiler

Responsibilities:
- understand free-form natural language;
- decompose intent into approved capabilities;
- identify state, actions, rules, views, effects and assumptions;
- choose primitives from Capability Registry;
- generate a structured candidate Blueprint;
- generate transparent assumptions/defaults where allowed;
- request repair/refinement when needed.

Layer 2 does **not** emit arbitrary JavaScript.

Compiler mental model:

```text
Natural Language
  ↓
Intent Decomposition
  ↓
Capability Selection
  ↓
Action / State / Rule / View / Effect Wiring
  ↓
Structured Candidate
```

### Layer 3 — LegoSpec Contract

Layer 3 is the versioned declarative contract between compiler and runtime.

It defines:
- schema/version;
- state model;
- primitive instances;
- action/state transitions;
- rule representation;
- effects;
- presets/patches;
- assumptions/provenance;
- compatibility metadata.

Layer 3 is **data**, not generated executable code.

Validation must include more than JSON shape:
1. structural/schema validation;
2. bind/reference validation;
3. rule/function validation;
4. patch-path validation;
5. capability allowlist validation;
6. version compatibility;
7. size/complexity/resource limits;
8. policy/security checks;
9. semantic/capability quality gates where defined.

Important:

> **Schema Valid ≠ Semantic Correct.**

### Layer 4 — Universal Lego Player

Layer 4 is the trusted browser runtime.

Responsibilities:
- hydrate a validated Blueprint/Instance;
- render approved primitives;
- own reactive instance state;
- execute approved state transitions;
- evaluate approved Rule AST/functions;
- run bounded effects;
- isolate component failures;
- support snapshot/share hydration;
- bind optional realtime sessions.

Layer 4 must **not**:
- classify free-form natural language;
- guess business meaning;
- silently invent formulas;
- execute arbitrary JS;
- contain domain-specific hardcoded app logic in core.

---

## 4. Core Execution Model

The preferred declarative execution model is:

```text
Action
  ↓
State Transition
  ↓
Rule / Capability
  ↓
View Projection
  ↓
Effect
```

Example:

```text
DiceRoller action
  ↓
state.dice
  ↓
rule AST / approved function
  ↓
StatCard
  ↓
condition → Confetti
```

The compiler produces the wiring. The runtime executes the wiring.

---

## 5. Capability Registry

The Capability Registry is a critical architectural boundary and should become a machine-readable source of truth.

Preferred flow:

```text
Capability Registry
  ├─→ Compiler capability metadata
  ├─→ Layer 3 schema constraints
  ├─→ Layer 4 component/function registry
  ├─→ Tests
  └─→ Documentation
```

Do **not** maintain separate manual copies of the same allowlist in:
- frontend code;
- Zod schema;
- System Prompt;
- docs.

Each capability should eventually carry metadata such as:
- name/type;
- version;
- props schema;
- state/bind contract;
- actions/events;
- rule/operator dependencies;
- fallback behavior;
- security classification;
- runtime compatibility.

---

## 6. Candidate Initial Rich Primitive Catalog

Current candidate initial catalog:

### Input Controls
1. `NumberInput`
2. `TextInput`
3. `SelectChoice`
4. `ToggleSwitch`

### Data & Visualization
5. `StatCard`
6. `DataTable`
7. `ChartVisualizer`

### Rich Media & Interactive
8. `Model3DViewer`
9. `LottieAnimator`
10. `WheelSpinner`
11. `DiceRoller`
12. `VideoPlayer`
13. `ConfettiTrigger`

### Layout & Composition
14. `Container`
15. `Repeater`

These 15 are a **candidate starting surface**, not a permanent closed list.

Future primitives are added only through Registry registration + implementation + schema + tests + compatibility metadata.

---

## 7. Generic Rule Engine

### Current Direction

NodeFF should avoid both extremes:

**Bad extreme A:** hardcode domain functions for every new game/use case.

```text
calculate18La()
calculateMahjong()
calculatePoker()
calculateROI()
...
```

**Bad extreme B:** let LLM write unrestricted expression/code strings.

Preferred direction:

> **Typed declarative Rule AST + audited generic standard library.**

Candidate generic operations:
- IF
- SUM
- MIN
- MAX
- UNIQUE
- COUNT
- COUNT_MATCHES
- arithmetic
- comparison
- logical operators
- bounded array operations
- bounded normalization operations

Conceptual example:

```json
{
  "op": "SUM",
  "args": [
    {
      "op": "UNIQUE",
      "args": [{ "ref": "state.dice" }]
    }
  ]
}
```

This is preferable to arbitrary code and may be preferable to unrestricted expression strings because it improves:
- static validation;
- dependency analysis;
- allowlisting;
- complexity limits;
- deterministic serialization;
- migrations/versioning;
- auditability.

### Domain Capability Escape Hatch

Some complex functions may eventually require approved domain capabilities.

Those must live behind:

```text
Universal Player
  ↓
Capability / Function Registry
  ↓
Versioned Approved Domain Capability
```

They do not belong in Universal Player core.

---

## 8. State Model

Separate these concepts:

### Blueprint
Reusable immutable declarative capability/UI/rule definition.

### Instance
Concrete current-use state of a Blueprint.

### Context
Controlled payload passed from one Micro-App to another.

### Delta
Validated runtime state update.

Principle:

> **Blueprint defines reusable capability; Instance defines current reality; Context connects one Micro-App to the next.**

---

## 9. State Binding Protocol

Writable components emit explicit typed transitions.

Conceptual:

```text
Component interaction
 → dispatch/update(key, value)
 → Instance State
 → dependency-aware recompute
 → affected Views/Effects
```

Components should not hide business state internally.

Bindings must validate:
- key existence;
- expected type;
- mutability;
- allowed path.

---

## 10. Assumptions and Semantic Defaulting

NodeFF can turn ambiguity into an editable interactive model, but inferred defaults must never masquerade as facts.

Candidate provenance:
- `user_provided`
- `compiler_assumption`
- `template_default`
- `external_capability`

Example:
A "20-person company dinner by seniority" request may compile into editable role counts/weights, but "boss pays 5x" is an assumption, not an objective truth.

Preferred UX:

> **Make assumptions visible and editable.**

---

## 11. Semantic Failure Model

Key failure classes:

- `GENERATION_FAILED`
- `VALIDATION_FAILED`
- `SEMANTIC_MISMATCH`
- `UNSUPPORTED_SEMANTICS`
- `RUNTIME_COMPONENT_ERROR`
- `BLUEPRINT_DEGRADED`

Critical principle:

> **render_success does not equal task_success.**

A schema-valid, perfectly rendered Blueprint can still solve the wrong problem.

Recovery flow:

```text
Candidate
 → validation/capability gate
 → semantic quality gate
 → trusted Blueprint

If failure:
 → bounded repair
 OR targeted user refinement
 OR transparent unsupported/degraded result
```

---

## 12. Fallback and Degradation

Dynamic Form Fallback is **not a semantic brain**.

It may render already-known typed semantics:
- number → NumberInput;
- enum/options → SelectChoice;
- boolean → ToggleSwitch;
- known result → StatCard.

It must not invent:
- business rules;
- formulas;
- domain facts;
- options;
- meaning.

Unsupported capability flow:

1. compose approved primitives if semantics are preserved;
2. degrade presentation only if core semantics remain intact;
3. use typed generic form only if semantics are already known;
4. otherwise return transparent unsupported/refinement state.

Do not silently convert "build Angry Birds" into a numeric text game and claim the original request was fulfilled.

---

## 13. Product Hard Walls

Strong in-scope:
- discrete / turn-based interaction;
- dice, wheel, cards, timers, voting, scoreboards;
- arithmetic and weighted distribution;
- interactive decision models;
- deterministic state composition;
- rich media via approved primitives.

Out-of-scope for core unless a separately approved capability exists:
- arbitrary continuous 60fps physics engines;
- unrestricted canvas/custom rendering;
- arbitrary user/LLM code execution;
- unbounded recursive/agentic RPG systems;
- unsupported OS/system access.

Important nuance:

> JSON itself is not the hard wall. The approved Runtime/Capability Registry is the hard wall.

---

## 14. Share / Save / Live Modes

### A. Portable Snapshot

Small, non-sensitive Blueprint/Instance payload:

```text
Canonicalize
 → Compress
 → URL Fragment
 → Receiver
 → Decode
 → Validate
 → Hydrate
```

Guardrails:
- URL fragment = transport, not database;
- compression ≠ encryption;
- sensitive data excluded by default;
- decoded-size limits required;
- no decompression-bomb risk;
- explicit share or debounced persistence, not write-on-every-mutation.

### B. Ephemeral Live Room

```text
Blueprint content ID
 + room_id
 + mutable Instance state/deltas
```

Realtime mutable state must remain separate from immutable Blueprint content.

Provider is abstracted.

### C. Durable Save

Separate:
- immutable Blueprint content;
- logical Blueprint identity/version/lineage;
- user save/ownership pointer;
- persistent Instance state only when needed.

Immutable CAS bodies are never "edited in place"; editing creates a new revision/content identity.

---

## 15. Content-Addressed Blueprint Model

Preferred conceptual model:

```text
Canonical Validated Blueprint
  ↓
Content Hash
  ↓
Common Pool / CAS
  ↓
Referenced by
  ├─ users
  ├─ rooms
  ├─ short links
  └─ lineage/remix graph
```

Separate:
- `content_id/hash` = exact immutable content identity;
- `blueprint_id` = optional stable logical identity;
- `revision/lineage` = ancestry/version graph;
- `instance_id` = concrete use state.

A content hash proves content identity/integrity, not:
- ownership;
- trust;
- safety;
- access permission.

---

## 16. Cache Model

Two distinct cache identities:

### Prompt / Canonical-Intent Cache
Used to discover reusable Blueprint candidates.

### Blueprint Content Hash
Used for immutable exact content identity.

A normalized Prompt SHA-256 can be an exact-cache optimization, but it is not semantic deduplication.

Cache reuse must remain aware of:
- schema version;
- Capability Registry version;
- Runtime compatibility;
- security/policy status;
- quality/trust status.

Bad schema-valid but semantically wrong Blueprints must not poison the Common Pool.

---

## 17. Determinism and Replay

"Same Blueprint JSON" alone does not guarantee identical runtime result.

Exact replay may require:
- Blueprint content/version;
- Runtime version;
- capability versions;
- initial Instance state;
- RNG seed/outcome log;
- action/delta log;
- external data snapshot/version.

Random actions such as Dice/Wheel must use trusted Runtime RNG, never raw generated JavaScript like `Math.random()`.

---

## 18. Security Model

Forbidden:
- `eval()`;
- `new Function()`;
- arbitrary generated JS/TS;
- arbitrary HTML/script execution;
- untrusted capability names.

JSON is transport, not automatically a sandbox.

Safety comes from:

```text
Data-only Contract
+ Runtime Schema
+ Capability Allowlist
+ Safe Rule VM
+ Sanitization
+ CSP / URL policy
+ Size / complexity limits
+ No arbitrary code
```

Remote media primitives require:
- allowed schemes/origins;
- CSP;
- MIME/type validation;
- size limits;
- redirect policy;
- privacy/tracking considerations.

Recursive Container/Repeater requires:
- depth limits;
- node limits;
- repeat-item limits;
- evaluation/render budgets.

---

## 19. Identity and Progressive Auth

Consumer path:
- open/use shared Micro-App without mandatory registration.

Creator path:
- create/share ephemeral Micro-App anonymously;
- authenticate only when durable value is requested.

Durable triggers may include:
- ownership;
- permanent editing;
- history;
- publishing;
- paid quota;
- monetization.

Use random first-party `anonymous_id` where practical.

Do not default to device fingerprinting.

Anonymous → authenticated claim flow must include ownership proof / claim token / replay protection.

---

## 20. App-to-App Composition

Candidate Universal Context Payload:
- `summary`
- `rawText`
- `structuredData`

Flow:

```text
App A result
 → user selects next capability
 → controlled Context Payload
 → App B hydration
```

Context transfer must be explicit, schema-controlled, and privacy-aware.

---

## 21. Implementation Ownership

Architecture/Spec owns:
- allowed frameworks/dependencies;
- schema;
- state model;
- rule grammar;
- security boundaries;
- primitive registry;
- acceptance criteria.

Cursor executes approved contracts.

> **Cursor must not silently make architecture decisions.**

Implementation agents must not:
- invent a second semantic router;
- introduce arbitrary code execution;
- create a parallel schema/runtime;
- reinterpret SSOT.

---

## 22. Candidate Implementation Technologies

Not yet approved as permanent architecture:

- React
- Tailwind CSS
- shadcn/ui
- Zod
- Zustand / reducer-based state
- Vercel AI SDK or direct provider SDK behind adapter
- PartyKit or alternative realtime provider
- Supabase / Cloudflare / alternatives for persistence
- typed Rule AST preferred for evaluation; `expr-eval` remains only a candidate fallback/implementation option subject to threat modeling.

Vendor choices remain replaceable.

---

## 23. Candidate Build Order

Before implementation, contracts and acceptance tests must be fixed.

Candidate order:

1. Layer 3 schema + Capability Registry contract
2. State engine + Rule VM
3. Universal Player + minimum primitives
4. validation/security boundaries
5. semantic compiler
6. share/snapshot
7. realtime
8. CAS/registry
9. progressive auth/persistence
10. telemetry/reliability loop

---

## 24. Open Decisions

Must be resolved before official spec lock:

1. Typed Rule AST vs restricted expression-string representation.
2. Exact initial primitive catalog and props.
3. Capability Registry source-of-truth format.
4. Blueprint schema/version strategy.
5. Runtime/capability compatibility strategy.
6. CAS canonicalization and digest rules.
7. Cache admission quality policy.
8. Snapshot URL size threshold.
9. Realtime protocol/provider.
10. Retry/repair budget.
11. Semantic quality gate.
12. External media source policy.
13. Runtime AI boundary for Tier 1 vs Tier 2.
14. Exact anonymity → ownership claim protocol.

---

## 25. Non-Negotiable Architecture Guardrails

1. No arbitrary generated JavaScript.
2. No `eval()` / `new Function()`.
3. Universal Player does not infer free-form intent.
4. Schema-valid does not imply semantic correctness.
5. Dynamic Form does not invent unknown meaning.
6. Blueprint, Instance, Context and Delta remain separate.
7. URL Hash is transport, not DB.
8. Local storage is recovery convenience, not authoritative persistence.
9. Sensitive state is excluded from URLs by default.
10. Existing valid Blueprint opens with 0 LLM calls.
11. Heavy work is delegated outside NFF core.
12. Vendor-specific technology remains behind interfaces.
13. Cache never bypasses validation/security.
14. Degradation is transparent.
15. Common Pool admission must prevent semantic cache poisoning.
16. Runtime core remains generic.
17. Architecture lives in GitHub SSOT/working brain, not chat memory.

---

**Status: WORKING / CONSOLIDATED**
