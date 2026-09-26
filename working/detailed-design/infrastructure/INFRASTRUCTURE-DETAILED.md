# appf2 Infrastructure — Detailed Design

> **PHASE 1 FREEZE AUDIT：PASS — Phase 1 applicable truth passed Final Audit and is eligible for Human-approved Build Freeze; Phase 2/3+ and deferred content are excluded.**

> 狀態：Working Current Truth — consolidated multi-phase detailed owner。
>
> Phase 1 section = BUILD_FREEZE_READY candidate；Phase 2 / 3 / 4+ sections = DEFERRED baseline。Future infrastructure content 同檔存在不代表 provider / scaling activation。

# appf2 Infrastructure — Phase 1

> Status：BUILD_FREEZE_READY / STEP2_REVIEWED。
>
> Shared infrastructure truth：`../../common-core/INFRA-ARCHITECTURE.md`
>
> Phase 1 scope 只包含本 section 明確啟用的 provider / plane / storage baseline；後續 Phase section 必須經 Evidence + Human approval + Build Freeze inclusion。

# 4. 為什麼是 Cloudflare Edge + Supabase Postgres

## 4.1 Cloudflare 作為 Edge / Serverless

appf2 適合 Global Edge 的原因：

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

appf2 的核心資料天然是關聯型：

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

但 appf2 的 Repository / Identity / Realtime / Storage 都必須保留 Adapter Boundary，不讓 Supabase API 成為 LegoSpec / Runtime Protocol 的一部分。

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
 → immutable Blueprint body
 → Postgres on cache miss
 → Cache-Control: immutable
 → CDN caches response

GET /api/v1/blueprints/{content_hash}/execution-admission
 → Edge Resolver
 → current trust / compatibility metadata
 → short internal metadata cache <= 15s
 → Browser hydration gate
~~~

結果：

~~~text
第一次
CDN miss → DB

之後
CDN hit → Browser
~~~

因為 content hash 改變就代表新 Blueprint，所以 immutable CDN cache 很自然。

但 Blueprint body cache不代表現在可執行；fresh ExecutionAdmission由獨立 mutable metadata path決定。

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

appf2 保留三種分享模式，但按需求啟動。

Phase 1 啟用策略由 F05 定義：

~~~text
Production default = Mode B / DURABLE_REFERENCE
Mode A = optional experiment, not Release 1 blocker
Mode C = deferred to F09
~~~


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
- product evidence；
- API idempotency operations（24h bounded durable control record）。

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


---

# appf2 Infrastructure — Phase 2

> Shared infrastructure truth：`../../common-core/INFRA-ARCHITECTURE.md`

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
- non-enforcing cost / future entitlement metadata hooks。

Phase 2 不部署 F13 entitlement / metering enforcement；這些只作未來 compatibility hooks，且不修改 immutable Blueprint core。

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


---

# appf2 Infrastructure — Phase 3

> Shared infrastructure truth：`../../common-core/INFRA-ARCHITECTURE.md`

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


---

# appf2 Infrastructure — Phase 4+

> Shared infrastructure truth：`../../common-core/INFRA-ARCHITECTURE.md`

# 15. 長期：Intent Commerce / Capability Network / Orchestration

長期新增的核心不是另一套 App Runtime，而是：

> **Capability Gateway + Provider Registry + Entitlement / Metering / Transaction Layer**

~~~mermaid
flowchart LR
    R[appf2 Runtime]
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

否則會破壞 appf2 的成本模型與即時性。

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
- appf2 自己定義 workflow contract。
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
