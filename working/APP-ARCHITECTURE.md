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


## 9. Detailed Application Design Inputs — Working

### 9.1 Product Runtime Identity
Current direction: NodeFF is not primarily an AI code generator. It is a **Dynamic UI Runtime Engine** and an **Intent-to-UI Protocol**. Natural language is compiled into declarative LegoSpec; the NodeFF runtime executes that controlled contract.

### 9.2 Dual Persistence Model
Separate two concepts:
- **Template / Blueprint:** reusable micro-app definition used by Community/Gallery and Fork & Remix; may contain prompt/template, LegoSpec, metadata, version and remix/source relationship. It must not inherit private instance data.
- **Instance Snapshot:** a specific execution state containing the current user-entered state plus the applicable LegoSpec/reference. Intended for exact sharing, resume and continuation. Candidate transport: URL hash, compressed payload, or short-link indirection when too large.

Reload/share should restore a valid instance without requiring LLM recompilation merely to recover state.

### 9.3 State Preservation Guardrail
Desired behavior is **state preservation without recompilation**. Normal interaction updates local state; reload/resume hydrates recoverable state; sharing reproduces the shared instance state when its payload is valid and complete.

Engineering correction: do not make “write to LocalStorage and URL Hash every millisecond” a hard requirement. Prefer debounced/batched persistence and canonical state serialization. Browser storage can be cleared or quota-limited, and URLs have practical size limits. The product goal is **deterministic state restoration**, not an absolute guarantee under every browser/storage failure. Sensitive data must not enter share URLs by default.

### 9.4 App-to-App Context / Prompt Piping
Support controlled composition between micro-apps:
- App A produces a standard **Universal Context Payload**.
- Candidate fields: `summary`, `rawText`, `structuredData`.
- User selects a suggested next action such as “轉化為下一個工具”.
- App B receives approved context as initial input/state.
- Transport may use URL payload, local session state or approved backend/share reference.
- Context transfer must be schema-controlled; arbitrary hidden data transfer is prohibited.

Working flow: **App A result → Context Payload → user-selected next capability → App B hydration → continue task**.

### 9.5 Experience Shell — Inspiration Capsule
Treat Inspiration Capsules as **creation scaffolds**, not static demos: editable example prompt, variable highlighting, Ghost Text and Progressive Refinement. Desired learning progression: **copy → modify → combine → create from scratch**. UX principle: **先完成，再學會；不是先學會，才能完成。** Prefer outcome-led presentation while keeping the prompt editable underneath.

### 9.6 Infrastructure-Aligned Application Flow
Assume edge-first + client-first execution: edge handles gate/normalization/cache/routing where appropriate; compiler performs semantic generation; verified LegoSpec returns to browser; normal interaction stays client-side without repeated LLM calls; realtime is invoked only for shared live state; persistent backend is introduced only for durable needs such as ownership, history, publishing, quota and commerce.

Latency guardrail: edge proximity can reduce network latency but cannot guarantee 3-second end-to-end generation. LLM inference, cold starts, provider latency and downstream services remain part of the total path. “3 seconds” is a product target/measurement, not an architectural guarantee.

### 9.7 Development Workflow — Working
Current workflow: **GitHub SSOT → Cursor executes → ChatGPT audits**. Cursor, GitHub, Supabase and managed edge/serverless hosting are candidate MVP tools/stack, not approved vendor decisions. Provider abstraction should preserve replaceability.

## 10. Architecture Suggestions / Questions to Resolve
1. Separate **Blueprint ID** from **Instance ID**.
2. Define canonical state serialization for resume/share/remix.
3. Define payload size thresholds: URL hash for small ephemeral state; short-link/backend indirection for large/stable state.
4. Define context permissions: which output fields may leave App A.
5. Treat edge as a deployment/execution strategy, not a promise that every operation runs at the nearest CDN node.
6. Keep hosting, database and LLM providers replaceable.
