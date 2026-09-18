# NodeFF Application Architecture

> Status: Working. Not authoritative until promoted through the NodeFF SSOT process.

## 1. System Identity

NodeFF is an **Intent-to-Interactive-App protocol and runtime**.

A user describes an intent. NodeFF compiles that intent into a validated declarative Blueprint, then a trusted browser runtime executes it as an interactive Micro-App.

```text
Intent
  ↓
Semantic Compiler
  ↓
Validated LegoSpec Blueprint
  ↓
Universal Lego Player
  ↓
Interactive Micro-App
```

NodeFF does not generate or deploy a new application bundle for every request.

> **NFF deploys the Runtime, not each generated App.**

The LLM is primarily a **semantic compiler at creation/refinement time**. Normal interaction with an existing Blueprint is local and deterministic where possible.

---

## 2. Product Execution Loop

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

For an already-valid Blueprint version:

- opening it should not require LLM recompilation;
- normal input, slider, dice, scoring and rule interaction should not require LLM calls;
- semantic refinement may invoke the compiler again;
- explicit runtime-AI capabilities may invoke an approved external AI capability.

Core principle:

> **Compile Once → Reuse Many → Execute Locally**

---

## 3. Four-Layer Responsibility Model

### Layer 1 — Ingestion & Routing

Owns:
- request intake;
- tier/safety/policy gate;
- normalization;
- exact/canonical-intent lookup;
- cache/registry routing;
- request limits and dispatch.

Does not own:
- free-form semantic interpretation;
- business-rule invention;
- UI generation.

### Layer 2 — Semantic Compiler

Owns:
- natural-language interpretation;
- intent decomposition;
- optional compiler-level archetype selection;
- capability selection from the Registry;
- state/action/rule/view/effect design;
- assumption extraction;
- structured candidate generation;
- bounded repair after validation failure;
- semantic refinement after user correction.

Does not own:
- arbitrary JavaScript generation;
- browser runtime execution;
- hidden fallback semantics.

Archetypes are compiler aids, not keyword routers inside the Player.

### Layer 3 — LegoSpec Contract

Owns the versioned data contract between compiler and runtime.

The contract describes:
- state;
- layout/component instances;
- actions and state transitions;
- rules;
- effects;
- presets/patches;
- assumptions/provenance;
- capability references;
- compatibility/version metadata;
- degradation/notice state when required.

Validation must cover more than JSON shape:

1. schema/type validity;
2. state binding and cross-reference validity;
3. Rule AST/operator validity;
4. capability allowlist validity;
5. patch path/operation validity;
6. version compatibility;
7. size/complexity limits;
8. security/policy constraints;
9. semantic/capability quality gates where defined.

> **Schema Valid ≠ Semantic Correct.**

A structurally valid Blueprint can still solve the wrong problem.

### Layer 4 — Universal Lego Player

Owns:
- hydration;
- component registry/factory;
- reactive Instance state;
- approved state transitions;
- Rule VM execution;
- bounded effects;
- local error isolation;
- snapshot/share restoration;
- optional realtime binding.

Does not own:
- natural-language classification;
- Regex/keyword intent routing;
- business meaning inference;
- formula invention;
- arbitrary code execution;
- silent semantic fallback.

The Player is a generic executor, not a second semantic compiler.

---

## 4. Declarative Execution Model

The core wiring model is:

```text
Action
  ↓
State Transition
  ↓
Rule / Capability
  ↓
View
  ↓
Effect
```

Example:

```text
DiceRoller
  ↓
state.dice
  ↓
approved Rule AST
  ↓
StatCard / LeaderBoard
  ↓
condition → Confetti
```

The compiler writes the wiring Blueprint. The Player executes only approved semantics.

---

## 5. Capability Registry

The Capability Registry is the boundary between model creativity and trusted execution.

```text
Capability Registry
  ├─ Compiler capability metadata
  ├─ Layer 3 schema constraints
  ├─ Layer 4 component/function registry
  ├─ Compatibility metadata
  ├─ Tests
  └─ Documentation
```

The same capability definition must not be independently maintained in multiple places. The Registry should be the source from which compiler context, runtime registration and validation constraints are derived.

Each capability should define:
- name/type;
- version;
- props schema;
- state/binding contract;
- inputs/outputs;
- actions/events;
- allowed rule/operator dependencies;
- fallback behavior;
- security classification;
- runtime compatibility.

