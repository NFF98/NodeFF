# appf2 Business Plan

> 狀態：Working Strategy Baseline。本文定義 appf2 的產品商業邏輯、發展節奏與各階段驗證 Gate；不是會議記錄，也不把尚未驗證的市場假設寫成事實。

# 1. 商業核心

appf2 要改變的不是某一種 App，而是傳統軟體的入口方式。

~~~text
Old
Idea / Need
→ Search App
→ Install
→ Learn
→ Configure
→ Use

appf2
Intent
→ App
→ Use
→ Share
→ Remix
~~~

核心宣言：

> **意圖就是 App。**

appf2 的產品是：

> **把當下 Intent 直接轉成可互動、可分享、可 Remix 的 Micro-App。**

appf2 不是 Decision App、AI Code Generator、Form Builder，也不是所有 Native App 的替代品。

Phase 1 的 Decision / Utility / Party / Social use cases 都只是 Wedge，不是產品邊界。

---

# 2. 五個不可犧牲的產品原則

所有 roadmap 與商業化都必須同時守住：

1. **No install setup**
2. **Everyone is the creator**
3. **Sharable, linkable**
4. **Intent Commerce**
5. **Fun and socialable**

其中 Intent Commerce 是長期方向，不代表 Phase 1 要先做 Marketplace。

---

# 3. 發展時間軸

appf2 採四段節奏，而不是把未來能力全部塞進 Phase 1。

| 時間 | 階段 | 核心任務 | 主要判斷 |
|---|---|---|---|
| **0–1 個月** | Core Proof | 證明 Intent → App → Use → Share → Remix | 產品核心循環是否成立 |
| **第 2–3 個月** | PMF Deepening | Reuse、Identity、Creator Value | 是否開始形成重複使用與資產價值 |
| **第 4–6 個月** | Scale Readiness | 強化 Reliability、Cost、External Capability Pilot | 是否值得進入平台化 |
| **6 個月後** | Continuous Platform Expansion | Intent Commerce / Capability Network | 供需是否足以形成 Network |

原則：

> **每一階段都由前一階段的 Evidence 解鎖，不以日期自動解鎖。**

時間是規劃上限，不是「到了日期就一定要做」。

---

# 4. Phase Roadmap Index

Phase roadmap 不再拆成平行檔案；本檔後段以單一 canonical owner 保留 Phase sections：

- `appf2 Product Roadmap — Phase 1`：0–1 個月 Core Proof。
- `appf2 Product Roadmap — Phase 2`：Reuse / Identity / Creator Value。
- `appf2 Product Roadmap — Phase 3`：Scale Readiness。
- `appf2 Product Roadmap — Phase 4+`：Intent Commerce / Capability Network。

前段只擁有跨 Phase 商業核心、產品原則、KPI 與 Strategic Guardrails；後段只擁有 phase-specific goal / gate / hypothesis，避免 duplicate truth。

> Roadmap 日期是 planning horizon，不是 implementation unlock。Phase activation 仍需 Evidence + Human approval。

# 5. 商業 Flywheel

第一個 Flywheel：

~~~text
More Intent
→ More Correct Blueprints
→ More Trusted Reuse
→ Faster / Cheaper
→ More Share
→ More Remix
→ More Intent
~~~

第二個 Flywheel：

~~~text
More Usage
→ More Failure / Correction Evidence
→ Better Semantic Reliability
→ More Trust
→ More Usage
~~~

第三個長期 Flywheel：

~~~text
More Intent Demand
→ More Valuable Capabilities
→ Better Outcome Coverage
→ More Transactions
→ More Providers / Creators
→ More Intent Demand
~~~

第三個 Flywheel 只在前兩個已成立後才有意義。

---

# 6. KPI Tree

appf2 不以 Vanity Metrics 管理。

## Core Value
- Successful Intent
- Time to First Useful App
- Semantic Mismatch
- Recovery Success

## Distribution
- Share Rate
- Share → Open
- Open → Use
- Use → Remix / Create

## Retention
- anonymous repeat use
- creator repeat creation
- reusable Blueprint use

## Economics
- cost per successful intent
- fresh compile vs reuse ratio
- paid capability gross margin

