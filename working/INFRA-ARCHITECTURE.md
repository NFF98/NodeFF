# NodeFF Infrastructure Architecture

> Status: Working. Not authoritative until promoted through the NodeFF SSOT process.

## 1. Infrastructure Mission

NodeFF infrastructure supports a **client-first, edge-assisted control plane**.

It is responsible for:
- request routing;
- semantic compilation;
- Blueprint validation/distribution;
- identity/quota;
- lightweight persistence;
- realtime coordination;
- telemetry;
- external-capability orchestration.

It is not intended to become the default execution plane for every interaction or heavy workload.

> **NFF is a lightweight Control Plane, not a Heavy Compute Plane.**

---

## 2. Logical Topology

```text
Browser
  ├─ Universal Player
  ├─ Local Instance State
  ├─ Rule VM
  └─ Optional Worker/WASM
       │
       ▼
NFF Edge / API Boundary
  ├─ Policy / Abuse / Tier Gate
  ├─ Cache / Registry Resolution
  ├─ Compiler Endpoint
  ├─ Auth / Quota
  ├─ Share / Short-Link Resolution
  └─ Capability Orchestration
       │
       ├─ LLM Provider Adapter
       ├─ Blueprint Registry / CAS
       ├─ Durable Metadata Store
       ├─ Realtime Adapter
       └─ External APIs / Workers / Storage
```

---

## 3. Cold Path and Warm Path

### Cold Path — New or Semantically Changed Intent

```text
Intent
 → Gate
 → Cache/Reuse Lookup
 → Semantic Compiler
 → Structured Candidate
 → Validation Pipeline
 → Trusted Blueprint
 → Canonicalize / Store
 → Return to Client
```

The cold path contains model/provider latency and compiler cost.

### Warm Path — Existing Blueprint

```text
Reference / Snapshot
 → Resolve / Decode
 → Compatibility + Trust Check
 → Hydrate
 → Execute Locally
```

Warm execution does not invoke the LLM merely to open or interact with an existing valid artifact.

---

## 4. Compiler Service Boundary

All production model compilation passes through an NFF-controlled endpoint.

Responsibilities:
- provider credentials;
- anonymous/account quota;
- rate limiting;
- abuse/policy gate;
- model routing;
- versioned Capability Registry context;
- schema/rule version selection;
- timeout/token budgets;
- repair policy;
- cost/latency telemetry;
- trusted-admission validation.

Provider secrets never ship in browser-visible environment variables.

The compiler service exposes an NFF-owned interface so model vendors remain replaceable.

---

## 5. Compiler Context

The compiler receives a versioned capability snapshot generated from the Capability Registry.

Do not hand-maintain a second primitive whitelist in the System Prompt.

Compiler context should identify:
- available primitives;
- allowed props;
- state contracts;
- actions/events;
- Rule VM operators;
- capability limits;
- degradation rules;
- schema/runtime version.

A compilation request sees a fixed capability snapshot even while the platform evolves over time.

---

## 6. Validation and Trust Admission

Trusted Blueprint admission path:

```text
Candidate
 → Structural Schema
 → State/Bind References
 → Rule AST / Operator Check
 → Patch Validation
 → Capability Check
 → Resource Budgets
 → Security / Policy
 → Semantic Quality Gate
 → Canonicalization
 → Content Hash
 → Registry Trust State
```

A schema-valid candidate is not automatically trusted.

Possible registry states:
- untrusted;
- validating;
- trusted;
- degraded;
- quarantined;
- deprecated.

A cache hit cannot bypass the gates appropriate to the artifact's trust/version state.

---

## 7. Repair and Retry

Structural or contract failures may enter a bounded repair loop:

```text
Validation Failure
 → sanitized machine-readable errors
 → compiler repair
 → full revalidation
```

Policy defines:
- retryable error classes;
- maximum attempts;
- token/time budget;
- circuit breaker;
- provider fallback if allowed;
- telemetry.

Semantic mismatch is different from malformed output. It may require user refinement rather than automatic retry.

Never expose secrets or unsafe internal payloads in repair prompts.

---

## 8. Blueprint Registry and Content Addressing

Validated immutable Blueprint content may be stored in a content-addressable Common Pool.

```text
Validated Blueprint
 → deterministic canonical serialization
 → digest
 → immutable content object
 → registry metadata
 → edge/cache distribution
```

Store separately:
- content object;
- logical Blueprint identity;
- lineage/revision;
- trust/policy metadata;
- user ownership/save pointer;
- Instance state.

Hash possession is not authorization.

Private/unpublished artifact access requires independent authorization.

---

## 9. Canonicalization

