# 06 — System

> Status：LEGACY INDEX — NON-CANONICAL
>
> 此檔案是早期橫向 Spec 模板，已不再作 implementation truth。

NodeFF 正式 Spec 結構：

~~~text
spec/functions/Fxx-*.md
→ Function end-to-end canonical Spec

spec/shared/*.md
→ Cross-Function shared canonical Spec
~~~

System/runtime細節由 Function Spec + approved shared runtime/architecture contracts承接。

規則：

- 不在此檔新增 Function-level API / UI / Data / Error / Acceptance 詳細內容。
- 若需要查目前 Working Current Truth，使用 working/functions/Fxx-*.md 與對應 shared Working文件。
- 若需要正式實作 Contract，使用已批准的 spec/functions 或 spec/shared。