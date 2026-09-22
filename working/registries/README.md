# Phase 1 Machine-readable Registries

此目錄是 Working 階段可由 CI / code generation / review 使用的 structured contract source。

- recovery-registry.json：stable source error → F12 recovery policy / message / actions。
- evidence-event-registry.json：stable event ID → F07 collection / property / retention metadata。
- acceptance-test-registry.json：stable Acceptance ID → Test Contract；已進 Formal的舊 ID保留原語意，以 superseded / deprecated lifecycle處理，不重用或改寫。

規則：

1. JSON registry不是第二份產品語意；source error/event meaning仍由Fxx + F12/F07擁有。
2. Registry負責把已批准語意變成machine-readable mapping。
3. 新增/變更stable ID時，Markdown owner與JSON registry必須同commit更新。
4. Spec promotion後，reviewed snapshot升到spec/shared對應registry。

Current Working registry baseline（2026-09-22）：

- Recovery mappings：122。
- Evidence event contracts：112。
- Acceptance / Test contracts：271（其中 `F00-AC-008`已在 Working superseded，待 Formal Refresh deprecated）。
