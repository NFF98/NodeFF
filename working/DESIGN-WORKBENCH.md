# appf2 Design Workbench

> 狀態：ACTIVE DISCUSSION BUFFER — **NOT SSOT**
>
> 用途：只暫存「尚未批准、尚未有 canonical owner」的產品／商業／架構討論。
>
> Current Product Design Truth 永遠在對應的 canonical `working/` 文件；本檔不得成為 shadow truth。

## Current Active Discussion

**NONE**

目前沒有尚未歸屬 canonical owner 的 Active Design Discussion。

## 使用規則

1. 新議題只有在「尚未決定」時才可暫存在這裡。
2. 一旦 User 批准，必須立即吸收到正確 canonical owner。
3. 已同步內容不得繼續完整保留在 Workbench。
4. Session closeout、過往 review notes、已關閉 delta 不放這裡；需要保存則進 `archive/`。
5. Build Freeze 前，本檔必須維持：
   - approved unique truth = 0
   - closed-but-unsynced item = 0
   - active orphan decision = 0
6. Workbench 不得直接成為 appf2-build Build Spec source。

## Evidence-Gated Open Questions

以下不是 Active Design Decision；目前資訊不足，必須靠 Prototype / Usage / Benchmark / Policy Evidence 才能回答。它們不阻擋 Phase 1 Build Freeze，除非未來明確影響某個 Phase 1 contract。

### OQ-001 — 哪一類 Phase 1 Use Case Wedge 真正最強？

候選包含 Utility、Decision、Game / Fun、Social、Sentimental / Creative。

已確定：Product Vision = Intent → App；任何單一 Wedge 都不是 appf2 最終產品邊界。

仍需要 Evidence：
- create → use completion
- repeat creation
- share → open → use
- remix rate
- semantic mismatch / correction
- retention / return behavior

### OQ-002 — 哪些 Phase 1 Capability 應真正進 Release Set？

已確定：
- 不以 Capability 數量當進度 KPI。
- Phase 1 優先高組合密度與 Semantic Correctness。
- Candidate Capability families 由 `working/common-core/CAPABILITY-FABRIC.md` 定義。
- Build ≠ Validated。

仍需要 Evidence：
- 哪些 Capability 已達 TESTED / VALIDATED。
- 哪些 Capability 對多種 Intent 有高覆蓋率。
- 哪些 Capability failure / confusion 成本過高。

真正問題：

> **哪些 Candidate Capability 已有足夠證據值得進 Release Set？**

### OQ-005 — Semantic Reuse 何時值得投入？

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

### OQ-006 — Phase 1 Anonymous Evidence 需要什麼 User-facing privacy governance？

已確定的 retention / identity / deletion rules 仍由 Data Model + F07 canonical owner 負責。

仍需要治理 Evidence / decision：
- User-facing notice 到什麼程度
- 是否／何時需要 consent
- explicit privacy reset UX
- secondary / research use 是否允許，以及需要什麼 boundary
- jurisdiction-driven requirement 若出現時怎麼處理

### Gate Rule

```text
Open Question
→ 不影響 Phase 1 contract：可繼續存在
→ 影響 Phase 1 contract：升級成 Active Discussion，先決定再 Build Freeze
```

目前沒有已知 Evidence-Gated Open Question 阻擋 Phase 1 Build Freeze。

---

## Historical Review Records

Closed cleanup / audit detail 不留在 Workbench，避免形成 shadow truth。歷史證據只在 archive：

- `archive/ProjectManagement/DESIGN-WORKBENCH-HISTORY-2026-09-25.md`
- `archive/ProjectManagement/SHADOW-TRUTH-AUDIT-2026-09-25.md`
