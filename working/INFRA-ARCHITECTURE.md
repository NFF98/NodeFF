# NodeFF Infrastructure Architecture — Working Brain

> Status: WORKING / NOT OFFICIAL SSOT
>
> Purpose: Consolidated infrastructure architecture for NodeFF. This file replaces prior accumulated working notes and defines the current infrastructure direction without locking unapproved vendors.

---

## 1. Infrastructure Principle

NodeFF is designed as a **lightweight Control Plane**, not a Heavy Compute Plane.

Golden rule:

> **NFF handles intent routing, compilation orchestration, Blueprint delivery, runtime coordination, state transport and commerce/control-plane concerns. Heavy computation and large durable data should run in the browser or specialized external services.**

---

## 2. High-Level Infrastructure

```text
Browser / Client
  │
  ├─ Local Universal Player
  ├─ Local Instance State
  ├─ Optional Web Worker / WASM
  │
  ▼
Edge / API Boundary
  ├─ Safety / Abuse / Tier Gate
  ├─ Cache / Registry Lookup
  ├─ Compiler API
  ├─ Auth / Quota
  └─ Routing
  │
  ├──────────────→ LLM Provider Adapter(s)
  │
  ├──────────────→ Blueprint Registry / CAS
  │
  ├──────────────→ Durable Metadata / Account Store
  │
  ├──────────────→ Realtime Adapter / Rooms
  │
  └──────────────→ External Capabilities / Workers
```

---

## 3. Cold Path vs Warm Path

### Cold Path — Compilation

```text
Intent
 → Edge/API Gate
 → Cache Lookup
 → Compiler
 → Structured Candidate
 → Validation
 → Trusted Blueprint
 → CAS/Response
```

Cold path may involve LLM latency and cost.

### Warm Path — Existing Blueprint

```text
Blueprint/Instance Reference
 → Resolve
 → Validate Compatibility
 → Hydrate
 → Execute Locally
```

Warm path should not require LLM merely to open or interact with an existing valid Blueprint.

Principle:

> **Compile Once → Reuse Many → Execute Locally**

---

## 4. Compiler Service Boundary

Production compiler must run behind an NFF-controlled server/edge API boundary.

```text
Browser
 → NFF Compiler Endpoint
 → Model Provider Adapter
 → Structured Candidate
 → Validation Pipeline
 → Trusted Blueprint
```

Responsibilities:
- provider credentials;
- anonymous/account quota;
- rate limits;
- abuse protection;
- model/provider routing;
- schema version;
- Capability Registry snapshot;
- timeout/retry;
- cost telemetry;
- sanitized repair loop;
- final validation before trusted admission.

Production provider secrets must never be shipped in browser-visible build variables.

---

## 5. Provider Abstraction

NodeFF must not depend architecturally on one LLM provider.

Preferred interface:

```text
CompilerService
 → ModelProviderAdapter
   ├─ Provider A
   ├─ Provider B
   └─ Provider C
```

Vercel AI SDK may be useful, but remains an implementation candidate.

Same principle applies to:
- realtime;
- durable storage;
- object storage;
- authentication;
- external workers.

---

## 6. Validation Pipeline

Candidate trusted-admission path:

```text
Model Candidate
 → Structural Schema
 → Cross-field References
 → Rule AST Validation
 → Patch Validation
 → Capability Validation
 → Complexity Budgets
 → Security / Policy
 → Semantic Quality Gate
 → Canonicalization
 → Content Hash
 → Trusted Registry
```

No cache path may bypass these gates.

---

## 7. Retry / Self-Correction

Repair loop:

```text
Validation Failure
 → sanitized structured error
 → bounded compiler repair
 → full revalidation
```

Retry policy must define:
- retryable errors;
- max attempts;
- token/time budget;
- circuit breaker;
- telemetry.

Semantic mismatch may require user refinement instead of blind retry.

Never send secrets or raw unsafe internal data back to a model.

---

## 8. Capability Registry Distribution

Capability metadata should be generated from Registry SSOT.

Each compile request receives a versioned capability snapshot.

Blueprint metadata should record compatibility context, including:
- schema version;
- Capability Registry version;
- Runtime compatibility;
- rule grammar version.

