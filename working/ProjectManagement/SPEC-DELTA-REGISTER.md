# NodeFF Spec Delta Register

> Status：Working Governance Current Truth
>
> Purpose：唯一追蹤 **Working Current Truth 已變更、但 frozen Formal Spec 尚未同步** 的 Material / Architecture-impacting Delta。
>
> 本 Register 不複製產品語意。產品 / Runtime / Data / API / UX / Recovery / Evidence / Acceptance 的 canonical meaning 仍由對應 Working owner 擁有；本文件只管理 traceability、promotion 與 verification。
>
> Formal Spec、Backlog / Sprint、Cursor implementation 不因本 Register 自動變更。任何 Formal promotion 仍需 User 明確批准。

---

# 1. Why This Register Exists

NodeFF 目前採：

~~~text
Working keeps moving
→ Formal Spec temporarily frozen
→ one pre-Cursor Formal Spec Refresh
~~~

因此必須避免：

- Working 已批准，但 Formal Spec 漏同步。
- Function Markdown 已同步，但 machine-readable registry 漏同步。
- Spec 已同步，但 Acceptance / Test 漏同步。
- Acceptance / Test 已同步，但 Backlog 漏派生。
- Backlog 出現無法反向追到 approved Working / Spec 的 orphan task。

本 Register 是以上差異的唯一總帳。

---

# 2. Delta ID

格式：

~~~text
SD-YYYYMMDD-NNN
~~~

Example：

~~~text
SD-20260922-001
~~~

同一個 semantic delta 即使影響多個 Function / Shared Contract，也只使用一個 Delta ID。

不得把同一件事拆成多筆以規避完整 promotion / verification。

---

# 3. Lifecycle

Canonical lifecycle：

~~~text
OPEN
→ REVIEWED
→ APPROVED
→ PROMOTED
→ VERIFIED
~~~

## OPEN

Material / Architecture-impacting Working Delta 已被識別，但 Working review 尚未完成。

## REVIEWED

Working review 已完成，內容已可批准，但尚未取得 User 明確批准。

## APPROVED

User 已明確批准 Working Current Truth。

代表：

- Working semantic owners 已閉合；
- 可等待既定 Formal Spec Refresh 時點；
- **不代表 Formal Spec 已同步**；
- **不代表 Cursor 可 implementation**。

## PROMOTED

該 Delta 所列全部 Formal targets 已完成 promotion。

Partial promotion 不得標 PROMOTED。

## VERIFIED

完成雙向 traceability verification：

~~~text
Working
→ Formal Spec
→ Acceptance / Test
→ Backlog

and

Backlog
→ Acceptance / Test
→ Formal Spec
→ Working
~~~

且沒有漏同步、orphan contract、orphan execution item。

只有 VERIFIED 才代表該 Delta 對 pre-Cursor Spec Refresh Gate 已清帳。

---

# 4. Required Fields Per Delta

每一筆 Delta 至少記：

- Delta ID
- Title
- Change Class
- Origin / Reason
- Canonical Working Sources
- Supporting Working / UX Evidence
- Affected Formal Spec Targets
- Acceptance / Test
- Registry / Stable ID Impact
- Status
- Working Approval / Closure Commit
- Promotion Commit
- Verification Evidence
- Notes / migration handling when relevant

---

# 5. Promotion Completeness Rule

一筆 Delta 若同時影響 human-readable contract 與 machine-readable registry：

> **兩者都必須 promotion，才算 PROMOTED。**

例如：

~~~text
F03 Runtime semantics changed
+ new F03 error
+ new F03 evidence events
+ new Acceptance/Test

→ F03 Formal Function Spec
→ Recovery Registry
→ Evidence Event Registry
→ Acceptance/Test Registry
~~~

只更新 F03 Markdown，不算完整 promotion。

---

# 6. Current Delta Summary

| Delta ID | Title | Status | Working Closure | Promotion | Verification |
|---|---|---|---|---|---|
| SD-20260922-001 | Runtime Global Loading + Timeout | **APPROVED** | 96800388424929c616f803976d4630561762b923 | PENDING | PENDING |

Current counts：

~~~text
OPEN = 0
REVIEWED = 0
APPROVED but not PROMOTED = 1
PROMOTED but not VERIFIED = 0

