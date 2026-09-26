# appf2 Design-to-Delivery Contract

> 狀態：CURRENT GOVERNANCE。
>
> `spec/` / Formal Spec / Working → Spec / Spec Promotion / Formal Spec Refresh 模型已 **RETIRED / NO-USE**。
>
> Current flow：**appf2 Working → Human-approved Build Freeze → appf2-build immutable BS-* → Delivery**。

# 1. Purpose

appf2 的設計不能停在 Chat，也不能讓 Cursor 在實作時自行發明產品或架構決策。

Canonical lifecycle：

```text
Discussion
→ appf2 Working Design
→ Review / Consistency / Delta / Acceptance / UI Audit
→ Human approval
→ Build Freeze
→ appf2-build Locked Build Spec
→ Backlog
→ Sprint
→ Cursor Implementation
→ Test / Evidence
→ Release
→ Production Evidence
→ appf2 Working Improvement
```

核心原則：

> 後一階段由前一階段的已批准內容派生，不重新發明需求。

# 2. Current Truth / Source of Truth

```text
Discussion
= 思考、比較、未定方案

appf2 Working
= 唯一可修改 Product Design Current Truth

appf2-build Locked BS-*
= 某一 approved Working commit 的 immutable implementation snapshot

appf2-build Delivery
= Backlog / Sprint / Code / Test / Evidence / Release
```

不存在 appf2 內部第二份 Formal Spec Current Truth。

# 3. Canonical Document Responsibilities

```text
working/common-core/APP-ARCHITECTURE.md
→ system boundary / top architecture

working/detailed-design/APP-DETAILED-DESIGN-OVERVIEW.md
→ Function Portfolio / dependency / phase / release scope

working/common-core/DATA-MODEL.md
→ shared canonical data model

working/common-core/API-CONVENTIONS.md
→ shared public API transport / control contract

working/common-core/EXECUTION-ADMISSION.md
→ fresh Blueprint trust / compatibility execution gate

working/common-core/ACCEPTANCE-CONVENTIONS.md
→ shared Acceptance → Test conventions

working/detailed-design/registries/
→ machine-readable Recovery / Evidence / Acceptance contracts

working/common-core/CAPABILITY-FABRIC.md
→ capability semantic contract

working/detailed-design/functions/Fxx-*.md
→ single Function end-to-end detailed Product Design truth

working/detailed-design/UI-UX/
→ screen composition / visual hierarchy / responsive / presentation truth

NFF98/appf2-build/build-spec/baselines/BS-*
→ Human-approved immutable implementation snapshot

NFF98/appf2-build/delivery/
→ backlog / sprint / evidence execution

NFF98/appf2-build/releases/
→ release execution
```

UI/UX 文件不得自行改寫 Function behavior semantics。需要改 Product behavior / state semantics / API / Data / Runtime 時，必須先回對應 Working canonical owner。

# 4. Function Design Unit

每個 Fxx 應完整串通：

```text
User Outcome
→ User Flow
→ UI / UX
→ Frontend State
→ Data / DB
→ API
→ Backend Processing
→ Capability / Runtime
→ Error / Recovery
→ Security / Permission
→ Telemetry / Evidence
→ Acceptance / Test
```

缺少 implementation 必需 contract 時，不得進 Build Freeze。

# 5. Working Maturity

建議使用：

```text
DRAFT
→ REVIEW
→ WORKING_BASELINE
→ BUILD_FREEZE_READY
```

舊 `SPEC_READY` 名稱只代表歷史治理狀態；**NO-USE 作為現行 authority gate**。

`BUILD_FREEZE_READY` 代表：
- required product semantics 已閉合；
- Acceptance/Test mapping 已足夠；
- blocking open decisions = 0；
- 可以進 Human Build Freeze Review。

它不等於 implemented / tested / released。

# 6. Stable Traceability IDs

正式設計項目使用 stable IDs，例如：

```text
F01-RQ-001
F01-UX-001
F01-DATA-001
F01-API-001
F01-POL-001
F01-ERR-001
F01-EVT-001
F01-SEC-001
F01-AC-001
TEST-F01-001
```

ID 不重用。淘汰時標記 deprecated / superseded，不重編造成 traceability 斷裂。

# 7. Build Freeze Gate

進入 Build Freeze 前必須確認：

```text
Scope / Non-Scope
User Flow
UI / UX
Frontend State
Data / DB
API / Contract
Backend / Runtime
Capability dependency
Error / Recovery
Security / Permission
Telemetry / Evidence
Acceptance / Test
Dependency / Compatibility
Open Decisions = 無 blocker
Phase Boundary
```

規則：

