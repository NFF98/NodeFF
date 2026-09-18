# NodeFF App Architecture（Working）

> 本文件為系統規格討論前的工作版，不是官方 SSOT。

## 1. 目的
定義 NodeFF 從「自然語言 Intent」到「可執行、可分享、可消失 Micro-App」的產品/應用程式架構，以及各模組責任邊界。

## 2. 核心產品循環
**Intent → Compile → Validate → Render → Interact → Share/Remix → Refine → Dispose**

核心原則：
- 使用者不需要安裝 App。
- LLM 是一次性 Semantic Compiler，不是每次互動的 runtime。
- LegoSpec 是核心 Contract。
- Browser Universal Lego Player 是主要執行環境。
- 多人即時 session 可透過 ephemeral room。
- 生成結果本質上是可分享、可 remix 的 Micro-App。
- Runtime 不執行任意 JavaScript。

## 3. Logical Architecture

```
User
 ↓
Experience / Prompt UI
 ↓
Layer 1 — Ingestion & Routing
 ├─ Safety / Tier Gate
 ├─ Normalize
 ├─ Cache
 └─ Dispatch
 ↓
Layer 2 — Semantic Compiler
 ├─ Context Injector
 ├─ LLM
 ├─ Intent / Archetype
 └─ Retry
 ↓
Layer 3 — Contract
 ├─ LegoSpec Schema
 ├─ Component Allowlist
 ├─ State Binding Validation
 └─ Notice / Fallback Validation
 ↓
Layer 4 — Universal Lego Player
 ├─ Registry / Factory
 ├─ Reactive State
 ├─ Expression Sandbox
 ├─ Error Boundary
 └─ Share Hydration
 ↓
Browser Micro-App
 ├─ Local interaction
 ├─ Optional PartyKit session
 └─ Optional approved external capabilities
```

## 4. Application Domains

### A. Experience Shell
負責 Prompt、靈感膠囊、Fork & Remix、生成狀態、結果卡與 Progressive Refinement。

### B. Compiler
負責把 Intent 轉成 declarative LegoSpec，不直接產生可執行任意 code。

### C. Contract
負責 Schema、version、validation、capability allowlist 與 fallback contract。

### D. Player Runtime
負責 component render、state、expression、interaction、error isolation。

### E. Session
負責多人 ephemeral state / room synchronization；不承擔自然語言理解。

### F. Share / Remix
負責可分享 URL、Blueprint identity、版本/來源與 remix 關係。

### G. Capability / Commerce
負責未來 C2C capability/API、計費、usage metering 與交易；與核心 renderer 解耦。

## 5. State Ownership
- UI transient state → Browser memory。
- Shareable public state → URL/hash 或 approved share payload。
- Ephemeral multiplayer state → Session layer。
- Persistent creator/history/commerce data → Backend DB。
- Secrets / credentials → 永不進入 client LegoSpec 或 URL。

## 6. Boundary Rules
- Layer 1 不做 semantic generation。
- Layer 2 不直接執行 code。
- Layer 3 不負責 UI runtime。
- Layer 4 不理解 intent、不決定 business fallback。
- Session 不成為永久資料庫。
- Business rules 不應硬編入 Universal Player。
- Capability providers 透過受控 contract 接入。

## 7. Major Data Flows

### New Intent
Prompt → Normalize → Cache → Compiler → Schema Validation → Verified LegoSpec → Player。

### Remix
Shared Blueprint → Hydrate → User edits → Delta Patch / Recompile → New Blueprint version。

### Multiplayer
Player → Room Join → Ephemeral Session State → Sync → Leave / TTL Destroy。

### Runtime Failure
Primitive error → Local Error Boundary → Component fallback → Telemetry → Blueprint health evaluation。

## 8. Open Design Items
- LegoSpec versioning / backward compatibility
- Action/state-machine contract
- Session synchronization contract
- capability API contract
- authentication boundary
- blueprint identity / publishing model
- telemetry schema
- commerce transaction boundary

**Status：Working。**