Adding a new primitive is a controlled platform change, not a prompt edit.

---

## 6. Initial Rich Primitive Surface

Current candidate catalog:

### Input Controls
1. `NumberInput`
2. `TextInput`
3. `SelectChoice`
4. `ToggleSwitch`

### Data & Visualization
5. `StatCard`
6. `DataTable`
7. `ChartVisualizer`

### Rich Media & Interaction
8. `Model3DViewer`
9. `LottieAnimator`
10. `WheelSpinner`
11. `DiceRoller`
12. `VideoPlayer`
13. `ConfettiTrigger`

### Layout & Composition
14. `Container`
15. `Repeater`

The catalog is an initial capability surface, not a permanent limit.

A primitive may be added only with:
- contract definition;
- runtime implementation;
- validation;
- security policy;
- tests;
- version/compatibility metadata.

---

## 7. Rule Representation

The runtime should avoid two failure modes:

1. hardcoding every domain rule into the Universal Player;
2. allowing the compiler to emit unrestricted code or expression strings.

Preferred direction:

> **Typed declarative Rule AST + audited generic operator library.**

Candidate operators include:
- arithmetic;
- comparison;
- boolean logic;
- `IF`;
- `SUM`;
- `MIN`;
- `MAX`;
- `COUNT`;
- `UNIQUE`;
- `COUNT_MATCHES`;
- bounded normalization;
- bounded collection transforms when safely defined.

Conceptual form:

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

Benefits:
- static reference checking;
- operator allowlisting;
- dependency analysis;
- resource limits;
- deterministic serialization;
- migration/versioning;
- auditability.

A domain-specific function is allowed only as an explicit versioned Capability Registry extension when generic rules cannot safely represent the behavior. It never becomes hidden Universal Player business logic.

---

## 8. State Model

NodeFF separates four first-class concepts.

### Blueprint

Immutable reusable declarative definition of:
- UI composition;
- state schema/defaults;
- actions;
- rules;
- effects;
- capability dependencies.

### Instance

Current execution reality:
- user-entered values;
- current game/tool state;
- optional room/session state;
- runtime progress.

### Context

Explicit schema-controlled output passed from one Micro-App to another.

Candidate fields:
- `summary`;
- `rawText`;
- `structuredData`.

### Delta

Validated change applied to mutable Instance state or, during semantic refinement, to produce a new Blueprint candidate/revision.

> **Blueprint defines reusable capability; Instance defines current reality; Context connects Micro-Apps; Delta changes state or produces a new revision.**

---

## 9. State Binding

Interactive components emit typed updates into Instance state.

```text
User Action
 → validated state update
 → dependency-aware rule evaluation
 → affected views/effects
```

A binding must validate:
- path existence;
- expected type;
- mutability;
- allowed write scope.

Components must not hide business state that cannot be represented in the contract.

Runtime state patches cannot mutate protected Blueprint metadata or capability declarations.

---

## 10. Assumptions and Ambiguity

Ambiguous human intent should be converted into an **inspectable, editable model**, not hidden model guesses.

Candidate provenance:
- `user_provided`;
- `compiler_assumption`;
- `template_default`;
- `external_capability`.

Example: for "20-person company dinner split by seniority", the compiler may create editable groups, counts, weights and scenarios. A generated role weight is an assumption, not a fact or fairness judgment.

Rule:

> **Compiler assumptions must be visible, editable and distinguishable from user-provided facts.**

For culturally variable, disputed or domain-sensitive rules, the model's world knowledge is not authoritative. The compiler must expose the assumed variant or request refinement.

---

## 11. Semantic Correctness and Failure Model

Primary failure classes:

- `GENERATION_FAILED`
- `VALIDATION_FAILED`
- `SEMANTIC_MISMATCH`
- `UNSUPPORTED_SEMANTICS`
- `RUNTIME_COMPONENT_ERROR`
- `BLUEPRINT_DEGRADED`

A valid render is not proof of successful intent fulfillment.

> **render_success ≠ task_success**

Recovery model:

```text
Candidate
 → Contract Validation
 → Capability/Security Validation
 → Semantic Quality Gate
 → Trusted Blueprint

Failure
 ├─ bounded compiler repair
 ├─ targeted user refinement
 ├─ transparent degradation
 └─ unsupported response
```

Runtime failures are isolated locally and recorded. They do not authorize the Player to reinterpret the original intent.

---

