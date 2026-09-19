# NodeFF Capability Fabric

> 狀態：Working / POC。本文定義 NodeFF Capability Fabric 的設計框架、Capability Card 原子契約、候選能力家族與驗證方式。現階段所有 Capability 都必須經過 Build / Test / POC Evidence 才能宣稱為可用能力。

# 1. 目的

Capability Fabric 回答兩個不同問題：

> **NodeFF 想具備哪些 App 能力？**

以及更重要的：

> **哪些能力已經真的 Build、Test，而且能可靠支撐產品核心循環？**

現階段 NodeFF 仍在 POC，因此本文中的能力清單主要代表 **Target Capability Space / Candidate Capability**，不是已驗證完成的產品能力。

Capability 不是單純 UI Component，而是 Runtime 可安全執行、Compiler 可理解、Blueprint 可引用、產品可以組合與演進的原子能力。

~~~text
Intent
 → Capability Selection
 → Composition
 → State / Rule / Event Wiring
 → Executable App
 → Use / Share / Remix
 → Evidence
~~~

Capability Fabric 必須從第一天同時服務：

~~~text
短期：證明產品核心循環
        ↓
中期：Reuse / Creator / Paid Value
        ↓
長期：Intent Commerce / Capability Network
~~~

但：

> **現在先設計得能走到未來，不代表現在就把未來功能全部做出來。**

---

# 2. Capability Card Contract — 原子層核心契約

Capability Card Contract 是 Capability Fabric 最重要的基礎。

如果原子層只描述技術 I/O，未來加入 Share、Remix、Creator、Paid、Commerce、External Provider 時，很容易反過來破壞 Runtime 與 Blueprint Contract。

因此每張 Card 從 Day 1 必須同時考慮四個面向：

~~~text
Technical Contract
      +
Product Contract
      +
Business / Ecosystem Hooks
      +
Evidence / Maturity
~~~

其中：

- **Technical Contract**：現在就必須能 Build / Validate / Execute。
- **Product Contract**：確保 Capability 不偏離 NodeFF 五個產品原則。
- **Business / Ecosystem Hooks**：先保留未來可擴張的語意與 metadata，不代表 Phase 1 實作完整商業功能。
- **Evidence / Maturity**：沒有 Build / Test / Evidence，就不能宣稱 Capability 已可靠可用。

---

## 2.1 Identity / Semantic

每張 Card 至少需要：

- Capability ID
- Name / Type
- Capability Family
- Semantic Meaning
- Intended Intent Classes
- Human-readable Description
- Compiler Selection Hints
- Version
- Compatibility

目的：

> Compiler 必須知道「什麼時候該用這張卡」，而不只是知道它有哪些 props。

---

## 2.2 Technical Execution Contract

定義 Runtime 真正可以執行的內容：

- Inputs / Outputs
- State Contract
- Actions
- Events
- Rules / Operators
- Bindings
- Dependencies
- Runtime Support
- Fallback / Degradation
- Permissions
- Security Class
- Resource Budget
- Cost Class
- Determinism / Replay requirements
- Tests

核心原則：

> Capability 只能透過受控 Contract 執行，不提供任意程式碼逃逸口。

---

## 2.3 Product Contract — 五個產品原則必須從原子層可被支援

NodeFF 的五個產品原則不是 Business Plan 最後才檢查，而要進入 Capability 設計 Gate。

### 1. No install setup

Card 要回答：

- 是否能直接在 Web / Browser 使用？
- 是否需要特殊 permission？
- 是否依賴 native install？
- permission 被拒絕時如何 degrade？
- share recipient 是否可以立即使用？

原則：

> Capability 不應讓 NodeFF 核心體驗退回「先安裝、先設定、才能用」。

### 2. Everyone is the creator

Card 要回答：

- Compiler 能否理解何時使用它？
- 使用者可調整哪些 meaningful parameters？
- 是否支援 Remix？
- 是否能安全複製與重新組合？
- 是否需要專業知識才能配置？

