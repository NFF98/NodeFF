# NodeFF 商業計畫

> 狀態：Working。除非依 NodeFF SSOT 流程正式升格，否則不具權威性。

## 1. 商業核心

NodeFF 要改變的不是某一種 App，而是「使用者為了完成一個短暫需求，必須先找 App、安裝 App、學 App、再切換 App」的使用模式。

NodeFF 的核心體驗是：

> **表達 Intent → 立即得到可互動、可分享、可 Remix 的 Micro-App。**

NodeFF 不是：
- AI Code Generator；
- 計算機集合；
- Generic Form Builder；
- 所有 Native App 的替代品。

核心產品假設：

> **短暫、情境化、需要互動或多人參與的 Intent，可以直接變成 Disposable Micro-App，而不需要安裝、部署或寫程式。**

最重要的產品判斷仍然是：

> 「20 人怎麼分帳」不是產品；  
> 「任何人遇到一個複雜決策 → NodeFF 立即變成一個可互動、可分享、可交易的小 App」才可能是產品。

---

# 2. 商業發展地圖

NodeFF 不應同時追求所有可能性。

目前商業發展分成三個階段：

```text
短期：證明產品核心循環
        ↓
中期：建立 Reuse / Creator / Paid Value
        ↓
長期：Intent Commerce / Capability Network
```

---

# 3. 短期：Phase 1 — 先證明核心循環

## 3.1 唯一優先目標

Phase 1 最重要的問題只有一個：

> **使用者能否描述一個短暫需求，快速得到正確有用的 Micro-App，立即使用、分享，並讓另一個人繼續使用或 Remix？**

必須先證明：

```text
Intent
 → Correct Micro-App
 → Immediate Use
 → Share
 → Recipient Use
 → Remix / Create
```

在這個循環成立以前，不應把主要資源投入 Marketplace、Creator Economy、Enterprise 或大量 Paid Feature。

---

## 3.2 Phase 1 的目標使用場景

初期不追求「任何 App」。

優先聚焦在具有以下共同特徵的 Intent：

- 短生命週期；
- 可互動；
- 有明確輸入與結果；
- 可以調整規則；
- 適合分享；
- 最好具有多人／Social 性質。

優先場景合併成三類：

### A. Decision / Allocation

例如：
- 晚餐吃什麼；
- 旅行方案；
- 投票；
- 分帳；
- 權重式分配；
- 家庭／活動費用；
- ROI／Scenario 比較。

### B. Party / Social Interaction

例如：
- Dice；
- Wheel；
- Card；
- Timer；
- Scoreboard；
- Turn-based party interaction。

### C. Disposable Utility

例如：
- 一次性 Calculator；
- Temporary Tracker；
- Decision Table；
- Parameterized Tool。

Phase 1 的目的不是證明每一個類別都成功，而是找到最容易形成：

> **Create → Use → Share → Remix**

的 Wedge。

---

## 3.3 Phase 1 的產品體驗

### Creation

不能只依賴空白 Prompt Box。

核心 Creation UX：

- Inspiration Capsules；
- Editable Prompt Template；
- Ghost Examples；
- Progressive Refinement；
- Fork & Remix。

使用者學習路徑：

> **copy → modify → combine → create from scratch**

產品原則：

> **先完成，再學會；不是先學會，才能完成。**

### Assumption UX

模糊 Intent 不應被模型偷偷替使用者決定。

例如：

```text
「20 人公司聚餐依職級分帳」
 → 可見的 role assumptions
 → editable counts
 → editable weights
 → result breakdown
```

產品價值之一是：

> **Fuzzy Intent → Explicit Assumptions → Interactive Model → User Adjustment**

### Quality

Phase 1 最大風險不是 JSON Error，而是：

> **Micro-App 看起來正常，但其實解錯問題。**

因此 Semantic Correctness 優先於 Visual Polish。

---

## 3.4 Phase 1 的 Distribution / Growth

NodeFF 的 Growth 應該由 Artifact 驅動，不是由 Account 驅動。

```text
Creator creates
 → Share
 → Recipient opens instantly
 → Uses
 → Remix / Creates
 → New artifact
```

所以：

- Share 是核心產品行為，不是 Export；
- Remix 必須比重新從空白開始容易；
- Recipient 不應先被 Registration Wall 擋住。

### Anonymous-First

短期原則：