## 12. Design Laws Derived from Failure Cases

These are permanent design constraints unless deliberately superseded through SSOT change control.

### No Client-Side Semantic Guessing

The Player must never infer open-ended intent through:
- Regex;
- numeric extraction;
- keyword routing;
- increasingly large `if/else` heuristics;
- relabeling an unrelated existing Blueprint.

The failed prototype pattern:

```text
Prompt → frontend heuristic → guessed logic → plausible but wrong app
```

is prohibited.

Required path:

```text
Prompt → Semantic Compiler → validated contract → deterministic Player
```

### Dynamic Form Is Rendering Fallback, Not Meaning Fallback

Generic form rendering may represent already-known typed semantics. It cannot invent domain facts, formulas, options or transformations.

> **Unknown UI may degrade generically; unknown meaning must not be fabricated.**

### Validation Is Multi-Layered

A runtime schema such as Zod may validate shape and cross-field invariants, but it does not establish semantic correctness.

### Contract Has One Definition Source

Do not maintain independently editable TypeScript interfaces and runtime schemas for the same contract. Prefer one source with generated/inferred secondary representations.

### Safe Interpreter Is Still a Security Boundary

"Not using `eval`" is not sufficient. The Rule VM must explicitly control allowed operators, references, complexity and resource use.

---

## 13. Transparent Degradation

When a request exceeds current capability:

1. preserve the original intent;
2. test whether approved primitives can preserve its core semantics;
3. degrade presentation only if the task remains materially equivalent;
4. include a visible notice for material degradation;
5. otherwise return unsupported/refinement state.

Layer 2 chooses the degradation contract. Layer 3 validates it. Layer 4 only renders it.

UX principle:

> **不中斷流程，但不隱瞞錯誤。**

Silent substitution is prohibited.

---

## 14. Product Capability Boundary

Strong fit:
- discrete and turn-based interactions;
- dice, wheel, cards, timers, voting, scoreboards;
- arithmetic and weighted allocation;
- interactive calculators;
- decision models;
- temporary social/group coordination;
- approved media/visualization primitives.

Outside the core capability boundary unless a dedicated approved engine/capability exists:
- arbitrary continuous 60fps physics;
- unrestricted Canvas/custom rendering;
- arbitrary generated functions/scripts;
- unbounded RPG/agent state machines;
- unrestricted OS/system access.

JSON itself is not the limitation. The intentional limit is the **trusted Capability Registry and Runtime boundary**.

A controlled `Model3DViewer` does not imply a general 3D game engine.

---

## 15. Sharing, Persistence and Collaboration

### Portable Snapshot

For small, non-sensitive state:

```text
Blueprint/Instance
 → canonicalize
 → compress
 → URL fragment
 → decode
 → validate
 → hydrate
```

Rules:
- URL Hash is transport, not a database;
- compression is not encryption;
- sensitive data is excluded by default;
- size/resource limits apply;
- persistence should be explicit or debounced/batched, not written on every state mutation.

### Ephemeral Live Room

```text
Blueprint Reference
 + Room ID
 + Mutable Instance State
 + Validated Deltas
```

Realtime state never mutates immutable Blueprint content.

### Durable Save

Durable persistence separates:
- immutable Blueprint body;
- logical Blueprint identity;
- revision/lineage;
- user ownership/save pointer;
- persistent Instance state only when product behavior requires it.

Editing immutable Blueprint content creates a new content identity/revision.

---

## 16. Blueprint Identity and Content Addressing

Canonical validated Blueprint content may be content-addressed:

```text
Canonical Blueprint
 → Content Hash
 → Common Pool
```

Separate identifiers:
- `content_id/hash`: exact immutable content identity;
- `blueprint_id`: optional stable logical identity;
- lineage/revision metadata;
- `instance_id`: concrete execution state.

Hash identity does not prove:
- authorship;
- ownership;
- trust;
- safety;
- authorization.

Personal state must not be silently deduplicated into the global Blueprint body.

---

## 17. Cache Semantics

Keep distinct:

### Prompt / Canonical-Intent Lookup
Used to discover reusable Blueprint candidates.

### Blueprint Content Hash
Used for exact immutable content identity.

A normalized Prompt hash is only an exact-cache optimization; it is not semantic equivalence.

Reusable artifacts remain bound to:
- schema version;
- Registry version;
- Runtime compatibility;
- policy/security status;
- quality/trust status.

