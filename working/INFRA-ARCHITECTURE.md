# NodeFF Infrastructure Architecture（Working）

> 本文件為系統規格討論前的工作版，不是官方 SSOT。

## 1. Infra Goal
以「低固定成本、edge-first、client-first、可水平擴展」支撐大量短生命週期 Micro-App。

## 2. Logical Infrastructure

```
Browser
 │
 ├─ CDN / Edge
 │    ├─ Request Gate
 │    ├─ Cache / KV
 │    └─ Routing
 │
 ├─ Compiler API
 │    └─ LLM Provider
 │
 ├─ Session / Realtime
 │    └─ Ephemeral Room
 │
 ├─ Persistent Backend
 │    ├─ Blueprint metadata
 │    ├─ Creator data
 │    └─ Commerce / usage records
 │
 └─ Observability
      ├─ Metrics
      ├─ Logs
      └─ Error / Recovery Events
```

## 3. Infrastructure Principles
1. **Client-first：** 能在瀏覽器完成的運算不進 server。
2. **Edge-first：** routing、cache、輕量 gate 優先在 edge。
3. **Ephemeral-first：** Tier 1 不建立不必要的永久資料。
4. **LLM-once：** 避免 runtime interaction 每次觸發 LLM。
5. **Isolation：** 一個 component / room / request 的失敗不應擴散。
6. **Provider abstraction：** LLM、KV、Realtime、DB 應透過 adapter 保持可替換。

## 4. Tier-to-Infra Mapping

| Tier | Runtime | Data | Typical Infra |
|---|---|---|---|
| Tier 1 | Browser | Local / ephemeral | CDN + Edge + client runtime |
| Tier 2 | Browser + server workers | Persistent | API + DB + worker + paid APIs |
| Tier 3 | 不執行或安全 fallback | Minimal | Edge gate / safe response |

## 5. Cache Architecture
候選流程：

```
Prompt
 ↓
Normalization
 ↓
Cache Key
 ↓
Edge KV
 ├─ Hit → Verified LegoSpec
 └─ Miss → Compiler
```

Cache value 應包含：
- LegoSpec
- schema version
- component registry version
- blueprint status
- compiler metadata

「純文字 hash」目前只是候選；後續可研究 canonical intent / semantic cache。

## 6. Realtime
Tier 1 multiplayer 使用 ephemeral room。
候選技術為 PartyKit 類 realtime room。

Working constraints：
- room lifecycle 應有 TTL / idle destruction。
- session state 優先放 memory。
- room limit 目前為候選值，不是正式規格。
- room crash 不應影響其他 room。

## 7. Persistence
只有需要以下能力時才進 persistent backend：
- Creator ownership
- History
- Paid quota
- Published blueprint metadata
- Commerce / settlement
- Long-lived session

## 8. Security Infra
- LLM output → schema validation → allowlist → runtime。
- 不允許 arbitrary JS / eval。
- External URL / media primitive 必須有安全政策。
- Share URL 不承載敏感資料。
- Secrets 只存在 server-side secret store。
- Rate limit / abuse protection 應在 edge/API 層。

## 9. Observability
最低事件：
- request_received
- cache_hit / cache_miss
- generation_failed
- validation_failed
- compile_success
- runtime_component_error
- fallback_rendered
- blueprint_degraded
- room_created / room_destroyed

正式 schema、retention、PII policy 後續定義。

## 10. Cost Architecture
核心成本控制手段：
- Cache hit bypass LLM。
- Tier 1 client execution。
- One-time compilation。
- Ephemeral rooms。
- Tier 2 usage-based charging。
- 不讓低價值/高風險 request 無限制消耗 backend / LLM。

## 11. Open Design Items
- 具體 cloud/provider 組合
- Edge KV 選型
- Realtime 選型
- DB 選型
- worker architecture
- deployment topology
- backup / disaster recovery
- rate limit
- SLO / capacity targets
- observability stack

**Status：Working。**

## 12. Detailed Infrastructure Design Inputs — Working

### 12.1 Serverless + Edge-first Direction
Working direction is **serverless + edge-first + client-first** to minimize fixed infrastructure operations and keep short-lived micro-app execution close to the client where practical.

These are goals, not guarantees:
- Managed infrastructure is preferred; this does not mean literally no backend infrastructure.
- No-traffic cost is not guaranteed to be $0 because providers may charge for storage, observability or other services.
- Edge execution does not mean every operation runs at the physically nearest CDN node.
- End-to-end latency still depends on LLM inference, network path, provider availability and downstream services.
- “3-second generation” should be measured as a product/SLO target.

