# appf2 Working Registries

> **CURRENT AUTHORITY：appf2 Working machine-readable Product Design contracts**

本目錄維護：
- `recovery-registry.json`
- `evidence-event-registry.json`
- `acceptance-test-registry.json`

規則：

1. Registry 必須對應 canonical Working Function / Shared contracts。
2. Registry 不得自行發明產品語意。
3. Stable ID 不重用；superseded / deprecated 必須保留 traceability。
4. Build Freeze 時，approved registry snapshot 隨其他 Working truth 一起投影到 `appf2/appf2-build/build-spec/baselines/BS-*`。
5. 舊 `spec/shared/*-REGISTRY.json` promotion 模型已 **RETIRED / NO-USE**。
