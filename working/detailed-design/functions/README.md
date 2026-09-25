# NodeFF Functions

> **CURRENT AUTHORITY：NodeFF Working Product Design Truth**

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
Evidence
Acceptance / Tests
Compatibility / Migration
```

規則：

1. 一個 Function 一份 canonical Working design。
2. 不把同一 Function 的 API / UI / Data 拆成平行主規格。
3. Phase 1 已完成詳細設計的 Function 仍以本目錄內容作 Current Truth。
4. Phase 2 / 3 deferred Function 可以是不完整 Working baseline；未完成部分不得由 Cursor自行補產品決策。
5. 舊 `SPEC_READY` / Formal Spec / promotion 字樣只代表 retired governance lifecycle，不建立第二份 authority。
6. Build execution需要時，Human-approved Build Freeze 從 Working 投影到 `NFF98/NFFBuild/build-spec/baselines/BS-*`。
7. NFFBuild baseline是 immutable implementation snapshot，不回寫覆蓋 NodeFF Working。