### 12.2 Candidate Hosting Models
Current candidates are Vercel/Cloudflare-class managed platforms for MVP speed and low operations, and AWS-native services for later granular control if scale/cost/data requirements justify it. No vendor is approved yet. The application contract must remain vendor-neutral.

### 12.3 State / Persistence Infrastructure
Distinguish:
1. Browser state — transient interaction and resumable local state.
2. Share payload — compact, non-sensitive instance state.
3. Ephemeral session state — multiplayer room memory.
4. Persistent records — blueprint, ownership, publishing, history, quota, commerce and required audit/telemetry.

URL Hash is a transport mechanism, not a database. LocalStorage is a local recovery mechanism, not an authoritative persistence layer.

### 12.4 Short-link Strategy
Use short-link/backend indirection when payload size, clean URLs, stable identity/versioning or durable references make embedded URL state impractical.

Candidate flow: **Instance State → serialize/compress → small: URL hash / large or stable: short-link reference → approved backend/KV**.

### 12.5 Cache Strategy
Retain **Prompt → normalization → cache key → Edge KV → verified LegoSpec / compiler**, while distinguishing exact/canonical prompt cache, semantic/canonical-intent cache and published Blueprint reuse. Cache hits must respect LegoSpec version, component registry version, policy/security status and materially relevant context.

### 12.6 Cost Boundary
Optimize for client-side execution, one-time compilation, cache reuse, ephemeral rooms and usage-based backend capabilities only when necessary. Edge infrastructure must not be treated as proof that LLM inference is cheap or free.

### 12.7 Recovery / Durability
Compiler failure → retry/fallback. Runtime failure → client isolation. Room failure → room-level recovery. Persistent backend failure → never silently claim data was saved. Corrupt/unsupported share payload → safe recovery or upgrade path.

### 12.8 Open Infrastructure Questions
- MVP hosting provider and edge runtime limits
- LLM provider/location and latency budget
- KV, realtime and persistent DB choices
- short-link implementation
- payload compression/size threshold
- backup/DR
- SLO/capacity targets
- observability provider

## 13. App Instance Infrastructure — Detailed Working Design

### 13.1 Cost Allocation Model
Working hypothesis:
- Initial semantic compilation is the main LLM-related platform cost.
- Normal UI interaction and deterministic calculations should remain client-side.
- Share/open of a lightweight instance should primarily consume delivery/bandwidth rather than server compute.
- Realtime collaboration, persistent storage, external APIs and Tier 2 workloads introduce additional platform costs.

User-provided estimates such as 0.0003–0.0005 USD per initial generation and “near-zero” sharing/storage are retained as **benchmarks to validate**, not committed cost facts.

### 13.2 Snapshot Storage Tiers
Candidate three-way model:
1. **URL Hash / LocalStorage:** small, ephemeral, non-sensitive instance state.
2. **Short Link / KV or DB:** large payloads, stable references, clean URLs, or durable sharing.
3. **Realtime Room:** shared base contract + ephemeral synchronized state.

A prior “90% lightweight / 10% complex” split is a planning hypothesis only; production distribution should be measured.

### 13.3 Snapshot Hydration
Candidate flow:

```
URL / Short Link / Room
       ↓
Decode / Fetch
       ↓
Schema + Version Validation
       ↓
Blueprint / Spec Resolution
       ↓
Instance State Hydration
       ↓
Local Runtime
```

The system should not call the LLM merely to reconstruct an already-valid shared instance.

### 13.4 Realtime Delta Transport
For shared editing, prefer validated state deltas rather than repeatedly transmitting full WidgetSpec payloads.

Working requirements:
- Base contract/version must be known by all participants.
- Delta schema must be validated.
- Ordering / deduplication / conflict semantics must be defined before production realtime.
- Clients should recalculate deterministic formulas locally where possible.
- Room state should remain ephemeral unless explicitly persisted.

### 13.5 Data Placement Boundary
```
Client
 ├─ UI state
 ├─ deterministic formulas
 ├─ valid WidgetSpec / compatible contract
 └─ local recovery state

Edge/API
 ├─ routing / gate
 ├─ compiler request
 ├─ cache
 └─ short-link / room coordination as required

Persistent backend
 ├─ Blueprint metadata
 ├─ ownership / publishing
 ├─ history
 ├─ quota / commerce
 └─ required durable records
```

### 13.6 Cost/Performance Validation Plan
The following user-provided numbers should become benchmark/SLO candidates rather than assumptions:
- compiler latency target;
- instance hydration target;
- local recalculation target;
- runtime bundle size;
- browser memory target;
- generation token cost;
- snapshot size;
- URL payload threshold;
- realtime delta size and frequency.

