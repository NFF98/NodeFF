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

### Detailed Design — Layer 4: Universal Lego Player Layer (Working)

**定位：** Layer 4 是前端端的 **Universal Lego Player / Rendering & Runtime Layer**。它不理解使用者語意，也不負責決定產品/業務意圖；它依照 Layer 3 的已驗證 LegoSpec Contract，在瀏覽器中完成渲染、狀態管理、受限運算、互動與容錯。

**核心責任：**
1. **Component Registry & Factory** — 依據 LegoSpec 的 `type` 從 allowlisted Registry 載入對應 React Component。
2. **Local Reactive State Store** — 將 LegoSpec 的 state hydration 到瀏覽器記憶體；Input/Action 更新 state 後，由 reactive subscription 精準觸發相關 UI 更新。
3. **Sandboxed Expression Evaluator** — 執行受限制的 expression，例如 `SUM`、`MAX`、`IF` 等；禁止 `eval()` 與任意 JavaScript execution。
4. **URL Hash Hydrator / Compressor** — 支援無資料庫分享；將可分享的 LegoSpec/state 壓縮至 URL hash，開啟連結後反向 hydration。
5. **Graceful Degradation & Error Boundary** — 未知 component、無效 expression 或單一 Lego runtime error 不得導致整頁 White Screen；應隔離並降級為安全提示/文字。

**Layer 3 / Layer 4 分工：**
- Layer 3：定義「長相與規則是什麼」— Contract / Validation。
- Layer 4：決定「如何在瀏覽器把它跑起來」— Rendering / State / Runtime Execution。
- Layer 4 不進行自然語言理解、不重新解讀 intent，也不自行發明 component type。

#### Transparent Protocol / Graceful Degradation

當需求超越 NodeFF 當前能力邊界時，系統不應假裝完成，也不應直接讓使用者得到空白/錯誤結果。

Working protocol：
- Layer 2 必須將「能力不足 + 替代方案」編碼進 LegoSpec 的 `notice`。
- Layer 4 在卡片頂部渲染 notice banner。
- 下方仍正常渲染可執行的替代 LegoSpec。
- 使用者因此能清楚知道「原始需求沒有被完整實現」以及「目前提供的是什麼替代方案」。

Example concept:
```json
{
  "title": "憤怒鳥：角度與力量試算版",
  "notice": {
    "type": "warning",
    "message": "⚠️ 本平台不支援 3D/物理動態遊戲。已將需求轉換為彈道角度、力量與機率計算的數值試算卡。"
  },
  "state": {
    "angle": 45,
    "power": 80
  },
  "layout": [
    { "type": "NumberInput", "label": "發射角度 (0-90°)", "bind": "angle" },
    { "type": "Slider", "label": "拉弓力量 (0-100)", "bind": "power" },
    {
      "type": "StatCard",
      "label": "預測命中率 & 破壞力",
      "expression": "..."
    }
  ]
}
```

**UX principle：**
> **Transparent limitation + usable fallback > silent substitution.**

#### Lego-fication / Five Atomic Roles

Working model: 多數 NodeFF 派對/決策微應用可由以下五類原子組合：
1. **State** — 儲存目前資料/遊戲狀態。
2. **Action** — 使用者觸發互動，例如 Button、DiceRoller、WheelSpinner、Timer。
3. **Rule / Expression** — 受限制的純資料運算與規則。
4. **View** — 顯示結果，例如 StatCard、LeaderBoard、CardFlipper。
5. **Effect** — WOW feedback，例如 Confetti、SoundEffect、Vibrate。

LLM 的工作不是生成任意程式，而是生成 wiring blueprint，例如：
**Action → State → Rule → View → Effect**。

#### Technical Boundary / Hard Wall (Working)

目前材料提出的主要 hard walls：
- 需要連續 60fps 物理碰撞 / 自由 Canvas / 3D action gameplay 的需求，不屬於目前 Layer 4 的標準微應用 runtime。
- 複雜、多分支、長篇 RPG / 大型 AI NPC 狀態系統，不屬於目前 declarative micro-app contract 的目標範圍。
- 需要前端未預建的任意 custom function / arbitrary JavaScript / 任意外部媒體執行的需求，不應由 LLM 自行發明 runtime capability。
- 超出能力時應依 Transparent Protocol 產生 notice + 可行 fallback，而不是 silent downgrade。

