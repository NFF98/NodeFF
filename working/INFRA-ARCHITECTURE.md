# NodeFF 基礎設施架構

> 狀態：Working。除非依 NodeFF SSOT 流程正式升格，否則不具權威性。

## 1. 基礎設施使命

NodeFF Infrastructure 採用 **client-first、edge-assisted 的 Control Plane**。

負責：
- request routing；
- semantic compilation；
- Blueprint validation／distribution；
- identity／quota；
- lightweight persistence；
- realtime coordination；
- telemetry；
- external capability orchestration。

它不是每次互動與所有 heavy workload 的預設 execution plane。

> **NFF 是 Lightweight Control Plane，不是 Heavy Compute Plane。**

---

## 2. 邏輯拓撲

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

## 3. Cold Path 與 Warm Path

### Cold Path — 新 Intent 或語意已變更

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

Cold Path 包含 model／provider latency 與 compiler cost。

### Warm Path — 既有 Blueprint

```text
Reference / Snapshot
 → Resolve / Decode
 → Compatibility + Trust Check
 → Hydrate
 → Execute Locally
```

Warm execution 不應只因「開啟／互動既有有效 artifact」而呼叫 LLM。

---

## 4. Compiler Service 邊界

Production 環境的所有 model compilation 都必須經過 NFF 控制的 endpoint。

責任：
- provider credentials；
- anonymous／account quota；
- rate limiting；
- abuse／policy gate；
- model routing；
- versioned Capability Registry context；
- schema／rule version selection；
- timeout／token budget；
- repair policy；
- cost／latency telemetry；
- trusted-admission validation。

Provider secret 永遠不得進入 browser-visible environment variables。

Compiler service 必須提供 NFF 自有介面，讓 model vendor 可以替換。

---

## 5. Compiler Context

Compiler 接收由 Capability Registry 產生的版本化 capability snapshot。

不得再人工維護第二份 primitive whitelist 於 System Prompt。

Compiler context 應包含：
- available primitives；
- allowed props；
- state contracts；
- actions／events；
- Rule VM operators；
- capability limits；
- degradation rules；
- schema／runtime version。

每次 compilation request 都使用固定版本的 capability snapshot，即使平台本身持續演進。

---

## 6. Validation 與 Trust Admission

Trusted Blueprint 的 admission path：

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

Schema-valid candidate 不等於 trusted。

可能的 registry state：
- untrusted；
- validating；
- trusted；
- degraded；
- quarantined；
- deprecated。

Cache hit 不得繞過與該 artifact trust／version 狀態相對應的檢查。

---

## 7. Repair 與 Retry

Structural／contract failure 可進入有界 repair loop：

```text
Validation Failure
 → sanitized machine-readable errors
 → compiler repair
 → full revalidation
```

Policy 必須定義：
- retryable error classes；
- maximum attempts；
- token／time budget；
- circuit breaker；
- 如允許時的 provider fallback；
- telemetry。

Semantic mismatch 與 malformed output 不同；前者可能需要使用者 refinement，而不是 blind retry。

Repair prompt 不得包含 secret 或不安全的 internal payload。

---

## 8. Blueprint Registry 與 Content Addressing

經驗證的 immutable Blueprint content 可進入 content-addressable Common Pool。

```text
Validated Blueprint
 → deterministic canonical serialization
 → digest
 → immutable content object
 → registry metadata
 → edge/cache distribution
```

必須分離保存：
- content object；
- logical Blueprint identity；
- lineage／revision；
- trust／policy metadata；
- user ownership／save pointer；
- Instance state。

知道 hash 不等於具有 authorization。

Private／unpublished artifact 仍需要獨立存取控制。

---

## 9. Canonicalization

Content hash 必須建立在 deterministic canonicalization 之上。

Canonicalization spec 必須定義：
- key ordering；
- number representation；
- omitted／default fields；
- 必要時的 Unicode normalization；
- schema version；
- digest algorithm／version。

邏輯上等價的內容，不應只因 JSON formatting 或 key ordering 不同而產生不同 identity。

---

## 10. Cache Architecture

存在三種不同問題：

### Exact Prompt Cache
針對完全相同或嚴格 canonicalized text 的快速 reuse。

### Canonical-Intent / Semantic Reuse
尋找語意上可能符合的 trusted Blueprint family。

### Blueprint Content Cache
依 immutable content hash 做精確 retrieval。

三種 key 不可混用。

「去標點／空格後做 Prompt SHA-256」最多只是 exact-cache optimization，不是 semantic identity。

