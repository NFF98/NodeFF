# NodeFF Acceptance / Test Contract Conventions

> 狀態：BUILD_FREEZE_READY / Phase 1 — Working Current Truth。
> Legacy Formal Spec reference：RETIRED / NO-USE；Build implementation snapshot 改由 Human-approved Build Freeze → NFFBuild BS-*。
> Canonical Role：把 Fxx Acceptance Criteria 轉成可實作、可測試、可追蹤的 Test Contract。

# 1. Core Rule

Acceptance 是產品/Function 的 observable truth；Test 是驗證方式。

每個 Required Acceptance 必須有至少一個 stable Test Contract：

~~~text
Acceptance ID
→ Test ID
→ verification type
→ fixture / setup
→ expected observable
→ implementation location
~~~

Test 不重新發明產品行為。

# 2. Verification Types

~~~text
AUTOMATED_CONTRACT
= API / Data / Security / Schema / Runtime boundary contract

AUTOMATED_BEHAVIOR
= deterministic Function behavior / policy

AUTOMATED_E2E
= Browser / UX / interaction flow

RUNTIME_EVIDENCE
= event stream / production-like evidence assertion

MANUAL_REVIEW
= 只有不適合可靠自動化的 copy / qualitative review
~~~

MANUAL_REVIEW 必須是例外，不得用來逃避可自動化 contract。

# 3. Working Registry

~~~text
working/registries/acceptance-test-registry.json
~~~

Registry 是 machine-readable mapping；Acceptance meaning仍由各 Fxx 擁有。

# 4. Implementation Rule

BUILD_FREEZE_READY 代表 Product Design / Acceptance contract 已足夠進 Build Freeze Review，不代表 implementation 或 test 已完成。

Implementation 階段 Cursor：

1. 依 implementation_location 建立 test artifact。
2. 不改 expected_observable 來配合 code。
3. 若測試發現 Spec矛盾，回 Design/Spec，不自行修改 contract。
4. IMPLEMENTED 之後，Required tests通過才可標 TESTED。

# 5. Runtime Evidence

RUNTIME_EVIDENCE test 必須：

- 使用 F07 registry-valid event；
- 明確 aggregation / success definition；
- 不以單次 click當 outcome；
- 不要求敏感 raw payload。

# 6. Manual Review

Manual test artifact至少記：

~~~text
setup
steps
expected observable
reviewer
result
evidence reference
~~~

# 7. Traceability

CI / review至少檢查：

- every Required AC has registry entry；
- Test ID unique；
- implementation_location unique；
- verification_type valid；
- expected_observable non-empty；
- deprecated AC不可被新 Test重用。

# Conclusion

Working Design完成 Acceptance meaning；Test Contract讓 Implementation知道「怎麼證明它真的完成」。
