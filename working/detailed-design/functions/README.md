# appf2 Functions

> **CURRENT AUTHORITY：appf2 Working Product Design Truth**

`working/detailed-design/functions/Fxx-*.md` 是 Function end-to-end Product Design 的 canonical home。

每個 Function 依成熟度可包含：

```text
Scope / Non-Scope
User Flow
UI / UX
Frontend State
Data / DB
API / Interfaces
Backend / Runtime
Capability dependency
Error / Recovery
Security / Permission
Evidence / Observability
Acceptance / Expected Observable
Compatibility / Versioning / Migration
```

規則：

1. 一個 Function 一份 canonical Working design。
2. 不把同一 Function 的 API / UI / Data 拆成平行主規格。
3. Phase 1 已完成詳細設計的 Function 仍以本目錄內容作 Current Truth。
4. Phase 2 / 3+ deferred Function 可以是不完整 Working baseline；必須明確標記 `DEFERRED_BASELINE / NOT_BUILD_FREEZE_READY`。
5. 日期本身不啟用 deferred Function；需要 Evidence + Human approval + complete Detailed Design + Build Freeze inclusion。
6. 未完成 detail不得由 appf2-build / Cursor自行補 Product Decision。
7. Human-approved Build Freeze 從 Working 投影到 `NFF98/appf2-build/build-spec/baselines/BS-*`；baseline immutable，不回寫覆蓋 appf2 Working。
8. Test mapping可留 stable Test ID / proof requirement；fixture、placement、CI 與 execution mechanics不留在 Function Design。