A schema-valid but semantically wrong Blueprint must not enter or remain promoted in the trusted Common Pool.

---

## 18. Determinism and Replay

Same Blueprint content does not automatically mean identical execution.

Exact replay may require:
- Blueprint hash/version;
- Runtime version;
- capability versions;
- Rule VM version;
- initial Instance state;
- RNG seed/outcomes;
- action/delta log;
- external-data snapshot/version.

Randomness such as Dice/Wheel must come from a trusted runtime action, never generated code such as `Math.random()`.

---

## 19. App-to-App Composition

Composition is explicit:

```text
App A Result
 → user-selected next capability
 → approved Context payload
 → App B hydration
```

No hidden cross-app data transfer.

Context is:
- schema-controlled;
- permission-aware;
- privacy-aware;
- intentionally selected by the user or product flow.

---

## 20. Identity and Progressive Authentication

Consumer:
- may open/use shared Micro-Apps without mandatory account creation.

Creator:
- may create/share ephemeral artifacts anonymously where feasible.

Authentication is requested when durable value requires identity:
- ownership;
- permanent editing;
- history;
- publishing;
- paid quota;
- monetization;
- cross-device persistence.

Anonymous continuity should use a random first-party `anonymous_id`, not default device fingerprinting.

Anonymous-to-account claim requires proof/claim-token/replay protection. Possessing a shared URL is not ownership proof.

---

## 21. Heavy Capability Boundary

NodeFF core is a lightweight control plane.

Heavy work is delegated to:
- browser Web Workers/WASM;
- specialized external APIs/workers;
- external durable stores.

The Micro-App may control parameters, show progress, and present results while the heavy operation runs elsewhere.

Long-lived chat/social-network behavior is not a core NFF responsibility. Ephemeral room chat may be a bounded realtime capability.

---

## 22. Implementation Governance

Architecture and specification own:
- contract definition;
- security boundaries;
- capability registry;
- rule grammar;
- state ownership;
- framework/dependency constraints;
- acceptance criteria.

Cursor executes those decisions.

> **Cursor must not silently introduce architecture.**

Implementation must not create:
- a second semantic router;
- a parallel contract;
- a second runtime;
- arbitrary execution paths;
- hidden business logic in the Player.

---

## 23. Candidate Technology Choices

Current candidates, not locked architecture:
- React;
- Tailwind / shadcn;
- Zod;
- Zustand or reducer-based state;
- Vercel AI SDK or provider SDK behind an NFF adapter;
- PartyKit or other realtime provider;
- Supabase / Cloudflare / other persistence;
- typed Rule AST/VM;
- `expr-eval` only if threat-model evaluation justifies it;
- `lz-string` or alternative snapshot compression.

Vendor substitution must not alter core contract semantics.

---

## 24. Build Order

Candidate implementation order:

1. Capability Registry contract
2. Layer 3 schema and versioning
3. state transition model
4. Rule AST + Rule VM
5. minimum Universal Player
6. initial primitive set
7. validation/security gates
8. Semantic Compiler
9. snapshot/share
10. CAS/registry/cache
11. realtime
12. progressive auth/durable persistence
13. telemetry/reliability loop

Each implementation stage requires explicit acceptance tests before expansion.

---

## 25. Decisions Still Open

- Rule AST vs restricted expression representation;
- final initial primitive set and props;
- Registry source format;
- Blueprint version/compatibility policy;
- CAS canonicalization/digest policy;
- semantic quality/admission gate;
- retry/repair budget;
- snapshot size threshold;
- realtime protocol/provider;
- runtime-AI Tier boundary;
- external media policy;
- anonymous-to-owner claim protocol.

---

## 26. Non-Negotiable Guardrails

1. No arbitrary generated JavaScript.
2. No `eval()` or `new Function()`.
3. Player never infers free-form intent.
4. Schema validity is not semantic correctness.
5. Generic fallback never fabricates meaning.
6. Blueprint, Instance, Context and Delta remain distinct.
7. URL Hash is transport, not DB.
8. LocalStorage is recovery convenience, not authoritative persistence.
9. Sensitive state is excluded from URLs by default.
10. Existing valid Blueprint execution requires no LLM by default.
11. Heavy work stays outside the core runtime.
12. Cache never bypasses compatibility/security/quality checks.
13. Degradation is explicit.
14. Runtime core remains generic.
15. Architecture is governed from GitHub, not conversational memory.