原則：

> Capability 不只是開發者元件，也必須能被 Intent 驅動與 Remix。

### 3. Sharable, linkable

Card 要回答：

- 哪些 state / config 可 serialization？
- 哪些資料可安全分享？
- 是否可 portable restore？
- 是否有 non-shareable / sensitive fields？
- share recipient 打開後是否能 deterministic restore？

原則：

> Shareability 必須在 Capability contract 層有明確邊界，而不是最後才補 Export。

### 4. Intent Commerce

Phase 1 不要求每張 Card 具備收費能力，但原子契約要能表達：

- Cost Class
- Entitlement Class
- External Provider requirement
- Transaction-capable flag / metadata
- Usage metering hook
- Provider / capability identity
- Policy / quota requirements

原則：

> 未來 Paid Capability / External Capability 應能掛進既有 Fabric，而不是建立第二套 Runtime。

### 5. Fun and socialable

不是每張 Card 都一定要是 Social Card，但要知道它是否能參與：

- animation / feedback；
- shared state；
- multiplayer / room；
- reaction / vote；
- score / progression；
- collaborative input；
- expressive / playful presentation。

Card 應標註：

- Social Composition Potential
- Realtime Requirement
- Feedback / Motion Hooks

目的：

> 避免 Capability Fabric 最後只剩 Text + Form + Chart，失去 NodeFF 的 Fun / Social 特性。

---

## 2.4 Reuse / Creator Contract — 為中期預留

中期商業目標是：

> **Reuse / Creator / Paid Value**

因此 Card 從原子層應可支援以下 metadata：

- Remixability
- Parameterization Surface
- Version Stability
- Backward Compatibility
- Attribution Support
- Creator-facing Configuration
- Ownership / License Class（若未來需要）
- Reuse Telemetry
- Blueprint Lineage Compatibility

這些欄位的存在不代表 Phase 1 要做 Creator Economy。

它代表：

> 如果 Phase 1 證明 Reuse / Remix 成立，我們不必重寫 Capability Contract 才能進入下一階段。

---

## 2.5 Commerce / Network Contract — 為長期預留

長期商業方向：

> **Intent Commerce / Capability Network**

因此 External / Paid Capability 未來需要能擴充：

- Provider Identity
- Provider Version
- Execution Location
- Authentication Requirement
- Pricing / Cost Metadata
- Metering
- Transaction Lifecycle
- SLA / Availability Metadata
- Trust / Certification Status
- Settlement / Revenue-share Hook
- Data Residency / Privacy Class

Phase 1 可以完全沒有第三方 Capability Provider。

但 Contract 不應假設：

> 所有 Capability 永遠都由 NodeFF 自己、免費、Client-side 執行。

---

## 2.6 Evidence / Telemetry Contract

每張 Capability 從 POC 開始都應能產生最低限度 Evidence：

- selected / not selected；
- execution success / failure；
- validation failure；
- semantic mismatch；
- user correction；
- share；
- recipient open / use；
- remix；
- reuse；
- latency；
- resource / external cost（如有）。

目的不是先建立大型 Analytics System，而是要能回答：

> **這張 Capability 真的有幫助 NodeFF 把 Intent 變成正確、有用、可分享、可 Remix 的 App 嗎？**

---

# 3. Capability Maturity — POC 階段不能把候選能力當成事實

每張 Capability 必須有明確成熟度：

~~~text
PROPOSED
   ↓
POC
   ↓
BUILT
   ↓
TESTED
   ↓
VALIDATED
   ↓
RELEASED
~~~

## PROPOSED

只有設計概念，尚未實作。

## POC

已做最小 Proof of Concept，用來確認技術可行性與組合方式。

## BUILT

已存在 Runtime implementation，但尚未完成完整驗證。

## TESTED

已通過：
- contract tests；
- runtime tests；
- security / resource tests；
- composition tests。

## VALIDATED