## Platform，6 個月後才重要
- external capability usage
- provider reliability
- transaction completion
- creator / provider earnings
- supply-demand coverage
- multi-capability workflow completion rate
- orchestration recovery / compensation success
- active certified providers / creator capabilities

---

# 7. Strategic Guardrails

1. Product Vision 永遠是 Intent → App，不被單一 Wedge 綁死。
2. Phase 1 優先 Semantic Correctness，不追求 Capability 數量。
3. First Value 前不強制 Registration。
4. Share 是 Distribution，Remix 是 Creation。
5. Paid Value 必須對應 Durable Value 或 Real Marginal Cost。
6. 不能做的 Intent 必須誠實回覆，不生成假成功。
7. Existing Blueprint 不重複消耗 LLM。
8. Fun / Social 必須持續存在，避免退化成 Generic Tool Builder。
9. 3 個月前不建 Marketplace。
10. 6 個月前只做 Commerce Pilot，不把 Capability Network 當既定事實。
11. Orchestration Engine 是長期 execution plane；Phase 1 不引入 Temporal / n8n 類依賴。
12. 雙邊市場必須由真實 demand + supply density 解鎖，不能先造 Marketplace。
13. 第三方 Provider 必須經 Capability Contract / Certification / Evidence，不以「有 API」等同「可用」。
14. 所有 Revenue / Growth / Cache / Latency 數字在實測前都是 Hypothesis。
12. Roadmap 由 Evidence Gate 推進，不由日期推進。

# 結論

appf2 的發展順序不是：

~~~text
先做大平台
→ 再找需求
~~~

而是：

~~~text
1 個月
證明 Intent → App → Share → Remix

3 個月
把成功 App 變成 Reuse / Identity / Creator Value

6 個月
證明 Reliability / Cost / Paid Capability 可以擴張

6 個月後
才持續建立 Intent Commerce / Capability Network
~~~

> **先證明核心循環，再累積資產，再建立交易網路。**


---

# Product Roadmap Sections

> Consolidated canonical roadmap。Phase labels describe planning / evidence gates；日期本身不 unlock implementation.

# appf2 Product Roadmap — Phase 1

> Shared business truth：`working/common-core/BUSINESS-PLAN.md`

# 4. 0–1 個月：證明核心循環

唯一優先問題：

> **使用者能不能很快把 Intent 變成正確、有用的 App，而且願意使用、分享、再 Remix？**

核心循環：

~~~text
Intent
→ Correct App
→ Immediate Use
→ Share
→ Recipient Use
→ Remix / Create
~~~

## 必須交付的產品能力

- Experience Shell / 靈感精靈
- Inspiration Capsules / Ghost Text
- Progressive Refinement
- Semantic Compiler
- Capability Resolution
- Trusted Blueprint
- Browser Runtime
- Share / Restore
- Remix
- Anonymous Identity
- Humanized Recovery
- 最小必要 Evidence

## Phase 1 UX 原則

使用者不應被迫先學 Prompt。

~~~text
Copy
→ Modify
→ Generate
→ Use
→ Remix
→ Create
~~~

模糊需求應轉成「可見、可修改的 assumptions」，而不是偷偷替使用者做決定。

## Phase 1 Growth

Growth unit 是 **可分享的 App Artifact**，不是 Account。

~~~text
Create
→ Share
→ Open
→ Use
→ Remix
→ New Create
~~~

First Value 前原則上不要求註冊。

## Phase 1 Business Model

收入不是主要 KPI。

免費核心應優先支援低邊際成本能力：

- browser execution
- deterministic rules
- approved capabilities
- shareable Blueprint
- bounded compilation

只有產生真實邊際成本或 Durable Value 才適合成為付費候選：

- runtime AI
- heavy API
- media generation
- durable storage
- larger realtime
- premium capability

## 1 個月 Gate

進入下一階段前，至少要有證據回答：

1. Intent 是否真的比 chat answer 更適合被做成 App？
2. Semantic correctness 是否足以讓人信任？
3. 使用者是否真的會 Share？
4. Recipient 是否真的會 Use？
5. Remix 是否會自然發生？
6. Anonymous-first 是否降低摩擦？
7. 每個 Successful Intent 的成本是否可持續？