#### Built-in Formula / Rule Runtime (Working)

Layer 4 可提供類似 spreadsheet 的**通用資料運算 primitives**，例如：
- `IF(condition, a, b)`
- `COUNT_MATCHES(array, value)`
- `UNIQUE(array)`
- `SUM(array)`
- `MAX(array)`

這些應保持為通用 runtime primitives，而非把特定產品的業務規則硬編進 Layer 4。

#### Important Design Notes / Suggestions

1. **Layer 4 的「無腦 renderer」與「預建 Rule Engine」要切乾淨。**  
   `SUM/MAX/IF` 這類 generic functions 可以屬於 runtime；但 `CALCULATE_18_LA`、特定遊戲稱號/得分規則屬於 domain logic，不應直接寫死在 Universal Player。否則 Layer 4 會逐漸變成「業務邏輯大雜燴」。

2. **「3D」與「3D 遊戲 Hard Wall」需要在正式設計中分開定義。**  
   可以保留 Rich Primitive（例如 Model3DViewer）作為受控展示元件，但不等於支援任意 3D engine / 60fps physics / action gameplay。正式 spec 應把「3D Viewer」與「3D Game Runtime」視為不同能力。

3. **URL hash 不應預設承載敏感資料。**  
   Hash 雖不會像一般 query parameter 一樣直接送至 server，但分享、瀏覽器歷史、截圖/複製連結等仍可能暴露資料。正式 Security Design 應定義可進入 share URL 的資料範圍與敏感資料禁止規則。

4. **Transparent Protocol 最好由 Schema 強制驗證。**  
   若某個 request 被 Layer 2 判定為 fallback/degraded，Layer 3 validator 應要求 `notice`；不要只依賴 System Prompt，避免 LLM 漏填。

5. **Error Boundary 與 validation 要有層級。**  
   Schema-invalid 應在 Layer 3 擋下；runtime exception 才由 Layer 4 Error Boundary 處理。兩者不要混為同一種錯誤。

6. **Layer 4 不應自行決定「降級成什麼」。**  
   Layer 2/3 決定合法的 fallback contract；Layer 4 只忠實執行與呈現。這能維持「Layer 4 無語意、無業務決策」的乾淨邊界。

**Working status:** 本節全部仍屬 working material，尚未成為官方 SSOT。


### Error Handling & System Recovery — Working

**目標：** NodeFF 的錯誤處理不是單一「Error Page」，而是依錯誤發生階段採取不同的 recovery strategy，並盡量維持使用者流程不中斷。

#### 1. Four Major Error Scenarios

| Error Scenario | Cause |
|---|---|
| **Error in Making（生成階段失敗）** | LLM 輸出破損 JSON、連線 timeout、或輸出未通過 NFF Primitive / Schema validation。 |
| **Made but Error in Request（生成成功但意圖不符）** | JSON 合法，但生成結果與使用者原始意圖不一致，例如要求 6 顆骰子加倍，卻產生 4 顆一般骰子。 |
| **Made but Run Error（生成成功但執行崩潰）** | 初次 render 正常，但互動後發生 runtime exception，例如除以零、undefined / NaN、或狀態流程進入無效狀態。 |
| **System Recovery Pipeline（跨層錯誤）** | 錯誤跨越 generation、validation、runtime 等多個階段，需要連續 recovery / telemetry。 |

#### 2. System Recovery Pipeline

Working flow：

```
[User Request / Interaction]
        │
        ├── (1) Generation failure?
        │       └──► Edge/Compiler Retry
        │                 └── failure
        │                       └──► Generic Base Spec / Safe Fallback
        │
        ├── (2) Intent mismatch?
        │       └──► User Micro-Refinement
        │                 └──► LLM Delta Patch
        │
        └── (3) Runtime failure?
                └──► Layer 4 Error Boundary
                          └──► Local Component Fallback
                                    └──► Telemetry + Invalid Mark
```

**核心原則：**
- Generation error → 修復「藍圖」。
- Intent mismatch → 修復「藍圖與使用者意圖的差集」。
- Runtime error → 隔離「壞掉的元件」，不要讓整張 micro-app 崩潰。
- Recovery 失敗 → 提供安全、可理解的 fallback，而不是 White Screen。

#### 3. Client-Side Error Boundary