- Consumer 不登入即可使用 Shared Micro-App；
- Creator 在可行時可先匿名建立與分享；
- 只有當 Durable Value 出現時才要求 Authentication。

Durable Value 包含：
- ownership；
- permanent editing；
- history；
- cross-device persistence；
- publishing；
- paid quota。

---

## 3.5 Phase 1 Business Model

Phase 1 的主要任務不是最大化 Revenue，而是驗證：

1. 有人願意 Create；
2. 產物真的 Useful；
3. 有人願意 Share；
4. Recipient 真的會 Use；
5. Recipient 會 Remix／Create；
6. Semantic Reliability 足夠建立 Trust。

### Tier 1 — 核心免費體驗

主要包含：
- client-side execution；
- approved primitives；
- deterministic local rules；
- small shareable snapshot；
- bounded compilation；
- modest ephemeral collaboration。

### Tier 2 — 成本型能力

只有真的產生成本／Durable Value 時才考慮收費：

- runtime AI；
- heavy external API；
- media generation；
- larger／longer live room；
- durable cloud state；
- persistent history；
- premium capability。

### Tier 3 — 不支援

- arbitrary code；
- unsafe OS/system access；
- 核心語意無法安全表達的需求。

---

## 3.6 Phase 1 必看的 Metrics

只保留能直接判斷核心循環是否成立的指標。

### Product Quality
- Intent → executable Blueprint success rate；
- Semantic Mismatch Rate；
- Refinement Rate；
- Time to First Useful Result。

### Activation / Usage
- Successful Executed Intents；
- meaningful interactions per Instance；
- repeat creation。

### Viral
- Share Rate；
- Share → Open；
- Open → Use；
- Use → Remix/Create。

### Retention
- Anonymous cohort repeat use；
- Creator repeat creation。

Phase 1 不需要先用大量 Revenue Metric 讓焦點分散。

---

## 3.7 Phase 1 必須驗證的假設

最重要的假設：

1. 某些 Intent 確實比 Chat Answer 更適合 Interactive Micro-App。
2. No-login experience 能提高使用與分享。
3. Share 的 Recipient 會真的互動。
4. Remix 會自然發生。
5. Social／Decision／Party 類別具有 organic distribution。
6. Visible Assumptions 能提高信任，而不是增加負擔。
7. Semantic Reliability 可以達到 repeat-use 水準。
8. Runtime economics 足以支援 generous free usage。

如果這些不成立，Long-term Platform Story 沒有意義。

---

# 4. 中期：PMF 後 — 建立 Reuse、Identity 與 Creator Value

只有 Phase 1 核心循環成立後，才進入這個階段。

## 4.1 Trusted Blueprint Reuse

從：

```text
每次 Intent → 從零 Compile
```

逐步變成：

```text
Intent
 → Retrieve Trusted Blueprint Family
 → Minimal Semantic Delta
 → Validate
 → Execute
```

商業價值：

- 更快；
- 更便宜；
- 更穩定；
- 更少 Semantic Failure；
- 更適合 Remix。

這是 NodeFF 從「AI 生成工具」走向「可累積平台」的重要轉折。

---

## 4.2 Progressive Identity

當使用者已得到價值後，再提供：

- Save；
- Ownership；
- Version History；
- Publishing；
- Cross-device；
- Private Blueprint；
- Paid Quota。

使用者生命週期可逐步成為：

```text
Use
 → Remix
 → Create
 → Save
 → Publish
```

Authentication 是 Durable Value 的交換，不是進站門票。

---

## 4.3 Creator Layer

如果有穩定的 Reuse 與 Remix 行為，再建立 Creator Value：

- Blueprint Discovery；
- Creator Profile／Reputation；
- Publishing；
- Reusable Blueprint Families；
- Premium Blueprint／Capability；
- Creator Monetization。

Creator Economy 不應在缺乏使用量與 Remix 行為前過早建立。

---

## 4.4 中期 Monetization

中期可驗證：

1. Durable Storage／History；
2. Premium Capability；
3. Larger／Longer Realtime；
4. Runtime AI／Heavy API；
5. Creator Paid Artifact；
6. Private／Team Workspace。

付費點應建立在：

> **Durable Value 或 Real Marginal Cost**

而不是把核心 creation/share loop 人為鎖住。

---

## 4.5 中期 Metrics

除了 Phase 1 Metrics，新增：

