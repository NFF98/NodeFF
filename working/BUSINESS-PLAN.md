# NodeFF 商業計畫

> 狀態：Working。除非依 NodeFF SSOT 流程正式升格，否則不具權威性。

## 1. 商業核心假設

NodeFF 要挑戰的是傳統 App 模式：使用者必須先尋找、安裝、學習、設定，再在不同 App 之間切換，才能完成一個其實只需要幾分鐘的任務。

NodeFF 的互動模型是：

> **表達 Intent → 立即得到可互動、可分享、可 Remix 的 Micro-App。**

NodeFF 不是「很多計算機的集合」，也不是 AI Code Generator。

更大的產品假設是：

> **任何短暫的人類 Intent、決策、社交互動或輕量工作流程，都可以在不安裝、不部署、不寫程式的情況下，轉化成一個 Disposable Interactive Product。**

討論中形成的核心表述：

> 「20 人怎麼分帳」不是產品本身；「任何人遇到一個複雜決策 → NodeFF 秒變成一個可互動、可分享、可交易的小 App」才可能是產品。

---

## 2. 五個產品原則

1. **No install setup**
2. **Everyone is the creator**
3. **Sharable, linkable**
4. **Intent Commerce**
5. **Fun and socialable**

除非經 SSOT 流程明確修改，產品、架構與商業模式都應維持這五個特性。

---

## 3. 使用者問題

傳統 App 的 friction 在以下情況特別明顯：

- 需求只存在幾分鐘或幾小時；
- 需求高度依賴當下的人、資料或情境；
- 需求太小，不值得安裝與設定一個完整 App；
- 固定 UI 無法表達特殊規則；
- 任務本身就是多人互動；
- 每次條件都略有不同，固定 template 不夠彈性。

Chat AI 能理解這些需求，但很多時候只回傳文字，而不是一個大家可以一起操作的互動物件。

NodeFF 的機會位於三者之間：

- 一次性的聊天回答；
- 固定功能的傳統 App；
- 客製化軟體開發。

---

## 4. 核心價值主張

NodeFF 把 Intent 轉成**可執行的互動物件**。

```text
Intent
 → Interactive Model
 → Use
 → Share
 → Other People Use
 → Remix / Refine
 → New Blueprint
```

這個 artifact 同時可以成為：

- 產品介面；
- 分享物件；
- 協作物件；
- Remix 起點；
- 未來的交易介面。

---

## 5. 最適合的使用場景

NodeFF 初期最適合的 territory：

### 社交決策
- 晚餐吃什麼；
- 旅行方案選擇；
- 禮物選擇；
- 投票；
- 群組協調。

### 共同金錢／資源分配
- 分帳；
- 權重式分攤；
- 活動費用分配；
- 家庭分工／費用；
- 情境比較。

### Party／輕量遊戲
- 骰子；
- 轉盤；
- 卡牌；
- 排行榜；
- 計時器；
- 回合制互動。

### Disposable Tools
- 一次性計算器；
- ROI／Scenario Model；
- 臨時 Tracker；
- Decision Table；
- Parameterized Utility。

### Temporary Live Session
- 群體互動；
- ephemeral room state；
- 短時間協作。

這些 use case 的共同點不是 domain，而是：

> **短生命週期、可互動、可調整、可分享。**

---

## 6. 產品邊界

NodeFF 不應宣稱可以取代所有軟體。

傳統 Native／Dedicated App 在以下需求仍然更適合：

- 長生命週期；
- 深度 Identity；
- Background Execution；
- 複雜 Durable History；
- 成熟 Notification；
- Hardware／OS Integration；
- 高頻率連續圖形運算；
- 高度客製、任意行為。

NodeFF 的核心是：

> **Instant Intent + Disposable + Composable Micro-App。**

清楚的邊界同時保護使用者期待、成本模型與安全模型。

---

## 7. Creation Experience

單一空白 Prompt Box 的思考成本太高。

NodeFF 應讓使用者在「完成事情」的過程中自然學會創作。

### Inspiration Capsules

Capsule 不是 Demo Gallery，而是 Editable Creation Seed。

使用者點擊後，應看到一段完整、可修改的需求文字，而不是只看到完成品。

### Implicit Intent Formula

使用者可以逐步學會：

```text
[情境 / 主題]
+ [成員 / 數據]
+ [特殊規則 / 條件]
```

不需要正式學 Prompt Engineering。

### Ghost Examples

輸入框可輪播自然語言範例，持續告訴使用者：

> 普通日常語言也能直接變成互動工具。

### Progressive Refinement

第一個 Prompt 不需要完美。

```text
rough intent
 → useful first Micro-App
 → contextual suggestion
 → incremental refinement
```

學習路徑：

> **copy → modify → combine → create from scratch**

UX 原則：

> **先完成，再學會；不是先學會，才能完成。**

NodeFF 應該讓人覺得是在「創造」，而不是在上 Prompt 課。

---

## 8. 使用者生命週期

理想 progression：

