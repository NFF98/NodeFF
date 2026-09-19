# NodeFF App Architecture

> 狀態：Working。這份文件只回答三件事：**NFF 有什麼、各自負責什麼結果、短／中／長期怎麼長。**
> Function 細節之後由 APP-DETAILED-DESIGN.md 與 working/functions/ 承接。

# 1. 一張圖看懂 NodeFF App

NodeFF 是 **Intent-to-App Runtime Platform**。

> **意圖就是 App。**

使用者不用先找 App、安裝 App、學 App；只要說出需求，NodeFF 把它變成可互動、可分享、可 Remix 的 Micro-App。

~~~mermaid
flowchart LR
    U[User]

    subgraph SHELL["① Experience Shell<br/>靈感精靈"]
        I[Inspiration / Ghost Text]
        R[Refine / Remix]
        E[Humanized Recovery]
    end

    subgraph ENGINE["② Intent-to-App Engine"]
        L1[Route]
        L2[Semantic Compiler]
        L3[Validate Contract]
        L4[Universal Runtime]
    end

    F["③ Capability Fabric<br/>NFF 真正會做什麼"]
    M["④ Model Gateway<br/>可切換 LLM"]
    D["⑤ State / Identity / Evidence"]
    APP["Interactive Micro-App"]

    U --> SHELL
    SHELL --> L1 --> L2 --> L3 --> L4 --> APP
    L2 <--> M
    L2 <--> F
    L3 <--> F
    L4 <--> F

    APP --> D
    SHELL --> D
    D -. improve .-> L2
    D -. capability gaps .-> F
~~~

NodeFF 不為每個 App 生成一套新程式碼。

它真正部署的是：

~~~text
Experience Shell
+ Semantic Compiler
+ Trusted LegoSpec
+ Universal Runtime
+ Capability Fabric
~~~

然後用不同 Blueprint 組出不同 App。

---

# 2. NFF 有哪些東西？各自負責什麼結果？

| 系統 | 說人話 | 最終要負責的結果 |
|---|---|---|
| **Experience Shell / 靈感精靈** | 幫使用者開始、修改、理解失敗 | 使用者不用學 Prompt，也知道下一步怎麼做 |
| **Layer 1 — Routing** | 接住需求、先做安全與路由 | 合法需求進正確流程，錯誤不直接丟工程碼 |
| **Layer 2 — Semantic Compiler** | 真正理解「你想做什麼」 | 把 Intent 變成正確 Capability 組合與 Blueprint |
| **Model Gateway** | 管理不同 LLM | 可以依成本、速度、能力切換模型，不綁死 Vendor |
| **Capability Fabric** | NFF 的 Lego 能力庫 | 決定 NFF 真正能做什麼、不能做什麼 |
| **Layer 3 — LegoSpec / Validation** | App 的可信任藍圖規格 | 不合法、不安全、不相容的 Blueprint 不能進 Runtime |
| **Layer 4 — Universal Runtime** | 把 Blueprint 真正跑起來 | 快速、本地、安全互動；一般操作不用再叫 LLM |
| **State / Identity / Evidence** | 記住 App、使用與改善證據 | 支援 Share、Remix、Reuse、Identity 與未來 Creator Value |
| **Recovery System** | 系統出錯時接住使用者 | 不 White Screen、不只顯示 404；保留資料並給下一步 |

## 2.1 Experience Shell / 靈感精靈

它不是另一個 AI Engine，而是 NodeFF 的「創作入口 + Recovery UI」。

包含：

~~~text
Inspiration Capsules
+ Ghost Text
+ Fork & Remix
+ Progressive Refinement
+ Humanized Recovery
~~~

核心學習循環：

~~~text
Copy
 → Modify
 → Generate
 → Use
 → Remix
 → Create
~~~

原則：

> **先完成，再學會；不是先學會，才能完成。**

---

## 2.2 Intent-to-App Engine：四層

~~~mermaid
flowchart LR
    A["Layer 1<br/>接住需求"] -->
    B["Layer 2<br/>理解需求"] -->
    C["Layer 3<br/>確認安全可執行"] -->
    D["Layer 4<br/>把 App 跑起來"]