Benchmark on representative mobile/desktop devices and real network conditions before locking the figures.

## 14. Infrastructure Questions Added
1. What exact URL payload size/encoding threshold should trigger short-link fallback?
2. What is the minimum durable data required for a short-link?
3. What realtime protocol provides ordering, deduplication and conflict resolution?
4. Which state changes are safe to broadcast to all room participants?
5. What are the bandwidth and observability costs at 1M / 10M / 100M interactions?
6. Which compiler latency and LLM cost targets are realistic for the chosen model/provider?


## 15. Control Plane / Heavy Work Infrastructure — Working

### 15.1 Control Plane Boundary
NFF infrastructure should keep the core platform lightweight. The NFF runtime coordinates UI/state/sync and delegates heavy computation or durable large-scale storage to the appropriate execution plane.

### 15.2 Heavy Work Execution Planes

**Client plane**
- WASM / Web Workers for browser-capable CPU-heavy tasks.
- NFF supplies UI, parameters, progress and result presentation.
- Compute cost is shifted to the user's device, but device capability and browser limits remain constraints.

**External worker/API plane**
- Async Action delegates server-required heavy work to approved cloud APIs or dedicated workers.
- NFF receives status/result through polling or webhook-driven integration.
- External provider/API cost is a real Tier 2 cost and must not be represented as NFF "$0" infrastructure.

**External durable-data plane**
- Large or long-lived datasets can remain in approved external storage/services.
- NFF should hold controlled references/permissions rather than becoming the default large-data store.

### 15.3 Room Chat Infrastructure
Ephemeral room chat fits the realtime session architecture:
- broadcast messages through the room channel;
- room-scoped state may remain in ephemeral memory;
- room destruction removes ephemeral state unless explicitly promoted to persistence.

Long-lived chat requires durable message storage, identity, notification and retention infrastructure and is outside the lightweight room model.

### 15.4 Async Action
Working infrastructure flow:

`Card UI → Async Action → External API/Worker → Webhook/Polling → Result State → Card UI`

The card remains a status/result surface rather than becoming the heavy compute environment.

### 15.5 Compilation Cost / Latency Boundary
Separate infrastructure paths:

**Cold Path**
`Edge/API → Compiler → LLM Provider → Validation → Blueprint/WidgetSpec`

**Warm Path**
`CDN/Edge → Blueprint/Instance Payload → Client Validation/Hydration → Runtime`

Warm-path opening of an already-valid artifact should bypass LLM inference.

### 15.6 Cache / Spec Registry
A verified Blueprint/WidgetSpec can be reused through edge/KV caching or a persistent registry.

Infrastructure requirements:
- version-aware cache keys/metadata;
- policy/security status;
- invalidation when schema/component/policy compatibility changes;
- cache-hit path must still perform appropriate validation.

### 15.7 Loading / Compilation UX Infrastructure
Cold compilation may exceed the runtime-open target. The application should be able to return an immediate lightweight loading response/state while the compiler completes, then hydrate the final WidgetSpec without treating the generation process as a deployment.

### 15.8 Cost Guardrail
Do not collapse these into one "$0" claim:
- client compute;
- NFF platform compute;
- LLM inference;
- external API/worker;
- bandwidth;
- realtime connections/messages;
- storage;
- observability.

They are separate cost dimensions and should be measured separately before formal pricing/SLO decisions.


## 16. Anonymous Identity / Metrics / Cache Economics — Working

### 16.1 Anonymous-first Infrastructure
Avoid creating durable account/DB records for every participant by default. Candidate anonymous continuity uses a random first-party browser identifier plus aggregate telemetry.

Do not assume anonymous mode is literally $0: analytics ingestion, edge requests, bandwidth, abuse controls and observability can still incur cost.

Device fingerprinting is not a default architecture choice because it can create privacy/compliance risk. Prefer first-party random identifiers with clear retention/deletion rules.

### 16.2 Progressive Auth Infrastructure
Persistent identity services become necessary when users request:
- durable ownership/editing;
- cross-device history;
- paid quota/billing;
- publishing/monetization;
- persistent statistics or other account-bound data.

Candidate promotion flow:
`anonymous session → authenticated account → secure artifact claim/migration`

Claim tokens/ownership proofs and replay protections need detailed design.

### 16.3 Measurement Semantics
Track anonymous browser/device cohorts separately from authenticated user cohorts.

Candidate events/dimensions:
- anonymous_id / account_id where applicable;
- create, open, execute, share, remix;
- anonymous_to_registered conversion;
- cohort return;
- cache hit/miss;
- compiler invocation;
- runtime-AI invocation.

