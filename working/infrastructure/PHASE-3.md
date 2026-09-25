# NodeFF Infrastructure — Phase 3

> Shared infrastructure truth：`../INFRA-ARCHITECTURE.md`

# 14. 中期 Heavy Capability

只有 Runtime 無法有效完成時加入：

~~~text
Capability Action
 → Edge Gateway
 → Job / External API
 → job_id
 → status
 → result
 → validated update
~~~

需要以下 workload 才建立 Queue / Background Worker：
- media generation；
- heavy AI；
- batch processing；
- long-running external workflow。

不要因為「未來可能需要」就讓 Phase 1 所有 request 都進 Queue。

---