1. Working 是唯一可修改 Current Truth。
2. Build Freeze 只能固定已 Review 的 Working，不重新改寫需求。
3. **沒有 User 明確批准，不得建立或啟用 appf2-build BS-*。**
4. Freeze 必須記 exact appf2 source commit。
5. Freeze inventory 必須列出 included Function / Shared / UI-UX / Registry files。
6. appf2-build baseline merge 後 immutable。
7. 後續 semantic change 必須回 appf2 Working，再建立新 baseline；不得改舊 baseline。

# 8. Build Freeze Handoff → appf2-build

appf2-design 只定義 Build Freeze handoff 必須保留的 traceability，不擁有 Backlog / Sprint / Cursor execution mechanics。

每個 frozen implementation item 至少必須能追蹤：

~~~text
Build Spec ID
source Working commit
Function ID
Requirement / Contract ID(s)
Acceptance ID(s)
Test ID(s)
Dependency
Phase scope
~~~

Backlog shape、Sprint lifecycle、task execution與 evidence recording由 `NFF98/appf2-build` canonical rules 擁有。

不得讓 appf2-build 從 Chat、未批准 Working delta 或 implementation convenience 發明 Product Truth。

# 9. Acceptance → Proof Handoff

Acceptance 是「什麼必須被證明」的 Product Design truth。

Canonical design-side conventions：
`working/common-core/ACCEPTANCE-CONVENTIONS.md`

Build Freeze 帶出 stable Acceptance ID、Test ID、Proof Scope 與 Expected Observable；fixture、test placement、runner、CI、evidence artifact與 pass/fail execution 全部由 appf2-build 擁有。

> Build 驗證 frozen Product Truth，不重新發明 Product Truth。

# 10. Executable Policy

Deterministic policy 應具有：

```text
Human-readable rule
+ stable Policy ID
+ machine-executable implementation
+ mapped tests
+ telemetry evidence where relevant
```

LLM 不得覆蓋 deterministic policy result。

# 11. Runtime Debug Traceability

Runtime failure 在可行時應能追蹤：

```text
request / session
Build Spec
Sprint / Task
Function
Blueprint hash / revision
Capability ID / version
Runtime stage
Error Class
Recovery Policy
Acceptance / Test
```

Stack trace 是工程資訊，不是 Consumer UX。

# 12. Error / Recovery Contract

預期 failure 應：
1. 有 stable Error ID / class。
2. 指明 retryable / terminal。
3. 指明 preserve context。
4. 對應 Humanized Recovery。
5. 有有效 next action，除非確實無法繼續。
6. 需要時產生 telemetry evidence。

# 13. Evidence Contract

每個 Function 在 Working Design 階段就應定義 Evidence，用來回答：

```text
Did it work technically?
Did it match user intent?
Did recovery work?
Was the function useful?
What did it cost?
Should we improve / expand / stop?
```

不得為 Debug 無限制收集敏感資料。

# 14. Release Ownership Boundary

Release authority 完全在 `NFF98/appf2-build`。

appf2-design 只提供 frozen Product / Acceptance truth；不維護 CI job、release checklist、deployment procedure 或 evidence storage mechanics。

Release 必須遵守的 Design invariants只有：

- 不得釋出違反 locked Build Spec 的 implementation；
- required Acceptance 必須有可追蹤 proof；
- Material Product / UX / API / Data / Runtime / Security change 必須先回 appf2 Working；
- Build Success 不等於 Product truth可被偷偷改寫。

# 15. Production Evidence Loop

```text
Production Evidence
→ detect mismatch / failure / friction
→ trace to Function / Policy / Capability
→ appf2 Working Delta
→ Human review / approval
→ new Build Freeze / Rebaseline when implementation truth changes
→ appf2-build delivery
```

Evidence 不得直接改 Production contract。

# 16. Change Control / Design Delta

### Minor
不改 user outcome / public contract / data compatibility。

→ 更新 canonical Working，保留 change trace。

### Material
改 UX flow、API、Data、Runtime semantics、Acceptance、Security、Compatibility。

→ Review affected Working owners；Human approval 後才能進下一次 Build Freeze。

### Architecture-impacting
改 Top Architecture、system boundary、Capability trust boundary、Blueprint model、Infra truth boundary。

→ 必須先在 appf2 Working 解決，不可在 appf2-build / Cursor 偷做。

若 implementation 發現 Material issue：

```text
appf2-build Finding
→ appf2 Working
→ Human approval
→ new BS-* Rebaseline
→ rebind backlog / sprint
```

# 17. Build Execution Ownership

Cursor / Agent rules、write scope、task execution、test placement、CI 與 release automation 的 canonical owner 是 `NFF98/appf2-build`。

appf2-design 不維護第二套 Cursor instruction。

Design 只要求 frozen implementation：

- 讀取 active locked Build Spec；
- preserve frozen Product contracts；
- 發現 Product / Contract mismatch 時回報 Finding，而不是在 implementation 中自行決策；
- Material change 必須回 appf2 Working → Human approval → new Build Freeze / Rebaseline。

