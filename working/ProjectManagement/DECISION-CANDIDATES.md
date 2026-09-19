# NodeFF Decision Candidates

> 狀態：Working — Not SSOT。

# 1. 這份文件的用途

本文件只記錄：

> **已經存在兩個以上合理方案，而且選擇其中一個會影響 Architecture、Contract、Compatibility 或 Implementation 的決策。**

它不是會議紀錄，也不是所有未完成事項的清單。

決策流程：

~~~text
Question
 → Options
 → Recommended Direction
 → Review
 → User Approval
 → Promote to spec/ or decisions/
~~~

一旦正式核准並移入 SSOT，本文件只保留簡短狀態或移除該 Candidate。

---

# 2. Current Decision Gates

## DC-001 — Rule Representation

**問題**  
Runtime rule 應使用：
- Typed Declarative Rule AST；
- Restricted Expression String；
- 或 Hybrid。

**目前方向**  
偏向 **Typed Declarative Rule AST**，因為更容易：
- static validation；
- allowlisting；
- dependency analysis；
- resource bounding；
- deterministic serialization；
- versioning。

**決策時點**  
F03 Runtime Execution / F04 Capability Registry 詳細設計前必須定案。

---

## DC-002 — Capability Registry Source Format

**問題**  
Capability Registry 的 machine-readable source 應採何種 canonical format，才能同時產生：
- Compiler metadata；
- validation schema；
- Runtime registration；
- documentation；
- tests / compatibility metadata。

**已確定原則**  
不能人工維護多份平行 Capability 定義。

**尚未決定**  
具體 source format 與 generation pipeline。

**決策時點**  
F04 Capability Registry 進入實作前。

---

# 3. 不應放在這裡的內容

以下改放 `OPEN-QUESTIONS.md`：
- 還不知道需求是否存在；
- 需要使用者數據驗證；
- 還沒有形成可比較方案的問題。

以下改放 Function Design：
- 已經決定方向，只剩 implementation details。

以下正式核准後移至：
- `spec/`
- `decisions/`
