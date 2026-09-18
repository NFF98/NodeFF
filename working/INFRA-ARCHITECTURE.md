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
