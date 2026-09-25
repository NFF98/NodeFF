# NodeFF Decision Candidates

> 狀態：ACTIVE DECISION GATE LIST — **NOT SSOT**
>
> 用途：只記錄「已有兩個以上合理方案，而且必須由 Human 做產品／架構選擇」的尚未決決策。

# Current Decision Gates

**NONE**

目前沒有尚未決定、會阻擋 Phase 1 Build Freeze 的 Architecture / Contract / Compatibility Decision Gate。

## 2026-09-25 Cleanup

以下舊 Decision 已確認為 resolved，因此不再列為 Active：

- DC-001 Rule Representation  
  → 已由 F02 / F03 固定為 pure typed Expression AST / Rule VM；不允許 free-form expression string。

- DC-002 Capability Registry Source Format  
  → 已由 F04 / Capability Fabric 固定為 One Canonical Versioned Source → deterministic generated Compiler / Validator / Runtime / Compatibility artifacts。

完整 proof：
- `archive/ProjectManagement/SHADOW-TRUTH-AUDIT-2026-09-25.md`

## Rules

1. 已決定的內容必須進 canonical Working owner，不得長期留在本檔。
2. 需要真實 usage / benchmark 才能回答的問題放 `OPEN-QUESTIONS.md`。
3. 純 implementation detail 不建立 Product Decision Gate。
4. Build Freeze 前：
   - unresolved blocking decision = 0
   - approved-but-unsynced decision = 0
