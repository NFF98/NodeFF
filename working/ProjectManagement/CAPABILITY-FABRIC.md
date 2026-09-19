# NodeFF Capability Fabric

> 狀態：Working。本文是 NodeFF 引擎底座能力的總表與設計入口；具體 Card Contract 會隨 Function Design 持續補充。

# 1. 目的

Capability Fabric 回答一個核心問題：

> **NFF 引擎目前到底能做什麼 App？**

Capability 不是單純 UI Component，而是 Runtime 可安全執行、Compiler 可理解、Blueprint 可引用的能力卡。

~~~text
Intent
 → Capability Selection
 → Composition
 → State / Rule / Event Wiring
 → App
~~~

---

# 2. Capability Card Contract

每張 Capability Card 最終至少定義：

- Name / Type
- Semantic Meaning
- Inputs / Outputs
- State Contract
- Actions
- Events
- Rules / Dependencies
- Permissions
- Security Class
- Resource / Cost Class
- Runtime Support
- Fallback
- Version / Compatibility
- Telemetry
- Tests

Card 只有完成 Contract + Runtime + Validation + Tests，才算真正可用。

---

# 3. Capability Families

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

# 4. Phase 分層

## Phase 1 — Foundation

優先建立高組合密度、可快速驗證 Idea-to-App 的能力：

- Core Layout / Form
- Text / Card / List
- Number / Text / Select / Toggle Input
- Stat / Table / Basic Chart
- Random / Dice / Wheel
- Timer / Score / Simple Turn
- Image / Audio / Video playback
- Basic Animation / Confetti
- Shareable State
- Basic Realtime Room（若 Use Case 驗證需要）

Phase 1 不追求完整 Game Engine、3D Engine 或 XR Runtime。

## Short-Term Expansion

由真實 Unsupported Intent 決定優先順序：

- Card / Deck / Player / Team
- Rich Timeline
- Camera / Recorder
- Map / Calendar
- Rich Animation
- Controlled 3D Scene
- More Realtime primitives
- Approved runtime AI

## Long-Term

- Rich 3D interaction
- AR / VR / XR
- Device / Sensor expansion
- External paid capabilities
- Third-party Capability Provider
- Capability Marketplace / Network

---

# 5. Capability Density

Capability 的價值不看數量，而看：

> **少量通用能力能組成多少有用 App。**

優先加入的 Capability 應具備：
1. 多 Intent 可重用；
2. 可與其他 Capability 組合；
3. Semantic Meaning 清楚；
4. Runtime 可安全執行；
5. Compiler 能正確選擇；
6. 可測試、可版本化。

---

# 6. Composition 原則

所有 Capability 應盡量共用統一模型：

~~~text
State
Action
Event
Rule
Permission
Wiring
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

可以形成 Party Game；

~~~text
Photo
 + Timeline
 + Music
 + Animation
 + Quiz
~~~

可以形成 Sentimental / Creative App。

Capability Fabric 的價值在「可組合」，不是單一卡片功能。

---

# 7. 新增 Capability 的 Gate

新增 Capability 前必須回答：

1. 哪些真實 Intent 需要它？
2. 現有能力為何無法合理組出？
3. 它是否是通用能力，而不是單一 App Template？
4. Contract 是否可清楚定義？
5. Security / Permission / Cost 是否可控制？
6. 是否能加入 Runtime Test 與 Compatibility Policy？
7. 是否提升 Capability Density？

---

# 8. 與其他文件的關係

- `APP-ARCHITECTURE.md`：定義 Capability 在四層架構中的位置。
- `APP-DETAILED-DESIGN.md`：安排哪些 Capability / Function 進入實作與 Release。
- `working/functions/`：描述具體 Function 如何使用 Capability。
- `TECHNICAL-MOAT.md`：說明 Capability Fabric 如何逐步形成技術優勢。

本文件是「能力總表」，不取代 Function 詳細設計。
