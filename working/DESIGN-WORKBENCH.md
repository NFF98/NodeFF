# NodeFF Design Workbench

> 狀態：Working Discussion Buffer  
> 用途：暫存目前正在收斂中的產品／商業／架構觀點。  
> 規則：本文件不是正式 SSOT；在使用者明確說 `sync` 前，不自動同步到其他 Working Docs、`spec/` 或 `decisions/`。

---

## 目前主題：Anonymous-First 與中期 Reuse / Identity 的銜接

### 問題

目前 Business Plan 有一個邏輯缺口：

短期強調 **No Registration**，但如果同時沒有 Usage Record、Anonymous Identity 與 Blueprint Lineage，就無法支撐中期的：

- Trusted Blueprint Reuse
- Creator Identity
- Blueprint Ownership
- Share / Remix Funnel
- Semantic Reliability Learning
- Anonymous → Registered Conversion

因此：

> **No Registration ≠ No Usage Record**

---

## 建議模型

### 短期：Anonymous Identity + Evidence Collection

短期不強制註冊，但從 Day 1 就建立 privacy-conscious anonymous product identity 與最小必要 telemetry。

候選識別：

- `anonymous_id`
- `session_id`
- `intent_id`
- `blueprint_id`
- `instance_id`
- `share_id`
- `parent_blueprint_id`

用來追蹤：

```text
Intent
 → Blueprint
 → Use
 → Share
 → Recipient Open
 → Recipient Use
 → Remix
```

因此 Phase 1 已經可以量測：

- Share Rate
- Share → Open
- Open → Use
- Use → Remix
- Repeat Creation
- Semantic Mismatch
- Blueprint Reuse

---

### 中期：Account Identity + Trusted Reuse + Creator Value

中期不是才開始建立 Identity，而是把既有 Anonymous Identity 升級成 Account Identity。

```text
anonymous_id
 → durable value requested
 → authenticate
 → ownership claim
 → user_id
```

可銜接：

- 先前建立的 Blueprint
- Remix History
- Saved Artifact
- Creator Ownership
- Durable History
- Paid Capability

---

## 關鍵修正

Business Plan 的階段描述應調整為：

### 短期
**Anonymous Identity + Measurement + Evidence Collection**

目的：
- 不阻擋 First Value；
- 但完整保留 PMF 與中期所需的產品證據。

### 中期
**Account Identity + Trusted Reuse + Creator Value**

目的：
- 將已累積的匿名使用證據轉成可重用、可擁有、可保存、可付費的產品層。

### 長期
**Intent Commerce + Capability Network**

---

## 目前原則

1. No Registration 不等於 No Tracking。
2. Anonymous tracking 必須 privacy-conscious，避免預設 fingerprinting。
3. Phase 1 就開始收集 Reuse / Share / Remix / Failure Evidence。
4. 中期主要是「利用已累積的 Evidence」，不是中期才開始收集。
5. Anonymous → Account 必須有 ownership claim / migration 機制。
6. 只收集產品所需的最小資料，不把 Anonymous Usage 視為 unrestricted training consent。

---

## 待同步文件

等使用者說 `sync` 後，再評估同步到：

- `working/BUSINESS-PLAN.md`
- `working/APP-ARCHITECTURE.md`
- `working/INFRA-ARCHITECTURE.md`
- `working/TECHNICAL-MOAT.md`