沒有這些 Evidence，不進 Creator Economy 或 Marketplace。

---


---

# appf2 Product Roadmap — Phase 2

> Shared business truth：`working/common-core/BUSINESS-PLAN.md`

# 5. 第 2–3 個月：Reuse、Identity、Creator Value

這一階段的目的不是增加功能數量，而是讓「一次性的好 App」開始變成可累積資產。

## 5.1 Trusted Reuse

從：

~~~text
Intent
→ Fresh Compile
~~~

逐步變成：

~~~text
Intent
→ Retrieve Trusted Blueprint Family
→ Minimal Semantic Delta
→ Validate
→ Execute
~~~

價值：

- 更快
- 更便宜
- 更穩定
- 更少 semantic failure
- 更容易 Remix

## 5.2 Progressive Identity

Authentication 只在 Durable Value 出現時要求。

~~~text
anonymous_id
→ value requested
→ authenticate
→ ownership claim
→ user_id
~~~

可解鎖：

- Save
- History
- Ownership
- Publishing
- Cross-device
- Private artifact
- account-gated durable value

## 5.3 Creator Value

只有 Reuse / Remix 行為存在後，才建立：

- creator attribution
- publishing
- reusable Blueprint family
- creator profile
- creator artifact / reusable family value signals
- creator analytics

不先假設 Creator Economy 一定成立；paid entitlement / monetization enforcement屬 Phase 3+，不得由 Phase 2 creator work偷偷啟用 F13。

## 3 個月 Gate

進入 Scale Readiness 前，至少要看到：

- repeat creation
- repeat use
- Blueprint reuse
- anonymous → account conversion
- save / publish behavior
- creator retention
- cost per successful intent 持續下降
- semantic mismatch 持續下降

---


---

# appf2 Product Roadmap — Phase 3

> Shared business truth：`working/common-core/BUSINESS-PLAN.md`

# 6. 第 4–6 個月：Scale Readiness

這不是全面平台化，而是確認 appf2 是否值得開始承接更高成本、更高價值的需求。

主要工作：

## Reliability

- Trusted Blueprint Families
- Compatibility / versioning
- Capability maturity governance
- failure quarantine
- recovery quality
- observability

## Cost

- reuse before compile
- CDN / cache optimization
- model routing by cost / capability
- batch telemetry
- only proven heavy work goes server-side

## Product Expansion

只針對真實 usage 證明需要的能力增加：

- Realtime
- Object / media storage
- runtime AI
- heavy external API
- semantic retrieval
- premium capability

## Commerce Pilot

可以開始驗證：

~~~text
Intent
→ Paid / External Capability
→ Price / Permission
→ Explicit User Choice
→ Execute
→ Meter
→ Result
~~~

這仍是 Pilot，不是 Marketplace。

## 6 個月 Gate

只有以下證據成立，才值得把 Intent Commerce / Capability Network 提升為主要平台方向：

- 明確 recurring demand
- 可識別的外部 capability supply
- 使用者願意為 outcome / durable value 付費
- provider execution 可被可靠控制
- 跨 Provider workflow 的 retry / timeout / compensation 可治理
- metering / entitlement 可被正確管理
- 供需雙方有足夠密度，不是只有單邊 catalog
- appf2 在交易鏈中提供不可取代的 orchestration value

---


---

# appf2 Product Roadmap — Phase 4+

> Shared business truth：`working/common-core/BUSINESS-PLAN.md`

# 7. 6 個月後：Intent Commerce / Capability Network

長期 appf2 的角色可能演進為：

> **Intent → Capability → Interaction → Transaction 的 Control Plane。**

~~~text
User Intent
→ Capability Selection
→ Dynamic App
→ Internal / External Capability
→ Outcome / Transaction
~~~

可能的 Provider：

- AI
- Data
- Search
- Booking
- Payment
- Commerce
- Media
- Specialized Compute
- External Workflow

長期商業模式候選：

- Capability transaction fee
- API margin
- premium capability
- creator revenue share
- provider / marketplace commission
- orchestration / workflow execution fee
- enterprise capability access / governance
- durable workspace / team value

但 Network 只有在真實供需密度成立後才有價值。

---
