# NodeFF Phase 1 Core — Cross-Function Consistency / Working → Spec Gate Audit

> Audit Status：COMPLETE
>
> Gate Verdict：HOLD — NOT SPEC_READY
>
> Audited Current Truth Commit：bd74d9f244ab63218bad78f60381ccb0f48fb9b6
>
> Scope：F00 / F01 / F02 / F03 / F04 / F05 / F06 / F07 / F12 / F16 + DATA-MODEL + Runtime / Error / Evidence / API / UX / Function Specs / Executable Acceptance。
>
> 本文件是 Gate Audit evidence，不是產品 Contract SSOT。實際設計真相仍由各 canonical Working 文件擁有。

# 1. Executive Verdict

Phase 1 Core 的產品與架構 Working Baseline 已成立，但依 DESIGN-TO-DELIVERY Working → Spec Gate 交叉檢查：

~~~text
Core Functions audited = 10
SPEC_READY = 0
WORKING_BASELINE but needs gate closure = 10
~~~

目前不可把任何 Core Fxx 標為 SPEC_READY，也不可讓 Cursor 自行補 implementation-facing contract 缺口。

# 2. Shared Contract Audit

| Area | Baseline Status | Spec Gate Status | Audit Result |
|---|---|---|---|
| Canonical Data Model | ✅ WORKING_BASELINE | 🟡 ALIGNMENT_REQUIRED | foundation正確；intent concurrency / idempotency / retention有 gap |
| Executable Blueprint | ✅ WORKING_BASELINE | 🟢 CORE_CONTRACT_READY | F02 contract完整；仍受跨 Function trust delivery / tests阻擋 |
| Concrete Registry | ✅ WORKING_BASELINE | 🟢 CORE_CONTRACT_READY | F04 registry semantics完整；event/error/test integration仍待 |
| Runtime Semantics | ✅ WORKING_BASELINE | 🟡 ALIGNMENT_REQUIRED | core Runtime完整；F16 correction replay exact interface未固定 |
| API Contracts | 🟡 DRAFT | 🔴 BLOCKED | common API owner / idempotency / trust assertion / lifecycle-data alignment未封口 |
| UX State Machines | 🟡 DRAFT | 🟡 ALIGNMENT_REQUIRED | core flow完整；post-accept Revert entry與local recovery persistence未封口 |
| Error Taxonomy | ✅ WORKING_BASELINE | 🟡 ALIGNMENT_REQUIRED | shared classes/policy完整；exact stable error-ID → recovery mapping尚不可生成 |
| Evidence Schema | ✅ WORKING_BASELINE | 🟡 ALIGNMENT_REQUIRED | common envelope/ingest/privacy完整；per-event executable registry metadata不足 |
| Function Specs | 🟡 DRAFT | 🔴 BLOCKED | 10個仍是 Working Baseline；0個通過完整 Spec Gate |
| Executable Acceptance | ❌ NOT_STARTED | 🔴 BLOCKED | Acceptance很多，但只有Seed mapping，尚無完整 executable contract |

# 3. Function Gate Result

| Function | Working | Spec Gate | Main Gap |
|---|---:|---:|---|
| F00 Experience Shell | ✅ | HOLD | local draft TTL / persistence policy；accepted correction後 Revert entry；Acceptance coverage |
| F01 Compilation / API | ✅ | HOLD | intent_version與DATA-MODEL不一致；idempotency store owner；raw intent retention；API convention ownership |
| F02 Validation | ✅ | HOLD | core contract強；被 fresh trust assertion跨邊界與Executable Acceptance阻擋 |
| F03 Runtime | ✅ | HOLD | F16 correction replay exact Runtime interface；fresh trust assertion；Acceptance coverage |
| F04 Registry | ✅ | HOLD | core registry強；event/error registry integration與Acceptance coverage |
| F05 Share / Restore | ✅ | HOLD | revoked/incompatible trust如何fresh傳到Browser；idempotency shared contract；Acceptance coverage |
| F06 Remix / Refine | ✅ | HOLD | shared idempotency；event/error executable mapping；Acceptance coverage |
| F07 Identity / Evidence | ✅ | HOLD | Fxx event seeds不足以生成完整 event-registry；dedupe implementation placement；Acceptance coverage |
| F12 Recovery | ✅ | HOLD | source error stable ID → policy/message/action exact generated mapping不足；Acceptance coverage |
| F16 Correction | ✅ | HOLD | F03 replay exact interface；Revert UX entry；snapshot/user-content retention；shared idempotency；Acceptance coverage |

# 4. Gate Blockers