除了技術測試，也已有足夠產品 Evidence 顯示：
- Compiler 能合理選用；
- Semantic outcome 正確；
- 真實 Use Case 可用；
- Share / Remix 等相關行為符合預期。

## RELEASED

已被納入正式可用 Capability Registry，具有：
- stable version；
- compatibility policy；
- telemetry；
- production acceptance。

原則：

> **Build 成功 ≠ Product Validated。**

> **Render 成功 ≠ Intent 成功。**

---

# 4. Capability Families — Target Capability Space

以下是目前希望 Capability Fabric 最終能覆蓋的能力家族，不代表現在已完成。

## A. Interface / Layout
Text、Button、Card、Container、Grid、Tabs、Modal、List / Repeater、Form Controls、Navigation。

## B. Data / Visualization
Stat、Table、Chart、Timeline、Progress、Ranking、Comparison、Map、Calendar、Graph。

## C. Game / Interaction
Random、Dice、Wheel、Card / Deck、Player、Team、Turn、Round、Score、Timer、Progression。

## D. Animation / Motion
Transition、Lottie、Particle、Confetti、Timeline Animation、State-driven Motion、Gesture。

## E. Audio / Video
Image、Audio、Video、Camera、Recorder、Playlist、Subtitle、Media Cue / Timeline。

## F. 2D / 3D Spatial
2D Canvas（受控）、3D Scene、Model、Camera、Lighting、Transform、Hotspot、Object Interaction。

## G. Device / Sensor
Camera、Microphone、Location、Motion、Orientation、File、Clipboard、QR / Barcode、Haptic。

## H. Realtime / Social
Room、Presence、Shared State、Vote、Shared Score、Turn Sync、Collaborative Input、Event Broadcast。

## I. AI / External
Text / Image / Speech AI、Search、Translation、External API、Data Provider、Specialized Compute。

## J. Future Spatial / XR
WebXR、Immersive Scene、Spatial Anchor、Gaze、Controller / Hand Input、Shared Spatial State。

---

# 5. Phase Strategy

## Phase 1 — 證明產品核心循環

Capability 的第一目標不是「數量很多」，而是支援：

~~~text
Intent
 → Correct App
 → Immediate Use
 → Share
 → Recipient Use
 → Remix / Create
~~~

目前 Phase 1 Candidate Set：

- Core Layout / Form
- Text / Card / List
- Number / Text / Select / Toggle Input
- Stat / Table / Basic Chart
- Random / Dice / Wheel
- Timer / Score / Simple Turn
- Image / Audio / Video playback
- Basic Animation / Confetti
- Shareable State
- Basic Realtime Room（只有 Use Case 證明需要時）

這些目前均應視為：

> **Candidate / POC scope，不是已確認無問題的 Release Capability。**

Phase 1 的工作是 Build + Test + Evidence，逐步把真正有效的卡升級到 VALIDATED / RELEASED。

---

## Middle Term — Reuse / Creator / Paid Value

只有 Phase 1 核心循環成立後，才逐步啟用：

- stable reusable Capability families；
- richer parameterization；
- creator-facing configuration；
- attribution / ownership；
- premium capability；
- runtime AI；
- larger realtime；
- durable state；
- reuse / lineage intelligence。

中期重點不是重做底座，而是利用 Phase 1 已留下的原子 Contract。

---

## Long Term — Intent Commerce / Capability Network

只有供需與使用證據成立後才進入：

- External paid capabilities；
- certified third-party providers；
- Booking / Payment / Commerce；
- Data / AI providers；
- provider metering；
- entitlement；
- transaction lifecycle；
- marketplace / network。

原則：

> Capability Network 是未來 Fabric 的擴張模式，不是 Phase 1 要先建的 Marketplace。

---

# 6. Capability Density

Capability 的價值不看數量，而看：

> **少量通用能力能組成多少有用 App。**

優先加入的 Capability 應具備：