```text
Open
 → Use
 → Remix
 → Create
 → Share
 → Save
 → Publish
 → Monetize
```

不是每個人都需要走完整條路。

最重要的 Early Loop 是：

```text
Intent
 → Correct Micro-App
 → Immediate Use
 → Share
 → Recipient Uses
 → Recipient Remixes / Creates
```

---

## 9. Anonymous-First Strategy

不應用 Registration 阻擋 First Value。

### Consumer
- 不登入即可開啟 shared Micro-App；
- 立即使用。

### Creator
- 在可行範圍內，不註冊也可建立與分享 ephemeral artifact。

### Progressive Authentication

當使用者要求 durable value 時再要求 identity：

- ownership；
- permanent editing；
- history；
- publishing；
- cross-device persistence；
- paid quota；
- monetization；
- payout。

這讓帳號 friction 與清楚的 user benefit 綁在一起。

Anonymous continuity 優先使用 privacy-conscious first-party identifier，不預設 fingerprinting。

---

## 10. Share 即 Distribution

NodeFF 有三種主要 distribution mode。

### Portable Snapshot
小型、公開、非敏感 Instance 透過 URL 分享。

### Durable Reference
Short Link 解析到 persistent artifact／reference。

### Live Room
多人進入同一個 temporary interactive session。

最重要的 growth property：

> **接收者不需要安裝 Creator 的 App，就能直接使用該 artifact。**

因此每一個成功 Micro-App 都可能同時是一個 distribution object。

---

## 11. Fork & Remix

Remix 應該比從空白開始更容易。

```text
Shared Blueprint
 → Open
 → Change one assumption/rule/input
 → Validate
 → New Blueprint
```

Remix 同時提供：

- 更低的 Creator friction；
- viral continuation；
- reusable structure；
- 可觀察的 preference／correction data；
- Blueprint family 形成的可能。

---

## 12. 產品品質定義

NodeFF 最大的產品風險不是 JSON 壞掉。

真正危險的是：

> **Micro-App 看起來很完整、也能操作，但其實解錯問題。**

Prototype failure history 已出現過：

- 營養需求被做成 AA 分帳；
- 午餐選擇被做成無意義算術；
- ROI Intent 被映射到不相關的 random-choice UI。

因此品質指標必須包含：

- semantic mismatch；
- unsupported semantics；
- user correction／refinement；
- successful repair；
- repeat execution；
- Blueprint family reuse。

畫面漂亮不等於產品成功。

---

## 13. Assumption 作為產品 UX

許多高價值 Intent 本來就很模糊。

NodeFF 可以把 ambiguity 轉成 editable model。

例如：

```text
「20 人公司聚餐依職級分帳」
 → visible role assumptions
 → editable counts
 → editable weights
 → scenario presets
 → result breakdown
```

Compiler 不得把模型推測的社會慣例當成事實。

這形成一種重要產品 interaction：

> **Fuzzy Intent → Explicit Assumptions → Interactive Model → User Adjustment**

---

## 14. Tier Model

### Tier 1 — Lightweight / Free-Oriented

適合：
- client-side deterministic execution；
- approved primitives；
- local rules；
- portable snapshots；
- modest ephemeral rooms；
- bounded compilation quota。

### Tier 2 — Paid / Cost-Bearing

由 durable 或高成本能力觸發，例如：
- persistent runtime AI；
- heavy external API；
- media generation；
- larger／longer realtime；
- durable cloud state；
- premium ownership／history；
- specialized paid capability。

### Tier 3 — Unsupported / Redirect

例如：
- arbitrary code execution；
- unsafe OS／system access；
- unsupported runtime capability；
- 無法安全表達核心語意的需求。

實際 entitlement／limit 尚未定案。

---

## 15. Compile-Once Economics

架構刻意把昂貴的 Semantic Compilation 與廉價的重複 execution 分開。

```text
One successful compilation
 → many local interactions
 → many opens
 → many shares
 → many remixes/reuses
```

成本主要集中在：
- initial compilation；
- semantic refinement；
- runtime-AI request；
- realtime；
- durable storage；
- external API；
- moderation／security；
- observability；
- bandwidth。

Trusted Blueprint reuse 越高，這個經濟模型越有利。

---

## 16. Reuse Economics

可能形成：

```text
More successful intents
 → more trusted Blueprint families
 → more retrieval/reuse
 → fewer cold compilations
 → lower cost + faster response
 → better UX
 → more usage
```

這是需要驗證的 business hypothesis。

Cache hit rate、cost reduction、latency 都必須量測，不可預設。

---

## 17. Creator Economics

「Everyone is the creator」代表使用者可以在不需要以下能力的情況下建立互動 artifact：

- source code；
- deployment；
- App Store Review；
- package management；
- 專門 frontend development。

潛在 creator value：
- save／publish useful Blueprint；
- reputation／discovery；
- Remix successful artifact；
- connect paid capability；
- 最終透過 usage 或 transaction monetization。

Creator monetization 是 PMF 後的擴張方向，不是 Phase 1 的先決條件。

---

