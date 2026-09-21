# NodeFF App Detailed Design

> 狀態：Working Design Baseline。
>
> **Canonical Responsibility：Function Portfolio / Dependency / Release Scope / Function Status Index。**
>
> 單一 Function 的 UI / Frontend / API / Data / Backend / Runtime / Error / Security / Evidence / Acceptance 詳細內容，唯一 canonical home 是 `working/functions/Fxx-*.md`。
>
> 本文件不得再次承載 Function 級詳細設計，避免形成兩份 Current Truth。

# 1. Purpose

Architecture 回答：
> NFF 是什麼、系統邊界在哪裡。

本文件回答：
> 有哪些 Functions、彼此依賴什麼、哪個 Phase 做、目前進度在哪裡、詳細設計去哪裡看。

Function 詳細設計回答：
> 這個 Function 從 User Outcome 到 UI / API / Data / Runtime / Error / Test 到底怎麼做。

---

# 2. Document Responsibility Boundary

~~~text
working/APP-ARCHITECTURE.md
→ Top Architecture / system boundary

working/APP-DETAILED-DESIGN.md
→ Function Portfolio / Dependency / Release / Status Index

working/DATA-MODEL.md
→ shared canonical data model

working/ProjectManagement/CAPABILITY-FABRIC.md
→ capability semantic contract

working/functions/Fxx-*.md
→ single Function end-to-end detailed design

working/DESIGN-TO-DELIVERY.md
→ Working → Spec → Execution → Test → Release governance
~~~

同一 Function 的 detailed behavior 不得同時在本文件與 Fxx 文件各維護一份。

---

# 3. Function Portfolio / Canonical Index

| ID | Function | 核心結果 | Phase | Working Status | Canonical Detail |
|---|---|---|---|---|---|
| F00 | Experience Shell / 靈感精靈 | User 能容易開始、Refine、Remix、Recovery | 0–1 月 | WORKING_BASELINE | `functions/F00-EXPERIENCE-SHELL.md` |
| F01 | Intent Compilation + Model Gateway | Intent → Blueprint Candidate | 0–1 月 | WORKING_BASELINE | `functions/F01-INTENT-COMPILATION.md` |
| F02 | Blueprint Validation / Trust Admission | 不可信 Blueprint 不進 Runtime | 0–1 月 | WORKING_BASELINE | `functions/F02-BLUEPRINT-VALIDATION.md` |
| F03 | Runtime Execution | Blueprint → Interactive App | 0–1 月 | WORKING_BASELINE | `functions/F03-RUNTIME-EXECUTION.md` |
| F04 | Capability Registry / Resolution | Compiler / Validator / Runtime 共用能力真相 | 0–1 月 | WORKING_BASELINE | `functions/F04-CAPABILITY-REGISTRY.md` |
| F05 | Share / Restore | Link → Recipient 可立即使用 | 0–1 月 | WORKING_BASELINE | `functions/F05-SHARE-RESTORE.md` |
| F06 | Remix / Refine | Existing App → Semantic Delta → New Blueprint | 0–1 月 | WORKING_BASELINE | `functions/F06-REMIX-REFINE.md` |
| F07 | Anonymous Identity & Evidence | No-login continuity + PMF evidence | 0–1 月 | DRAFT | `functions/F07-ANONYMOUS-IDENTITY-EVIDENCE.md` |
| F08 | Durable Identity / Ownership | Anonymous → Account → Ownership | 2–3 月 | DEFERRED_BASELINE | `functions/F08-DURABLE-IDENTITY-OWNERSHIP.md` |
| F09 | Realtime Room | 多人共享 Instance State | 2–3 月 | DEFERRED_BASELINE | `functions/F09-REALTIME-ROOM.md` |
| F10 | Blueprint Reuse / Retrieval | Trusted Blueprint reuse | 2–3 月 | DEFERRED_BASELINE | `functions/F10-BLUEPRINT-REUSE-RETRIEVAL.md` |
| F11 | External Capability Execution | AI / API / Heavy Work 受控執行 | 4–6 月 | DEFERRED_BASELINE | `functions/F11-EXTERNAL-CAPABILITY-EXECUTION.md` |
| F12 | Humanized Recovery Orchestration | 技術錯誤 → 可理解、可繼續 UX | 0–1 月 | DRAFT | `functions/F12-HUMANIZED-RECOVERY.md` |
| F13 | Entitlement / Metering | Premium / Costly Capability 可控可量測 | 2–6 月 | DEFERRED_BASELINE | `functions/F13-ENTITLEMENT-METERING.md` |
| F14 | Provider Registry / Certification | External Capability 可被信任與版本化 | 6 月後 | DEFERRED_BASELINE | `functions/F14-PROVIDER-REGISTRY-CERTIFICATION.md` |
| F15 | Transaction / Settlement | Commerce Outcome 可追蹤、對帳、結算 | 6 月後 | DEFERRED_BASELINE | `functions/F15-TRANSACTION-SETTLEMENT.md` |
| F16 | Result Feedback / Logic Correction | 錯誤結果可修正、比較、回退 | 0–1 月 | DRAFT | `functions/F16-RESULT-CORRECTION.md` |
| F17 | Heterogeneous Workflow Orchestration | 多異質 steps 完成同一 Outcome | 6 月後 | DEFERRED_BASELINE | `functions/F17-WORKFLOW-ORCHESTRATION.md` |