Content hashing requires deterministic canonicalization.

The canonicalization specification must define:
- key ordering;
- number representation;
- omitted/default fields;
- Unicode normalization if relevant;
- schema version;
- digest algorithm/version.

Equivalent logical content must not accidentally produce different identities solely because of serialization formatting.

---

## 10. Cache Architecture

Three different cache/reuse concerns exist.

### Exact Prompt Cache

Fast reuse for identical or strictly canonicalized text.

### Canonical-Intent / Semantic Reuse

Finds a likely trusted Blueprint family for semantically similar intent.

### Blueprint Content Cache

Exact retrieval by immutable content hash.

These keys are not interchangeable.

A punctuation/whitespace-stripped Prompt SHA-256 is at most an exact-cache optimization. It is not a semantic identity.

Cache metadata includes:
- schema version;
- Registry version;
- Runtime compatibility;
- policy/security status;
- trust/quality status.

---

## 11. Cache Poisoning Defense

A Blueprint may pass schema validation yet be semantically wrong.

Therefore:
- trusted Common Pool admission includes quality status beyond shape validation;
- semantic mismatch reports affect reuse confidence;
- unhealthy versions may be quarantined/deprioritized;
- remediation produces a new validated revision rather than mutating immutable content.

The system must not amplify a wrong Blueprint globally simply because it is cheap to reuse.

---

## 12. Portable Snapshot Transport

Suitable only for small, non-sensitive snapshots.

```text
Canonical Snapshot
 → compress
 → URL Fragment
 → decode
 → decompression/resource guard
 → schema/version/security validation
 → hydrate
```

Controls:
- maximum encoded size;
- maximum decoded size;
- decompression limits;
- sensitive-field exclusion;
- integrity/version checks where required.

Compression does not provide confidentiality.

URL Hash is a transport mechanism, not authoritative persistence.

---

## 13. Durable Reference Path

Use a short-link/backend reference when:
- payload is too large;
- stable identity is required;
- access control is required;
- durable ownership/history is required;
- sensitive data must not travel in the URL.

The short reference resolves to authorized server-side metadata/content references; it does not imply mutable Blueprint blobs.

---

## 14. Realtime Rooms

Realtime is optional, not the default execution model.

```text
Immutable Blueprint Reference
 + Room ID
 + Mutable Room Instance State
 + Ordered Validated Deltas
```

The provider stays behind an adapter.

The protocol must define:
- room identity;
- presence;
- join/reconnect;
- ordering;
- deduplication;
- conflict handling;
- state snapshot/recovery;
- idle TTL;
- participant limits;
- rate limits;
- abuse controls.

No "0ms sync" guarantee is assumed.

Ephemeral room chat may share the same realtime boundary. Long-lived Discord/Telegram-style history, background notifications and durable messaging are outside the NFF core unless explicitly added as a separate capability.

---

## 15. Heavy Work Delegation

### Browser Compute

Use Web Workers, WASM or browser-native compute when appropriate.

NFF provides:
- parameters;
- progress;
- result visualization.

### External Job

```text
NFF Action
 → external API/worker
 → job/status reference
 → webhook/poll/event
 → result
 → Player presentation
```

Used for:
- heavy AI;
- media generation;
- long-running processing;
- large database queries;
- specialized compute.

### Durable Large Data

Large durable datasets remain in suitable external/backend storage. NFF keeps controlled references, permissions and presentation logic.

---

## 16. Runtime Rule VM

Preferred infrastructure contract:
- typed Rule AST;
- explicit operator/function registry;
- deterministic evaluation semantics;
- versioned grammar;
- execution step/size limits;
- no host-object access;
- no arbitrary property traversal;
- no arbitrary code.

An expression library such as `expr-eval` is acceptable only if it satisfies the NFF threat model. "Not eval()" is not a security proof.

Threat model includes:
- exposed functions/operators;
- property/prototype escape;
- recursion;
- CPU exhaustion;
- memory exhaustion;
- oversized collections;
- non-determinism.

---

## 17. Patch and Delta Security

Runtime state patches require:
- allowlisted operations;
- allowlisted mutable paths;
- type validation;
- resulting-state validation;
- maximum operation count;
- maximum payload size.

Runtime patches cannot alter:
- schema;
- capability declarations;
- ownership;
- trust metadata;
- protected Blueprint fields.

Semantic Blueprint refinement runs through the compiler/validation path and creates a new content identity where content changes.

---

## 18. External Asset Boundary

Remote 3D, Lottie, video or other media is untrusted external content.

