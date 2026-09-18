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

**Important:** Everything in this file remains working discussion material unless explicitly approved and moved into `spec/` or `decisions/`.
