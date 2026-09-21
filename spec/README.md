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

spec/01–11 是早期橫向模板，現在只保留 navigation / legacy compatibility。

它們不得承載 Function-level 詳細 implementation truth。

## Current Phase 1 Gate

Latest audit：

- working/ProjectManagement/PHASE1-CORE-SPEC-GATE-AUDIT.md
- Verdict：HOLD — NOT SPEC_READY

在 Gate 關閉前，spec/functions 不放假裝批准的 Function Spec。