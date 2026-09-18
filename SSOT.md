# NodeFF — SSOT

> NodeFF 專案的唯一真實來源（Single Source of Truth）。

## 狀態

- 專案：NodeFF
- Repository：`NFF98/NodeFF`
- 預設分支：`main`
- 規格狀態：Initial structure

## 目的

本文件定義 NodeFF 的權威專案結構與治理規則。

## SSOT 規則

1. 產品決策記錄於 `spec/` 或 `decisions/`。
2. 執行狀態記錄於 `execution/`。
3. 不得建立平行或重複的真實來源。
4. 程式碼必須遵循已核准的規格。
5. 任何會實質改變產品行為的變更，必須先更新相關規格，再進行實作。
6. `decisions/` 記錄會實質影響架構、產品方向或限制條件的決策。
7. `execution/CHANGELOG.md` 記錄已交付或已提交的變更。
8. **專案文件預設必須使用繁體中文（Traditional Chinese / zh-Hant）撰寫。** 技術名詞、程式碼識別字、API／Schema／Protocol 名稱、檔名、套件名與產品專有名稱可保留英文，以避免語意失真。

## 文件語言規則

- 適用範圍：Repository 內的 Markdown 文件與其他面向人類閱讀的規格／設計文件。
- 預設語言：繁體中文。
- 技術術語可採「繁體中文說明 + 英文原名」或直接保留業界通用英文，例如 Blueprint、LegoSpec、Rule AST、Capability Registry。
- 程式碼、JSON、CLI 指令、API 欄位、型別名與 identifier 不翻譯。
- 若引用外部英文原文，可保留原文，但其設計結論與 NodeFF 規則必須以繁體中文表達。
- 未經明確決策，不得建立另一套不同語言的平行文件作為第二份 SSOT。

## 專案結構

```text
SSOT.md
README.md
spec/
  01-PRODUCT.md
  02-PROBLEM.md
  03-REQUIREMENTS.md
  04-USER-FLOWS.md
  05-DATA-MODEL.md
  06-SYSTEM.md
  07-API.md
  08-UI.md
  09-SECURITY.md
  10-NON-FUNCTIONAL.md
  11-ACCEPTANCE.md
decisions/
  .gitkeep
execution/
  BACKLOG.md
  SPRINT.md
  CHANGELOG.md
```

## 權威順序

1. `SSOT.md`
2. `spec/`
3. `decisions/`
4. `execution/`
5. 程式碼與測試

## 變更控制

如果預計實作的內容與目前規格衝突，必須停止實作，先修正規格或記錄明確決策後再繼續。