This reduces drift among:
- compiler prompt/context;
- runtime components;
- schema;
- tests;
- docs.

---

## 9. Blueprint Registry / CAS

Candidate pipeline:

```text
Validated Blueprint
 → Canonical Serialization
 → Digest
 → Immutable CAS Object
 → Registry Metadata
 → Edge Cache
```

Separate:
- immutable content;
- logical Blueprint identity;
- lineage/revision;
- ownership/save pointers;
- Instance state.

Common Pool:
- immutable trusted Blueprint content.

Personal layer:
- references;
- ownership;
- favorites;
- history;
- account metadata;
- paid metadata.

Knowing a hash must not automatically grant access to private content.

---

## 10. Cache Architecture

### Exact Prompt Cache
Fast optimization for exact/canonicalized prompt reuse.

### Semantic / Canonical-Intent Reuse
Retrieves likely reusable Blueprint families.

### Blueprint Content Cache
Immutable content lookup by content hash.

These are different concerns.

Raw punctuation-stripped Prompt SHA-256 is not universal semantic deduplication.

Cache entries should retain:
- validation status;
- quality/trust status;
- schema version;
- registry version;
- runtime compatibility;
- policy status.

---

## 11. Cache Poisoning Protection

A Blueprint can be:
- syntactically valid;
- schema valid;
- runtime renderable;
- semantically wrong.

Therefore, trusted Common Pool admission cannot equal "schema passed".

Candidate statuses:
- untrusted;
- validating;
- trusted;
- degraded;
- quarantined;
- deprecated.

Failure reports may reduce reuse priority or quarantine bad artifacts.

---

## 12. Share Transport

### URL Snapshot

Suitable for:
- small;
- non-sensitive;
- portable;
- self-contained snapshots.

Pipeline:

```text
Canonical Payload
 → Compress
 → URL Fragment
 → Decode
 → Resource Limit Check
 → Schema/Compatibility Validation
 → Hydrate
```

Requirements:
- max encoded size;
- max decoded size;
- decompression limits;
- sensitive-field exclusion;
- integrity/version checks;
- no assumption that compression provides privacy.

### Short Link / Backend Reference

Use when:
- payload too large;
- stable identity needed;
- permissions required;
- durable reference needed.

---

## 13. Realtime Infrastructure

Realtime is optional and activated only when product mode requires live synchronization.

Logical model:

```text
Immutable Blueprint
 + Room ID
 + Mutable Room Instance State
 + Validated Deltas
```

Room mutable state never mutates the immutable Blueprint.

Realtime provider remains behind an adapter.

Policy must define:
- room size;
- idle TTL;
- reconnect;
- ordering;
- dedupe;
- conflict strategy;
- presence;
- rate limits;
- abuse controls.

No assumption of literal "0ms sync".

---

## 14. Heavy Work Paths

### Browser Compute
Use:
- Web Workers;
- WASM;
- browser-native compute.

NFF handles:
- parameters;
- progress;
- result presentation.

### External Worker/API
Use when task requires:
- expensive AI;
- long-running generation;
- specialized compute;
- large database query.

Pattern:

```text
NFF Action
 → External Job
 → Async Status
 → Poll/Webhook/Event
 → Result
```

The Micro-App becomes a status/progress/result surface.

### Durable Large Data
Keep large durable datasets outside the lightweight Runtime core.

NFF stores controlled references/permissions as needed.

---

## 15. Runtime Rule VM

Preferred direction:
- typed Rule AST;
- explicit operator/function allowlist;
- deterministic evaluator;
- versioned grammar;
- resource-bounded execution.

If an expression library such as `expr-eval` is considered, it must pass threat-model testing.

"Not eval()" does not automatically mean safe.

Threat model includes:
- unsafe function exposure;
- property access;
- prototype escape;
- recursion;
- oversized expressions;
- CPU exhaustion;
- memory exhaustion;
- oversized arrays.

---

## 16. Patch / Delta Security

Runtime patches require:
- allowed operations;
- allowed mutable paths;
- type validation;
- result validation;
- operation count limit;
- payload size limit;
- protected metadata boundaries.

Preset patching cannot mutate schema, capability declarations, ownership or protected Blueprint metadata.

---

## 17. External Asset Security

