# NodeFF Infrastructure Architecture

> 狀態：Current Working Baseline / POC。本文是 NodeFF Infrastructure 的設計方案，不是討論紀錄。目標是在 **短期最低成本驗證核心循環** 的同時，不阻斷中期 Reuse / Identity / Creator Value 與長期 Intent Commerce / Capability Network。

# 1. Architecture Decision

NodeFF 採用：

> **Browser Runtime + Global Edge Control Plane + PostgreSQL System of Record + Pluggable External Capability Plane**

Phase 1 建議實作組合：

| Layer | Phase 1 Baseline |
|---|---|
| Web / CDN | Cloudflare Pages / Static Assets |
| Edge / Serverless API | Cloudflare Workers |
| Runtime | Browser-side React Universal Runtime |
| Durable Database | Supabase PostgreSQL |
| LLM | Provider Adapter，僅由 Serverless Compiler 呼叫 |
| Capability Registry | Versioned code/build artifact |
| Blueprint Cache | Content-hash URL + CDN immutable cache |
| Identity | First-party anonymous ID |
| Telemetry | Batched meaningful events → Postgres |
| Auth / Realtime / Storage | 先不啟用；需要時沿用 Supabase 能力 |
| Queue / Worker / Vector DB | Phase 1 不建立 |

這不是因為 Cloudflare 或 Supabase 是產品核心，而是目前這個組合最符合：

- No install；
- Client-first；
- Compile Once → Reuse Many → Execute Locally；
- Anonymous-first；
- Share / Remix；
- 低固定成本；
- 小團隊低維運；
- 未來可逐層擴張；
- 不把 Protocol 綁死在單一 Vendor。

---

# 2. 設計原則

## 2.1 Runtime 與 Control Plane 分離

NodeFF 最大量的互動應發生在 Browser：

~~~text
Button
Dice
Wheel
Timer
Form
Rule
Animation
State Transition
        ↓
Browser Runtime
~~~

Server 不應成為每次互動的中介。

Server / Edge 只處理：

~~~text
Compile
Validate
Resolve
Share
Identity
Telemetry
External Capability
Durable State
~~~

核心原則：

> **Serverless 不是把傳統 Server 換個名字；真正省成本的是讓大部分 Runtime 根本不需要 Server。**

---

## 2.2 Expensive Path 與 Cheap Path 分離

### Cold Path

~~~text
Intent
 → Edge Gate
 → Reuse Lookup
 → Semantic Compiler
 → Validation
 → Blueprint
 → Store
 → Browser Runtime
~~~

主要成本：
- LLM；
- validation；
- durable write。

### Warm Path

~~~text
Blueprint Hash / Share Reference
 → CDN / Edge
 → Blueprint
 → Browser Hydration
 → Local Execution
~~~

主要目標：

> **0 runtime LLM call for normal deterministic interaction**

### Heavy Capability Path

~~~text
Runtime Action
 → Capability Gateway
 → External Provider / Worker
 → Result
 → Validated State Update
~~~

只有真的需要 AI、media、booking、payment、specialized compute 才進這條路。

---

# 3. 整體架構圖

~~~mermaid
flowchart TB
    USER[User / Shared Recipient]

    subgraph RUNTIME["Browser Runtime Plane"]
        WEB[React Web App]
        PLAYER[Universal Runtime]
        CAP[Capability Runtime]
        RULE[Rule VM]
        STATE[Instance State]
        LOCAL[Local Cache / Recovery]
    end

    subgraph EDGE["Global Edge Control Plane - Cloudflare"]
        CDN[Static Assets / CDN]
        ROUTER[Edge Router / Policy / Quota]
        COMPILER[Compiler API]
        VALIDATOR[Blueprint Validation]
        RESOLVER[Blueprint / Share Resolver]
        EVENTS[Telemetry Intake]
        GATEWAY[External Capability Gateway - later]
    end

    subgraph DATA["Durable State Plane - Supabase"]
        PG[(PostgreSQL)]
        AUTH[Auth - activate later]
        REALTIME[Realtime - activate later]
        STORAGE[Object Storage - activate later]
        VECTOR[pgvector - activate later]
    end

    subgraph EXT["External Capability Plane"]
        LLM[LLM Provider]
        EXTAPI[AI / Search / Booking / Payment / Media / Other API]
    end

    USER --> CDN
    CDN --> WEB
    WEB --> PLAYER
    PLAYER --> CAP
    PLAYER --> RULE
    PLAYER --> STATE
    PLAYER --> LOCAL

    WEB --> ROUTER
    ROUTER --> COMPILER
    COMPILER --> LLM
    COMPILER --> VALIDATOR
    VALIDATOR --> PG

    WEB --> RESOLVER
    RESOLVER --> PG

    WEB --> EVENTS
    EVENTS --> PG

    PLAYER -. only when required .-> GATEWAY
    GATEWAY -. later .-> EXTAPI

    PG -. middle term .-> AUTH
    PG -. middle term .-> REALTIME
    PG -. middle term .-> STORAGE
    PG -. reuse evidence .-> VECTOR
