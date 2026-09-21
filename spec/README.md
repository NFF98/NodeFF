# NodeFF Formal Spec

> Canonical Structure：Function-centric + Shared Contracts。
>
> 本目錄只保存已通過 Working → Spec Gate 的 implementation contracts。

## Canonical Spec Ownership

~~~text
spec/functions/Fxx-*.md
→ 單一 Function 的完整 end-to-end Spec

spec/shared/*.md
→ 真正跨 Function 的共享 Contract
~~~

禁止再依 Frontend / Backend / API / DB / UI 拆成平行詳細主規格。

## Promotion Rule

~~~text
working/functions/Fxx-*.md
→ Cross-Function Gate Review
→ SPEC_READY
→ spec/functions/Fxx-*.md
~~~

Shared Working Truth：

~~~text
working/DATA-MODEL.md
working/INFRA-ARCHITECTURE.md
working/ProjectManagement/CAPABILITY-FABRIC.md
working/DESIGN-TO-DELIVERY.md
~~~

只有通過 Gate 的 shared contract 才升到 spec/shared。

## Legacy Root Files

spec/ 根目錄仍保留的早期橫向模板（01–07、09–11）只作 navigation / legacy compatibility。

`spec/08-UI.md` 已刪除；UI/UX 不再回到舊橫向單檔模式。

它們不得承載 Function-level 詳細 implementation truth。

## Current Phase 1 Gate

Latest re-audit：

- working/ProjectManagement/PHASE1-CORE-SPEC-GATE-REAUDIT.md
- Completion report：working/ProjectManagement/PHASE1-GATE-CLOSURE-SPRINT-REPORT.md
- Verdict：PASS — SPEC_READY
- Phase 1 Core Function Specs：10 / 10 promoted

Implementation authority：

~~~text
spec/functions/
spec/shared/
~~~

Historical pre-closure HOLD audit：

- working/ProjectManagement/PHASE1-CORE-SPEC-GATE-AUDIT.md