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

## 11. App Instance — Detailed Working Design Inputs

### 11.1 Instance Cost Model
Working hypothesis: most Micro-App instances should be **client-executed**, so ongoing interaction/rendering should have near-zero incremental platform compute cost. Platform cost is expected to concentrate on initial compilation and exceptional capabilities such as realtime, persistent storage or external APIs.

Candidate operating split:
- **Lightweight instance:** state/spec transported through compressed URL Hash plus local browser recovery; no persistent DB required.
- **Large/stable instance:** use short-link/backend or KV indirection when URL payload size, stable identity or durable reference requires it.
- **Realtime instance:** store/share a room base spec once, then synchronize small state deltas through a realtime channel.

The previously discussed “90% / 10%” distribution is a planning hypothesis, not a measured production ratio.

### 11.2 Snapshot Share Mechanics
Candidate flow:

```
Current App Instance
  ↓
Canonicalize Logic + UI Spec + State
  ↓
Compress
  ├─ small → URL Hash
  └─ large/stable → Short Link / Backend Reference
  ↓
Receiver opens link
  ↓
Hydrate + Validate
  ↓
Render same valid Instance state
  ↓
Optional Fork / Remix
```

The share payload conceptually contains the information required to restore the instance, but implementation should distinguish:
- reusable **Blueprint**;
- concrete **Instance State**;
- schema/version metadata required for compatible hydration.

“Exact restoration” is the target for a valid, complete payload. It is not a promise that every browser/storage failure is recoverable.

### 11.3 Instance vs Blueprint Publishing
- Instance may contain personal/user-entered state.
- Publishing a reusable Blueprint should not silently publish private instance data.
- Publishing should explicitly derive a clean template/blueprint representation from the current instance.
- Blueprint and Instance should have separate identities and lifecycle/version semantics.

### 11.4 Realtime Collaboration
For multiplayer/shared editing:
- A room may use a base Blueprint/LegoSpec plus an initial instance state.
- Subsequent user interactions should preferably transmit **validated Delta State** rather than repeatedly transmit the full spec.
- Each client keeps the executable contract locally and applies incoming deltas to local state.
- Recalculation remains local when the required formulas/logic are deterministic and available client-side.
- Room/session state remains ephemeral unless the product explicitly promotes it to persistent history.

### 11.5 Dynamic Variations Without Fixed App Templates
NFF should not be designed as a hard-coded set of ten fixed cards. The working architecture is:
**Primitive UI Components + Declarative Logic + Reactive State + Generic Fallback**.

Candidate primitives include:
- Numeric input / slider
- Toggle / selection group
- Dynamic item list
- Countdown / progress visualization
- Result / summary display

The exact primitive registry is still open.

A new variation should normally be represented by a different composition/configuration of approved primitives and declarative rules, rather than requiring a new bespoke React component for each user request.

### 11.6 Spec Diff / Remix
For a refinement such as “加 5% 服務費”:
1. Current validated Spec + user refinement intent is sent to the compiler.
2. Compiler returns a validated revised Spec or explicit Delta Patch.
3. Existing compatible instance state is mapped/preserved where possible.
4. Player hydrates the revised contract without unnecessarily discarding user-entered state.

The exact patch format (e.g. RFC 6902) remains a design choice; the important contract is **minimal semantic change + state preservation**.

### 11.7 Declarative Logic / Formula Engine
Working concept: **Logic as Data**.

A WidgetSpec may express formulas/rules declaratively rather than embedding arbitrary JavaScript. Candidate logic categories:
- arithmetic/formula rules;
- conditional rules;
- state-derived calculations;
- bounded transformations;
- approved deterministic algorithms such as settlement/minimization.

Example concept:

```json
{
  "logic": {
    "currencyRate": 0.21,
    "hasTax": true,
    "taxRate": 0.10,
    "formulas": {
      "itemShare": "price * (personWeight / totalWeight)",
      "grandTotal": "hasTax ? rawTotal * (1 + taxRate) : rawTotal"
    },
    "settlementAlgorithm": "minimize_transfers"
  }
}
```

The expression evaluator must remain sandboxed and allowlisted. No `eval` or arbitrary dynamic JavaScript. Complex business-specific algorithms should be represented as approved capabilities/operations rather than silently added to the universal player.

### 11.8 Generic Dynamic Form Fallback
When a request cannot map cleanly to a specialized primitive composition, the system should prefer a transparent generic form representation when safe and meaningful:

**Inputs → Logic → Outputs**

This is a graceful-degradation path, not a guarantee that every natural-language request can always be fulfilled. Unsupported, unsafe, or semantically ambiguous requests may still require notice, refinement or rejection according to the Contract/Tier rules.

### 11.9 Performance / Cost Claims — Validation Status
User-provided candidate figures such as 300ms compiler generation, 30ms hydration, 16ms local recalculation, 50KB gzip runtime, 15–35MB memory, 0.0003–0.0005 USD per generation, 500-character URL threshold and 1KB average snapshot are **targets/estimates to benchmark**, not current architecture guarantees.

Likewise, “1M interactions ≈ $0 platform compute” is a business hypothesis that depends on CDN, bandwidth, observability, realtime, storage and other provider pricing.

## 12. Architecture Questions Added From This Discussion
1. What is the canonical `WidgetSpec` schema for UI + logic + state references?
2. Which data is safe to embed in URL Hash, and what must use short-link/backend storage?
3. What exact threshold triggers URL Hash → short-link?
4. Is realtime state based on Supabase Realtime, PartyKit, or an adapter interface?
5. How are concurrent deltas ordered, deduplicated and conflict-resolved?
6. Which declarative formulas/algorithms are built into Layer 4 versus exposed as approved capabilities?
7. How does Spec Diff preserve/migrate state when fields are renamed, removed or structurally changed?
8. What is the version compatibility policy for old shared Instances?
