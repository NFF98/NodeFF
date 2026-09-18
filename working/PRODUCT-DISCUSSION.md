# NodeFF Product Discussion

## Purpose
Working notes for NodeFF product discussions before decisions are approved into the official specification.

## Status
- Working document — **not SSOT**
- Nothing here is an approved product decision unless explicitly moved into `spec/` or `decisions/` after user approval.

## Discussion Notes

### Top Mission / Game-Changing Reason
The user identified the following source material as the starting point for NodeFF's top mission / game-changing reason:

- NodeFF aims to challenge the traditional App model by reducing or eliminating the friction created by apps as isolated containers.
- **Zero Cross-App Friction:** a user's natural-language intent can potentially chain multiple C2C APIs/data capabilities in the background, instead of requiring manual app switching, copying, and pasting.
- **Intent-adaptive UI / Disposable UI:** instead of forcing users through fixed app pages, the interface can be dynamically composed around the user's current intent and only expose the capabilities needed for that task.
- The proposed ecosystem shift is from users finding and operating individual apps toward users expressing intent while underlying capability providers become composable services/APIs.
- The source describes a possible end state in which users care less about which app provides a function and more about whether the generated experience solves the immediate problem; creators can focus on individual capability blocks/APIs.
- The technical direction described in the source uses LLMs as a declarative compiler: natural language is transformed into structured logic/UI/data-flow specifications rather than arbitrary raw code, with a reusable runtime/player rendering those specifications.
- The source specifically describes semantic parsing, delta editing/JSON Patch, and declarative logic synthesis as key AI capabilities.

### Five Key Principles
Current working keys identified by the user:

| # | Key |
|---:|---|
| 1 | **No install setup** |
| 2 | **Everyone is the creator** |
| 3 | **Sharable, linkable** |
| 4 | **Intent Commerce** |
| 5 | **Fun and socialable** |

### Business Idea Exploration
Initial business/application directions explored from the current NodeFF keys:

| # | Idea | Intent Commerce | Social |
|---:|---|:---:|:---:|
| 1 | **Group Bill Negotiator** — 聚餐分帳、誰該付多少 | ★★★ | ★★★ |
| 2 | **Trip Decision Game** — 朋友輸入「週末去哪」，自動產生方案＋投票 | ★★ | ★★★ |
| 3 | **Gift Decision Engine** — 輸入「送這個人什麼」，多人共同決策 | ★★★ | ★★★ |
| 4 | **Dinner Battle** — 「今晚吃什麼」變成朋友間即時遊戲 | ★★ | ★★★ |
| 5 | **Price Negotiation Simulator** — 幫兩邊模擬/協商價格 | ★★★ | ★★ |
| 6 | **Event Cost Splitter** — 婚禮、旅行、Party 等多人動態分攤 | ★★★ | ★★★ |
| 7 | **Office Politics Calculator** — 聚餐、送禮、紅包等社會慣例決策 | ★★ | ★★★ |
| 8 | **Household Decision Maker** — 情侶/家庭「誰做什麼、誰付多少」 | ★★★ | ★★★ |
| 9 | **Second-hand Deal Maker** — 買賣雙方輸入條件，自動生成交易方案 | ★★★ | ★★ |
| 10 | **Crowd Decision App** — 把任何「大家怎麼決定？」瞬間變成可分享的小 App | ★★★ | ★★★ |

### Working Product Hypothesis
A recurring hypothesis from the discussion is:

> 「20 人怎麼分帳」不是產品本身；「任何人遇到一個複雜決策 → NodeFF 秒變成一個可互動、可分享、可交易的小 App」才可能是產品。

This remains a working hypothesis and is not yet an approved product decision.

### Phase 1 Scope — Working
The uploaded Phase 1 material frames NFF as a **dynamic micro-application engine**, not a replacement for native apps.

**Boundary / positioning:**
- Native Apps: high-stickiness, long-lifecycle experiences with deep identity/data, background system capabilities.
- NFF: instant-intent, single-session, disposable experiences with zero-download / zero-registration entry.
- NFF is aimed at long-tail, fragmented, dynamically generated, C2C/social micro-app experiences rather than replacing mature native apps.