- Blueprint Reuse Rate；
- Retrieval vs Fresh Compilation Ratio；
- Anonymous → Registered Creator Conversion；
- Save／Publish Rate；
- Creator Retention；
- Paid Capability Usage；
- Free → Paid Conversion；
- Cost per Successful Intent。

---

# 5. 長期：Intent Commerce 與 Capability Network

這是 NodeFF 的平台化方向，不是 Phase 1 Roadmap。

長期可能演進成：

```text
User Intent
 → Capability Selection
 → Dynamic Micro-App
 → External API / Service
 → Transaction / Outcome
```

使用者不需要知道功能屬於哪一個傳統 App。

可能的 Capability Provider：

- AI Service；
- Data Source；
- Booking；
- Commerce；
- Media Generation；
- Specialized Calculation；
- External Workflow；
- Paid API。

NodeFF 的角色變成：

> **Intent → Capability → Interaction → Transaction 的 Control Plane。**

---

## 5.1 Intent Commerce

如果某個 Intent 需要外部付費能力：

```text
Intent
 → Capability Match
 → Price / Permission
 → Execute
 → Result
```

NodeFF 可能收取：
- Capability transaction fee；
- API margin；
- Marketplace commission；
- Creator revenue share。

但 Intent Commerce 只有在實際供需形成後才成立。

---

## 5.2 Capability Network Effect

真正的長期 Network Effect 可能是：

```text
More Users
 → More Intent Demand
 → More Capability Providers
 → More Capability Coverage
 → Better Micro-Apps
 → More Users
```

這目前仍是 Strategic Hypothesis。

不能在沒有供需密度前假設 Marketplace 本身就是 moat。

---

# 6. 商業 Flywheel

如果前述三個階段逐步成立，NodeFF 的核心 Flywheel 可能是：

```text
More Intent
 → More Correct Blueprints
 → More Trusted Reuse
 → Lower Cost / Faster UX
 → More Sharing
 → More Remix
 → More Intent
```

同時產生第二個品質 Flywheel：

```text
More Usage
 → More Failure / Correction Data
 → Better Semantic Reliability
 → More Trust
 → More Usage
```

這兩個 Flywheel 比單純追求「更多 AI Generation」更重要。

---

# 7. 五個產品原則

所有階段都必須維持：

1. **No install setup**
2. **Everyone is the creator**
3. **Sharable, linkable**
4. **Intent Commerce**
5. **Fun and socialable**

其中前四項很容易讓產品最後變成 Tool Platform，因此第五項 **Fun and socialable** 必須持續作為產品檢查點，避免 NodeFF 退化成 Generic Form Builder。

---

# 8. 商業 Guardrails

1. **短期只證明核心 Loop，不同時做全部 Platform Vision。**
2. First Value 前不強制 Registration。
3. Share 是核心 Distribution。
4. Remix 是核心 Creation Mechanism。
5. Semantic Correctness 高於 Visual Polish。
6. Assumption 必須可見，不得偽裝成事實。
7. Existing Blueprint 不應反覆消耗 LLM。
8. Paid Feature 優先綁定 Durable Value 或 Real Cost。
9. Product Boundary 必須誠實，不承諾 Arbitrary Software Generation。
10. Business／Cost／Growth 數字在量測前一律視為 Hypothesis。
11. 不因 Marketplace／Creator Economy 聽起來宏大，就提前犧牲 Phase 1 Focus。
12. NodeFF 必須維持 Fun／Social／Shareable，而不是變成另一個 Enterprise Form Builder。

---

# 9. 尚未驗證的數字

以下目前都不是事實：

- 80% Registration Drop-off；
- 特定 Anonymous CPUI；
- 特定 Registered Monthly Cost；
- K-factor > 1；
- 5M Monthly Intents；
- 90% Cache／Cost Reduction；
- 固定 Room Limit；
- Exact Model Cost；
- Zero Marginal Cost；
- Guaranteed Millisecond Latency。

未經 NodeFF 真實數據驗證前，不應用於正式 Business Case。

---

# 10. 目前 Focus

目前不需要同時回答「NodeFF 最終可以成為多大的平台」。

現在只需要回答：

> **NodeFF 能不能讓一個真實 Intent 變成正確、有用、可分享，而且會被下一個人繼續使用的 Micro-App？**

如果答案是 Yes，再進入：

```text
Phase 1 Core Loop
      ↓
Trusted Reuse
      ↓
Creator / Paid Value
      ↓
Intent Commerce
      ↓
Capability Network
```

這就是目前 Business Plan 的優先順序。