Remote media capabilities such as 3D models, Lottie and video create an external-content boundary.

Requirements:
- scheme/origin allowlist;
- CSP;
- MIME validation;
- size limits;
- redirect handling;
- tracking/privacy consideration;
- failure fallback;
- optional proxy/cache policy.

A valid URL string alone is insufficient.

---

## 18. Resource Budgets

Schema-valid content can still attack availability.

Validate budgets for:
- total Blueprint bytes;
- decoded snapshot bytes;
- component node count;
- nesting depth;
- Repeater expansion;
- Rule AST node count;
- evaluation steps;
- state size;
- media count;
- remote asset size.

---

## 19. Determinism / Replay Metadata

For reproducible execution, track as needed:
- Blueprint content hash;
- schema version;
- Runtime version;
- capability versions;
- rule grammar/evaluator version;
- initial state;
- RNG seed/outcomes;
- action log;
- external data version/snapshot.

CAS alone does not guarantee replay equivalence.

---

## 20. Identity Infrastructure

Anonymous-first consumer flow:
- random first-party anonymous ID;
- no mandatory login.

Authentication appears when durable/account-bound value is requested.

Identity promotion:

```text
anonymous_id
 → create/use/share
 → durable-value request
 → authenticate
 → prove claim eligibility
 → migrate/associate eligible artifacts
```

Do not use possession of a shared URL as sole proof of ownership.

---

## 21. Data Classes

### Client-only
- transient UI state;
- local Instance state;
- cached Blueprint.

### Share transport
- small public snapshot;
- non-sensitive context.

### Ephemeral backend
- room state;
- presence;
- live deltas.

### Durable backend
- account;
- ownership pointers;
- publishing metadata;
- history when opted/needed;
- commerce;
- quota;
- trusted Blueprint registry metadata.

### Never client-exposed
- provider secrets;
- internal credentials;
- privileged signing keys.

---

## 22. Telemetry

Candidate events:
- generation_started
- generation_failed
- validation_failed
- semantic_mismatch
- unsupported_semantics
- compiler_repair_attempted
- compiler_repair_failed
- wrong_archetype_detected
- runtime_component_error
- blueprint_degraded
- fallback_rendered
- blueprint_opened
- blueprint_remixed
- share_opened
- capability_invoked

Track separately:
- render success;
- user task success proxy;
- correction/refinement;
- runtime reliability.

Privacy, retention and training/reuse rights require explicit governance.

---

## 23. Security Non-Negotiables

1. No production LLM secret in browser.
2. No arbitrary JavaScript from Blueprint.
3. No `eval()` / `new Function()`.
4. JSON alone is not considered a sandbox.
5. Rule/function capability allowlist.
6. Strict transport/resource limits.
7. Remote content policy.
8. Validation at trust boundaries.
9. Cache does not bypass validation.
10. Hash is not authorization.
11. Compression is not encryption.
12. Unknown capability does not execute.
13. Error Boundary is defense-in-depth, not primary validation.

---

## 24. Vendor Status

Current vendors/libraries discussed are candidates only:
- Vercel / Cloudflare
- Supabase
- PartyKit
- OpenAI / Claude / DeepSeek / Groq or others
- Zod
- Zustand
- expr-eval
- lz-string
- React / Tailwind / shadcn

Architecture should survive replacement of any one of them.

---

## 25. Claims That Remain Targets / Hypotheses

Do not encode as guarantees:
- 0ms interaction;
- <5ms / <10ms cache;
- 1ms validation;
- 90% cost reduction;
- $0 marginal cost;
- 100% sandbox safety;
- 99.9% structured correctness;
- fixed free-room limits;
- exact LLM latency;
- exact provider pricing.

These require benchmarking and provider validation.

---

## 26. Open Infrastructure Decisions

1. Runtime hosting/edge provider.
2. LLM provider adapter implementation.
3. Realtime provider.
4. persistent DB/object store.
5. CAS canonicalization algorithm.
6. digest/version policy.
7. Rule VM implementation.
8. retry budget.
9. trust/admission scoring.
10. URL snapshot size threshold.
11. media proxy policy.
12. room TTL/limits.
13. telemetry retention/privacy policy.
14. private Blueprint authorization model.

---

**Status: WORKING / CONSOLIDATED**
