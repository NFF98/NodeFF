# F01 — Intent Compilation + Model Gateway

> 狀態：DRAFT — MIGRATED CURRENT TRUTH
>
> 本文件在 SSOT Cleanup 中由 `working/APP-DETAILED-DESIGN.md` 的既有 Function 級內容搬入。此次搬移 **不改產品架構、不新增功能決策**；只是把既有 Current Truth 放回單一 Function canonical home。
>
> Horizon：0–1 月
>
> Delivery 規則：`working/DESIGN-TO-DELIVERY.md`
>
> Function Portfolio / Dependency / Release Scope：`working/APP-DETAILED-DESIGN.md`

# 1. Migrated Current Truth

F01 不允許「User Prompt → LLM 直接腦補 → Blueprint」的一步式生成。

正式流程：

~~~text
User Intent
→ Intent Analysis
→ Structured Intent Envelope
→ Clarification Policy
   ├─ READY
   ├─ READY_WITH_VISIBLE_ASSUMPTIONS
   └─ NEEDS_CLARIFICATION
→ Resolved Intent
→ Blueprint Compilation
→ F02 Validation
~~~

分工：
- LLM：理解 Intent、列出 unknown / ambiguity / assumption。
- NFF Clarification Policy：決定直接做、顯示假設、或必須追問。
- F00：把問題與假設用可編輯 UX 呈現。
- LLM 無權自行把關鍵缺口當成不重要。

#### Structured Intent Envelope

第一階段 LLM 只輸出 Intent Envelope，不產 Blueprint。

最低欄位：

~~~text
goal
actors / entities
known_inputs
constraints
requested_output
candidate_rules
missing_fields[]
ambiguities[]
assumptions[]
capability_hints[]
~~~

每個 missing / ambiguity / assumption 至少有：

~~~text
id
semantic_role
description
source
required_for_execution
impact_level
confidence
can_default
proposed_default
alternatives
user_visible
rationale
~~~

source：
- USER_EXPLICIT
- DOMAIN_KNOWN
- NFF_DEFAULT
- LLM_PROPOSED

impact_level：
- LOW
- MEDIUM
- HIGH
- CRITICAL

LLM_PROPOSED 永遠不能偽裝成 USER_EXPLICIT 或 DOMAIN_KNOWN。

#### Clarification Policy

這是 NFF-owned deterministic policy，不是另一個自由 Prompt。

~~~text
CP-001 必要執行值缺失，且沒有安全明確 default
→ NEEDS_CLARIFICATION

CP-002 有兩個以上合理 interpretation，且會造成 HIGH / CRITICAL 結果差異
→ NEEDS_CLARIFICATION

CP-003 涉及金額、權限、外部成本或不可逆行為，關鍵規則不是 User Explicit
→ NEEDS_CLARIFICATION

CP-004 有安全、可逆 default，但會影響業務結果
→ READY_WITH_VISIBLE_ASSUMPTIONS

CP-005 只影響畫面或 cosmetic，不影響核心結果
→ READY

CP-006 資訊完整且沒有 material ambiguity
→ READY
~~~

規則：
- 一次最多問 1–3 個最高資訊價值問題。
- 問題必須直接對應 blocker / material ambiguity。
- 已回答問題不得重問，除非上游條件改變。
- Policy rule 有 stable ID 與 version，可測試、可 telemetry、可擴充。
- Domain-specific required fields 可由 Domain Policy Pack 擴充，但不能繞過 Core Policy。

#### Question Priority

~~~text
Execution Blocker
> Safety / Money / Permission
> High Outcome Divergence
> Core Business Rule
> Secondary Preference
> Cosmetic
~~~

同層優先問「回答一次可以消除最多下游不確定性」的問題。

#### Visible Assumptions

NFF 必須區分：

~~~text
FACT
= User 明講或可信資料源提供

DEFAULT
= NFF 版本化預設

PROPOSAL
= LLM 建議

UNKNOWN
= 目前不能可靠決定
~~~

UI 不得把 PROPOSAL 顯示成 FACT。

公司分帳例：

~~~text
User:
「公司 50 人，有老闆、經理、員工，聚餐幫我分帳」

解析：
total_people = 50
roles = owner / manager / employee
bill_total = UNKNOWN
role_counts = UNKNOWN
weight_rule = PROPOSAL(3:2:1)

UI:
總金額 [_____]
老闆 [1]  經理 [5]  員工 [44]
建議權重：老闆 [3] : 經理 [2] : 員工 [1]
「這是建議值，可直接修改」
~~~

確認後才形成 Resolved Intent。

#### LLM Prompt Contract

不採單一 mega-prompt，採兩個版本化 Prompt。

**Prompt A — Intent Analyst**

輸入：
- raw user intent
- conversation / correction context
- relevant Inspiration Capsule metadata
- capability semantic catalog
- domain policy metadata

硬指令：
1. Preserve user-stated facts exactly.
2. Separate facts, unknowns, defaults and proposals.
3. Never invent a required business value.
4. Identify ambiguities that materially change outcome.
5. Propose defaults only when safe and reversible.
6. Mark proposal provenance and impact.
7. Output Structured Intent Envelope only.
8. Do not generate Blueprint yet.

**Prompt B — Blueprint Composer**

只有 Clarification Gate 通過後才執行。

輸入：
- resolved_intent
- accepted_visible_assumptions
- capability_registry_snapshot
- LegoSpec schema
- security/resource policy
- existing_blueprint when refining

硬指令：
1. Treat resolved_intent as semantic source of truth.
2. Do not introduce new business assumptions.
3. Use only registered capabilities/operators.
4. Preserve invariants and requested totals.
5. Output Blueprint Candidate only.
6. Never output arbitrary JavaScript.

Prompt 必須帶：
- prompt_version
- schema_version
- registry_version
- model_adapter
- evaluation_fixture_version

因此 Prompt 可回放、A/B、Regression Test，不是散落字串。

#### Fast Path

Clarification Gate 每次都執行，但 User 不一定每次被問。

~~~text
Clear Intent
→ READY
→ immediately compile

Minor material assumption
→ READY_WITH_VISIBLE_ASSUMPTIONS
→ show/edit assumption
→ compile

Critical missing information
→ NEEDS_CLARIFICATION
→ ask blocker
→ merge answer
→ re-run policy
→ compile
~~~

Model Gateway 最小要求：

- NFF-owned interface
- 至少一個 production adapter
- provider config 不進 LegoSpec
- timeout / provider failure 可分類
- future provider switch 不改 F02 / F03 contract

Acceptance：

- output 只能是受控 Blueprint Candidate
- unsupported intent 不 fake success
- provider failure 有 bounded recovery
- semantic mismatch 可被 evidence 捕捉

# Status Note

此文件目前是從既有 Portfolio 文件搬出的 Working 內容，**不因搬家自動升格為完整 Function Spec / SPEC_READY**。後續 Detailed Design 仍需依 Design-to-Delivery Contract 補齊缺少的 UI / API / Data / Error / Security / Evidence / Acceptance 等部分。
