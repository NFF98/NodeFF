# Shared Specs

> Canonical home for approved cross-Function contracts。

適合放這裡：

~~~text
DATA-MODEL.md
API-CONVENTIONS.md
EXECUTION-ADMISSION.md
CAPABILITY-CONTRACT.md
EVIDENCE-REGISTRY.md
RECOVERY-REGISTRY.md
ACCEPTANCE-CONVENTIONS.md
~~~

只有真正跨 Function、且由多個 Fxx共同引用的 contract才放 shared。

規則：

1. Shared Spec不得複製 Function-specific細節。
2. Function Spec引用 Shared Spec，不重寫第二份。
3. Shared Spec若改變 public/data/runtime/security contract，所有受影響 Fxx需重新 Review。