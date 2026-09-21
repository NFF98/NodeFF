# Phase 1 Machine-readable Registries

此目錄是 Working 階段可由 CI / code generation / review 使用的 structured contract source。

- recovery-registry.json：stable source error → F12 recovery policy / message / actions。
- evidence-event-registry.json：stable event ID → F07 collection / property / retention metadata。

規則：

1. JSON registry不是第二份產品語意；source error/event meaning仍由Fxx + F12/F07擁有。
2. Registry負責把已批准語意變成machine-readable mapping。
3. 新增/變更stable ID時，Markdown owner與JSON registry必須同commit更新。
4. Spec promotion後，reviewed snapshot升到spec/shared對應registry。
