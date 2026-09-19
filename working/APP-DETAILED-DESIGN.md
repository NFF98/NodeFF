# NodeFF App Detailed Design Index

> 狀態：Working。本文是功能詳細設計的總表與共同格式；真正的實作細節放在 `working/functions/`。

# 1. 設計方式

NodeFF 的詳細設計採 **Function-Oriented**，不是單純拆成 Frontend Design / Backend Design。

每個 Function 在同一份設計內描述：

- Product Behavior
- User Flow
- Frontend
- Backend
- API / Contract
- Data / State
- Capability Dependencies
- Error / Recovery
- Security / Permission
- Telemetry
- Acceptance Criteria
- Release Dependency

這確保一個功能從 UX 到 Runtime / Backend 都能完整追蹤。

---

# 2. Function Design Lifecycle

~~~text
Idea / Requirement
 → Architecture Fit
 → Function Design
 → Acceptance Criteria
 → Backlog / Sprint
 → Implementation
 → Test
 → Release
~~~

沒有完成必要 Design / Acceptance 的 Function，不應直接交給 Cursor 自行決定架構。

---

# 3. Function 總表

| ID | Function | 主要目的 | 主要層 | 狀態 |
|---|---|---|---|---|
| F01 | Intent Compilation | Intent → Blueprint | L1-L3 | 待詳細設計 |
| F02 | Blueprint Validation | Blueprint trust admission | L3 | 待詳細設計 |
| F03 | Runtime Execution | 執行 Blueprint / Instance | L4 | 待詳細設計 |
| F04 | Capability Registry | 管理可執行 Capability | L2-L4 | 待詳細設計 |
| F05 | Share / Restore | 分享與開啟 Micro-App | L1/L4 | 待詳細設計 |
| F06 | Remix / Refine | Blueprint semantic revision | L2-L4 | 待詳細設計 |
| F07 | Anonymous Identity & Evidence | No-login continuity + telemetry | Cross-cutting | 待詳細設計 |
| F08 | Durable Identity / Ownership | Account / Save / Claim | Cross-cutting | 中期 |
| F09 | Realtime Room | 多人 Instance state | L4/Infra | 依 Use Case |
| F10 | Blueprint Reuse / Retrieval | Trusted reuse | L1-L3 | 中期 |
| F11 | External Capability Execution | AI / API / heavy job | Cross-cutting | 依 Capability |

此表是規劃入口，不代表已核准 Release Scope。

---

# 4. Function Design 文件格式

每個 Function 使用以下結構：

~~~text
# Fxx — Function Name

1. Purpose / Scope
2. User Behavior
3. Preconditions
4. Main Flow
5. Frontend Design
6. Backend Design
7. API / Contract
8. State / Data
9. Capability Dependencies
10. Error / Recovery
11. Security / Permission
12. Telemetry
13. Acceptance Criteria
14. Dependencies
15. Release / Migration Notes
16. Open Decisions
~~~

---

# 5. Release 管理方式

Function Design 是 Architecture 與 Execution 之間的橋樑。

~~~text
Function Design
 → execution/BACKLOG.md
 → execution/SPRINT.md
 → Code / Tests
 → execution/CHANGELOG.md
~~~

Release 不應直接以「做前端」、「做後端」作為唯一單位，而應以可驗收的 Function / User Outcome 為主。

---

# 6. 文件責任

- `APP-ARCHITECTURE.md`：整體架構。
- `CAPABILITY-FABRIC.md`：底座能力。
- `APP-DETAILED-DESIGN.md`：Function 索引、格式、依賴與 Release 對應。
- `working/functions/Fxx-*.md`：單一 Function 的詳細設計。
- `INFRA-ARCHITECTURE.md`：基礎設施與部署設計。
