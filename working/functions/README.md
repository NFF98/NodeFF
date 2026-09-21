# NodeFF Function Designs

此目錄是 NodeFF **單一 Function 詳細設計的 canonical home**。

~~~text
APP-DETAILED-DESIGN-OVERVIEW.md
→ Portfolio / Dependency / Release / Status Index

working/functions/Fxx-*.md
→ 該 Function 唯一的 end-to-end detailed design
~~~

每份 Fxx 最終應完整描述 User Outcome、Flow、UI/UX、Frontend State、Data/DB、API、Backend/Runtime、Capability Dependencies、Error/Recovery、Security/Permission、Telemetry/Evidence、Acceptance/Test、Dependency/Compatibility、Release/Migration。

規則：

1. APP-DETAILED-DESIGN 不再複製 Function 級詳細內容。
2. Fxx 若改 shared Data / Architecture / Capability boundary，必須回 shared canonical contract Review。
3. DRAFT / DEFERRED_BASELINE 只是已搬入 Current Truth，不代表 SPEC_READY。
4. F02 / F03 / F04 已有 WORKING_BASELINE；其他 Function 後續逐步深化。
5. Cursor 只能依 approved Spec 實作，不以 Portfolio 摘要取代 Fxx contract。

共同 Delivery 規則：`../DESIGN-TO-DELIVERY.md`

Portfolio / Dependency / Release Scope：`../APP-DETAILED-DESIGN-OVERVIEW.md`