## GATE-B01 — intent_version vs DATA-MODEL mismatch

F01 API 使用 intent_version 做 optimistic concurrency，但 DATA-MODEL.intent_record 沒有 version 欄位或等價 canonical concurrency token。

Required closure：固定 intent concurrency token、更新 DATA-MODEL 與 F01 API、加入 concurrent answer / compile tests。

## GATE-B02 — Idempotency persistence / owner undefined

F01 / F05 / F06 / F16 都要求 mutation idempotency。F01已有 logical record與24h target，但 DATA-MODEL沒有 idempotency entity；Infra Phase 1 又不希望 Edge KV 成為必要 truth。

Required closure：選定 Postgres idempotency_operation 或其他 explicit durable/edge mechanism，並固定 key scope、request digest、logical result、TTL、cleanup、concurrency、error mapping。

## GATE-B03 — Fresh Blueprint Trust Assertion to Browser not exact

F02要求 Runtime execute前確認 current trust / compatibility；F05又允許 content-hash Blueprint body被 immutable CDN長快取。trust_status本身是 mutable DB truth。

目前缺 exact contract：Browser / F03 hydrate當下如何知道 CDN Blueprint 此刻仍可執行，而不是已 REVOKED / INCOMPATIBLE。

Required closure：固定 execution admission check位置、trusted metadata/assertion、cache/revocation semantics，direct /b path不得繞過 current trust。

## GATE-B04 — F16 Correction Replay ↔ F03 Runtime interface未固定

F16需要 validated child + replay inputs + RNG/timer context → fresh Runtime → comparable result，但 F03尚無 exact correction replay interface。

Required closure：replay input validation、derived/rule recompute、RNG、timer、LIMITED_COMPARISON、failure/disposal、exact internal interface。

## GATE-B05 — Revert semantics有Backend，缺完整 Shell UX entry

F16已定 ACCEPTED + REVERT_TO_BASE → REVERTED；F00 Compare只定 Accept New / Keep Previous / Adjust Again。接受新版本後從 APP surface如何再次觸發 Revert沒有 canonical UX。

Required closure：current-session Revert / Previous Version entry、scope/lifespan、unsafe target handling、successful revert後 surface。

## GATE-B06 — Local Recovery / User Content Retention不完整

F00只寫 Browser persistence = versioned key + TTL，未固定 draft TTL。F07只固定 product_event 90 days與 unsent event queue 24h，沒有固定 raw_intent / correction snapshot / local recovery draft exact retention。

Required closure：prompt/clarification/correction local draft TTL、raw_intent durable retention、result_snapshot retention、protected data deletion behavior。

## GATE-B07 — Cross-Function API conventions沒有 shared canonical owner

F01目前承載 common API conventions；F05引用F01；F16有新 mutation API但未完整明示共用 headers/error envelope；F07 batch又有 event_id dedupe例外。

Required closure：建立 shared API convention contract，或明確提升一個 canonical section成 cross-function owner，固定 envelope、request_id、idempotency default/exception、HTTP status、anonymous identity、timeout、versioning、route naming。

## GATE-B08 — Evidence Event Registry目前不可生成

F07要求每個 event有 event_type、event_name、function_id、schema_version、collection_class、required_context、allowed_properties、retention_class、metric_tags、deprecated。

Core目前約有102個 seeded event IDs，但各 Fxx 多數只有名稱與少量 dimensions，沒有 per-event完整 registry metadata。

Required closure：每個 Release 1 event補 exact event contract或建立可生成 structured source。

## GATE-B09 — Error Taxonomy語意完整，但 machine mapping不足

Phase 1 Core約有121個 source error IDs。F12有 common recovery classes/policies與代表性 mapping，但尚未完整形成 Fxx-ERR-nnn → policy_id → severity → retryability → message_key → next_actions → evidence class 的 exact registry。

Required closure：建立 exact Recovery Mapping Registry source。

## GATE-B10 — Executable Acceptance未成立

10個 Core Function共有257個 Acceptance；目前149個有 Test Mapping Seed，108個尚未在Seed中映射。即使已Seed-mapped，也仍不是 executable test artifact。

Required closure：每個 Required/Critical AC固定 TEST ID、verification type、fixture/input、expected observable outcome、implementation location、automated/manual/runtime-evidence。

# 5. Acceptance Mapping Coverage