Anonymous IDs must not be presented as exact human-user counts.

### 16.4 LLM Cost Boundary
For a verified compiled Blueprint:
- open/share/hydrate → no LLM required;
- deterministic runtime actions → no LLM required;
- cache/registry hit → no LLM required;
- semantic contract change/cache miss/retry/runtime-AI capability → may require LLM.

Thus the cost model should measure **LLM calls per successful compilation/version**, not assume “one LLM call forever.”

### 16.5 Cache Persistence
Blueprint reuse requires a durable-enough cache/registry strategy. URL embedding can distribute a specific artifact, but global reuse/search requires an indexed cache/registry.

Cache lifecycle must define:
- version compatibility;
- TTL/eviction;
- validation/security status;
- semantic equivalence confidence;
- invalidation after runtime/schema/policy changes.


## 17. Content-Addressable Blueprint Infrastructure — Working

### 17.1 CAS Registry
Candidate infrastructure:
`Compiler Candidate → Validate → Canonicalize → SHA-256 (or approved digest) → CAS Registry/Object Store → Edge Cache`

Identical canonical Blueprint content can deduplicate to one stored object.

### 17.2 Common vs Personal Storage
**Common layer:** immutable Blueprint blobs addressed by content ID.

**Personal layer:** lightweight references and account-bound metadata. Personal history/settings/state are stored only when product requirements justify persistence.

This avoids coupling global executable content with per-user authorization records.

### 17.3 Retrieval Path
`HTTP route/room reference → edge lookup → Blueprint object → integrity/compatibility checks → client`

Exact sub-5ms retrieval and zero marginal cost are performance/economic targets, not infrastructure guarantees.

### 17.4 Realtime Binding
Room connection metadata should reference the immutable Blueprint content/version plus room identity. Room mutable state/deltas remain separate from CAS.

Realtime provider should be behind an adapter; current PartyKit references remain candidate implementation details.

### 17.5 CAS Security / Operations
Required detailed design later:
- deterministic JSON canonicalization;
- digest algorithm/version;
- trusted vs untrusted/quarantined registry status;
- schema/component-runtime compatibility;
- policy revalidation;
- cache invalidation;
- garbage collection/reference counting;
- abuse/storage amplification controls;
- maximum Blueprint size;
- authorization for private/unpublished Blueprints;
- moderation/takedown behavior.

A content hash is not an access-control boundary: knowing a hash must not automatically grant access to private content.


## 18. Semantic Compiler Service Boundary — Failure Case Learning

### 18.1 Compiler Service
The open-ended Prompt path should terminate at a controlled NFF compiler service rather than browser-side heuristic synthesis.

Candidate path:
`Browser → NFF Edge/API Compiler Endpoint → LLM Provider Adapter → Structured Candidate → Validation → CAS/Response`

### 18.2 Secret Boundary
Do not expose production LLM provider keys through browser-build environment variables such as `VITE_LLM_API_KEY`. Browser-visible variables are not secret storage.

Compiler endpoint responsibilities should include:
- provider credentials;
- authentication/anonymous quota;
- rate limiting/abuse controls;
- model/provider routing;
- schema version;
- telemetry/cost measurement;
- timeout/retry/circuit breaker;
- validation before trusted-registry admission.

### 18.3 Failure Telemetry Expansion
Add candidate events/reasons:
- `semantic_mismatch`;
- `unsupported_semantics`;
- `compiler_repair_attempted`;
- `compiler_repair_failed`;
- `wrong_archetype_detected`;
- `fallback_semantic_blocked`.

A render-success event must not be treated as task success.

### 18.4 Cache Poisoning Guardrail
A semantically wrong but schema-valid Blueprint must not become globally reusable merely because it has a valid hash.

Trusted Common Pool admission should require the appropriate quality/validation status. Failure reports can quarantine/deprioritize a Blueprint and prevent a bad cached artifact from multiplying globally.


## 19. Compiler Validation / Provider Abstraction — Working

### 19.1 Provider Adapter
The compiler service should expose an NFF-owned interface independent of any one model vendor.

Candidate:
`CompilerService → ModelProviderAdapter → selected provider`

Vercel AI SDK may be one implementation option. Provider portability is an architectural requirement; a specific SDK is not yet approved as permanent infrastructure.

### 19.2 Structured Output Pipeline
Candidate:
`Prompt + Registry Context + Schema → Model → Structured Candidate → Runtime Schema Validation → Cross-field Validation → Security/Capability Gate → CAS`