搬家本身不代表 Function 已完成 Detailed Design。

---

# 4. Function Dependency Map

~~~mermaid
flowchart TD
    F00[F00 Experience Shell]
    F01[F01 Intent Compilation]
    F02[F02 Validation]
    F03[F03 Runtime]
    F04[F04 Capability Registry]
    F05[F05 Share / Restore]
    F06[F06 Remix / Refine]
    F07[F07 Anonymous Evidence]
    F12[F12 Recovery]
    F16[F16 Result Correction]

    F08[F08 Identity / Ownership]
    F09[F09 Realtime]
    F10[F10 Reuse / Retrieval]
    F13[F13 Entitlement / Metering]

    F11[F11 External Capability]
    F14[F14 Provider Registry]
    F15[F15 Transaction / Settlement]
    F17[F17 Workflow Orchestration]

    F00 --> F01
    F04 --> F01
    F01 --> F02
    F04 --> F02
    F02 --> F03
    F04 --> F03

    F03 --> F05
    F05 --> F06
    F01 --> F06

    F07 --> F01
    F07 --> F05
    F07 --> F06

    F00 --> F16
    F03 --> F16
    F06 --> F16
    F16 --> F01
    F16 --> F02
    F16 --> F07

    F12 --> F00
    F01 --> F12
    F02 --> F12
    F03 --> F12
    F04 --> F12

    F07 --> F08
    F05 --> F08

    F04 --> F10
    F07 --> F10
    F10 --> F01

    F03 --> F09
    F08 --> F09

    F04 --> F11
    F03 --> F11
    F13 --> F11

    F08 --> F13
    F07 --> F13

    F11 --> F14
    F13 --> F14
    F14 --> F15
    F11 --> F17
    F13 --> F17
    F14 --> F17
    F17 --> F15
~~~

設計含義：

> **第 1 個月不是「先做畫面」，而是先建立完整 Core Loop 的最短可信任路徑。**

---

# 5. Release Scope

## Release 1 — Core Loop，0–1 月

~~~text
F00 + F01 + F02 + F03 + F04 + F05 + F06 + F07 + F12 + F16
~~~

Outcome：
> Intent → Correct App → Use → Share → Remix → Correct Result → Recover

Release 1 Gate：

~~~text
Create works
+ Semantic quality measurable
+ Runtime stable
+ Share works
+ Recipient uses
+ Remix works
+ Wrong result / logic can be corrected without restarting
+ Old / new result can be compared or reverted
+ Failure recoverable
+ Evidence collected
~~~

Build 成功不等於 Release 1 完成。