| Function | Acceptance | Seed-mapped | Still Unmapped |
|---|---:|---:|---:|
| F00 | 28 | 15 | 13 |
| F01 | 24 | 16 | 8 |
| F02 | 22 | 14 | 8 |
| F03 | 29 | 15 | 14 |
| F04 | 19 | 9 | 10 |
| F05 | 21 | 12 | 9 |
| F06 | 23 | 13 | 10 |
| F07 | 29 | 17 | 12 |
| F12 | 28 | 18 | 10 |
| F16 | 34 | 20 | 14 |
| TOTAL | 257 | 149 | 108 |

注意：Seed-mapped也不等於 executable；149只是已有文字上的 TEST mapping。

# 6. Additional Material Gaps

## MAT-01 — F01 lifecycle vs persisted clarification_status需切清楚

F01 lifecycle包含 RECEIVED / ANALYZING / NEEDS_CLARIFICATION / READY / COMPOSING / VALIDATING / VALIDATED / failures；DATA-MODEL只有 clarification_status到 READY。需明確定義哪些 durable、哪些 derived、哪些由 compiler_run / validation_run表示。

## MAT-02 — API abuse / cost control需要 common rule

F01/F16會花LLM成本，F05可建立durable share，F07只有event ingestion有具體rate limits。Spec前至少需 anonymous mutation rate-limit class、expensive compile/correction budget、429 semantic與F12 mapping。

## MAT-03 — Result snapshot trust level需標清楚

F16 before/after result由Browser Runtime計算後提交。Server可驗schema/hash relation，但不能把Client payload當客觀 trusted execution proof。result_snapshot需標為 user-session comparison evidence / client-produced semantic snapshot。

# 7. Cleanup Findings

## CLEAN-01 — Open Decisions有已被 downstream閉合的舊文字

F00/F01/F02/F03/F04/F05/F06仍列出由 F05/F06/F07/F12/F16 未來決定的項目，但 downstream現在已完成。Review前需逐份標已閉合、指向 canonical owner，只有真未決才留下。

## CLEAN-02 — Baseline Status與Spec Gate Status必須分開

✅ WORKING_BASELINE只代表 Current Working Truth存在，不代表可開發。Audit建議後續同時顯示 Baseline Status與Spec Gate Status。

# 8. Spec Promotion Structure Conflict

Current Working採 Function-centric Fxx，但 /spec 仍是早期橫向模板：Requirements / User Flows / Data Model / System / API / UI / Security / Acceptance，而且目前都是 Draft / TBD。

若直接照舊填寫，F01/F05/F16的API、UI、Data會被拆進多份spec，重新形成雙SSOT。

Working → Spec前必須固定 Spec canonical structure。建議：

~~~text
spec/shared/
  DATA-MODEL.md
  API-CONVENTIONS.md
  CAPABILITY-CONTRACT.md
  ...

spec/functions/
  F00-EXPERIENCE-SHELL.md
  F01-INTENT-COMPILATION.md
  ...
~~~

舊11份 spec模板應 deprecated / index-only / shared-summary 化，不再承載平行詳細主規格。這是文件治理調整，不是產品架構改動。

# 9. Recommended Gate Closure Order

~~~text
1. Spec canonical structure / promotion rule
↓
2. Data/API alignment: intent_version / status / idempotency / retention
↓
3. Shared API conventions
↓
4. Fresh trust / compatibility admission to Browser
↓
5. F03 ↔ F16 correction replay exact contract
↓
6. F00/F16 Revert + local recovery UX closure
↓
7. Exact Error Recovery Registry
↓
8. Exact Evidence Event Registry
↓
9. Complete AC → TEST mapping
↓
10. Produce executable/manual/runtime-evidence test contracts
↓
11. Re-run Cross-Function Audit
↓
12. Promote eligible Fxx to SPEC_READY
~~~

# 10. Final Gate Decision

~~~text
Architecture / Product Direction = stable
Core Working Design = substantially complete
Cross-Function Contract Closure = incomplete
Working → Spec Gate = HOLD
Cursor Production Implementation from Working docs = NOT AUTHORIZED
~~~

Audit沒有發現需要推翻四層架構、immutable Blueprint、Capability Registry、Browser Runtime、Share/Remix/Correction核心方向的問題。

真正需要做的是：把已經正確的架構，封成不需要 Cursor猜測的 implementation contract。

# Latest Re-Audit

The original HOLD result is historical evidence of the pre-closure state.

Latest result：

- working/ProjectManagement/PHASE1-CORE-SPEC-GATE-REAUDIT.md
- Audited commit：c206a2590bfd8ebd0a2bb2b6a4922354956cff11
- Verdict：PASS — ELIGIBLE FOR SPEC PROMOTION

Do not use the original HOLD verdict as current gate status after this re-audit.
