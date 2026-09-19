# NodeFF Open Questions

> 狀態：Working — Not SSOT。

# 1. 這份文件的用途

本文件只記錄：

> **目前資訊不足，不能合理做出設計決策，需要更多 Use Case、Prototype、Benchmark 或 Product Evidence 才能回答的問題。**

與 `DECISION-CANDIDATES.md` 的差別：

- **Open Question**：現在還不知道答案。
- **Decision Candidate**：已有可選方案，需要做選擇。

---

# 2. Product / Capability Questions

## OQ-001 — Phase 1 最強 Use Case Wedge 是什麼？

目前已知可能包括：
- Utility；
- Decision；
- Game / Fun；
- Social；
- Sentimental / Creative。

不應先假定最終類別。需由 Prototype 與真實 Usage 驗證。

## OQ-002 — Phase 1 Capability Set 要多大？

需要在：
- Capability Coverage；
- Build Complexity；
- Semantic Reliability；
- Time-to-Market

之間取得平衡。

具體 Card 清單由 `CAPABILITY-FABRIC.md` 持續收斂。

## OQ-003 — Realtime 是否為 Phase 1 必要能力？

若主要 Wedge 強烈依賴多人同步，需提前；否則可延後。

---

# 3. Infrastructure / Runtime Questions

## OQ-004 — Portable Snapshot 與 Durable Reference 的切換門檻？

需依：
- payload size；
- privacy；
- ownership；
- persistence；
- browser / URL constraints

實測後決定。

## OQ-005 — Semantic Reuse 何時值得投入？

需要先量測：
- Blueprint family 重複率；
- fresh compilation cost；
- semantic mismatch；
- reuse correctness。

沒有真實 usage 前，不應過早建立複雜 retrieval system。

## OQ-006 — Anonymous Evidence 的 retention / privacy policy？

已確定 Phase 1 需要匿名產品 evidence，但 retention、deletion、consent / notice 與研究用途仍需另行治理。

---

# 4. 處理原則

Open Question 不會阻擋所有開發。

只有當某問題會阻擋特定 Function 的 Acceptance / Architecture 時，才將它升級為該 Function 的 Decision Gate。
