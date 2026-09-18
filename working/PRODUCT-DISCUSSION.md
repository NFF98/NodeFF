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
