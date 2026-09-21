# NodeFF — SSOT

> NodeFF 專案的唯一真實來源（Single Source of Truth）。

## 狀態

- 專案：NodeFF
- Repository：NFF98/NodeFF
- 預設分支：main
- Working：Function-centric Current Truth
- Spec：Function-centric reviewed implementation contracts

## 目的

本文件定義 NodeFF 的權威專案結構與治理規則，避免同一 Function 被拆成 API / UI / Data 多份平行真相。

## SSOT 規則

1. Discussion / Chat 不是 implementation truth。
2. working/ 是目前可修改的 Current Working Truth。
3. spec/ 只放已 Review、可直接實作的正式 Contract。
4. execution/ 只能由已批准 Spec 派生。
5. 同一層級同一語意只能有一個 canonical owner。
6. Function detailed truth 以 Fxx 為單位，不拆成平行 FE/BE/API/DB 主規格。
7. Shared contract 只有真正跨 Function 時才進 shared owner。
8. 程式碼與測試不得覆蓋 Spec。
9. 產品行為 / public contract / data / security 變更必須先更新對應 Working/Spec。
10. decisions/ 記錄 architecture/product-impacting decisions。
11. execution/CHANGELOG.md 記錄已交付或已提交的 execution change。
12. 文件預設使用繁體中文；技術 identifier / API / Schema / Protocol 名稱可保留英文。

## Canonical Structure

~~~text
SSOT.md
README.md

working/
  APP-ARCHITECTURE.md
  APP-DETAILED-DESIGN-OVERVIEW.md
  DATA-MODEL.md
  API-CONVENTIONS.md
  EXECUTION-ADMISSION.md
  ACCEPTANCE-CONVENTIONS.md
  functions/
    Fxx-*.md
  registries/
    recovery-registry.json
    evidence-event-registry.json
    acceptance-test-registry.json

spec/
  functions/
    README.md
    Fxx-*.md
  shared/
    README.md
    DATA-MODEL.md
    API-CONVENTIONS.md
    EXECUTION-ADMISSION.md
    ACCEPTANCE-CONVENTIONS.md
    RECOVERY-REGISTRY.json
    EVIDENCE-EVENT-REGISTRY.json
    ACCEPTANCE-TEST-REGISTRY.json

decisions/
execution/
~~~

## Legacy Spec Files

spec/01-PRODUCT.md 到 spec/11-ACCEPTANCE.md 為早期橫向模板，現在只保留 index / navigation / legacy context。

它們：

- 不是 implementation truth；
- 不新增 Function-level detailed API / UI / Data / Error / Acceptance；
- 不得與 spec/functions 或 spec/shared 形成第二份 SSOT。

## 權威順序

同一語意的 authority 依 lifecycle：

~~~text
Spec
> Working
> Discussion
~~~

Repository governance authority：

1. SSOT.md
2. reviewed spec/functions + spec/shared
3. decisions/
4. working/（尚未升 Spec 的 Current Working Truth）
5. execution/
6. code / tests

若 code 與 approved Spec 衝突，以 Spec 為準並停止 implementation decision drift。

## Working → Spec

Working 只有通過 DESIGN-TO-DELIVERY 的 Spec Gate 才可升格。

Spec promotion：

- Function detailed contract → spec/functions/Fxx-*.md
- cross-Function shared contract → spec/shared/*
- 升格是 reviewed snapshot，不是重新改寫產品需求。

## Machine-readable Registries

Phase 1 Working registries：

- working/registries/recovery-registry.json
- working/registries/evidence-event-registry.json
- working/registries/acceptance-test-registry.json

它們把已批准的人類可讀 Contract 轉成 CI / codegen / review 可驗證形式，不建立第二套產品語意。

## 變更控制

如果預計實作內容與 approved Spec 衝突：

1. 停止實作；
2. 回 Working / Review；
3. 更新 shared / Function canonical owner；
4. 重新通過相關 Gate；
5. 再進 execution。
