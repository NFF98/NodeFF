# NodeFF Infrastructure — Phase 2

> Shared infrastructure truth：`../INFRA-ARCHITECTURE.md`

# 13. 中期：Reuse / Identity / Creator Value

中期不是換架構，而是啟用 Phase 1 預留的能力。

## Identity

啟用 Supabase Auth 或同等 Adapter：

~~~text
anonymous_id
 → authenticate
 → ownership claim
 → user_id
~~~

保留原本：
- Blueprint lineage；
- share history；
- creator artifacts；
- eligible anonymous evidence。

## Reuse

先使用 PostgreSQL 做：
- exact / structured retrieval；
- Blueprint family metadata。

有足夠 Evidence 後，再在相同 Postgres 啟用 pgvector：

~~~text
Intent Embedding
 → Candidate Blueprint Families
 → Compatibility / Trust Check
 → Adapt / Validate
~~~

因此中期不需要立刻購買獨立 Vector DB。

## Creator Value

增加：
- ownership；
- attribution；
- publishing；
- save / history；
- premium entitlement。

這些是 metadata / identity layer，不修改 immutable Blueprint core。

## Realtime

若 Social / Multiplayer POC 證明必要：

第一選擇先使用已整合的 Supabase Realtime 或同等 Adapter。

只有當：
- concurrency；
- room model；
- latency；
- cost

證明不適合，才切換 specialized realtime provider。

## Storage

有 image / audio / video / 3D asset 後才啟用 Object Storage。

第一階段可沿用 Supabase Storage；media egress 成為主要成本後，再評估 R2 / S3 類型 provider。

---