**Phase 1 boundary model under discussion:**
- **Tier 1:** lightweight client-side / ephemeral experiences, including real-time social games, calculators, timers, and browser/WASM workloads.
- **Tier 2:** experiences requiring paid runtime APIs, persistent cloud storage, heavier AI/media computation, or larger/longer-lived rooms.
- **Tier 3:** requests exceeding browser/OS/security boundaries or lacking meaningful UI value; these are rejected or redirected.
- Core engine behavior under discussion: existing Lego primitives → direct declarative rendering; missing specialized UI → generic form fallback; heavy workloads → cloud-worker escalation; unsafe/unsupported system-level requests → hard reject.
- Security direction: no arbitrary dynamic JavaScript execution; generated JSON selects approved primitives and parameters.

**Phase 1 product/experience direction:**
- Consumer entry should preserve the zero-friction principle.
- Creator experiences can use progressive authentication when persistent ownership, history, or paid capabilities become necessary.
- Candidate experience categories include social games, group decisions, cost splitting, temporary calculators/tools, and other short-lived intent-driven micro-apps.

**Open decisions from the Phase 1 material:**
1. Runtime LLM usage: quota within free tier vs. automatically Tier 2 when runtime AI is required.
2. Ephemeral room limits: proposed example is 10 concurrent users / 15-minute idle destruction.
3. Macro-app reframing: automatically reduce a large-app request to an NFF-sized intent, or ask for confirmation first.

**Working note / better suggestion:** Keep Phase 1 focused on proving the **instant-intent → generated micro-app → share/use → disappear** loop. Treat exact cost figures, room limits, and technical thresholds as provisional until validated by implementation and real usage.

### UI/UX Design — Working
The user proposes that **「靈感膠囊」不是展示 Demo，而是降低思考成本的 Prompt 教學與創作入口**. Its core purpose is to teach users how to give better instructions through **Fork & Remix** rather than asking them to start from a blank input box.

**Four mechanisms under discussion:**

#### 1. 點擊即帶入「可編輯樣板」(Fork & Remix)
Clicking an inspiration capsule does not immediately jump to a generated result. Instead, the complete example text is inserted into the Prompt input and key variables are highlighted for editing.

Example:
- Capsule: **[ 💰 3人多幣分帳 ]**
- Input becomes: **「3人去[東京]旅遊，[小明]付日幣 15000，[小華]負擔雙份」**
- User can directly change 「東京」→「韓國」、 「日幣」→「韓幣」 and immediately learn how to express their own need.

Working UX principle: **editing an existing example should be easier than inventing a request from zero.**

#### 2. 建立「三段式心智模型」(The Implicit Formula)
Through comparison of 3–5 capsules, users can implicitly learn a useful input structure:

**[ 情境/主題 ] + [ 成員/數據 ] + [ 特殊規則/條件 ]**

Examples:
- **[ 5人開會 ] + [ 時薪 500 元 ] + [ 預計討論 1 小時 ]**
- **[ 晚餐決策 ] + [ 燒肉/拉麵/健康餐 ] + [ 預算 400 內、不要火鍋 ]**

The intended behavior is that users gradually copy this structure into their own requests without needing to study a formal Prompt tutorial.

#### 3. 靜態與動態 Ghost Text (打字機預覽)
When the input is empty, the placeholder can automatically rotate through complete natural-language examples in a typewriter-like presentation.

Examples:
- 「深蹲 5 組，從 60kg 開始每組加 5kg，每組休息 90 秒」
- 「月薪 65,000，扶養 1 人，幫我算實領薪資與勞健保」

Purpose: continuously demonstrate that **ordinary everyday language can be directly turned into a usable NFF experience.**

#### 4. 漸進式對話微調 (Progressive Refinement)
The first request does not need to be perfect.

Example flow:
1. User: **「幫我做個 3 人分帳」**
2. NFF generates a basic 3-person bill-splitting card.
3. The generated card then presents contextual suggestion capsules such as:
   - **[ 💡 試試加入：匯率換算 ]**
   - **[ 💡 試試加入：權重比例 ]**
4. User incrementally improves the generated micro-app instead of rewriting the original request.

This turns Prompt learning into a low-pressure loop:

**點擊現成範例 → 替換關鍵字 → 生成 → 隨手微調**

### UI/UX Working Hypothesis
The deeper UX idea is not merely **「教使用者寫 Prompt」**, but **「讓使用者在完成事情的過程中，自然學會如何描述需求」**.

Inspiration capsules therefore function simultaneously as:
- examples,
- editable templates,
- learning scaffolds,
- starting points for creation,
- and remixable/shareable seeds.

