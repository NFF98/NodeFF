# NodeFF Architecture Evolution — Phase 4+

> Canonical Role：Phase 4+ architecture additions / activation only. Shared architecture invariants remain in `working/core/APP-ARCHITECTURE.md`.

## 6 個月後：Intent Commerce / Capability Network

逐步加入：

- external provider registry
- provider certification
- booking / payment / commerce
- metering
- transaction lifecycle
- settlement
- SLA / trust
- broader creator / provider ecosystem
- Heterogeneous Orchestration Plane
- async workflow state / retry / timeout / compensation
- evidence-based provider discovery / routing
- human approval step when required

長期新增的是「多 Capability 如何可靠完成一個 Outcome」，不是第二套 App Runtime。

~~~text
Intent
→ Resolved Intent
→ Capability Graph
→ Runtime local steps
→ External / Async steps when required
→ Retry / Compensation / Approval
→ Validated Outcome
~~~

Orchestration Engine 只負責執行已被 NFF Contract 描述的 workflow。
Temporal、n8n 或其他 workflow engine 都只能位於 Adapter 後方，不可把 vendor DSL 寫進 Blueprint 核心。

仍維持：

~~~text
Intent
→ Capability Selection
→ Blueprint
→ Runtime
→ External Gateway only when required
~~~

不能演變成所有 Interaction 都經過中央 Commerce Server。

---
