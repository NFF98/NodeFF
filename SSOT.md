# NodeFF — SSOT

> NodeFF Product Design 的唯一真實來源（Single Source of Truth）。

## Repository Authority

```text
NFF98/NodeFF
= WHAT / WHY / WHEN
= Product Design Current Truth

NFF98/NFFBuild
= HOW / EXECUTION / EVIDENCE / RELEASE
= Build & Delivery Authority
```

NodeFF 唯一可修改 Current Truth：

```text
working/
```

不存在第二份 Formal Spec Current Truth。

## Canonical Flow

```text
Discussion
→ NodeFF Working
→ Review / Consistency / Delta / Acceptance / UI Audit
→ Human approval
→ Build Freeze
→ NFFBuild immutable BS-*
→ Backlog
→ Sprint
→ Cursor
→ Test / Evidence
→ Release
```

Build Spec 不是新的 Product Design SSOT；它是某一 approved Working commit 的 immutable implementation snapshot。

## SSOT Rules

1. Chat / Discussion 不是 Product Design truth。
2. `working/` 是 NodeFF 唯一 Product Design Current Truth。
3. 同一語意只能有一個 canonical Working owner。
4. Function detailed truth 以 Fxx 為單位，不拆成平行 FE / BE / API / DB 主規格。
5. Shared contract 只有真正跨 Function 時才進 shared Working owner。
6. `working/UI-UX/` 擁有 Screen composition / visual hierarchy / responsive / presentation；Function behavior semantics 仍由 `working/functions/Fxx-*.md` 擁有。
7. Machine-readable registries 把已批准 Working contract 轉為可驗證形式，不建立第二套產品語意。
8. Material Product / Architecture / UX / Contract / Acceptance change 必須先更新 NodeFF Working 並經 Human approval。
9. Cursor 不得從 raw demand、Chat、歷史 Spec 或過期報告自行發明 Product Truth。
10. Implementation finding 若改變 UX / Contract / Product Semantics，必須回到 NodeFF Working；批准後建立新的 NFFBuild baseline。
11. 文件預設使用繁體中文；技術 identifier / API / Schema / Protocol 可保留英文。

## Canonical Structure

```text
README.md
SSOT.md

working/
  APP-ARCHITECTURE.md
  APP-DETAILED-DESIGN-OVERVIEW.md
  DATA-MODEL.md
  API-CONVENTIONS.md
  EXECUTION-ADMISSION.md
  ACCEPTANCE-CONVENTIONS.md
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
  ProjectManagement/

decisions/
```

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

Backlog / Sprint / implementation evidence / release execution 全部由 `NFF98/NFFBuild` 承接。

## Build Freeze

Human-approved Build Freeze 必須固定：

- exact NodeFF Working source commit
- included Functions / Shared / UI-UX / Registries
- Phase / scope / non-scope
- Acceptance/Test mapping
- approval reference

Freeze 後輸出到：

```text
NFF98/NFFBuild/build-spec/baselines/BS-Px-nnn/
```

已鎖定 baseline 不得修改；任何 Product Design semantic change 都回 NodeFF Working，批准後建立新 baseline。

## Authority Order

同一 Product Design 語意衝突時：

```text
NodeFF Working Current Truth
> approved decision records
> historical reports / discussion
```

Implementation scope / execution conflict時：

```text
Active NFFBuild locked BS-*
> NFFBuild backlog / sprint / code / test / evidence
```

如果 Active Build Spec 與最新 NodeFF Working 不同，不代表任一方錯誤：
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

全部視為 **LEGACY GOVERNANCE / NO-USE FOR CURRENT AUTHORITY**，除非已在現役 Working 文件中明確改寫成 Build Freeze / NFFBuild BS-* 流程。
