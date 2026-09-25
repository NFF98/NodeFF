# NodeFF Data Model — Phase 2 Extensions

> Shared invariants：`../DATA-MODEL.md`
>
> 本檔只定義 Phase 2 相對於 Phase 1 的新增／migration hooks；不得複製 Phase 1 tables。

# 1. F08 Identity / Ownership

未來新增：

~~~text
user_identity
identity_claim
artifact_ownership
creator_attribution
~~~

透過 mapping 連接 anonymous identity / Blueprint，不修改 Blueprint body。

# 2. F10 Trusted Reuse / Vector

Evidence Gate 通過後，優先沿用 PostgreSQL + pgvector。

未來 logical extension：

~~~text
blueprint_embedding
- blueprint_hash
- embedding_model
- embedding_version
- embedding_vector
- source_semantic_version
- created_at
~~~

啟用前必須由 F10 定義：

- embedding source；
- privacy boundary；
- invalidation / version policy；
- retrieval quality Acceptance；
- exact / structured reuse precedence；
- compatibility / trust re-check。

> Vector 是 retrieval index，不是 source of truth。Blueprint / lineage 仍以 PostgreSQL canonical records 為 truth。

Dedicated Vector DB 只有 pgvector 的 scale / latency / cost evidence 不足時才考慮。

# 3. F09 Realtime

Room State：

~~~text
Immutable Blueprint
+ room metadata
+ mutable Instance State
~~~

不得修改 `blueprint_content`。