~~~

### Layer 1 — Ingestion & Routing

負責：

~~~text
Intent
→ Safety / Policy / Quota
→ Reuse Lookup
→ Route
~~~

結果：

> **把請求送到正確地方，並保存原始 Intent / Recovery Context。**

它不負責猜業務語意。

### Layer 2 — Semantic Compiler

這是 NFF 的「語意大腦」。

負責：

~~~text
Understand Intent
→ Check Capability Coverage
→ Select Capabilities
→ Compose State / Rule / Action / Event
→ Produce Blueprint Candidate
~~~

結果：

> **正確的 Blueprint，不是 JavaScript。**

### Layer 3 — LegoSpec Contract + Validation

這是 Compiler 與 Runtime 的「信任門」。

檢查：

- Schema；
- Capability 是否存在；
- State / Binding / Rule 是否合法；
- Permission / Resource；
- Version / Compatibility；
- Degradation 是否誠實；
- Security boundary。

結果：

> **只有可信任 Blueprint 才能進 Runtime。**

### Layer 4 — Universal Runtime

負責：

~~~text
Hydrate
→ State
→ Action
→ Rule / Capability
→ View
→ Effect
~~~

結果：

> **Micro-App 在 Browser 裡快速、安全地跑。**

一般 Button、Dice、Wheel、Timer、Calculation、Animation 等互動：

> **預設 0 LLM call。**

Runtime 不猜 Intent、不選模型、不發明 Capability、不執行任意 generated code。

---

## 2.3 Capability Fabric：NFF 真正「會什麼」

Capability Fabric 不是第五層。

它橫跨 Layer 2、3、4：

~~~mermaid
flowchart TB
    F["Capability Fabric"]

    F --> C["Layer 2<br/>知道何時該用"]
    F --> V["Layer 3<br/>知道是否能合法組合"]
    F --> R["Layer 4<br/>真正執行"]
~~~

同一份 Capability Source 應產生：

~~~text
Compiler Metadata
+ Validation Contract
+ Runtime Registration
+ Compatibility Metadata
~~~

避免 Compiler、Validator、Runtime 各自維護一套能力表。

詳細 Card Contract 與 Maturity：

- working/ProjectManagement/CAPABILITY-FABRIC.md

### 如果 User 要的東西 NFF 不會怎麼辦？

每個 Intent 必須得到四種明確結果之一：

~~~text
FULLY_SUPPORTED
PARTIALLY_SUPPORTED
EXTERNAL_OR_HEAVY_REQUIRED
UNSUPPORTED
~~~

~~~mermaid
flowchart TD
    I[User Intent] --> C{Capability Coverage}

    C -->|Full| A[直接生成 App]
    C -->|Partial| B["保留核心語意<br/>明確告知降級"]
    C -->|External / Heavy| X["說明時間 / 權限 / 費用<br/>讓 User 選"]
    C -->|Unsupported| U["不亂做<br/>說明缺口 + Alternative / Refine"]

    U --> G[Capability Gap Evidence]
    G --> P[Future Capability POC]
~~~

核心規則：

> **做不到可以承認；不能做錯還假裝成功。**

---

## 2.4 Model Gateway：LLM 可以自由切換

LLM 切換屬於 **Layer 2 Semantic Compiler**。

~~~mermaid
flowchart LR
    SC[Semantic Compiler] --> MR[Model Router]
    MR --> NI[NFF Model Interface]
    NI --> A[Provider A]
    NI --> B[Provider B]
    NI --> C[Provider C]
~~~

Router 可依：

- model capability；
- structured output；
- latency；
- cost；
- quota；
- availability；
- fallback policy；

選模型。

因此：

> **換 LLM 不應影響 LegoSpec、Capability Fabric、Runtime。**

Provider SDK 不能進入核心 Contract。

---

## 2.5 State / Identity / Evidence

NFF 需要分清：

~~~text
Blueprint
= App 的不可變定義

Instance
= 這次執行中的狀態

Context
= App 與 App 之間允許傳遞的資料

Delta
= 受控修改

Recovery Context
= 出錯時保留的 Intent / Input / Progress
~~~

Phase 1 採 Anonymous-First：