Cache metadata 至少需要：
- schema version；
- Registry version；
- Runtime compatibility；
- policy／security status；
- trust／quality status。

---

## 11. Cache Poisoning 防禦

Blueprint 可能：
- syntax valid；
- schema valid；
- runtime renderable；
- 但 semantic wrong。

因此：
- Trusted Common Pool admission 必須包含 shape 之外的 quality status；
- semantic mismatch report 會影響 reuse confidence；
- unhealthy version 可被 quarantine／deprioritize；
- 修復後產生新 revision，不修改 immutable content。

系統不能只因一份 Blueprint 很便宜可 reuse，就把錯誤大規模放大。

---

## 12. Portable Snapshot Transport

只適用於小型、非敏感 snapshot。

```text
Canonical Snapshot
 → compress
 → URL Fragment
 → decode
 → decompression/resource guard
 → schema/version/security validation
 → hydrate
```

控制：
- maximum encoded size；
- maximum decoded size；
- decompression limits；
- sensitive-field exclusion；
- 必要時的 integrity／version checks。

Compression 不提供 confidentiality。

URL Hash 是 transport，不是 authoritative persistence。

---

## 13. Durable Reference Path

以下情況使用 short-link／backend reference：
- payload 太大；
- 需要 stable identity；
- 需要 access control；
- 需要 durable ownership／history；
- sensitive data 不應出現在 URL。

Short reference 解析到受授權的 server-side metadata／content reference，不代表 Blueprint blob 本身可變。

---

## 14. Realtime Room

Realtime 是選用能力，不是預設 execution model。

```text
Immutable Blueprint Reference
 + Room ID
 + Mutable Room Instance State
 + Ordered Validated Deltas
```

Provider 必須藏在 adapter 後方。

Protocol 必須定義：
- room identity；
- presence；
- join／reconnect；
- ordering；
- deduplication；
- conflict handling；
- state snapshot／recovery；
- idle TTL；
- participant limits；
- rate limits；
- abuse controls。

不假設 literal「0ms sync」。

Ephemeral room chat 可以共用 realtime boundary。Discord／Telegram 型長期歷史、background notification、durable messaging 不屬於 NFF core，除非未來另行定義成獨立 capability。

---

## 15. Heavy Work Delegation

### Browser Compute

適合時使用 Web Workers、WASM 或 browser-native compute。

NFF 負責：
- parameters；
- progress；
- result visualization。

### External Job

```text
NFF Action
 → external API/worker
 → job/status reference
 → webhook/poll/event
 → result
 → Player presentation
```

用於：
- heavy AI；
- media generation；
- long-running processing；
- large database query；
- specialized compute。

### Durable Large Data

大型長期資料應放在適合的 external／backend storage。NFF 僅保存必要的 controlled reference、permission 與 presentation logic。

---

## 16. Runtime Rule VM

較佳 infrastructure contract：
- typed Rule AST；
- explicit operator／function registry；
- deterministic evaluation semantics；
- versioned grammar；
- execution step／size limits；
- no host-object access；
- no arbitrary property traversal；
- no arbitrary code。

若考慮 `expr-eval` 等 expression library，必須先滿足 NFF threat model。「不是 eval」不是安全證明。

Threat model 包含：
- exposed functions／operators；
- property／prototype escape；
- recursion；
- CPU exhaustion；
- memory exhaustion；
- oversized collections；
- non-determinism。

---

## 17. Patch 與 Delta Security

Runtime state patch 必須具備：
- allowlisted operations；
- allowlisted mutable paths；
- type validation；
- resulting-state validation；
- maximum operation count；
- maximum payload size。

Runtime patch 不得修改：
- schema；
- capability declaration；
- ownership；
- trust metadata；
- protected Blueprint fields。

Semantic Blueprint refinement 必須經過 Compiler／Validation path；只要 content 改變，就產生新的 content identity。

---

## 18. External Asset 邊界

Remote 3D、Lottie、Video 等 media 都是 untrusted external content。

控制可能包括：
- allowed schemes／origins；
- CSP；
- MIME／content checks；
- size limits；
- redirect rules；
- privacy／tracking restrictions；
- optional proxy／cache；
- timeout／fallback behavior。

單純通過 `url()` 格式驗證不足以代表安全。

---

## 19. Resource Budgets

Schema-valid payload 仍可能造成 Runtime resource exhaustion。

必須為下列項目設定明確 budget：
- Blueprint bytes；
- decoded snapshot bytes；
- component nodes；
- nesting depth；
- Repeater expansion；
- Rule AST nodes；
- evaluation steps；
- state size；
- patch operations；
- media count；
- external asset size。