Layer 4 的每個可執行 Primitive 應有局部錯誤隔離能力。

若某個 component 的 expression / runtime logic 發生 exception：
- 該 component 顯示安全的錯誤狀態，例如「運算異常，已恢復預設值」。
- 不應直接造成整張 card / micro-app White Screen。
- 不應影響同一 PartyKit room 的其他 UI 或多人 session。

這與 Layer 3 Schema Validation 的責任不同：
- **Layer 3：** 阻止 invalid contract 進入 runtime。
- **Layer 4：** 防止合法 contract 在實際執行時的 exception 擴散。

#### 4. Algorithmic Downgrade / Invalid Blueprint Handling

Working proposal：

- 若同一 Blueprint 在 Client Runtime 持續觸發 execution error，可將其標記為 invalid / unhealthy。
- 原始材料提出「超過 2 次即降權 / Unpublish」作為候選策略。
- 這個 **2 次門檻目前不應視為正式規格**；正式設計需要再決定計數方式、時間窗口、去重方式、是否以版本為單位，以及 false-positive protection。
- Unpublish / Common Pool 的具體資料模型與權限邏輯，後續應在詳細設計補齊。

#### 5. Graceful Degradation

對使用者而言，系統應盡可能維持「仍然可以完成事情」：

**特殊能力失敗 → 標準 UI fallback → 核心資料 / session 能力繼續運作。**

例如：
- 特殊動畫失敗 → fallback 到標準按鈕 / 選單。
- 單一計算元件失敗 → 該區塊顯示安全狀態，不影響其他元件。
- 整張 Blueprint 無法安全執行 → 回到 Generic Base Spec / Safe Fallback。

**UX principle：**
> **不中斷流程，但不隱瞞錯誤。**

#### 6. Telemetry / Recovery Observability

每次 recovery 都應留下最小必要的 telemetry event，以便後續定位壞 Blueprint 與改善生成品質。

Working event categories：
- generation_failed
- validation_failed
- intent_refinement
- runtime_component_error
- blueprint_degraded
- fallback_rendered

Telemetry 不應記錄不必要的敏感使用者資料；正式 Privacy / Security Design 再定義 retention、sampling、PII handling 與 access control。

#### 7. Important Design Suggestions

1. **不要把「Self-Healing」理解成系統可以任意修改自己的程式。** NodeFF 的 recovery 應是受控的 retry、delta patch、fallback、component isolation 與 blueprint quarantine，而不是 runtime 自我生成 / 執行任意 code。
2. **Error Recovery 必須有上限。** Retry / Delta Patch 不應無限循環；正式設計需要定義 retry budget / circuit breaker。
3. **Intent mismatch 最好保留使用者控制權。** 系統可以提供 refinement suggestion，但不應偷偷修改使用者需求後直接替換結果。
4. **「2 次即 Unpublish」先保留為候選，不升格為硬規則。** Client error 次數本身可能受到瀏覽器、網路或 transient failure 影響。
5. **Recovery outcome 要可觀測。** 否則「降級成功」與「其實一直壞」在營運上無法區分。

**Working status:** 本節全部仍屬 working material，尚未成為官方 SSOT。


### Detailed App Design Inputs — Latest Working Discussion

The latest discussion adds these concepts to the system-design workout:
- **Product identity:** Dynamic UI Runtime Engine + Intent-to-UI Protocol.
- **Dual persistence:** Template/Blueprint versus filled Instance Snapshot.
- **State preservation:** restore valid state without LLM recompilation; LocalStorage and URL hash are mechanisms, not absolute guarantees.
- **App-to-App composition:** Universal Context Payload (`summary`, `rawText`, `structuredData` are current candidates) moves approved output from App A to a user-selected App B.
- **Experience Shell:** Inspiration Capsules are creation scaffolds using Fork & Remix, Ghost Text and Progressive Refinement.
- **Infrastructure alignment:** edge-first/client-first is a strategy, not a guarantee of nearest-node execution or 3-second generation.
- **Implementation candidates:** Cursor + GitHub + managed serverless hosting + candidate Supabase persistence; vendor choices remain open.

**New working architectural principle:**
> **Blueprint defines reusable capability; Instance defines current reality; Context connects one micro-app to the next.**

These should become first-class concepts in later data-model and API design rather than being mixed into one generic “app” object.