~~~

重點：

> **Phase 1 實際必須運行的只有 Browser + Cloudflare Edge/Serverless + PostgreSQL + LLM。**

圖中的 Auth、Realtime、Storage、Vector、External Gateway 是相同架構的擴張點，不是 Phase 1 dependency。

---

# 4. 為什麼是 Cloudflare Edge + Supabase Postgres

## 4.1 Cloudflare 作為 Edge / Serverless

NodeFF 適合 Global Edge 的原因：

- Web App 靜態資源可全球 CDN 發布；
- API 大部分是 short-lived / I/O-heavy；
- LLM Compiler 不需要常駐 Application Server；
- Share Resolver 天然適合 Edge；
- 流量初期不可預測；
- 不需要先維護 VM / container cluster / Kubernetes。

Cloudflare 在 Phase 1 的角色只需要：

~~~text
Static Hosting
+ Edge Routing
+ Serverless API
+ CDN Cache
~~~

不把整個 Cloudflare product catalog 一開始全部使用。

---

## 4.2 PostgreSQL 作為唯一 System of Record

NodeFF 的核心資料天然是關聯型：

~~~text
anonymous identity
 → intent
 → blueprint
 → share
 → remix
 → lineage
 → creator
 → ownership
 → entitlement
 → transaction
~~~

因此 PostgreSQL 比一開始使用多個 NoSQL / KV / Vector Database 更適合。

Postgres 同時能承載：
- structured metadata；
- JSONB Blueprint；
- lineage；
- ownership；
- anonymous evidence；
- creator relationships；
- entitlement / commerce metadata；
- future vector embeddings。

原則：

> **先用一個資料庫解決 90% 問題；只有 access pattern 證明需要時才拆。**

---

## 4.3 為什麼 Phase 1 使用 Supabase Postgres

Supabase 的價值不是「現在全部使用」，而是：

~~~text
Phase 1
Postgres

需要後
+ Auth
+ Realtime
+ Storage
+ pgvector
~~~

因此中期可以擴張而不必立刻新增四個不同 Vendor。

但 NFF 的 Repository / Identity / Realtime / Storage 都必須保留 Adapter Boundary，不讓 Supabase API 成為 LegoSpec / Runtime Protocol 的一部分。

---

# 5. Phase 1 Runtime Plane

Browser 是主要 execution plane。

~~~text
React
 ├─ Universal Runtime
 ├─ Capability Registry Runtime
 ├─ Rule VM
 ├─ Instance State
 └─ Local Cache
~~~

Phase 1 Runtime 原則：

1. Existing Blueprint 一般互動完全 local。
2. Runtime 不猜 free-form Intent。
3. Runtime 不直接持有 privileged secrets。
4. Runtime AI 必須是明確 Capability，不是預設 execution path。
5. Heavy Compute 優先使用 Browser Worker / WASM；真的不能本地做才外送。
6. Capability Contract 決定哪些 state 可 share、persist、sync、meter。

---

# 6. Capability Registry 的 Infrastructure 位置

Phase 1 的 Capability Registry **不應先放 Database 做成動態服務**。

建議：

> **Registry = versioned source artifact in code repository → build-time generated machine-readable snapshot**

同一份 source 產生：

~~~text
Compiler Context
Validator Schema
Runtime Registration
Capability Documentation
Compatibility Metadata
~~~

好處：
- 沒有額外 Registry database/service；
- 不會有 Compiler / Validator / Runtime 三份 allowlist 漂移；
- deployment 可以精確綁定 Registry version；
- POC 階段最容易測試。