Only the final validated artifact can enter a trusted reusable pool.

### 19.3 Retry
“Retry once” is currently a candidate policy, not a fixed invariant.

Retry design must define:
- retryable error classes;
- maximum attempts;
- repair context;
- timeout/token budget;
- circuit breaker;
- telemetry.

Semantic mismatch may require user refinement rather than blind automatic retry.

### 19.4 Expression Engine Security
Do not equate “not eval()” with “100% sandbox safe.”

Any expression library must be threat-modeled and tested for:
- available functions/operators;
- object/property access;
- prototype/property escape;
- resource exhaustion;
- recursion/complexity;
- oversized arrays/expressions;
- deterministic execution requirements.

Prefer an explicit NFF function allowlist/AST grammar. `expr-eval` remains a candidate until validated against the threat model.

### 19.5 Patch Engine Security
Preset/delta patches require:
- allowed operations;
- allowed paths;
- schema-valid resulting state;
- size/operation limits;
- rejection of protected metadata/contract mutations during runtime state patches.

### 19.6 Performance Claims
User-provided values such as Zod validation “1ms”, edge retrieval “<5ms” and local update “0ms” remain benchmark targets/examples, not guarantees.


## 20. Cache Identity / Registry Distribution / Share Transport — Working

### 20.1 Two Different Hash Problems
Do not conflate Prompt hashing with Blueprint CAS.

**Prompt/canonical-intent cache key**
Used to search for a reusable candidate Blueprint.

**Blueprint content hash**
Derived from canonical validated Blueprint content and used as immutable content identity.

A raw “remove punctuation/whitespace then SHA-256” prompt key can be an exact-cache optimization, but cannot provide semantic deduplication by itself.

### 20.2 Cache Admission
A cache entry should reference validation metadata:
- schema version;
- capability registry version;
- runtime compatibility;
- policy/security status;
- quality/trust status;
- created/validated timestamps as appropriate.

“Validated” means it passed defined gates; it does not mean bug-free.

### 20.3 Compiler Context Distribution
Generate model capability context from the Capability Registry rather than hand-editing a separate whitelist in prompts. This reduces drift among:
- runtime components;
- schema;
- compiler instructions;
- tests;
- documentation.

### 20.4 URL Snapshot Safety
Compressed URL payloads require:
- maximum encoded/decoded size;
- decompression-bomb/resource limits;
- schema/version validation;
- integrity checks where appropriate;
- sensitive-field exclusion;
- no assumption that compression makes data private.

### 20.5 Realtime Claims
PartyKit remains a candidate provider behind an adapter. “0ms sync” is not a literal guarantee. Room destruction/idle TTL must be explicitly configured/verified against chosen provider semantics.

### 20.6 Provider-neutral Durable Storage
Supabase, Cloudflare KV/object storage or other services remain candidates. Logical architecture must not couple ownership/auth/version semantics to one vendor.

### 20.7 Self-Correction Loop
Candidate:
`validation error → sanitized structured repair feedback → compiler repair attempt → full revalidation`

Do not blindly echo raw internal errors, secrets or unsafe payloads back to a model. Retry remains bounded by retry/cost/circuit-breaker policy.


## 21. Contract Security / Determinism / Capability Context — Working

### 21.1 JSON Is Transport, Not Sandbox
Security controls must apply to JSON fields that can influence runtime behavior:
- expression grammar;
- URLs/media sources;
- rendered text/HTML policy;
- patch paths;
- action/effect names;
- component props;
- payload/decompression sizes.

No `eval()` / `new Function()`; only allowlisted interpreters/capabilities.

### 21.2 Compiler Metadata
Compiler capability metadata should be generated/versioned from Registry SSOT for each compilation request. A request sees a fixed capability snapshot; the platform can evolve the registry over time.

Store/associate relevant registry/schema version with compiled Blueprints for later compatibility checks.

### 21.3 Replay / Cache Compatibility
CAS identity alone is not enough for deterministic execution across runtime upgrades.

Cache/replay metadata should consider:
- schema version;
- runtime compatibility;
- capability versions;
- policy status;
- optional RNG seed/external snapshot identifiers.

### 21.4 Latency / Cost Corrections
Do not encode “0ms”, “zero latency”, “100% sandbox safety”, “99.9% valid”, or “0 cost” as guarantees.

Use measurable SLO/benchmark language once providers, payload sizes, regions and test methodology are defined.

### 21.5 URL / WebSocket Safety
JSON portability does not imply arbitrary payload safety. URL snapshots and realtime messages still require schema validation, authorization where relevant, size/rate limits and sanitization.

Compression is not encryption.