~~~text
anonymous_id
→ Intent
→ Blueprint
→ Use
→ Share
→ Remix
~~~

目的不是監控所有操作，而是保留：

- Semantic Reliability；
- Share / Remix Funnel；
- Capability Gap；
- Blueprint Reuse；
- 未來 Anonymous → Account migration。

---

# 3. NFF 整體怎麼跑？

真正重要的不是 Layer 名稱，而是五條產品路徑。

## 3.1 Create

~~~mermaid
flowchart LR
    A[Inspiration / Intent]
    B[Route]
    C[Compile]
    D[Capability Resolution]
    E[Validate]
    F[Blueprint]
    G[Runtime]

    A --> B --> C --> D --> E --> F --> G
~~~

結果：

> **Intent → Correct App**

## 3.2 Use

~~~text
Existing Blueprint
→ Resolve
→ Compatibility / Trust Check
→ Browser Runtime
→ Local Interaction
~~~

結果：

> **已存在的 App 不需要重新 Compile。**

## 3.3 Share

~~~text
Blueprint / Share Reference
→ Recipient Opens Link
→ Restore
→ Execute
~~~

結果：

> **接收者不用安裝、最好也不用先註冊，就能立即使用。**

## 3.4 Remix / Refine

~~~text
Existing Blueprint
+ User Change
→ Semantic Delta
→ Compile / Validate
→ New Immutable Blueprint
~~~

結果：

> **每個 App 都可以成為下一個創作的起點。**

## 3.5 Error / Recovery

NodeFF 內部可以出現：

~~~text
401
402
404
500
timeout
provider error
validation error
runtime exception
~~~

但一般 User 不應直接看到這些。

~~~mermaid
flowchart LR
    T[Technical Failure]
    C[Classify]
    R[Recovery Policy]
    S[Recovery UX State]
    U["Human Message<br/>+ Next Action"]

    T --> C --> R --> S --> U
~~~

使用者應看到：

> **發生什麼 + 我們保留了什麼 + 你現在可以做什麼**

| 系統內部 | User 看到 |
|---|---|
| 401 | 「這個內容需要登入後才能繼續。」＋登入 |
| 402 | 「這項能力需要額外額度。」＋替代方案／繼續 |
| 404 | 「這個 App 連結找不到或已失效。」＋返回／重建 |
| Compiler timeout | 「這次還沒成功做出 App，你的需求已保留。」＋重試 |
| Capability Gap | 「目前還不能完整做到這個效果。」＋替代／調整 |
| Component crash | 只隔離壞掉區塊，其餘 App 繼續運作 |

Error 原則：

~~~text
Never White Screen
Never Raw Technical Error as UX
Preserve User Input
Always Give a Next Action
No Infinite Retry
No Fake Success
~~~

Failure 也必須形成 Evidence，讓 Compiler 與 Capability Fabric 變好。

---

# 4. 短、中、長期怎麼開發？

核心不是每個階段換一套架構，而是：

> **同一個 Intent → Blueprint → Runtime 核心，逐步增加能力。**

~~~mermaid
flowchart LR
    P1["短期<br/>Prove Core Loop"]
    P2["中期<br/>Reuse / Identity / Creator"]
    P3["長期<br/>Intent Commerce / Capability Network"]

    P1 --> P2 --> P3
~~~

## 4.1 短期 — 證明核心循環

要證明：

~~~text
Intent
→ Correct App
→ Immediate Use
→ Share
→ Recipient Use
→ Remix
~~~

必須做好的系統：

- Experience Shell / 靈感精靈；
- Layer 1–4；
- Model Gateway 基本 Adapter；
- Phase 1 Capability Fabric；
- Blueprint / Instance；
- Share / Restore；
- Anonymous Evidence；
- Humanized Recovery。

Phase 1 **不追求所有 Intent 都支援**。

成功標準是：

> **能做的要做對；不能做的要講清楚，而且 User 還能繼續。**

## 4.2 中期 — Reuse、Identity、Creator Value

當核心循環有 PMF Evidence，再增加：

~~~text
Anonymous → Account
Blueprint Reuse
Trusted Blueprint Families
Ownership
Creator Attribution
History / Save
Realtime where proven
Premium Capability
Semantic Retrieval
~~~

