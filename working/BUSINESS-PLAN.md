# NodeFF Business Plan（Working）

> 本文件為商業假設與驗證框架，不是已驗證的市場事實，也不是官方 SSOT。

## 1. Product Thesis
NodeFF 的核心不是「另一個 AI App Builder」，而是讓使用者把一個一次性/短生命週期需求直接變成可使用、可分享、可 remix 的 Micro-App。

核心循環：
**想法 → Intent → Micro-App → 分享/多人使用 → Remix → 新 Intent**

## 2. Initial Beachhead
優先驗證：
- Group Decision
- Cost Splitting
- Party / Social Games
- Temporary Calculators / Tools
- Short-lived collaborative utilities

共同特徵：
- 不值得下載 App。
- 需要多人或立即使用。
- 結果具有分享價值。
- 規則/介面可由 declarative primitives 表達。

## 3. Value Proposition

### Consumer
「不用找 App、不用安裝、不用先學工具；直接說你要做什麼。」

### Creator
「不用從零開發；用自然語言產生、修改、分享一個 Micro-App。」

### Capability Provider
「把既有能力/API 包裝成可被 Intent 組合的 capability。」

### Platform
「建立 Intent → Capability → Micro-App → Share/Use 的交易與分發層。」

## 4. Monetization Hypotheses
目前只作為待驗證假設：
1. Premium creation / higher generation quota
2. Tier 2 compute / API pass-through
3. Creator monetization / revenue share
4. Capability API marketplace / transaction fee
5. Business/team usage
6. Sponsored capability / distribution

不應在尚未驗證前假設任何一種為主要收入來源。

## 5. Growth Loop

```
User creates Micro-App
 ↓
Share link
 ↓
Friend opens without install
 ↓
Friend uses / remixes
 ↓
New Micro-App
 ↓
More sharing
```

這個 loop 與傳統下載型 App 的 acquisition model 不同，應成為 Phase 1 核心驗證對象。

## 6. Key Business Metrics
### North-star candidates
- Executed intents
- Successful micro-app sessions
- Share-to-open rate
- Remix rate
- Repeat creation rate

### Quality
- Generation success rate
- Intent correction rate
- Runtime error rate
- Fallback rate
- Blueprint reuse rate

### Economics
- LLM cost / successful intent
- Infra cost / session
- Tier 2 gross margin
- Revenue / creator
- Revenue / active capability

## 7. Go-to-Market Hypothesis
先從「不值得下載 App、但值得立刻使用」的場景切入，而不是試圖一次覆蓋所有 App 類別。

內容/分發可圍繞：
- 可直接分享的 Micro-App
- Inspiration Capsules
- Fork & Remix examples
- 社交/派對玩法
- 特定高頻決策 templates

## 8. Business Risks
- Cold start：沒有好玩的 examples / capabilities 時，使用者沒有理由創作。
- Generation quality：合法 JSON 不代表 intent 正確。
- Runtime trust：fallback 太頻繁會破壞信任。
- Distribution：分享必須比傳統 App invite 更低摩擦。
- Cost：高 LLM / API usage 可能侵蝕 margin。
- Abuse / security：公開 creator ecosystem 會引入惡意或低品質內容。
- Network effect timing：C2C marketplace 需要供需兩側。

## 9. Phase 1 Validation
先驗證四件事：
1. 使用者是否願意用自然語言產生 Micro-App。
2. 使用者是否願意分享 generated link。
3. 收到 link 的人是否真的會打開並使用。
4. Remix 是否自然形成第二輪創作。

若這四件事未成立，不應急著擴大 marketplace / commerce。

## 10. Business Model Evolution
```
Phase 1
Consumer Micro-App utility
        ↓
Phase 2
Creator / Remix ecosystem
        ↓
Phase 3
Capability marketplace
        ↓
Phase 4
Intent Commerce / settlement
```

這是工作假設，不是時間表承諾。

## 11. Open Questions
- 第一個 beachhead 到底是哪一類？
- Consumer 與 creator 是否同一產品入口？
- 哪些 Tier 2 能力值得付費？
- Capability provider 如何 onboarding？
- 交易抽成發生在哪個 layer？
- Marketplace trust / moderation 如何做？

**Status：Working。**