The desired experience is that users gradually move from **copying → modifying → combining → creating from scratch**, without needing to understand prompt-engineering terminology.

**Better suggestion:** Avoid making the product feel like a Prompt school. The UI should optimize for **getting the user to a useful result quickly**, while the learning happens invisibly through examples and refinement. In other words: **「先完成，再學會；不是先學會，才能完成。」**

A second UX principle worth validating later: the capsule should be **outcome-led rather than prompt-led**. Show users what they can make/do (e.g. 「3人多幣分帳」) and let the editable prompt remain the mechanism underneath. This keeps NFF feeling like a consumer creation tool rather than an AI prompt editor.

### Working Status
All content in this file remains working discussion material unless explicitly approved and moved into `spec/` or `decisions/`.

### Detailed Design — Layer 2: Semantic Compiler Layer (Working)

**定位：** 將非結構化的自然語言，轉換為符合 NodeFF 定義的結構化 JSON。

**核心元件 / processing：**
- **Context Injector：** 注入 System Prompt 與 NFF Component Registry 可用清單，讓 LLM 只知道目前前端可使用的 Lego/Component primitives。
- **LLM Inference Engine：** 可使用 Groq / OpenAI 相容 API；強制 Structured Outputs（JSON Mode）。
- **Intent Convergence：** 將自然語言意圖收斂為可處理的 Archetype，例如「午餐吃什麼」→ Decision Archetype、「算熱量」→ Entity Archetype。
- **Schema Validator：** 後端以 Pydantic 或 Zod 做第一次結構驗證，並檢查 bind 的變數是否存在於 initialState；失敗時觸發內部 Retry。

**核心工程決策（Working）：One-time Compiler**
- LLM 不負責使用者每次互動時的即時運算。
- LLM 將自然語言一次性編譯成宣告式 DSL：LegoSpec JSON AST。
- JSON 傳送完成後，後續 Slider、Input、狀態變更等互動由瀏覽器端 runtime 處理，以避免每次互動都重新呼叫 LLM。
- 目標是將 LLM interaction cost 從隨互動次數增加的模式，轉為一次編譯後由 client runtime 持續處理。

**與 Layer 1 的接口關係（Working）：**
- Layer 1 負責邊界路由、快取命中與請求派發。
- Cache Miss 的新請求進入 Layer 2。
- Layer 2 產生並驗證 LegoSpec JSON AST，成功後交給後續 Layer。

**Architecture Boundary（Working）：**
NodeFF 的核心技術方向暫定為：**約 12–15 個高階領域 Component Libraries（可包含 3D、動畫、影音等 Rich Primitives）＋純宣告式 JSON Contract＋瀏覽器端 AST 安全沙盒 Renderer/Runtime。**

**Working caution：** 上述「100%」、「O(1)」、「sub-millisecond」、「12–15 個」等數字/性能表述目前視為設計目標或假設，不視為已驗證的實際性能保證；後續詳細設計與實測再確認。

### Detailed Design — Layer 1: Ingestion & Routing Layer (Working)

**定位：** 接收 User Prompt，進行成本與安全性過濾，並決定請求走向。

**核心 processing：**
- **Tier 3 Defense Interception：** 檢查惡意 payload、純閒聊/知識問答、或要求底層 OS 權限等不適用請求；命中後直接阻斷並回傳純文字/錯誤卡片。
- **Edge KV Cache：** 以 prompt normalization 後的 SHA-256 作為 Key，以已驗證的 LegoSpec JSON Blueprint 作為 Value；Cache Hit 時直接回傳，繞過 LLM。
- **Task Dispatch：** Cache Miss 時封裝 request 並派送至 Layer 2。

**Edge KV Working Definition：** Edge KV 是部署於 CDN edge 的低延遲 key-value storage，例如 Cloudflare KV / Vercel KV。其用途是讓相同或可標準化為相同 key 的意圖可以重用已驗證 blueprint。

**Cache flow（Working）：**
User Prompt → Normalize → SHA-256 Key → Edge KV Lookup → Hit: Verified LegoSpec / Miss: Layer 2

**Working caution：** 「去除空格與標點後直接 hash」目前只是候選 normalization 策略；不同語意但文字不同的 prompt 仍可能造成 cache miss，未來可考慮 canonical intent key / semantic cache。

