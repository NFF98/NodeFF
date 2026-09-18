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