## 18. Intent Commerce

長期方向：

```text
Intent
 → Capability Selection
 → Micro-App
 → API / Service / Transaction
 → Outcome
```

可能的 capability supply：
- AI service；
- data source；
- booking；
- specialized calculation；
- media generation；
- commerce／transaction API；
- paid Blueprint／capability package。

NodeFF 長期可能成為「使用者消費能力」的 orchestration 與 interaction layer，而不必關心功能原本屬於哪個傳統 App。

這仍然是 strategic hypothesis，不是已驗證 marketplace。

---

## 19. Monetization Paths

可能 revenue mechanism：

1. compiler／runtime-AI quota；
2. durable history／storage；
3. 更大或更長的 live room；
4. premium capability；
5. external API pass-through + margin；
6. Intent Commerce transaction fee；
7. creator monetization；
8. private／team environment；
9. 未來若有需求，再加入 enterprise governance。

Monetization 不得破壞 zero-friction first use。

---

## 20. Growth Model

Growth 應該是 artifact-driven，而不是 account-driven。

```text
Creator makes useful/fun artifact
 → shares it
 → recipient opens instantly
 → recipient interacts
 → recipient remixes/creates
 → new artifact
```

重要 metrics：

- share rate；
- share → open；
- open → meaningful interaction；
- interaction → remix／create；
- remix descendants per Blueprint family；
- repeat creation；
- anonymous → registered creator conversion。

K-factor 只有在其組成指標實際量測後才有意義。

---

## 21. Measurement Model

### Activation
- intent → executable Blueprint success；
- time to first useful result；
- semantic success／refinement rate。

### Engagement
- executed intents；
- meaningful Instance interactions；
- Blueprint opens；
- repeat creation；
- repeat sharing。

### Viral
- share／open／use／remix funnel；
- descendants per shared artifact；
- recipient-to-creator conversion。

### Retention
- anonymous browser／device cohort；
- registered creator cohort；
- repeat use／creation。

### Monetization
- free → paid；
- premium capability usage；
- paid creator activity；
- transaction volume／GMV（如適用）。

Anonymous identifier 不得被當成精確的人數。

---

## 22. Trust、Privacy 與 Ownership

NodeFF 可能處理私人、短暫的群組資料。

商業可行性依賴以下 trust：

- 哪些資料可以進 share URL；
- telemetry collection；
- retention；
- deletion；
- private／public Blueprint distinction；
- moderation；
- creator ownership；
- external capability data transfer；
- training／research reuse。

Anonymous usage 不代表使用者同意資料可無限制拿去 model training。

Durable artifact ownership 必須明確且經 authentication。

---

## 23. PMF 假設

NodeFF 必須驗證：

1. 對某些 Intent，使用者真的偏好 Interactive Micro-App，而不是 Chat Answer。
2. No-login access 能實質提升分享與使用。
3. 接收者會互動，而不只是看。
4. Remix 會自然發生。
5. Social／Decision／Party 類別具有 organic sharing。
6. 使用者能理解並信任 visible assumptions。
7. Semantic reliability 足以支撐 repeat use。
8. Blueprint family reuse 頻率足以產生經濟價值。
9. Progressive Auth 在產生價值後能順利轉換。
10. 使用者願意為 durable／expensive capability 付費。
11. Intent Commerce 有真實 provider／user demand。
12. Runtime economics 能支撐 generous free usage。

---

## 24. 尚未驗證的數字

以下不得當成已成立事實：

- 80% registration drop-off；
- 特定 anonymous CPUI；
- 特定 registered monthly cost；
- K-factor > 1；
- 5M monthly intents；
- 90% cache／cost reduction；
- 固定 room limits；
- exact model cost；
- zero marginal cost；
- guaranteed millisecond latency。

在 NodeFF 實際量測前，它們都只是 benchmark／hypothesis。

---

## 25. Phase 1 商業目標

Phase 1 在擴張成大平台故事之前，只需要先證明一件事：

> **一個人能否表達短暫 Intent，快速得到正確有用的 Micro-App，立即使用、分享，並讓另一個人使用或 Remix？**

最小 proof loop：

```text
Intent
 → Correct Interactive Blueprint
 → Immediate Value
 → Share
 → Recipient Use
 → Remix
```

Marketplace、Creator Economy 與更大的 Network Effect，應建立在這個 loop 的證據之上。

---

## 26. 商業 Guardrails

1. First Value 前不強制 Registration。
2. Share 是核心產品行為，不是 Export Feature。
3. Remix 必須降低 Creation Friction。
4. 既有 Blueprint execution 不應反覆消耗 LLM。
5. Semantic Correctness 比 Visual Polish 更重要。
6. Assumption 必須可見，不得假裝成事實。
7. Product Boundary 必須誠實。
8. Pricing／Cost／Performance 數字在量測前都維持 hypothesis。
9. Paid Feature 應綁定 durable value 或 expensive capability。
10. NodeFF 必須保留 Fun／Social 性質，不能退化成只有 Generic Form Builder。