### Detailed Design — Layer 3: Contract Layer / LegoSpec JSON Schema (Working)

**定位：** NodeFF 架構的核心契約層。以宣告式 Schema 嚴格定義 State、UI Layout、Logic/Actions，以及資料與畫面的綁定關係。

**Schema 核心三大區塊：**
- **state：** 定義所有變數的初始值與型別（目前討論包含 Number、String、Array）。
- **layout：** 定義 UI Lego/Component 的排列順序與層級。
- **logic/actions：** 定義 UI 互動如何改變 State，例如數學公式或狀態機變更。

**Working JSON Contract example：**
```json
{
  "archetype": "calculation",
  "state": { "budget": 400, "item_price": 100 },
  "layout": [
    { "type": "NumberInput", "bind": "budget", "label": "預算上限" },
    { "type": "StatCard", "expression": "budget / item_price", "label": "可買數量" }
  ]
}
```

此契約的核心目的，是讓 LLM 產生明確結構，而不是讓前端透過 Regex 猜測變數或 UI 關係。

**15 個高階 Domain Primitives（Working Catalog）：**
1–4 **Input Controls：** NumberInput、TextInput、SelectChoice、ToggleSwitch。
5–7 **Data & Visualization：** StatCard、DataTable、ChartVisualizer。
8–13 **Rich Media & Interactive Engine：** Model3DViewer、LottieAnimator、WheelSpinner、DiceRoller、VideoPlayer、ConfettiTrigger。
14–15 **Layout & Composition：** Container、Repeater。

**TypeScript / Zod schema direction（Working）：**
- 使用 Zod 建立 component contract。
- 共通 BaseItem：`id` optional、`label` required。
- Input components 使用 `bind` 指向 state key；NumberInput 支援 min/max/step/unit；TextInput 支援 placeholder；SelectChoice 支援 label/value options；ToggleSwitch 綁定 boolean state。
- StatCard 使用 expression 與 optional format；DataTable 綁定 array 並定義 columns；ChartVisualizer 定義 bar/line/pie、資料來源與 x/y keys。
- Model3DViewer 使用 model URL、autoRotate 與 optional triggerState；LottieAnimator 使用 source URL、loop、speed；WheelSpinner 使用 items 與 bind；DiceRoller 使用 1–6 顆骰子與 bind；VideoPlayer 使用 source URL、autoplay、muted；ConfettiTrigger 使用 condition。
- Container 為遞迴 children 容器；Repeater 綁定 array state 並以 render 定義重複子藍圖。
- 最終以 discriminated union（以 `type` 為 discriminator）組成 LegoSpec Component Item Schema。

**State Binding Protocol（Working）：**
- 具修改能力的 components（例如 NumberInput、SelectChoice、WheelSpinner、DiceRoller）透過統一 state context / bridge，概念上以 `onChange(key, value)` 寫入瀏覽器記憶體中的 gameState。
- 表現/統計 components（例如 StatCard、ConfettiTrigger）在 gameState 變更後重新求值，不直接持有業務 state。
- Expression 使用受限制的 sandbox evaluator（目前材料舉例 expr-eval）執行數學/邏輯 expression。
- Container 與 Repeater 提供巢狀與重複組合能力，讓 Domain Primitives 可以組合成具備資料、互動、動畫與 Rich Media 的微應用。

**Security boundary（Working）：**
- LegoSpec 是 declarative contract，不是任意程式碼執行介面。
- Component parameters 與 state binding 必須經 Schema validation。
- 仍維持 Layer 2 / Layer 3 的核心原則：LLM 產生 JSON contract；Renderer/Runtime 只執行 Registry 中被允許的 component types 與受限制的 expression。

**Working caution / design points：**
- 「15 個」目前記錄為現有設計 catalog，不代表未來永遠只能有 15 個；Registry 應保留版本化與擴充能力。
- `logic/actions` 已列為 Schema 三大區塊，但目前提供的 JSON example 尚未展示該區塊；詳細 action/state-machine contract 仍需在後續詳細設計補齊。
- 原始材料同時使用 `computed` 與 `expression` 兩種命名；目前工作筆記以 `expression` 為主，但正式 Schema 命名尚未批准。
- 「100% 符合定義」與「封鎖任何 ACE」先視為設計目標；正式安全模型需在 Security 詳細設計中明確定義 validator、sandbox、allowlist 與 threat model。