架構重點：

- 不重做 Runtime；
- 不重做 Blueprint；
- Capability Card 已保留 Remix / Ownership / Entitlement hooks；
- Identity 加在既有 anonymous evidence 之上；
- Reuse 使用既有 lineage / compatibility；
- Semantic Retrieval 是增強 Compiler，不取代 Compiler。

目標：

> **把一次性的好 App，變成可重用、可擁有、可創作的資產。**

## 4.3 長期 — Intent Commerce / Capability Network

當供需成立，再增加：

~~~text
External Capability Providers
Provider Registry
Paid Capability
Entitlement
Metering
Booking / Payment / Commerce
Transaction Lifecycle
Settlement
Trust / Certification
~~~

整體仍然是：

~~~mermaid
flowchart LR
    I[Intent]
    C[Capability Selection]
    B[Blueprint]
    R[Runtime]
    G[Capability Gateway]
    P[External Provider]

    I --> C --> B --> R
    R -. only when required .-> G --> P
~~~

不是所有互動都送到 Commerce Server。

目標：

> **使用者只表達 Intent，NFF 可以組合內部與外部 Capability 完成事情。**

## 4.4 發展地圖

| 階段 | 主要產品結果 | 新增能力 | 不應現在先做 |
|---|---|---|---|
| **短期** | Intent → App → Share → Remix | Compiler、Runtime、Capability、Recovery、Anonymous Evidence | Marketplace、大型 Realtime、複雜 Vector Infra |
| **中期** | Reuse + Identity + Creator Value | Ownership、Account、Trusted Reuse、Creator、必要 Realtime | 大型 Commerce Network |
| **長期** | Intent Commerce + Capability Network | Provider、Metering、Entitlement、Transaction、Settlement | 不再另造第二套 Runtime |

---

# 5. 不可違反的架構規則

這些規則保護 NodeFF 不會在開發過程越做越歪。

1. **LLM 只能產生受控 Blueprint，不生成／執行任意 JavaScript。**
2. **Runtime 不做 free-form Intent 推理。**
3. **Capability Fabric 是 NFF 可執行能力的唯一邊界。**
4. **Schema Valid ≠ Semantic Correct。**
5. **Unsupported Intent 不得用錯誤語意假裝完成。**
6. **LLM Vendor 必須藏在 Model Gateway 後。**
7. **Blueprint / Instance / Context / Delta / Recovery Context 分離。**
8. **Existing Blueprint 一般互動預設 0 LLM。**
9. **Share / Remix 是核心路徑，不是附加 Export。**
10. **Error code 是工程資訊，不是 Consumer UX。**
11. **Component failure 不得造成整個 App White Screen。**
12. **Heavy / Paid / External Work 必須經 Capability Boundary。**
13. **短、中、長期增加能力，不推翻核心 Runtime / Blueprint 模型。**

## 文件責任

~~~text
APP-ARCHITECTURE.md
→ NFF 有什麼、各自負責什麼、整體怎麼跑、怎麼成長

ProjectManagement/CAPABILITY-FABRIC.md
→ NFF 到底會什麼、Capability Card、Maturity

INFRA-ARCHITECTURE.md
→ Browser / Edge / Serverless / DB / External Service 怎麼部署

APP-DETAILED-DESIGN.md
→ 每個 Function 如何真正設計與交付

working/functions/
→ Frontend / Backend / API / Data / Error / Acceptance 詳細實作規格
~~~

---

# 結論

NodeFF App Architecture 可以濃縮成：

~~~text
讓人容易表達 Intent
        ↓
正確理解 Intent
        ↓
只使用可信任 Capability
        ↓
產生可驗證 Blueprint
        ↓
Browser Runtime 低成本執行
        ↓
Use / Share / Remix
        ↓
失敗也給人性化交代
        ↓
Evidence 讓下一次更準
~~~

短期先證明這個循環。

中期在同一個底座上加入 **Reuse / Identity / Creator Value**。

長期再加入 **Intent Commerce / Capability Network**。

> **不是每個階段重做一次 NFF，而是同一個核心逐步長大。**