超過 resource budget 時應 fail closed，或依 contract policy 明確降級。

---

## 20. Determinism 與 Replay Metadata

精確 replay 可能需要：
- content hash；
- schema version；
- Runtime version；
- capability versions；
- Rule VM version；
- initial state；
- RNG seed／outcome log；
- ordered actions／deltas；
- external-data snapshot／version。

Content addressing 本身無法保證跨 Runtime／環境版本的 replay equivalence。

---

## 21. Identity 與 Progressive Auth Infrastructure

預設 Consumer path：
- 不強制註冊；
- 需要 continuity 時使用 privacy-conscious first-party `anonymous_id`。

只有 durable account-bound value 才導入 authentication。

```text
anonymous_id
 → create/use/share
 → durable value requested
 → authenticate
 → prove claim eligibility
 → associate/migrate eligible records
```

持有 public／shared link 不足以證明 ownership。

Device fingerprinting 不作為預設 identity mechanism。

---

## 22. Data Placement

### Browser
- transient UI state；
- 一般 Instance state；
- cached trusted Blueprint；
- local recovery state。

### Share Transport
- 明確可分享、非敏感的 snapshot／context。

### Ephemeral Backend
- room state；
- presence；
- live deltas；
- short-lived job／session coordination。

### Durable Backend
- accounts；
- ownership／save pointers；
- publishing metadata；
- quota／billing；
- 必要時的 history；
- commerce；
- trusted registry metadata；
- protected references。

### Never Client-Exposed
- provider secrets；
- privileged credentials；
- signing keys。

LocalStorage 只是 local recovery convenience，不是 authoritative persistence。

---

## 23. Telemetry 與 Reliability Signals

核心 events 包括：
- compilation started／completed／failed；
- validation failure；
- semantic mismatch；
- unsupported semantics；
- repair attempted／failed／succeeded；
- wrong composition／archetype；
- runtime component error；
- degraded／fallback render；
- Blueprint opened；
- Blueprint remixed；
- share opened；
- capability invoked。

必須區分：
- render success；
- runtime success；
- task-success proxy；
- user correction／refinement。

Telemetry 必須另有 privacy、retention 與 reuse governance。

---

## 24. Security Invariants

1. Browser code 不得包含 provider secret。
2. Blueprint 不得包含任意 JavaScript。
3. 不使用 `eval()` 或 `new Function()`。
4. JSON 是資料 transport，不自動等於 sandbox。
5. 只有 registered component／operator／action 可以執行。
6. Remote content 必須受限制。
7. Untrusted boundary 需要重新 validation。
8. Resource budget 必須執行。
9. Cache 不得繞過 policy／trust checks。
10. Hash 不等於 authorization。
11. Compression 不等於 encryption。
12. Unknown capability 必須 fail closed。
13. Error Boundary 是 defense-in-depth，不是主要 validation。
14. Semantic trust 與 schema validity 必須分離。

---

## 25. Vendor Abstraction

已討論候選包括：
- Vercel／Cloudflare；
- Supabase；
- PartyKit；
- OpenAI／Anthropic／DeepSeek／Groq 或其他 model provider；
- Zod；
- Zustand；
- React；
- `lz-string`；
- `expr-eval`。

未經明確批准，任何一項都不是架構依賴。Provider-specific behavior、pricing、quota 不得進入核心 protocol semantics。

---

## 26. Performance 與 Cost Claims

以下在 benchmark 前都只是 measurement target／hypothesis：
- 0ms local interaction；
- sub-5ms／sub-10ms cache；
- 1ms validation；
- 90% cost reduction；
- zero marginal cost；
- 100% sandbox safety；
- 99.9% structured correctness；
- fixed free-room limits；
- exact generation latency；
- exact provider unit economics。

未來 Performance requirement 應使用可測量的 SLO，並明確標示：
- workload；
- region；
- payload size；
- percentile；
- provider／configuration；
- test methodology。

---

## 27. 尚未決定的 Infrastructure 項目

- hosting／edge provider；
- model adapter implementation；
- realtime provider／protocol；
- durable store／object store；
- CAS canonicalization／digest；
- Registry persistence／distribution；
- Rule VM implementation；
- retry／circuit-breaker policy；
- trust／admission scoring；
- URL snapshot size threshold；
- media proxy／source policy；
- room limits／TTL；
- privacy／telemetry retention；
- private Blueprint authorization model。