1. 能服務多種 Intent；
2. 能與其他 Capability 高度組合；
3. Semantic Meaning 清楚；
4. Runtime 可安全執行；
5. Compiler 能正確選擇；
6. 支援 NodeFF 核心 Share / Remix 路徑；
7. 可測試、可版本化；
8. 不阻斷中期 Reuse / Creator 發展；
9. 不把未來 Paid / External Capability 鎖死；
10. 能產生足夠 Evidence 判斷是否值得留下。

---

# 7. Composition 原則

所有 Capability 應盡量共用統一模型：

~~~text
State
Action
Event
Rule
Permission
Wiring
Evidence
~~~

例如：

~~~text
Player
 + Wheel
 + Timer
 + Score
 + Sound
 + Animation
~~~

可以形成 Party Game。

~~~text
Photo
 + Timeline
 + Music
 + Animation
 + Quiz
~~~

可以形成 Sentimental / Creative App。

未來：

~~~text
Product
 + Search
 + Availability
 + Payment
 + Map
~~~

可能形成 Commerce App。

這三者應盡量使用同一套 Capability composition grammar，而不是三套不同 Runtime。

---

# 8. 新增 Capability 的 Gate

新增 Capability 前必須回答四組問題。

## Product Fit

1. 哪些真實 Intent 需要它？
2. 是否幫助 Create → Use → Share → Remix？
3. 是否符合 NodeFF 五個產品原則？
4. 是否具有足夠通用性，而不是單一 App Template？

## Technical Fit

5. 現有 Capability 為何無法合理組出？
6. Contract 是否能清楚定義？
7. Security / Permission / Resource 是否可控制？
8. Runtime 是否能 deterministic / bounded execution？

## Future Fit

9. 是否可 Remix / Reuse？
10. 是否會阻斷 Creator / Paid Value？
11. 若未來成為 External / Paid Capability，現有 Contract 是否可延伸？
12. 是否能維持同一套 Runtime / Registry 模型？

## Evidence

13. POC 要驗證什麼？
14. Build / Test acceptance 是什麼？
15. 哪些 telemetry 才能知道它真的有效？
16. 什麼條件才能從 POC 升為 RELEASED？

---

# 9. Capability Card 建議結構

未來每張具體 Card 可依此格式設計：

~~~text
Capability
├─ Identity / Semantic
├─ Technical Contract
│  ├─ Input / Output
│  ├─ State
│  ├─ Action / Event
│  ├─ Rule / Binding
│  └─ Runtime / Security / Resource
│
├─ Product Contract
│  ├─ No-install
│  ├─ Creator / Remix
│  ├─ Share / Restore
│  └─ Fun / Social
│
├─ Business / Ecosystem Metadata
│  ├─ Cost / Entitlement
│  ├─ Provider
│  ├─ Metering
│  └─ Commerce hooks
│
├─ Evidence
│  ├─ Telemetry
│  ├─ Success / Failure
│  └─ Semantic Feedback
│
└─ Maturity
   ├─ PROPOSED
   ├─ POC
   ├─ BUILT
   ├─ TESTED
   ├─ VALIDATED
   └─ RELEASED
~~~

這個結構的目的，是讓 Capability 從 POC 到 Platform 都使用同一個概念模型，但各階段只實作當下真正需要的部分。

---

# 10. 與其他文件的關係

- `working/APP-ARCHITECTURE.md`：定義 Capability 在四層架構中的位置。
- `working/APP-DETAILED-DESIGN.md`：安排 Capability 相關 Function 的具體實作與 Release。
- `working/functions/`：描述實際 Function 如何使用 Capability。
- `working/TECHNICAL-MOAT.md`：說明 Capability Fabric 如何逐步形成技術優勢。
- `working/ProjectManagement/BUSINESS-PLAN.md`：定義 Capability Fabric 必須支援的產品原則與商業發展順序。

本文件是 Capability 的設計總表與驗證框架，不取代個別 Capability / Function 詳細設計。
