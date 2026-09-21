# Function Specs

> Canonical home for approved Function-level implementation contracts。

每個 Fxx Spec 必須完整包含：

~~~text
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
~~~

規則：

- 一個 Function 一份 canonical Spec。
- 不把同一 Function 的 API/UI/Data 拆成平行主規格。
- File name沿用 Working 的 Fxx stable identity。
- 只有 SPEC_READY Function可進此目錄。
- Working仍是可修改 Current Working Truth；Spec是批准後 implementation contract。