實際 agent mechanics 以 appf2-build 的 `AGENTS.md`、`.cursor/rules/`、`delivery/` 與 `harness/` 為唯一 authority。

# 18. Software Engineering Guardrails

- Requirement traceability
- Contract-first design
- Versioned schema / policy
- Explicit acceptance
- Backward compatibility awareness
- Security by design
- Observability by design
- Testability
- Failure / recovery design
- Deterministic policy where required
- Change control
- No arbitrary generated code
- No hidden product decision in implementation

# 19. Per-Phase Application

Design-to-Delivery governance 跨 Phase 共用，不為 Phase 2 / 3+ 複製另一套流程。

Current Phase 1 / Build Freeze candidate：

~~~text
F00 F01 F02 F03 F04 F05 F06 F07 F12 F16
~~~

Canonical scope owners：
- Product / Business：`working/common-core/BUSINESS-PLAN.md` 的 `appf2 Product Roadmap — Phase 1` section。
- Architecture：`working/common-core/APP-ARCHITECTURE.md` 的 `appf2 Architecture Evolution — Phase 1` section。
- Infrastructure：`working/detailed-design/infrastructure/INFRASTRUCTURE-DETAILED.md` 的 Phase 1 section。
- Data：`working/detailed-design/data-model/DATA-MODEL-DETAILED.md` 的 Phase 1 Detailed Contract。
- Capability：`working/common-core/CAPABILITY-FABRIC.md` 的 `appf2 Capability Roadmap — Phase 1` section。
- Function portfolio：`working/detailed-design/APP-DETAILED-DESIGN-OVERVIEW.md`。

Phase 2 / 3+ content 可以存在於同一 canonical owner 內作 deferred baseline，但 **日期不 unlock scope**。只有 Evidence + Human approval + Build Freeze inclusion 才成為 implementation truth。

# 20. Definition of Done

一個 Function 的完成不是「頁面會跑」。

```text
Approved Build Spec
+ implementation mapped
+ Acceptance/Test passed
+ Error / Recovery verified
+ Security verified
+ Evidence verified
+ Release Gate passed
+ Production Evidence可回溯
```

# 21. Commit / Revert Rule

每次改變 GitHub Current Truth 的更新，都要有可辨識、可回退 commit。

回報至少包含：

```text
Commit
Changed
Why
Impact
Revert
```

Material / Architecture-impacting change 不與無關 cleanup 混在同一 commit。

# 22. Retired Governance Notice

以下模型已 **RETIRED / NO-USE**：

```text
Working → Formal Spec → appf2 Backlog / Sprint
spec/functions/
spec/shared/
Formal Spec Refresh
Spec Promotion
```

歷史 Audit / Re-Audit / Closure Report 可以保留上述文字作歷史證據，但不得作 Current Governance。

Current model only：

```text
appf2 Working
→ Human-approved Build Freeze
→ appf2-build immutable BS-*
→ appf2-build Delivery
```

# 23. Working Content Quality Review + Build Freeze Migration Rule

> 本節是 Working Review 與 Build Freeze 前 migration 的 canonical governance rule。
>
> 這裡的 `migration` 指 **appf2 Working → Human-approved Build Freeze input** 的收斂；不代表已退休的 Formal Spec / Spec Promotion 模型。

## 23.1 Review Objective

Working Content Quality Review 不是單純「瘦身」或「去重」。

Canonical review model：

```text
Cleanup
+ Completeness
+ Consistency
+ Ownership
+ Traceability
+ Freeze Readiness
= Working Content Quality Review
```

Review 的 KPI 不是文件數或字數變少，而是：

> **更少重複、更少模糊、沒有矛盾、缺口補齊、owner 清楚，並足以在不靠 Chat / Memory / Cursor 猜測的情況下進 Build Freeze。**

## 23.2 Mandatory Review Dimensions

每次 Working Content Quality Review 至少必須同時檢查：

1. **Duplicate / Shadow Truth**
   - 同一 Product / Architecture / Data / API / Runtime / UX / Acceptance truth 只能有一個 canonical owner。
   - 其他文件以 reference / dependency 表達，不建立近似副本。

2. **Contradiction**
   - Common Core、Detailed Design、Function、UI/UX、Data、Infrastructure、Registry 互相不得產生不一致 semantics。

3. **Wrong Owner / Boundary**
   - Truth 必須位於正確 canonical owner。
   - Design 定義 WHAT / WHY / WHEN / observable correctness。
   - appf2-build 定義 HOW TO EXECUTE / TEST / EVIDENCE / CI / SPRINT / RELEASE。

