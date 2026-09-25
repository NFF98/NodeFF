# appf2 — SSOT

> appf2 Product Design 的唯一真實來源（Single Source of Truth）。

## Repository Authority

```text
appf2/appf2-design
= WHAT / WHY / WHEN
= Product Design Current Truth

appf2/appf2-build
= HOW / EXECUTION / EVIDENCE / RELEASE
= Build & Delivery Authority
```

appf2 唯一可修改 Current Truth：

```text
working/
```

不存在第二份 Formal Spec Current Truth。

## Canonical Flow

```text
Discussion
→ appf2 Working
→ Review / Consistency / Delta / Acceptance / UI Audit
→ Human approval
→ Build Freeze
→ appf2-build immutable BS-*
→ Backlog
→ Sprint
→ Cursor
→ Test / Evidence
→ Release
```

Build Spec 不是新的 Product Design SSOT；它是某一 approved Working commit 的 immutable implementation snapshot。

## SSOT Rules

1. Chat / Discussion 不是 Product Design truth。
2. `working/` 是 appf2 唯一 Product Design Current Truth。
3. 同一語意只能有一個 canonical Working owner。
4. Function detailed truth 以 Fxx 為單位，不拆成平行 FE / BE / API / DB 主規格。
5. Shared contract 只有真正跨 Function 時才進 shared Working owner。
6. `working/detailed-design/UI-UX/` 擁有 Screen composition / visual hierarchy / responsive / presentation；Function behavior semantics 仍由 `working/detailed-design/functions/Fxx-*.md` 擁有。
7. Machine-readable registries 把已批准 Working contract 轉為可驗證形式，不建立第二套產品語意。
8. Material Product / Architecture / UX / Contract / Acceptance change 必須先更新 appf2 Working 並經 Human approval。
9. Cursor 不得從 raw demand、Chat、歷史 Spec 或過期報告自行發明 Product Truth。
10. Implementation finding 若改變 UX / Contract / Product Semantics，必須回到 appf2 Working；批准後建立新的 appf2-build baseline。
11. 文件預設使用繁體中文；技術 identifier / API / Schema / Protocol 可保留英文。

## Canonical Structure

```text
README.md
SSOT.md

working/
  README.md
  DESIGN-WORKBENCH.md

  core/
    README.md
    APP-ARCHITECTURE.md
    APP-DETAILED-DESIGN-OVERVIEW.md
    DATA-MODEL.md
    INFRA-ARCHITECTURE.md
    BUSINESS-PLAN.md
    CAPABILITY-FABRIC.md
    TECHNICAL-MOAT.md
    API-CONVENTIONS.md
    ACCEPTANCE-CONVENTIONS.md
    EXECUTION-ADMISSION.md
    DESIGN-TO-DELIVERY.md

  architecture/
    evolution/
      PHASE-1.md
      PHASE-2.md
      PHASE-3.md
      PHASE-4-PLUS.md

  data-model/
    PHASE-1.md
    PHASE-2.md
    PHASE-3.md
    PHASE-4-PLUS.md

  infrastructure/
    PHASE-1.md
    PHASE-2.md
    PHASE-3.md
    PHASE-4-PLUS.md

  roadmap/
    product/
      PHASE-1.md
      PHASE-2.md
      PHASE-3.md
      PHASE-4-PLUS.md
    capability/
      PHASE-1.md
      PHASE-2.md
      PHASE-3.md
      PHASE-4-PLUS.md

  functions/
    Fxx-*.md

  UI-UX/
    PHASE1-SCREEN-INVENTORY.md
    screens/
    overlays/
    references/

  registries/
    recovery-registry.json
    evidence-event-registry.json
    acceptance-test-registry.json

archive/
```

## Growth / Phase Modularity Rule

同一產品語意仍只能有一個 canonical owner，但大型 owner 可以拆成 shared root + phase modules：

```text
Shared Core
+ Phase 1 module
+ Phase 2 delta
+ Phase 3 delta
+ Phase 4+ delta
```

規則：
1. 不建立 Phase 2 的整套平行 Working copy。
2. Phase module 只描述該 Phase 新增／啟用／migration／Gate，不複製 shared core。
3. Current Truth = shared root + 目前已啟用的 phase modules。
4. Future / deferred module 不因存在就自動進 implementation scope。
5. Build Freeze 必須明確列出本次包含哪些 phase modules。

## Retired / No-Use Structures

### `spec/`

**RETIRED / NO-USE.**

舊 `spec/` 曾是 reviewed implementation snapshot。Preservation Audit 已確認：

- required unique content = 0
- spec-only stable IDs = 0
- spec-only registry entries = 0
- Working 比舊 Spec 更新

因此 `spec/` 已移除，不再是任何 lifecycle / implementation authority。

### `execution/`

**RETIRED / NO-USE.**

Backlog / Sprint / implementation evidence / release execution 全部由 `appf2/appf2-build` 承接。

### `archive/`

**HISTORICAL EVIDENCE ONLY / NO AUTHORITY.**

`archive/` 可保存已退役治理、舊 Gate 報告、過去討論與協作紀錄，但不得作為：
- Product Design Current Truth
- Build Freeze input
- appf2-build Build Spec source
- Cursor implementation authority

若 archive 與 `working/` 衝突，一律以 `working/` 為準。

## Build Freeze

Human-approved Build Freeze 必須固定：

- exact appf2 Working source commit
- included Functions / Shared / UI-UX / Registries
- Phase / scope / non-scope
- Acceptance/Test mapping
- approval reference

Freeze 後輸出到：

```text
appf2/appf2-build/build-spec/baselines/BS-Px-nnn/
```

已鎖定 baseline 不得修改；任何 Product Design semantic change 都回 appf2 Working，批准後建立新 baseline。

## Authority Order

同一 Product Design 語意衝突時：

```text
appf2 Working Current Truth
> historical reports / discussion
```

Implementation scope / execution conflict時：

```text
Active appf2-build locked BS-*
> appf2-build backlog / sprint / code / test / evidence
```

如果 Active Build Spec 與最新 appf2 Working 不同，不代表任一方錯誤：
- Working = 最新 Product Design truth
- locked BS-* = 當次已批准 implementation snapshot

需要同步時必須走 Rebaseline，不得偷偷改舊 BS-*。

## Historical References

任何歷史文件中的：

- `spec/`
- Formal Spec
- Working → Spec
- Spec Promotion
- Formal Spec Refresh

全部視為 **LEGACY GOVERNANCE / NO-USE FOR CURRENT AUTHORITY**，除非已在現役 Working 文件中明確改寫成 Build Freeze / appf2-build BS-* 流程。