Controls may include:
- allowed schemes/origins;
- CSP;
- MIME/content checks;
- size limits;
- redirect rules;
- privacy/tracking restrictions;
- optional proxy/cache;
- timeout/fallback behavior.

A syntactically valid URL is not sufficient validation.

---

## 19. Resource Budgets

Schema-valid payloads can still exhaust the runtime.

Set explicit budgets for:
- Blueprint bytes;
- decoded snapshot bytes;
- component nodes;
- nesting depth;
- Repeater expansion;
- Rule AST nodes;
- evaluation steps;
- state size;
- patch operations;
- media count;
- external asset size.

Resource-budget violations fail closed or degrade according to contract policy.

---

## 20. Determinism and Replay Metadata

Exact replay may require:
- content hash;
- schema version;
- Runtime version;
- capability versions;
- Rule VM version;
- initial state;
- RNG seed/outcome log;
- ordered actions/deltas;
- external-data snapshot/version.

Content addressing alone does not guarantee replay equivalence across environment/version changes.

---

## 21. Identity and Progressive Auth Infrastructure

Default consumer path:
- no mandatory registration;
- privacy-conscious first-party `anonymous_id` where continuity is needed.

Authentication is introduced for durable account-bound value.

```text
anonymous_id
 → create/use/share
 → durable value requested
 → authenticate
 → prove claim eligibility
 → associate/migrate eligible records
```

Possession of a public/shared link is not sufficient proof of ownership.

Device fingerprinting is not the default identity mechanism.

---

## 22. Data Placement

### Browser
- transient UI state;
- normal Instance state;
- cached trusted Blueprint;
- local recovery state.

### Share Transport
- explicitly shareable, non-sensitive snapshot/context.

### Ephemeral Backend
- room state;
- presence;
- live deltas;
- short-lived job/session coordination.

### Durable Backend
- accounts;
- ownership/save pointers;
- publishing metadata;
- quota/billing;
- history where required;
- commerce;
- trusted registry metadata;
- protected references.

### Never Client-Exposed
- provider secrets;
- privileged credentials;
- signing keys.

LocalStorage is local recovery convenience, not authoritative persistence.

---

## 23. Telemetry and Reliability Signals

Core events include:
- compilation started/completed/failed;
- validation failure;
- semantic mismatch;
- unsupported semantics;
- repair attempted/failed/succeeded;
- wrong composition/archetype;
- runtime component error;
- degraded/fallback render;
- Blueprint opened;
- Blueprint remixed;
- share opened;
- capability invoked.

Separate:
- render success;
- runtime success;
- task-success proxy;
- user correction/refinement.

Telemetry collection requires explicit privacy, retention and reuse governance.

---

## 24. Security Invariants

1. No provider secret in browser code.
2. No arbitrary Blueprint JavaScript.
3. No `eval()` or `new Function()`.
4. JSON is data transport, not automatically a sandbox.
5. Only registered components/operators/actions execute.
6. Remote content is constrained.
7. Untrusted boundaries revalidate.
8. Resource budgets are enforced.
9. Cache cannot bypass policy/trust checks.
10. Hash is not authorization.
11. Compression is not encryption.
12. Unknown capabilities fail closed.
13. Error Boundary is defense-in-depth, not validation.
14. Semantic trust is distinct from schema validity.

---

## 25. Vendor Abstraction

Discussed candidates include:
- Vercel / Cloudflare;
- Supabase;
- PartyKit;
- OpenAI / Anthropic / DeepSeek / Groq or other model providers;
- Zod;
- Zustand;
- React;
- `lz-string`;
- `expr-eval`.

None is an architectural dependency until explicitly approved. Provider-specific behavior, pricing and quota must remain outside core protocol semantics.

---

## 26. Performance and Cost Claims

The following remain measurement targets or hypotheses unless benchmarked:
- 0ms local interaction;
- sub-5ms/sub-10ms cache;
- 1ms validation;
- 90% cost reduction;
- zero marginal cost;
- 100% sandbox safety;
- 99.9% structured correctness;
- fixed free-room limits;
- exact generation latency;
- exact provider unit economics.

Performance requirements should eventually be expressed as measured SLOs with:
- workload;
- region;
- payload size;
- percentile;
- provider/configuration;
- test methodology.

---

## 27. Decisions Still Open

- hosting/edge provider;
- model adapter implementation;
- realtime provider/protocol;
- durable store/object store;
- CAS canonicalization/digest;
- Registry persistence/distribution;
- Rule VM implementation;
- retry/circuit-breaker policy;
- trust/admission scoring;
- URL snapshot size threshold;
- media proxy/source policy;
- room limits/TTL;
- privacy/telemetry retention;
- private Blueprint authorization model.

