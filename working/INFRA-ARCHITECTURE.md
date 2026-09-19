# NodeFF Infrastructure Architecture

> 狀態：Current Working Baseline。本文定義 NodeFF 目前採用的 Infrastructure 方向、Phase 1 部署方式、Database 選擇與中長期擴充邊界。

# 1. 目前架構決定

NodeFF Phase 1 採用：

> **Client-First + Serverless + Edge + PostgreSQL**

核心目的不是先建立大型 Backend，而是用最少 Infrastructure 支撐：

~~~text
Intent
 → Compile
 → Validate
 → Execute
 → Share
 → Use
 → Remix
~~~

目前方向如下：

| 項目 | Phase 1 決定 |
|---|---|
| Frontend | React Web App，靜態資源由 CDN / Edge Hosting 發布 |
| Runtime | Browser 端執行 Universal Runtime |
| Backend | Serverless / Edge Functions，不建立常駐 Application Server |
| API | Stateless API 為主 |
| Database | PostgreSQL |
| Phase 1 DB Provider | Supabase Postgres |
| LLM | 只能由 Serverless / Edge Compiler API 呼叫 |
| Cache | Browser / CDN / Edge Cache 優先；額外 KV 視實測再加入 |
| Realtime | 非 Phase 1 預設依賴，需要的 Use Case 再加入 |
| Object Storage | Phase 1 非必要；大型 Media / Asset 才加入 |
| Queue / Worker | Phase 1 非必要；有 long-running job 才加入 |
| Vector DB | Phase 1 不使用 |
| Runtime AI | Phase 1 不作一般互動預設 |

架構原則：

> **沒有必要進 Server 的互動，就留在 Client。沒有必要長時間運行的 Backend，就使用 Serverless。能靠 Edge 解決的 Routing / API / Cache，就盡量靠近使用者。**

---

# 2. Phase 1 整體架構圖

~~~mermaid
flowchart TB
    U[User Browser]

    subgraph CLIENT["Client / Browser"]
        WEB[React Web App]
        RT[Universal Runtime]
        STATE[Local Instance State]
        CACHE[Local Cache / Recovery]
    end

    subgraph EDGE["Serverless + Edge"]
        ROUTER[Edge Router / API Gateway]
        COMPILER[Compiler API]
        VALIDATOR[Blueprint Validator]
        SHARE[Share Resolver]
        EVENTS[Telemetry API]
    end

    subgraph DATA["Data Layer"]
        PG[(PostgreSQL / Supabase)]
    end

    subgraph EXTERNAL["External"]
        LLM[LLM Provider]
    end

    U --> WEB
    WEB --> RT
    RT --> STATE
    RT --> CACHE

    WEB --> ROUTER
    ROUTER --> COMPILER
    COMPILER --> LLM
    COMPILER --> VALIDATOR
    VALIDATOR --> PG

    WEB --> SHARE
    SHARE --> PG

    WEB --> EVENTS
    EVENTS --> PG

    PG --> ROUTER
~~~

這張圖代表 Phase 1 真正需要部署的東西。

不需要：
- 一台永遠開著的 Node.js server；
- Kubernetes；
- Microservice cluster；
- message queue；
- vector database；
- dedicated realtime cluster；
- data warehouse。

---

# 3. 為什麼使用 Serverless + Edge

NodeFF 的 workload 很適合 Serverless：

- 大部分 App interaction 在 Browser Runtime 完成；
- Backend request 主要集中在 Compile、Share、Telemetry；
- 流量早期高度不確定；
- 不值得為 idle time 維持常駐 Server；
- Compiler request 本身是短生命週期工作。

Edge 的角色主要是：

~~~text
Request
 → Routing
 → Policy / Quota
 → Cache / Reuse
 → Serverless Function
~~~

Phase 1 不把所有 computation 強行搬到 Edge。

如果某個工作超出 Edge Runtime 適合的 CPU / memory / execution-time 範圍，未來才交給 Region Serverless Function、Worker 或 External Job。

---

# 4. Frontend / Runtime

Frontend 是 NodeFF 最大的 execution plane。

~~~text
React App
 ├─ Universal Runtime
 ├─ Capability Runtime
 ├─ Rule VM
 ├─ Instance State
 └─ Local Cache
