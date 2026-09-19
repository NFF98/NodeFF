# NodeFF Infrastructure Architecture

> 狀態：Working。本文描述 NodeFF 的基礎設施拓撲、服務責任、資料位置與執行邊界；功能實作細節由 Function Design 承接。

# 1. Infrastructure 使命

NodeFF 採用 **Client-First、Edge-Assisted Control Plane**。

核心原則：

> **能在可信任 Runtime 本地完成的互動，就不送回 Server；需要 Semantic、Durable、Realtime 或 External Capability 時，再使用後端服務。**

因此 Infrastructure 主要負責：

- Intent compilation；
- validation / trust admission；
- Capability Registry distribution；
- Blueprint storage / resolution；
- anonymous / account identity；
- quota / policy；
- realtime coordination；
- external capability orchestration；
- telemetry / reliability evidence。

它不是所有 App Interaction 的中央 execution server。

---

# 2. 邏輯拓撲

~~~text
Browser / Client
 ├─ Universal Runtime
 ├─ Instance State
 ├─ Rule VM
 ├─ Capability Runtime
 └─ Local Cache / Recovery
        │
        ▼
NFF Edge / API
 ├─ Routing / Policy / Quota
 ├─ Compiler API
 ├─ Blueprint / Share Resolver
 ├─ Identity / Ownership
 ├─ Telemetry Intake
 └─ Capability Orchestration
        │
        ├─ LLM Provider Adapter
        ├─ Capability Registry
        ├─ Blueprint / Metadata Store
        ├─ Realtime Provider
        └─ External API / Worker / Storage
~~~

核心 Protocol 不綁定單一 Cloud、LLM、Database 或 Realtime Provider。

---

# 3. 四種主要執行路徑

## 3.1 Cold Path — 新 Intent

~~~text
Intent
 → Policy / Quota
 → Reuse Lookup
 → Semantic Compiler
 → Validation
 → Trusted Blueprint
 → Store / Return
 → Client Runtime
~~~

這是主要產生 LLM cost 與 compilation latency 的路徑。

## 3.2 Warm Path — 既有 Blueprint

~~~text
Blueprint Reference / Snapshot
 → Resolve
 → Trust + Compatibility Check
 → Hydrate
 → Local Execution
~~~

一般互動不重新呼叫 LLM。

## 3.3 Realtime Path

~~~text
Immutable Blueprint
 + Room ID
 + Mutable Instance State
 + Validated Deltas
~~~

Realtime 只同步需要共享的 Instance State，不修改 Blueprint 本體。

## 3.4 External Capability Path

~~~text
Runtime Action
 → NFF Capability Gateway
 → External API / Worker
 → Status / Result
 → Validated Result
 → Runtime
~~~

Heavy AI、Media Generation、Booking、Payment、Specialized Compute 等走此路徑。

---

# 4. 核心 Infrastructure Services

## Compiler Service

責任：
- model provider abstraction；
- capability context injection；
- structured output；
- bounded repair；
- cost / latency control。

Provider secret 永遠不進 Browser。

## Capability Registry

Capability 的 machine-readable source，提供：
- semantic metadata；
- contract；
- version；
- compatibility；
- security / permission；
- runtime availability。

Compiler 與 Runtime 不各自維護平行能力清單。

## Blueprint Registry / Store

分離：
- immutable Blueprint content；
- logical identity / lineage；
- trust / policy metadata；
- ownership / save pointer；
- Instance state。

Content hash 不等於 ownership 或 authorization。

## Identity Service

Phase 1：
- privacy-conscious first-party `anonymous_id`；
- session / share / remix continuity。

中期：
- account；
- ownership claim；
- durable history；
- cross-device。

## Realtime Service

負責：
- room；
- presence；
- ordered state updates；
- reconnect；
- recovery；
- limits / abuse protection。

## Telemetry / Reliability Service

從 Day 1 收集最小必要 evidence：

- Intent / compilation outcome；
- selected capabilities；
- validation / runtime failure；
- semantic mismatch；
- share / open / remix；
- user correction。

目的為產品量測與未來 Learning Graph，不等同 unrestricted model-training consent。

---

# 5. Data Placement

## Client

適合：
- transient UI state；
- normal Instance state；
- trusted Blueprint cache；
- local recovery。

## Share Transport

只放：
- 使用者明確分享；
- 小型；
- 非敏感；
- 可安全還原的 snapshot / reference。

URL Hash 是 transport，不是 database，也不是 encryption。

## Ephemeral Backend

適合：
- room state；
- presence；
- short-lived session；
- temporary job status。

## Durable Backend

適合：
- account / ownership；
- saved Blueprint pointer；
- publication metadata；
- lineage；
- quota / billing；
- trusted registry metadata；
- durable history（需要時）。

## Secret Boundary

永不 Client-exposed：
- provider secrets；
- signing keys；
- privileged credentials。

---

# 6. Cache 與 Reuse

必須分開三種概念：

1. **Exact Request Cache**：完全相同 request 的快速 reuse。
2. **Semantic / Blueprint Family Retrieval**：找到可能可重用的可信結構。
3. **Content Cache**：依 immutable Blueprint content identity 精確取得。

任何 Cache / Reuse 都不能繞過：
- version compatibility；
- trust / policy；
- security；
- semantic quality status。

---

# 7. Security 與 Resource Boundary

Infrastructure 必須確保：

- 不執行 generated JavaScript；
- 不使用 `eval()` / `new Function()`；
- Capability / Action / Rule 必須 allowlisted；
- external asset 視為 untrusted；
- state delta 必須 validated；
- Blueprint / snapshot 有 size / complexity budget；
- unknown capability fail closed；
- hash 不代表 authorization；
- compression 不代表 privacy。

Rule VM、Media、3D、Realtime、External API 等高風險能力，細節在對應 Function / Capability Design 中定義。

---

# 8. Reliability 與 Recovery

系統需區分：

- compilation failure；
- validation failure；
- semantic mismatch；
- runtime failure；
- external capability failure。

原則：

> **不能因為畫面 render 成功，就判定使用者 Intent 已成功。**

Structural failure 可 bounded repair；Semantic mismatch 通常需要 refinement / correction，而不是無限 retry。

---

# 9. Vendor Abstraction

以下皆屬可替換實作，不得進入核心 Protocol Semantics：

- Hosting / Edge Provider
- LLM Provider
- Database / Object Store
- Realtime Provider
- Queue / Worker
- Media / AI Provider

Vendor 選擇應由 Cost、Latency、Reliability、Region、Developer Velocity 與 Operational Complexity 決定。

---

# 10. 與 Function Design 的關係

Infrastructure Architecture 只定義共用服務與邊界。

具體功能，例如：

- Intent Compilation；
- Share / Restore；
- Anonymous Identity；
- Realtime Room；
- External Capability；

必須在 `working/functions/` 中描述實際 Frontend / Backend / API / Data Flow / Acceptance。

~~~text
Infrastructure Boundary
 → Function Design
 → Backlog / Sprint
 → Implementation / Release
~~~

---

# 11. Phase 1 Infrastructure Focus

Phase 1 只優先建立核心循環需要的 Infrastructure：

~~~text
Intent
 → Compile
 → Validate
 → Execute
 → Share
 → Use
 → Remix
~~~

因此近期優先：

1. Compiler API
2. Capability Registry
3. Blueprint Validation
4. Runtime-compatible Blueprint Store / Resolution
5. Share / Restore
6. Anonymous Identity + Evidence
7. 基本 Telemetry

Realtime、Durable Account、Heavy Capability、Semantic Retrieval 依實際 Use Case 與 Phase 需求逐步加入。