中長期第三方 Capability Network 出現後，才新增：

~~~text
Static Trusted Registry
        +
Dynamic Certified Provider Registry
~~~

不需要 Phase 1 就建立 Marketplace Registry Service。

---

# 7. Blueprint Storage：Phase 1 就保留未來 Reuse 能力

Blueprint 採：

> **immutable canonical content + content hash + separate lineage / ownership**

Phase 1 可直接在 PostgreSQL 保存：

~~~text
blueprint_content
- content_hash
- canonical_blueprint JSONB
- schema_version
- registry_version
- trust_status
- created_at

blueprint_lineage
- child_hash
- parent_hash
- relation_type
- created_at
~~~

Personal / Identity metadata另外保存，不複製 Blueprint body。

這可以支援：

~~~text
短期
Share / Remix

中期
Trusted Reuse / Creator / Ownership

長期
Capability / Commerce lineage
~~~

不需要 Phase 1 建立獨立 CAS service。

---

# 8. Blueprint Delivery：不用先買 KV

Phase 1 不建議把 Edge KV 當必要基礎設施。

對 immutable Blueprint：

~~~text
GET /b/{content_hash}
 → Edge Resolver
 → Postgres on cache miss
 → Cache-Control: immutable
 → CDN caches response
~~~

結果：

~~~text
第一次
CDN miss → DB

之後
CDN hit → Browser
~~~

因為 content hash 改變就代表新 Blueprint，所以 immutable CDN cache 很自然。

這比一開始維護：

~~~text
DB + KV + CDN
~~~

更簡單、更便宜。

未來若量測發現：
- prompt → blueprint lookup 很熱門；
- semantic lookup 成本高；
- metadata lookup 成為瓶頸；

再加入 Edge KV。

---

# 9. Sharing Architecture

NodeFF 保留三種分享模式，但按需求啟動。

## Mode A — Portable Snapshot

適合：
- 小；
- 非敏感；
- ephemeral；
- 不需要 ownership。

~~~text
URL Fragment
 → Decode
 → Validate
 → Runtime
~~~

優點：幾乎零 backend retrieval cost。

限制：URL size、privacy、版本 compatibility。

## Mode B — Durable Blueprint Reference

~~~text
/share/{id}
 → Edge
 → Blueprint Hash
 → CDN / DB
 → Runtime
~~~

適合：
- stable link；
- analytics；
- lineage；
- future ownership。

## Mode C — Live Room

中期或有 POC Evidence 後：

~~~text
Blueprint Hash
 + Room ID
 + Instance State
 + Realtime Delta
~~~

Realtime 永遠同步 Instance，不修改 immutable Blueprint。

---

# 10. Anonymous Identity 與 Evidence

Phase 1：

~~~text
random first-party anonymous_id
 → create
 → use
 → share
 → open
 → remix
~~~

不使用 fingerprinting。

初始 logical data：

~~~text
anonymous_identity
compiler_run
blueprint_content
blueprint_lineage
share
product_event
semantic_feedback
~~~

Telemetry 不應記錄每個 local UI render。

只記錄對產品有意義的 events，例如：
- compilation outcome；
- capability selected；
- semantic mismatch；
- share；
- open；
- use；
- remix；
- correction；
- failure。

Client 應 batch telemetry，避免每次 interaction 都產生一個 Server request。

---

# 11. Phase 1 Database Boundary

Phase 1 PostgreSQL 主要做：

- anonymous continuity；
- immutable Blueprint；
- lineage；
- share reference；
- compiler evidence；
- product evidence。

不做：
- realtime game-state write on every click；
- raw runtime event firehose；
- large media；
- long-running job state machine；
- dedicated semantic vector store；
- analytics warehouse。

原則：

> **Database 保存 durable truth，不保存每個瞬間。**

---

# 12. Phase 1 成本模型

Infrastructure 成本設計順序：

## 1. 把 Execution 留在 Browser

最高價值的成本控制。

## 2. Compile Once

LLM 只在 semantic compilation / refinement 時使用。

## 3. Immutable Blueprint CDN Cache

讓熱門 Shared App 不反覆打 DB。

## 4. One Database

