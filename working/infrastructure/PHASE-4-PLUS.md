# NodeFF Infrastructure — Phase 4+

> Shared infrastructure truth：`../core/INFRA-ARCHITECTURE.md`

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
