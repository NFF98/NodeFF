# NodeFF Capability Roadmap — Phase 4+

> Shared capability contract：`../CAPABILITY-FABRIC.md`

# 14. 6 個月後：Capability Network + Orchestration

只有供需證據成立後才逐步加入：

- certified third-party providers
- provider registry
- booking / payment / commerce
- usage metering
- transaction lifecycle
- settlement
- provider SLA
- capability certification
- marketplace discovery
- creator / provider economics
- multi-capability workflow composition
- async step lifecycle
- retry / timeout / idempotency metadata
- compensation / rollback semantics
- human-in-the-loop step when required

長期 Fabric 不只描述「一個 Capability 能做什麼」，還要能描述「多個 Capability 如何可靠合作」。

~~~text
Resolved Intent
→ Capability Graph
→ Step A: Internal Capability
→ Step B: External Provider
→ Step C: Async Worker
→ Step D: Human / Approval if required
→ Validated Outcome
~~~

Orchestration metadata 必須仍然來自 Capability Contract；不能讓外部 workflow engine 自己發明 NFF semantics。

長期 Fabric：

~~~text
Internal Capability
        +
Creator Capability
        +
Paid Capability
        +
External Provider Capability
        ↓
Same Capability Contract
        ↓
Same Blueprint Model
        ↓
Same Runtime Boundary
        +
NFF Orchestration Contract
~~~

---
