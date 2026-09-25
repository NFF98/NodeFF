# NodeFF Open Questions

> 狀態：EVIDENCE-GATED QUESTIONS — **NOT SSOT**
>
> 本檔只保留「現在無法靠設計討論合理回答，必須靠 Prototype / Usage / Benchmark / Policy Evidence 才能回答」的問題。
>
> Open Question 不等於 Phase 1 blocker；只有明確影響 Build Freeze contract 時才升級成 Decision Gate。

# 1. Product / Capability

## OQ-001 — 哪一類 Phase 1 Use Case Wedge 真正最強？

目前候選包含：
- Utility
- Decision
- Game / Fun
- Social
- Sentimental / Creative

已確定：
- Product Vision = Intent → App。
- 任何單一 Wedge 都不是 NodeFF 最終產品邊界。

仍需要 Evidence：
- create → use completion
- repeat creation
- share → open → use
- remix rate
- semantic mismatch / correction
- retention / return behavior

只有真實 usage 才能回答哪一類 Wedge 最值得加碼。

## OQ-002 — 哪些 Phase 1 Capability 應真正進 Release Set？

已確定：
- 不以 Capability 數量當進度 KPI。
- Phase 1 優先高組合密度與 Semantic Correctness。
- Candidate Capability families 已在 `CAPABILITY-FABRIC.md` 定義。
- Build ≠ Validated。

仍需要 Evidence：
- 哪些 Capability 已達 TESTED / VALIDATED。
- 哪些 Capability 對多種 Intent 有高覆蓋率。
- 哪些 Capability failure / confusion 成本過高。

真正問題不是「Capability Set 要多大」，而是：

> **哪些 Candidate Capability 已有足夠證據值得進 Release Set？**

# 2. Reuse / Learning

## OQ-005 — Semantic Reuse 何時值得投入？

目前架構已確定：
- Phase 1 不先建立 dedicated Vector DB。
- 先使用 exact / structured retrieval。
- 有足夠 Evidence 後，可在相同 PostgreSQL 啟用 pgvector。

仍需要 Evidence：
- Blueprint family 重複率
- fresh compilation cost
- semantic mismatch rate
- reuse correctness
- latency / cost improvement

達到實際收益前，不提前建立複雜 semantic retrieval system。

# 3. Privacy Governance

## OQ-006 — Phase 1 Anonymous Evidence 需要什麼 User-facing privacy governance？

已確定、**不是 Open Question**：
- raw product event retention = 90 days
- raw intent / result value retention = 30 days
- local draft = 7 days
- explicitly enabled raw debug payload max = 7 days
- anonymous_id 不是 authorization / ownership proof
- deletion / anonymization 必須走 explicit policy

仍需要治理決定：
- User-facing notice 到什麼程度
- 是否／何時需要 consent
- explicit privacy reset UX
- secondary / research use 是否允許，以及需要什麼 boundary
- jurisdiction-driven requirement 若出現時怎麼處理

# 4. Resolved / Removed

以下問題已不再是 Open Question：

- OQ-003 Realtime 是否為 Phase 1 必要能力  
  → **RESOLVED**：F09 = 2–3 月 / Evidence-gated；Realtime 不是 Phase 1 dependency。

- OQ-004 Portable Snapshot vs Durable Reference  
  → **RESOLVED FOR PHASE 1**：Production default = Durable Reference；Portable Snapshot = optional experiment；Realtime mode deferred to F09。

# 5. Gate Rule

Build Freeze 前只需確認：

~~~text
Open Question
→ 不影響 Phase 1 contract：可繼續存在
→ 影響 Phase 1 contract：升級成 Decision Gate 並先解決
~~~

目前沒有已知 Open Question 阻擋 Phase 1 Build Freeze。