## Release 2 — Durable Value，2–3 月

~~~text
F08 + F10
+ F09 if proven
+ F13 Basic
+ hardening of Release 1
~~~

Outcome：
> Reuse → Identity → Ownership → Creator Value

## Release 3 — Scale Readiness，4–6 月

~~~text
F11
+ F13 Production
+ reliability / compatibility / cost hardening
~~~

Outcome：
> External / Paid Capability 可以安全接入

## Continuous Platform Releases，6 月後

~~~text
F14 + F15 + F17
+ provider / commerce / orchestration expansion
~~~

Outcome：
> Intent Commerce / Capability Network / Heterogeneous Orchestration 持續擴張

日期不自動解鎖下一 Phase；Evidence Gate 才解鎖。

---

# 6. Cross-Function Contract Index

本節只指出 canonical owner，不重複 Contract 內容。

| Contract | Canonical Home |
|---|---|
| Blueprint / Trust Admission | `functions/F02-BLUEPRINT-VALIDATION.md` + `DATA-MODEL.md` |
| Runtime Semantics | `functions/F03-RUNTIME-EXECUTION.md` |
| Capability Contract / Registry | `ProjectManagement/CAPABILITY-FABRIC.md` + `functions/F04-CAPABILITY-REGISTRY.md` |
| Result Quality / Logic Correction | `functions/F16-RESULT-CORRECTION.md` |
| Recovery | `functions/F12-HUMANIZED-RECOVERY.md` |
| Anonymous Evidence | `functions/F07-ANONYMOUS-IDENTITY-EVIDENCE.md` |
| Durable Identity / Ownership | `functions/F08-DURABLE-IDENTITY-OWNERSHIP.md` + `DATA-MODEL.md` |
| Delivery / Acceptance / Release Gate | `DESIGN-TO-DELIVERY.md` |

---

# 7. Function Design Rule

每個 Fxx 最終必須在自己的文件串通：

~~~text
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
~~~

缺少任何必要環節，就不是 SPEC_READY。

---

# 8. Portfolio Guardrails

1. Function 是 User Outcome，不是單純 technical module。
2. Frontend / Backend / Runtime 必須在同一 Function flow 裡一起設計。
3. Architecture 決定邊界，Cursor 不發明新架構。
4. 所有跨 Function Contract 只能有 canonical source。
5. Error / Recovery 是功能本身，不是最後補上的例外。
6. Result Correction 是核心 UX，不是把錯誤 Prompt 叫 User 從頭重做。
7. Runtime Success 不等於 Semantic / Product Success。
8. Capability Gap 是 Evidence，不是用 heuristic 假裝解決。
9. Phase 1 優先完成完整 Core Loop，不追求大量 Capability。
10. 第 2–3 個月才把 Anonymous Value 升成 Durable Identity。
11. 第 4–6 個月才把 External / Paid Capability 提升為正式 execution path。
12. 6 個月後才持續建 Provider / Transaction / Orchestration Network。
13. Workflow engine vendor 只能是 Adapter，不得成為 NFF semantic contract。
14. Multi-step external workflow 必須有 timeout / retry / idempotency / compensation policy。
15. 日期不自動解鎖功能；Evidence Gate 才解鎖。
16. 所有新 Function 必須證明不破壞 Intent → Blueprint → Runtime 核心。

---

# 9. Design → Delivery

Lifecycle、Traceability ID、Working → Spec Gate、Acceptance → Test、Runtime Debug、Release Gate、CT Commit/Revert 規則，只引用：

> `working/DESIGN-TO-DELIVERY.md`

本文件不再複製 Delivery Contract。

# Conclusion

APP-DETAILED-DESIGN 現在只做一件事：

> **管理 NodeFF 的 Function 地圖：有誰、依賴誰、何時做、目前做到哪裡，以及詳細設計唯一去哪裡看。**

真正 Function 行為只存在各自 Fxx canonical file；不再出現 APP-DETAILED-DESIGN 一套、Fxx 又一套的 Current Truth 衝突。
