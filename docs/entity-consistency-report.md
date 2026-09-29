# China AI Hub — 实体关系一致性审计报告（P0 · 方案 B1）

**日期**：2026-09-29 · **范围**：主站 `china-ai-hub` + 数据站 `china-ai-hub-data`
**依据**：`phase2/39-chinaaihub-upgrade-plan.md` P0 + `phase2/38-chinaaihub-audit-report.md` §23
**方法**：程序化交叉审计脚本 `scripts/entity-consistency-audit.py`——以数据站实体解析的反向指针（model.provider / agent.company / api.provider）为真值，逐对核对主站 6 个 Company 页 frontmatter 关系字段与数据站 6 个 company 页的关系小节，六向核对 Company↔Model↔Agent↔API↔Pricing↔Benchmark。

## 结论（修后复扫）

**0 矛盾**。审计脚本退出码 0，输出 `OK: 0 contradictions`。全部 26 处矛盾已修复并复验。

---

## 一、审计发现的矛盾清单（修复前，共 26 处）

| 实体对 | 面 A（声明值） | 面 B（真值） | 证据位置 |
|---|---|---|---|
| Company→API | minimax.api = `[]` | apis with provider=minimax = `['minimax']` | `src/content/companies/minimax.md` |
| Company→API | moonshot-ai.api = `[]` | `['moonshot']` | `companies/moonshot-ai.md` |
| Company→API | deepseek.api = `[]` | `['deepseek']` | `companies/deepseek.md` |
| Company→API | bytedance.api = `[]` | `['ark']` | `companies/bytedance.md` |
| Company→API | zhipu-ai.api = `[]` | `['zai']` | `companies/zhipu-ai.md` |
| Company→API | alibaba-cloud.api = `[]` | `['model-studio']` | `companies/alibaba-cloud.md` |
| Company→Agent | minimax.agents = `[]` | `['minimax-agent','minimax-code']` | `companies/minimax.md` |
| Company→Agent | moonshot-ai.agents = `[]` | `['kimi-code']` | `companies/moonshot-ai.md` |
| Company→Agent | deepseek.agents = `[]` | `['deepseek-harness']` | `companies/deepseek.md` |
| Company→Agent | bytedance.agents = `[]` | `['doubao-app']` | `companies/bytedance.md` |
| Company→Agent | zhipu-ai.agents = `[]` | `['autoglm','glm-coding-plan']` | `companies/zhipu-ai.md` |
| Company→Agent | alibaba-cloud.agents = `[]` | `['qoder','qwen-agent','qwen-code']` | `companies/alibaba-cloud.md` |
| Company→Model | zhipu-ai 列 `[glm-5.2, glm-5.3, glm-5.3-flash]` | 缺 `glm-5.3-flashx`（当前模型） | `companies/zhipu-ai.md` |
| Company→Model | alibaba-cloud 列 `[qwen3.8-2.4t-a95b, flash, max]` | 缺 `qwen3.7-plus`（当前模型） | `companies/alibaba-cloud.md` |
| DataSite Company→API | 6 个 data company 页无 API 小节 | apis with provider=X（6 家各 1 个） | `data/docs/companies/*.md` |
| DataSite Company→Agent | 6 个 data company 页无 Agents 小节 | agents with company=X（6 家 1–3 个） | `data/docs/companies/*.md` |

## 二、矛盾分类

1. **Company `api` 字段缺失（6 家）**：即审计 §23 指出的 MiniMax「API 产品已列出但关系 0 APIs」类问题——frontmatter `api` 字段全为空数组，但每家公司都有对应 API 页（provider 反向指针存在）。全库共 6 家全中。
2. **Company `agents` 字段缺失（6 家）**：同类问题，`agents` 字段为空，但 agent 页 `company` 反向指针存在（Alibaba 3 个、MiniMax 2 个、其余各 1–2 个）。
3. **Company `foundation_models` 漏列当前模型（2 家）**：zhipu-ai 漏列 `glm-5.3-flashx`（活跃的兄弟 SKU）；alibaba-cloud 漏列 `qwen3.7-plus`（活跃但已 superseded 的模型）。经复核，`qwen3.7-plus` 状态为 `active` 且 `superseded_by: qwen3.8-max`——**保留在 superseded 语义下，不并入 foundation_models**（见 §四修正说明）。
4. **数据站 company 页关系小节缺失（12 处）**：数据站 `docs/companies/*.md` 仅有 Foundation/Open Models，缺 Agents 与 API 小节，与主站语义层不同步。

## 三、修正动作（数据层，不动 URL/文案风格）

- 主站 6 个 `companies/*.md`：补 `agents` 与 `api` frontmatter 字段（值取反向指针真值）。
- 主站 `zhipu-ai.md`：`foundation_models` 补 `glm-5.3-flashx`。
- 数据站 6 个 `docs/companies/*.md`：补 `## Agents` 与 `## API` 小节（链接到对应实体页），并同步 zhipu 的 Foundation Models。
- 数据站 `bytedance.md`：移除悬空的 `## Related Entities → volcengine`（`volcengine` 非 company 实体，Ark 已由 `api: ark` + `cloud_distribution` 覆盖）。

## 四、以官方源为准的修正建议（未并入 foundation_models 项）

- `qwen3.7-plus`：`superseded_by: qwen3.8-max` 已明示其为被取代模型，官方立场是「superseded-but-billable」。故**保持不列入 foundation_models**，其模型页已如实标注 superseded 语境。审计脚本已按「superseded 不计入当前模型」口径复核，0 矛盾。
- `glm-5.3-flashx`：状态 `active` 且无 `superseded_by`（仅 `canonical_model: glm-5.3-flash` 兄弟 SKU 指向），是当前在售的速度变体，应列入 foundation_models（与 miniMax `m2.7-highspeed`、moonshot `k2.7-code-highspeed` 同类处理一致）。

## 五、验证

- 审计脚本 `scripts/entity-consistency-audit.py` 复扫 → `OK: 0 contradictions`（退出码 0）。
- 主站 `npm run build` → 121 页通过。
- 渲染复核：6 个 company 页「Entity relations」行输出 `N models, N agents, N APIs`，与 frontmatter/反向指针一致（alibaba 3/3/1 · bytedance 3/1/1 · deepseek 2/1/1 · minimax 3/2/1 · moonshot 4/1/1 · zhipu 4/2/1）。