PRE-CURSOR SPEC REFRESH GATE = HOLD
~~~

HOLD 是目前預期狀態：Formal Spec 仍 frozen，尚未進 pre-Cursor Formal Spec Refresh。

---

# 7. SD-20260922-001 — Runtime Global Loading + Timeout

## Delta ID

SD-20260922-001

## Title

Runtime Global Loading + Timeout

## Change Class

MATERIAL

## Origin / Reason

來源為 O05 Loading / Building / Hydration ④A Low-fi Review。

User 已確認：

- S03 normal Runtime interaction 也建立 logical global processing state。
- Stage label + checkpoint-derived Progress % 為全站 processing direction。
- progress 不代表剩餘時間，不得 fake inflation。
- Runtime action 必須有 bounded timeout lifecycle。
- Hard Timeout 後 late / stale completion 不得 commit。
- integrity 成立時保留 last-known-good Runtime；不成立時 fail closed。
- Recovery Retry 建立新的 operation token。

## Canonical Working Sources

Semantic owners：

- working/functions/F00-EXPERIENCE-SHELL.md
- working/functions/F03-RUNTIME-EXECUTION.md
- working/functions/F12-HUMANIZED-RECOVERY.md

## Supporting Working / UX Evidence

- working/UI-UX/screens/S03-APP-RUNTIME.md
- working/UI-UX/overlays/O05-LOADING-BUILDING-HYDRATION.md
- working/UI-UX/PHASE1-SCREEN-INVENTORY.md
- working/DESIGN-WORKBENCH.md

Supporting Screen / UX files不是 Formal promotion targets；Function / Shared contracts仍是 behavior authority。

## Affected Formal Spec Targets

Human-readable Function Specs：

1. spec/functions/F00-EXPERIENCE-SHELL.md
2. spec/functions/F03-RUNTIME-EXECUTION.md
3. spec/functions/F12-HUMANIZED-RECOVERY.md

Machine-readable Shared Spec Registries：

4. spec/shared/RECOVERY-REGISTRY.json
5. spec/shared/EVIDENCE-EVENT-REGISTRY.json
6. spec/shared/ACCEPTANCE-TEST-REGISTRY.json

**Promotion completeness = 6 / 6 targets synced。**

## Acceptance / Test

Superseded lifecycle：

- F00-AC-008 / TEST-F00-008
  - Formal baseline保留原 stable ID / 原語意。
  - Working disposition = SUPERSEDED。
  - Formal Refresh 時標記 deprecated；不得改寫或重用舊 ID。

New required contracts：

~~~text
F00-AC-029 → TEST-F00-029
F00-AC-030 → TEST-F00-030
F00-AC-031 → TEST-F00-031
F00-AC-032 → TEST-F00-032

F03-AC-030 → TEST-F03-030
F03-AC-031 → TEST-F03-031
F03-AC-032 → TEST-F03-032
F03-AC-033 → TEST-F03-033
F03-AC-034 → TEST-F03-034
F03-AC-035 → TEST-F03-035
F03-AC-036 → TEST-F03-036

F12-AC-029 → TEST-F12-029
F12-AC-030 → TEST-F12-030
F12-AC-031 → TEST-F12-031
~~~

Total new Acceptance / Test contracts：14。

## Registry / Stable ID Impact

Recovery：

~~~text
F03-ERR-021 RUNTIME_ACTION_TIMEOUT
→ F12-POL-011 Runtime Timeout Preserve Last Known Good
~~~

Evidence：

~~~text
F03-EVT-011 runtime_operation_started
F03-EVT-012 runtime_checkpoint_completed
F03-EVT-013 runtime_soft_timeout_observed
F03-EVT-014 runtime_action_timed_out
F03-EVT-015 stale_completion_discarded
F03-EVT-016 runtime_safe_state_restored
~~~

Working registry delta relative to frozen Formal baseline：

~~~text
Recovery Registry
121 → 122

Evidence Event Registry
106 → 112

Acceptance/Test Registry
257 → 271
~~~

## Status

APPROVED

Reason：

- Working Function Delta Review 已完成。
- User 已批准 Working Current Truth。
- F00 / F03 / F12 已標 WORKING_DELTA_CLOSED / FORMAL_REFRESH_PENDING。
- Formal Spec 依 sequencing rule 維持 frozen，尚未 promotion。