Phase 1 不同時養：
- Postgres；
- KV；
- Vector DB；
- Analytics DB；
- Queue storage。

## 5. Meaningful Telemetry Only

避免 event volume 自己製造 Infra Cost。

## 6. No Always-On Server

不用 VM、Kubernetes、常駐 Node server。

因此 Phase 1 主要 variable cost 仍應是：

> **LLM Compilation + 真正發生的 Serverless / DB usage**

而不是 Runtime interaction。

---

# 13. 中期：Reuse / Identity / Creator Value

中期不是換架構，而是啟用 Phase 1 預留的能力。

## Identity

啟用 Supabase Auth 或同等 Adapter：

~~~text
anonymous_id
 → authenticate
 → ownership claim
 → user_id
~~~

保留原本：
- Blueprint lineage；
- share history；
- creator artifacts；
- eligible anonymous evidence。

## Reuse

先使用 PostgreSQL 做：
- exact / structured retrieval；
- Blueprint family metadata。

有足夠 Evidence 後，再在相同 Postgres 啟用 pgvector：

~~~text
Intent Embedding
 → Candidate Blueprint Families
 → Compatibility / Trust Check
 → Adapt / Validate
~~~

因此中期不需要立刻購買獨立 Vector DB。

## Creator Value

增加：
- ownership；
- attribution；
- publishing；
- save / history；
- premium entitlement。

這些是 metadata / identity layer，不修改 immutable Blueprint core。

## Realtime

若 Social / Multiplayer POC 證明必要：

第一選擇先使用已整合的 Supabase Realtime 或同等 Adapter。

只有當：
- concurrency；
- room model；
- latency；
- cost

證明不適合，才切換 specialized realtime provider。

## Storage

有 image / audio / video / 3D asset 後才啟用 Object Storage。

第一階段可沿用 Supabase Storage；media egress 成為主要成本後，再評估 R2 / S3 類型 provider。

---

# 14. 中期 Heavy Capability

只有 Runtime 無法有效完成時加入：

~~~text
Capability Action
 → Edge Gateway
 → Job / External API
 → job_id
 → status
 → result
 → validated update
~~~

需要以下 workload 才建立 Queue / Background Worker：
- media generation；
- heavy AI；
- batch processing；
- long-running external workflow。

不要因為「未來可能需要」就讓 Phase 1 所有 request 都進 Queue。

---

# 15. 長期：Intent Commerce / Capability Network / Orchestration

長期新增的核心不是另一套 App Runtime，而是：

> **Capability Gateway + Provider Registry + Entitlement / Metering / Transaction Layer**

~~~mermaid
flowchart LR
    R[NodeFF Runtime]
    G[Capability Gateway]
    P[Provider Registry]
    E[Entitlement / Policy]
    M[Metering]
    T[Transaction / Settlement]
    X[External Capability Providers]

    R --> G
    G --> P
    G --> E
    G --> X
    G --> M
    M --> T
~~~

Capability Card 從 Day 1 預留的：
- provider identity；
- cost class；
- entitlement；
- metering hook；
- auth requirement；
- execution location；

就是未來接入這層的橋樑。

長期仍維持：

~~~text
Intent
 → Capability Selection
 → Blueprint
 → Runtime
 → Capability Gateway only when required
~~~

不能變成：

~~~text
Intent
 → all interactions through central commerce server
~~~

否則會破壞 NodeFF 的成本模型與即時性。

## Heterogeneous Orchestration Plane

當真實需求出現多步、跨 Provider、長時間執行時，才新增獨立 Orchestration Plane：

~~~text
Capability Action
→ Orchestration Contract
→ Durable Workflow State
→ Provider / Worker Steps
→ Validate Each Result
→ Retry / Recovery / Compensation
→ Final Outcome
~~~

Infra 規則：
- NFF 自己定義 workflow contract。
- 外部 workflow engine 必須放在 Adapter 後，可替換。
- workflow state 與 Browser Instance 分離。
- 每個 step 必須可追蹤 provider、version、attempt、timeout、result。
- Phase 1 不需要 workflow engine；只有 evidence 證明 multi-step durable work 成立才導入。

---

# 16. 長期 Data / Platform Scaling

只有指標證明需要才逐項啟動：

## Database Scale
- read replica；
- partitioning；
- connection pooling；
- region strategy。