~~~

既有有效 Blueprint：

~~~text
Open
 → Validate Compatibility
 → Hydrate
 → Execute
~~~

正常互動不需要重新呼叫 Backend 或 LLM。

這是 NodeFF 控制 Cost 與 Latency 的核心。

---

# 5. Serverless / Edge Backend

Phase 1 Backend 不做大型 monolithic server。

主要 Endpoint：

~~~text
/api/compile
/api/share/*
/api/events
/api/blueprint/*
~~~

## /api/compile

負責：
- anonymous / account quota；
- policy / abuse check；
- Capability Registry context；
- LLM provider call；
- Blueprint validation；
- bounded repair；
- telemetry。

## /api/share

負責：
- short reference resolution；
- Blueprint lookup；
- permission / availability check。

## /api/events

負責：
- product telemetry；
- compiler outcome；
- semantic mismatch；
- share / open / remix evidence。

## /api/blueprint

只處理需要 Server persistence / resolution 的 Blueprint。

小型、非敏感且適合 portable transport 的 Artifact，不必一律進 Database。

---

# 6. Database：PostgreSQL

NodeFF 的主要 Database 選擇：

> **PostgreSQL**

Phase 1 預設使用：

> **Supabase Postgres**

選 PostgreSQL 的原因不是因為 NodeFF 要做大型傳統 Backend，而是因為後續資料天然具有關聯性：

~~~text
anonymous_id
 → intent
 → blueprint
 → share
 → remix
 → ownership
 → account
~~~

以及：

~~~text
Blueprint
 → Version / Lineage
 → Capability Usage
 → Execution Evidence
~~~

PostgreSQL 能同時處理：
- relational metadata；
- JSON / JSONB Blueprint metadata；
- ownership / lineage；
- telemetry 的早期資料量；
- future account / commerce relationships。

因此 Phase 1 不需要同時引進多種 Database。

---

# 7. Phase 1 Database Scope

Phase 1 Database 只保存真正需要 Server-side continuity 的資料。

建議初始 logical entities：

~~~text
anonymous_identity
compiler_run
blueprint
blueprint_lineage
share
product_event
semantic_feedback
~~~

Phase 1 原則：

- Blueprint content 與 metadata 可先由 PostgreSQL 承載；
- 不急著建立獨立 CAS service；
- 不急著導入 Object Storage；
- 不急著建立 Vector DB；
- 不急著建立 Analytics Warehouse。

如果資料規模或 access pattern 真的證明需要，再拆。

---

# 8. Phase 1 Data Flow

## Create

~~~mermaid
sequenceDiagram
    participant U as Browser
    participant E as Edge / Serverless
    participant L as LLM
    participant D as PostgreSQL

    U->>E: Intent
    E->>E: Policy / Quota
    E->>L: Compile Intent
    L-->>E: Blueprint Candidate
    E->>E: Validate
    E->>D: Store Blueprint + Evidence
    E-->>U: Valid Blueprint
    U->>U: Execute locally
~~~

## Existing App

~~~text
Shared Link
 → Edge / CDN
 → Resolve Blueprint
 → Browser Runtime
 → Local Interaction
~~~

不因每次 Button / Dice / Form / Rule interaction 再碰 LLM。

---

# 9. Cache Strategy

Phase 1 採漸進式 Cache，不先建立複雜 Cache Infrastructure。

優先順序：

~~~text
Browser Cache
 → CDN / Edge Cache
 → Database
 → Compiler
~~~

只有當量測證明有價值時，再增加：

- Edge KV；
- Exact Intent Cache；
- Trusted Blueprint Reuse Cache；
- semantic retrieval。

Cache 永遠不能跳過：
- Blueprint version check；
- security；
- compatibility；
- trust status。

---

# 10. Phase 1 成本模型

Phase 1 應保持 Infrastructure 極薄。

主要必要 variable cost：

> **LLM Compilation**

原因是：
- React Runtime 在 Client；
- 正常 interaction 不使用 Server compute；
- Existing Blueprint 不重複 compile；
- Database 只承擔 metadata / continuity；
- Serverless request 按使用量產生成本。

因此 Phase 1 應優先優化：

~~~text
Compile Once
 → Reuse
 → Execute Locally
 → Share
 → Remix
~~~

而不是先投入大型 Infrastructure。

---

# 11. 中期 Infrastructure — 有產品證據後才加入

以下項目與 Phase 1 核心架構分開管理。

只有真實 Use Case / PMF 證明需要後才進入項目：

## Durable Identity / Storage

加入：
- Account；
- Ownership；
- History；
- Cross-device；
- Private Blueprint；
- Longer retention。

仍以 PostgreSQL 為主要 System of Record。

## Realtime

當 Social / Multiplayer Use Case 證明需要時加入：

~~~text
Blueprint
 + Room
 + Presence
 + Mutable Instance State
 + Validated Delta
~~~

Realtime provider 獨立於核心 Runtime。

## Object Storage

只有出現：
- uploaded image；
- audio；
- video；
- 3D asset；
- generated media；

才加入 Object Storage / CDN。

## Background Job / Queue

只有出現：
- media generation；
- heavy AI；
- long-running compute；
- batch processing；

才加入 Worker / Queue。

## Semantic Reuse

只有累積足夠 Blueprint / Intent Evidence 後，再評估：
- embedding；
- vector retrieval；
- Blueprint family retrieval。

Phase 1 不預先支付這個複雜度與成本。

---

# 12. 長期 Infrastructure — Paid Capability / Platform Layer

長期若 NodeFF 進入 Intent Commerce / Capability Network，再增加：

~~~text
External Capability Gateway
 ├─ Paid AI
 ├─ Search / Data
 ├─ Booking
 ├─ Payment
 ├─ Commerce
 ├─ Media Generation
 └─ Specialized Compute
~~~

以及可能需要：

- multi-region database / replication；
- dedicated cache layer；
- event streaming；
- analytics warehouse；
- large-scale observability；
- capability billing / settlement；
- provider SLA monitoring；
- third-party capability sandbox；
- large realtime infrastructure。

這些不是 Phase 1 dependency。

---

# 13. Infrastructure 發展順序

~~~text
PHASE 1
React + Browser Runtime
        ↓
Serverless + Edge API
        ↓
PostgreSQL
        ↓
LLM Compiler
        ↓
Share + Anonymous Evidence


MIDDLE TERM
Account / Ownership
        ↓
Realtime
        ↓
Object Storage
        ↓
Background Jobs
        ↓
Semantic Reuse


LONG TERM
Paid External Capabilities
        ↓
Intent Commerce
        ↓
Capability Network
        ↓
Multi-region / Platform Infrastructure
~~~

原則：

> **只有前一階段的 Product Evidence 證明需要，才啟動下一層 Infrastructure。**

---

# 14. Security Boundary

Phase 1 即必須成立：

1. LLM / provider secret 只存在 Serverless / Edge environment。
2. Browser 不持有 privileged credential。
3. Blueprint 不包含 arbitrary JavaScript。
4. Runtime 不使用 `eval()` / `new Function()`。
5. Capability / Rule / Action 必須來自 allowlisted Registry。
6. Database 不因 public share link 自動授予 ownership。
7. Anonymous identity 不使用 device fingerprinting。
8. Sensitive data 不進 URL snapshot。
9. External content 一律視為 untrusted。
10. Serverless API 必須具備 rate / quota / payload limits。

---

# 15. 與 App Architecture 的關係

`APP-ARCHITECTURE.md` 定義：

> NodeFF App 如何被 Compile、Contract、Execute。

本文定義：

> 這些能力實際部署在哪裡、資料放哪裡、Serverless / Edge / DB 如何配合。

具體 Function 的 Frontend / Backend / API / Acceptance 仍由：

- `APP-DETAILED-DESIGN.md`
- `working/functions/`

承接。

---

# 16. Phase 1 Infrastructure 結論

目前 NodeFF 不需要一套昂貴的 Platform Infrastructure。

需要的是：

> **Browser Runtime + Serverless/Edge Control Plane + PostgreSQL + bounded LLM Compiler。**

也就是：

~~~text
Client 做大部分 Execution
Edge 做 Routing / API
Serverless 做按需 Backend
PostgreSQL 做 Durable Data
LLM 只做 Semantic Compilation
~~~

這是目前 Phase 1 Infrastructure baseline。