## Working Approval / Closure Commit

96800388424929c616f803976d4630561762b923

Commit message：

docs: close Runtime loading and timeout function delta

## Promotion Commit

PENDING

只有 6 / 6 Formal targets 同步後才能填入 promotion commit 並把狀態改為 PROMOTED。

## Verification Evidence

PENDING

至少需記錄：

- Working → Formal diff audit
- Formal stable ID lifecycle audit
- Formal registries completeness / counts
- Acceptance → Test mapping check
- Formal Spec → Backlog forward mapping
- Backlog → Acceptance / Formal / Working reverse mapping
- orphan contract = 0
- orphan execution item = 0

完成後才可改為 VERIFIED。

---

# 8. Pre-Cursor Gate Query

正式 Cursor implementation 前，必須以本 Register 執行：

~~~text
OPEN = 0
REVIEWED = 0
APPROVED but not PROMOTED = 0
PROMOTED but not VERIFIED = 0
~~~

等價規則：

> **所有 active Spec Delta 必須 VERIFIED。**

任何一項非 0：

~~~text
SPEC REFRESH GATE = HOLD
CURSOR IMPLEMENTATION = HOLD
~~~

不得以「大部分已同步」解除 Gate。

---

# 9. Forward Traceability Check

每筆 Delta 必須完整核對：

~~~text
Working Current Truth
→ Formal Function / Shared Spec
→ Acceptance / Test Contract
→ Backlog item
~~~

檢查：

1. 每個 canonical Working change都有對應 Formal owner。
2. 所有受影響 Formal owners均已同步。
3. Required stable ID / registry mapping均已同步。
4. Required Acceptance均有 Test Contract。
5. Backlog item只從已 promotion的 Formal Spec / Acceptance派生。

---

# 10. Reverse Traceability Check

從 downstream 反查：

~~~text
Backlog
→ Acceptance / Test
→ Formal Spec
→ Working Delta / approved baseline
~~~

任何因本輪 Refresh 新增 / 修改的：

- Backlog item
- Acceptance / Test
- Formal contract
- Registry entry

都必須能回到：

- 本 Register 的一筆 SD-*；或
- 已存在且未變更的 approved Formal baseline。

不得有：

~~~text
orphan backlog
orphan acceptance
orphan formal contract
unregistered working delta
~~~

---

# 11. Discovery Rule For Future Deltas

只要 Material / Architecture-impacting Working change會使 frozen Formal Spec 不再等同 Current Truth，就必須新增或更新一筆 SD-*。

特別是 canonical Working owner出現以下概念時：

- FORMAL_REFRESH_PENDING
- WORKING_DELTA_*
- superseded Formal stable ID
- new / changed Acceptance
- new / changed Error / Policy / Event
- API / Data / Runtime / Security / Compatibility semantic change

都必須確認能追到本 Register。

Visual-only、copy-only 且不改 semantic contract 的 change，不必強制建立 Spec Delta。

---

# 12. Governance Rules

1. 本 Register 是 Spec Delta 的唯一總帳，不在其他文件建立平行 Delta ledger。
2. Delta semantic truth仍由 canonical Working owner擁有。
3. APPROVED 不等於 PROMOTED。
4. PROMOTED 不等於 VERIFIED。
5. Working file寫 CLOSED 不代表 Formal debt已清。
6. Partial Formal promotion不得改為 PROMOTED。
7. Formal promotion仍需 User明確批准。
8. Spec Refresh完成後才進 Backlog / Sprint refresh。
9. Backlog / Sprint refresh完成且 Gate通過後，才可解除 Cursor implementation HOLD。
10. 每次 status transition都必須有 GitHub commit / evidence reference。

---

# Current Truth

截至 2026-09-22：

~~~text
SD-20260922-001
Runtime Global Loading + Timeout
= APPROVED
= Working closed
= Formal promotion pending
= Verification pending

NEXT
→ UI/UX Cross-Screen Consistency Review

HOLD
→ High-fi until Cross-Screen gate allows
→ Formal Spec Refresh until planned pre-Cursor refresh
→ Backlog / Sprint refresh
→ Cursor implementation
~~~