## Analytics
當 Postgres telemetry 不再適合 operational + analytics 共用時，才導出到 warehouse / event platform。

## Cache
熱門 metadata / semantic retrieval 成為瓶頸後才加 dedicated distributed cache。

## Multi-region
Global static / edge 可以從 Day 1 全球化。

Database 不需要 Day 1 multi-region write。

只有：
- geographic latency；
- availability target；
- compliance；
- scale

證明需要後才增加 multi-region data strategy。

## Commerce Reliability
เงินจริง交易出現後，才加入：
- idempotency；
- durable transaction log；
- reconciliation；
- webhook processing；
- outbox/event workflow；
- settlement audit。

---

# 17. Vendor Lock-in Boundary

以下不能出現在 LegoSpec 核心語意中：

- Cloudflare Worker；
- Supabase table/API；
- specific LLM vendor；
- realtime vendor；
- payment vendor；
- object-storage vendor。

必須經過 NFF-owned interfaces：

~~~text
CompilerAdapter
BlueprintRepository
IdentityProvider
RealtimeProvider
ObjectStore
CapabilityProvider
PaymentProvider
WorkflowEngineAdapter
ProviderRegistry
TelemetrySink
~~~

所以 Phase 1 可以選成本最低、開發最快的 Vendor，中長期需要更換時不用重寫 Blueprint / Runtime。

---

# 18. 不建議的架構

Phase 1 不建議：

## 全部 Server-side Rendering / Server Runtime

會讓每個互動都變成 backend cost，與 NodeFF 核心相反。

## Kubernetes / Microservices

目前沒有 traffic / team / isolation 證據支持這個 operational cost。

## 一開始使用多種 Database

Postgres 已足以支援 POC、中期 identity/reuse 與早期 commerce metadata。

## 一開始建 Dedicated Vector DB

沒有 Blueprint corpus 與 reuse evidence 前是 premature optimization。

## 一開始建 Edge KV as source of truth

KV 適合 cache，不適合 ownership / lineage / commerce truth。

## 一開始把所有 Capability 做成 Remote Service

會犧牲成本、latency、offline-ish local interaction 與 composability。

---

# 19. Infrastructure Evolution Map

~~~text
PHASE 1 — Prove Core Loop

Browser Runtime
      +
Cloudflare Static / CDN
      +
Cloudflare Workers
      +
Supabase PostgreSQL
      +
LLM Compiler

Intent → App → Use → Share → Remix


MIDDLE TERM — Reuse / Identity / Creator

same architecture
      +
Supabase Auth
      +
pgvector when evidence exists
      +
Realtime when use case proves it
      +
Object Storage when media needs it
      +
Background Jobs only for heavy capability


LONG TERM — Commerce / Network

same Runtime + Blueprint model
      +
Capability Gateway
      +
Provider Registry
      +
Entitlement / Metering
      +
Transaction / Settlement
      +
Heterogeneous Orchestration Plane
      +
WorkflowEngineAdapter
      +
Dynamic Certified Provider Registry
      +
specialized scaling only where proven
~~~

---

# 20. 最終 Architecture Thesis

NodeFF 最成本有效的架構，不是找到一個「最便宜的 Cloud」。

真正的成本優勢來自：

> **把 Semantic Intelligence 集中在 Compile，把大量 Interaction 留在 Browser，把 Durable Truth 集中在 Postgres，把 Heavy / Paid Work 明確切成 Capability。**

因此目前推薦基準：

> **Cloudflare Edge/Serverless + Supabase Postgres + Browser Runtime**

是 Phase 1 很適合的組合。

更重要的是，真正需要保護的不是 Vendor choice，而是這四個邊界：

1. **Runtime Plane** — 本地、安全、便宜。
2. **Edge Control Plane** — 無狀態、按需、全球。
3. **Durable State Plane** — PostgreSQL 為真實來源。
4. **External Capability Plane** — Heavy / Paid / Commerce 可插拔。
5. **Orchestration Plane** — 多步、非同步、跨 Provider 工作流可恢復、可替換、可治理。

只要這四個邊界保持穩定，NodeFF 可以從 POC 走到 Reuse / Creator，再走到 Intent Commerce / Capability Network / Heterogeneous Orchestration，而不需要中途推翻整套 Infrastructure。