4. **Obsolete Governance / Shadow Process**
   - 清除或明確標記已失效的流程、舊 authority、舊 phase-folder assumptions、retired Formal Spec / Promotion wording。
   - 歷史紀錄可保留，但不得被誤讀為 Current Governance。

5. **Missing Design Truth**
   - Review 必須主動找「沒寫、寫不完整、實作者仍需自行決策」的地方並補入 canonical owner。
   - 包含但不限於 input / output、state transition、failure、timeout、retry、empty/loading/partial states、persistence、compatibility、lifecycle、permission、recovery、evidence、acceptance。

6. **Ambiguity**
   - 「適當」、「必要時」、「快速」、「系統判斷」、「友善處理」等非 deterministic wording 必須檢查是否需要轉成 rule / state / enum / threshold / contract。
   - 會影響 implementation outcome 的模糊處不得留給 Cursor 自行解釋。

7. **Edge-case Completeness**
   - Happy path 以外，必須檢查 network failure、timeout、invalid input / blueprint、expired / stale state、duplicate request、race、partial state、restore mismatch、mobile / responsive constraints 等 relevant failure modes。

8. **Cross-layer Completeness**
   - 每個 Function 應可追蹤：
   ```text
   Product Intent
   → Function Behavior
   → Data
   → API
   → Runtime
   → UI State
   → Error / Recovery
   → Evidence
   → Acceptance
   ```
   - 中間斷鏈即視為 design gap。

9. **Acceptance Readiness**
   - Design 不負責測試執行方式，但必須明確定義「什麼叫做正確」。
   - Critical behavior 必須具有可觀察、可驗證的 Acceptance truth，足以讓 appf2-build 建立 Test mapping。

10. **Phase Applicability**
    - Phase 是 scope / applicability metadata，不得產生第二份 SSOT。
    - 必須明確區分 universal contract、Phase 1 required、deferred Phase 2 / 3+。
    - 日期本身不得自動 unlock implementation scope。

11. **Non-functional Requirements**
    - 依功能需要檢查 latency / timeout、security、privacy、anonymous identity、cache semantics、reliability、idempotency、recoverability、accessibility、responsive behavior、observability / evidence。
    - 該定義的 boundary 不得留空。

12. **Lifecycle / Versioning / Compatibility**
    - Blueprint、schema、registry、share / restore、runtime contract、data model 等若存在版本演進，需定義 backward compatibility / reject / migrate / restore 行為。

13. **UI ↔ Function Parity**
    - Function 有 behavior 但沒有 UI state，或 UI 有 interaction 但 Function / Runtime contract 沒有 owner，均視為 gap。
    - UI/UX 不得自行發明 Product semantics。

14. **Registry Completeness**
    - Registry 必須足以限制 compiler / runtime 的合法能力、參數、validation 與 compatibility。
    - 不得只列名稱、卻把 contract 留給 LLM 或前端猜。

15. **Assumption / Decision Debt**
    - 未真正決定的內容不得偽裝成已完成 truth。
    - 必須標記為 OPEN / DECISION REQUIRED / DEFERRED，並判斷是否為 Build Freeze blocker。

16. **Cross-reference Integrity**
    - path、Function ID、Screen / Overlay、Registry、Data / API / Acceptance reference 必須指向現行 canonical owner。
    - 重整後的舊 path / stale reference 必須修正。

## 23.3 Review Execution Rule

Review 必須同時執行兩條線：

```text
Track A — Cleanup
duplicate
obsolete
wrong owner
contradiction
stale reference
build-only execution detail

Track B — Completeness
missing truth
ambiguity
edge cases
cross-layer gaps
acceptance gaps
NFR gaps
version / lifecycle gaps
UI ↔ Function gaps
registry gaps
decision debt
```

不得因 Track A 完成就宣稱 Review 完成。

## 23.4 Canonical Review Order

除非有 blocker，Review 順序為：

```text
working/common-core/
→ working/detailed-design/data-model/
→ working/detailed-design/infrastructure/
→ working/detailed-design/functions/
→ working/detailed-design/UI-UX/
→ working/detailed-design/registries/
→ cross-file consistency audit
→ acceptance mapping audit
→ UI/UX consistency audit
→ registry audit
→ Human approval
→ Build Freeze
```

Review 期間：
- 不改既定 folder structure，除非發現真正 authority blocker 並經 Human approval。
- 不因 cleanup 直接把全部 Working 搬入 appf2-build。
- 只在 Build Freeze 後 migration 該次 approved implementation truth。

## 23.5 Build Freeze Fitness Test

Working Content Quality Review 完成的最後判準：

> **如果今天把 Phase scope freeze，appf2-build / Cursor 能否只靠 approved Working truth，無需口頭補充、Chat 記憶或自行發明，即可建立唯一、正確、可驗證的 implementation contract？**

若答案不是 YES，則仍有 Review gap，不得進 Build Freeze。

