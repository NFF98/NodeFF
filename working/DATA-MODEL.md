# NodeFF Canonical Data Model

> 狀態：Working Current Truth — Shared Data Model Index / Invariants。本文只保留跨 Phase 不應重複的資料原則；Phase-specific schema / tables / migration additions 拆到 `working/data-model/`。
> Legacy Formal Spec reference：RETIRED / NO-USE；Build implementation snapshot 改由 Human-approved Build Freeze → NFFBuild BS-*。
>
> Delivery / Traceability 規則以 `working/DESIGN-TO-DELIVERY.md` 為準；Infrastructure boundary 以 `working/INFRA-ARCHITECTURE.md` 為準。

# 1. Purpose

這份文件回答：

~~~text
什麼資料是 NodeFF 的 durable truth？
哪些只存在 Browser？
哪些資料 immutable？
Share / Remix / Correct 怎麼關聯？
哪些資料可進 PostgreSQL？
哪些資料不能被無限制收集？
未來 Identity / Reuse / pgvector 怎麼接而不推翻 Phase 1？
~~~

它不是：

- F01 的 Intent payload schema；
- F02 的完整 LegoSpec schema；
- F03 的 Runtime state machine；
- F07 的完整 telemetry event catalog；
- Database migration script。

上述內容由各 Function / Spec 承接，但不得違反本文。

---

# 2. Canonical Data Principles

## DM-P01 — PostgreSQL = Durable Truth

Phase 1 的 durable truth 存 PostgreSQL。

~~~text
Browser
= fast / local / ephemeral runtime state

PostgreSQL
= durable artifact / lineage / share / evidence truth
~~~

Browser local state 不能成為 ownership、share lineage、validated Blueprint 或 correction history 的唯一真相。

## DM-P02 — Blueprint Immutable

Validated Blueprint content 一旦以 content hash 保存，不得原地修改。

~~~text
Blueprint A
→ Refine / Remix / Correct
→ Blueprint B
~~~

B 是新 content；A 保留。

## DM-P03 — Blueprint / Instance / Result / Context / Delta 分離

~~~text
Blueprint
= immutable app definition

Instance
= current browser runtime state

Result Snapshot
= 特定 Blueprint + 特定 inputs 的可比較結果

Context
= approved cross-app / external context；Phase 1 不建立 durable Context store

Delta
= controlled semantic change；記錄在 Remix / Correction flow，不直接 mutation Blueprint
~~~

## DM-P04 — Durable Only When Product Value Requires It

Phase 1 不把每一次 button click、timer tick、render state 寫進 DB。

只有下列資料預設 durable：

- anonymous continuity；
- Intent / compile lifecycle 的必要記錄；
- validated Blueprint；
- Blueprint lineage；
- durable share reference；
- semantic correction / mismatch evidence；
- meaningful product events。

## DM-P05 — User Content ≠ Telemetry

Raw Intent、Result、User Input 可能含敏感內容。

Telemetry 只能收完成產品判斷所需的最小資料；不得因 debug 方便把 user content 全量複製到 event payload。

## DM-P06 — Vendor Neutral

LegoSpec / Function Contract 不得依賴 Supabase table API。

Application 透過 NFF-owned repository / service interface 使用資料層。

---

# 3. Phase Data Model Modules

Shared invariants 留在本文件；每個 Phase 的詳細 schema 只存在一個 phase module，不把 Phase 2／3／4 additions 一直塞回同一份長文件。

- Phase 1 detailed model：`working/data-model/PHASE-1.md`
- Phase 2 extensions：`working/data-model/PHASE-2.md`
- Phase 3 extensions：`working/data-model/PHASE-3.md`
- Phase 4+ extensions：`working/data-model/PHASE-4-PLUS.md`

Current implementation owner：

> **Phase 1 Build Freeze 讀 shared invariants + PHASE-1.md；未被該 Phase 啟用的 future module 不進 implementation scope。**

# 4. Cross-Phase Future Execution Rule

外部 job / workflow 的共用資料邊界：

外部 job / workflow state 必須另有 durable execution model，不塞進 Browser Instance 或 Blueprint JSON。

---

# 5. Growth Rule

1. Shared invariant 改變 → 更新本文件。
2. 新 Phase entity / table / index / migration → 寫進對應 Phase module。
3. 不建立 `DATA-MODEL-PHASE2.md` 這種平行完整複製版。
4. Phase 2 不複製 Phase 1 schema；只寫新增／改變／migration。
5. 舊 Phase module 保留當時 canonical design history；Current Truth 由 shared root + 已啟用 phase modules 組成。
