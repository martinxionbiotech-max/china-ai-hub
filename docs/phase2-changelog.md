# China AI Hub — Phase 2 变更日志（phase2-changelog）

**日期**：2026-09-27 · **验证方式**：官方源核实 + build + RE-SCAN

---

## 主站（china-ai-hub）

| File | Problem | Change | Source | Verification |
|---|---|---|---|---|
| `src/content/models/qwen3.7-plus.md` | pricing 库引用无实体的模型 | **新增实体页**（等价 qwen3.7-plus-2026-05-26，国际/北京双区价格，其余字段标注 not publicly documented）| alibabacloud.com model-pricing | 2026-09-27 curl 200 |
| `src/content/models/glm-5.3-flashx.md` | pricing 库引用无实体的模型 | **新增实体页**（独立计费 SKU，$0.37/$1.25，与 Flash $0.15/$0.50 区分）| docs.z.ai pricing | 2026-09-27 curl 200 |
| `src/content/models/glm-5.3-flash.md` | FlashX 错误地作为 alias 混入 Flash 实体 | 清理 alias（glm-5.3-flashx/GLM-5.3-FlashX），version: FlashX → Flash | Z.ai 官方导航「Flash/FlashX」为两个 SKU | 2026-09-27 |

## Data Hub（china-ai-hub-data）

| File | Problem | Change | Source | Verification |
|---|---|---|---|---|
| `docs/models/glm-5.3-flash.md` | Version=FlashX + Aliases 含 flashx + limitation 提及 FlashX | 清理全部 FlashX 混用，Version → Flash | 同主站 | 2026-09-27 |
| `docs/models/qwen3.7-plus.md` | 缺实体 | **新增**（JSON-LD @id 锚定主站 + 价格章节 + 诚实 Known Limitations）| 官方定价页 | 2026-09-27 |
| `docs/models/glm-5.3-flashx.md` | 缺实体 | **新增**（同上结构）| Z.ai 定价页 | 2026-09-27 |

## 审计结论

| 项 | 结果 |
|---|---|
| Pages reviewed | 主站 116 页（build 输出）+ Data Hub 全模型集 |
| Pages modified | 主站 3 文件、Data Hub 3 文件 |
| Data conflicts fixed | 2（均为 pricing↔model 引用缺口）|
| Source issues fixed | 0（全部行已有官方源）|
| Schema issues fixed | 0（RE-SCAN 验证通过）|
| Orphan pages fixed | 0（检查为 0 孤儿）|
| Remaining issues | P2 可选改进（technology 深化、comparison 差异绑源、research 分段标记）|
| Recommended next phase | GSC 数据积累后做 query-driven 长尾页；历史价格数据积累后启用 price history 展示 |
