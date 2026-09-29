# China AI Hub — Phase 2 Change Log（B4 P3 Research 原创 4 篇）

**日期**：2026-09-29 · **范围**：主站 `china-ai-hub`（src/content/research/ 新增 4 篇原创研究）
**依据**：`phase2/39-chinaaihub-upgrade-plan.md` P3（§11/§28 原创模式）+ `phase2/38-chinaaihub-audit-report.md` §10/§11/§5
**验证方式**：零编造（全部数值取自站内已刊载事实——data 站 JSON/主站实体页/research 既有，查不到如实写 uncertainty）· 每篇 ≥3 处「China AI Hub analysis indicates」主观判断且每判断前有证据链 · `npm run build` 125 页通过（新增 4 页）· 内链逐条 grep 核对目标存在

## 新增 4 篇原创 Research（P3 原创模式）

| Slug | 词数 | 原创观点数 | 数据锚点 | 来源数 | 核心原创观点 |
|---|---|---|---|---|---|
| `how-chinese-ai-api-pricing-has-changed` | 1,958 | 3 | price_history 5 条 + 6 家价格锚点 + 订阅产品价 | 8 | 价格战从 DeepSeek 触发→行业转订阅/阶梯定价的结构性迁移 |
| `china-ai-agent-ecosystem-structure-and-gaps` | 1,857 | 3 | 10 agent 实体 + B2-a 字段（underlying model/platform/MCP） | 8 | 中国 agent 高度依赖自有模型厂商、跨模型中立 agent 稀缺（仅 Qwen Code/Qoder 两家，均为阿里） |
| `open-weight-vs-api-economics-in-china` | 1,847 | 3 | Qwen A95B 开源案例 + 价格锚点 + 许可触发点 | 6 | 开源权重=对冲 API 锁定的营销资产（保真度缺口是策略） |
| `china-ai-coding-models-the-agent-led-race-2` | 1,881 | 3 | Terminal-Bench 2.1/3.0 分裂 + SWE-bench 三变体 + DeepSWE/AutomationBench | 7 | coding benchmark 方法学分歧使「最强编程模型」宣称不可验证 |

每篇结构：Research Question → Methodology → Evidence → Data → Analysis → Counterpoints/Limitations → China AI Hub Interpretation（主观观点）→ Conclusion → Sources；四层标签（Official fact / Vendor-reported / Third-party / China AI Hub analysis）贯穿；不写「Best」类断言。

---

# China AI Hub — Phase 2 Change Log（B3 Data Hub 八要素 + 首页 China AI Market at a Glance）

**日期**：2026-09-29 · **范围**：数据站 `china-ai-hub-data`（59 实体页）+ 主站 `china-ai-hub`（首页）
**依据**：`phase2/39-chinaaihub-upgrade-plan.md` P2（§13-15 防薄页 + §2 首页）+ `phase2/38-chinaaihub-audit-report.md` §2/§15
**验证方式**：零编造（Definition/Key facts 全部从页内既有字段合成，名称从目标页 H1 解析）· 数据站 `mkdocs build --clean` 通过（含 git-revision-date-localized 插件自动注入 dateModified）· 主站 `npm run build` 121 页通过 · dist grep 确认八要素/Glance 区块渲染

## A · Data Hub 八要素补全（§13-15 防薄页）

对 6 集合全部 59 个实体页（models 21 / companies 6 / agents 10 / apis 6 / pricing 6 / benchmarks 10）补齐八要素，**缺哪补哪，不重写正文**：

1. **Entity definition**（一句话）→ 全部实体页新增 `## Definition`（agent/benchmark 原有 `## Description` 保留，不再重复加）
2. **Key facts**（3-6 条）→ 全部实体页新增 `## Key facts`
3. **Relationships / Related entities** → 既有 `Provider`/`Related Agents`/`Foundation Models`/`Underlying Models`/`API Platform`/`Relevant Models` 等小节承载，本批未重写
4. **Evidence** → 既有 `Sources` 表承载
5. **Source history** → 有据的保留（models release_history 4 页 / pricing price_history 6 页 / companies timeline 6 页）；无据的实体页新增诚实标注 `## Source history`：`No documented source-change events located as of <last_verified>`（43 页：models 17 + agents 10 + apis 6 + benchmarks 10）
6. **Update date** → 新增 `mkdocs-git-revision-date-localized-plugin`（requirements.txt + mkdocs.yml），从 git 历史自动注入 `dateModified`（勿手写死）；移除 pricing/benchmarks JSON-LD 内 16 处硬编码 `dateModified`
7. **Related entities** → 见 #3
8. **Canonical main-site link** → 全部实体页已有；本批修复 2 处悬空 canonical（`glm-5.3-flashx`→`glm-53-flashx`、`qwen3.7-plus`→`qwen37-plus`，含 JSON-LD `@id`/`url` 同步）

| 集合 | 页数 | Definition 新增 | Key facts 新增 | Source history 标注 |
|---|---|---|---|---|
| models | 21 | 21 | 21 | 17 |
| companies | 6 | 6 | 6 | 0（6 页全有 timeline）|
| agents | 10 | 0（已有 Description）| 10 | 10 |
| apis | 6 | 6 | 6 | 6 |
| pricing | 6 | 6 | 6 | 0（6 页全有 price_history）|
| benchmarks | 10 | 0（已有 Description）| 10 | 10 |
| **合计** | **59** | **39** | **59** | **43** |

辅助脚本 `scripts/b3_eight_elements.py` 新增（可复跑，幂等：先剥离旧块再重插）。

## B · 主站首页 China AI Market at a Glance（§2）

首页新增 `## China AI Market at a Glance` 计数区块，9 项计数**全部从 Astro collection 运行时读取**（`models/companies/agents/apis/pricing/benchmarks.length` + 3 项派生计数 `open_weight===true` / `context_window>=1_000_000` / `capabilities.vision===true`），零硬编码数字；每项链接到对应列表页（`/models/`、`/companies/`、`/agents/`、`/api/`、`/pricing/`、`/benchmarks/`，派生项链接 `/models/`）。

| 计数项 | 当前值 | 链接 |
|---|---|---|
| Models tracked | 21 | /models/ |
| Companies tracked | 6 | /companies/ |
| AI agents tracked | 10 | /agents/ |
| API platforms | 6 | /api/ |
| Pricing providers | 6 | /pricing/ |
| Benchmarks tracked | 10 | /benchmarks/ |
| Open-weight models | 12 | /models/ |
| 1M-context models | 11 | /models/ |
| Multimodal models | 10 | /models/ |

## 审计结论

| 项 | 结果 |
|---|---|
| 实体页改动 | 59（Definition 39 + Key facts 59 + Source history 43 + canonical 修复 2）|
| 新增基础设施 | 1（git-revision-date-localized 插件）+ 1 辅助脚本 |
| Fabricated data | 0（全部要素从页内既有字段合成）|
| 数据站 build | mkdocs build --clean 通过（dateModified 自动注入 2026-09-28）|
| 主站 build | 121 页通过 |

---

# China AI Hub — Phase 2 Change Log（B2-b Answer Blocks 标准化 + Where this model fits 负载表）

**日期**：2026-09-29 · **范围**：主站 `china-ai-hub`（20 页）
**依据**：`phase2/39-chinaaihub-upgrade-plan.md` P1 后两件套（§17/§5）+ `phase2/38-chinaaihub-audit-report.md` §5/§17
**验证方式**：增量插入（不重写正文）· `npm run build` 121 页通过 · dist grep 确认负载表/五段块渲染 · 负载表判定仅取页内既有事实（零编造）

## A · Answer Blocks 标准化（§17）

20 个已深化页（8 核心模型 + 6 对比 + 6 公司）统一五段块：Short answer → Key facts → What this means → What is uncertain → Sources。前三段已由既有答案前置块承载（模型/公司页 `**What it is / Key characteristics / Why it matters**` 粗体块 + 对比页 `At a glance` 表 + `Why each difference matters` 节），本批**增量补缺两段**：`## What is uncertain`（明确未知/未公开项，逐页从页内既有 `known_limitations` + 正文「not publicly disclosed」提取，不编造）+ `## Sources`（页内既有来源列表，链接沿用 frontmatter `sources` 的 source_url）。格式统一（小标题一致），保留全部既有内容与内链。

| 段 | 覆盖 | 说明 |
|---|---|---|
| Short answer | 20/20（既有） | 答案前置块「What it is」/对比页导语 |
| Key facts | 20/20（既有） | 「Key characteristics」/对比页 At a glance 表 |
| What this means | 20/20（既有） | 「Why it matters」/Why each difference matters |
| What is uncertain | 20/20（本批新增） | 0→20 页 |
| Sources | 20/20（本批新增） | 0→20 页（答案块内来源列表，与模板底部 SourceBadge 区并存） |

## B · Where this model fits 负载表（§5）

8 核心模型页各补 `## Where this model fits` 表：Workload | Relevance（High / Moderate / Unknown / No evidence），8 维固定：long-context analysis / coding / structured API workflows / agent orchestration / local-self-hosted deployment / GUI automation / video generation / enterprise cloud。**只按页内既有事实判定**（如页内无 GUI 证据 → No evidence；无 self-hosting → No evidence）。表后附一句「Relevance judgments are China AI Hub analysis based on documented capabilities, not vendor claims.」。无 Best overall 排名。

维度分布（8 页 × 8 维 = 64 格）：

| 判定 | 计数 | 占比 |
|---|---|---|
| High | 35 | 54.7% |
| Moderate | 11 | 17.2% |
| No evidence | 18 | 28.1% |
| Unknown | 0 | 0% |

**No evidence 集中维度**：video generation 8/8（8 页均非视频生成模型）、GUI automation 7/8（仅 Doubao 有 computer-use 证据）。**Unknown 0 格**——所有维度均有页内事实可判定（无「查不到」的悬空格）。

辅助脚本 `scripts/b2b_insert.py` 新增（一次性插入，可复跑校验）。

---

# China AI Hub — Phase 2 Change Log（B2-a 公司页 Entity Hub + Agent 字段深化）

**日期**：2026-09-29 · **范围**：主站 `china-ai-hub` + 数据站 `china-ai-hub-data`
**依据**：`phase2/39-chinaaihub-upgrade-plan.md` P1 前两件套 + `phase2/38-chinaaihub-audit-report.md` §7/§12
**验证方式**：先 grep 确认站内实体 slug 存在再落链接（0 虚构页）· 主站 `npm run build` 121 页通过 · 数据站 `mkdocs build` 通过 · 逐页 grep dist 确认 Hub/字段表渲染

## A · 6 公司页 → Entity Hub（§7）

每页正文末尾新增 `## Entity hub` 显式结构，分 8 类小节（Models / Products / API / Agents / Research-Technology / Comparisons / Pricing / Benchmarks），**每节只链站内真实存在的实体页**（grep 确认 slug）。目标语义达成：ByteDance → Doubao Seed 模型 → Volcengine Ark API → 模型/产品 单跳可达（页面内链接，不新增页面）。保留既有正文、四层标签与分析不动。

| File | Hub 小节数 | 链接数 | 说明 |
|---|---|---|---|
| `src/content/companies/bytedance.md` | 7 | 14 | 无 Benchmarks（站内无 doubao 模型基准）；Products 链 Doubao App/Ark |
| `src/content/companies/deepseek.md` | 8 | 23 | 唯一含 Research 原创页链接（how-deepseek-changed…） |
| `src/content/companies/alibaba-cloud.md` | 8 | 22 | Models 含被取代 qwen3.7-plus |
| `src/content/companies/minimax.md` | 8 | 18 | — |
| `src/content/companies/moonshot-ai.md` | 8 | 23 | Benchmarks 7 项（kimi-k3 覆盖最广） |
| `src/content/companies/zhipu-ai.md` | 8 | 18 | Research 链接 glm-agent-oriented-ai |

## B · 10 Agent 页字段深化（§12）

每页正文末尾新增 `## Field reference` 表（Field | Value | Evidence type），统一 19 字段：underlying model / target users / platform / OS / browser-computer use / coding / autonomous task execution / MCP / tool calling / memory / workflow / API / pricing / region / open-source / deployment / limitations / source / last verified。**只填有据值，查不到的显式写 Not publicly documented**（不编造）。Underlying model / API 值内链到对应实体页，建立 Agent→Model→Company→API 关系链。四层标签与既有正文结论不变。

| File | 填值数 | Not publicly documented |
|---|---|---|
| `src/content/agents/autoglm.md` | 15 | 4 |
| `src/content/agents/deepseek-harness.md` | 17 | 2 |
| `src/content/agents/doubao-app.md` | 14 | 5 |
| `src/content/agents/glm-coding-plan.md` | 16 | 3 |
| `src/content/agents/kimi-code.md` | 17 | 2 |
| `src/content/agents/minimax-agent.md` | 14 | 5 |
| `src/content/agents/minimax-code.md` | 17 | 2 |
| `src/content/agents/qoder.md` | 16 | 3 |
| `src/content/agents/qwen-agent.md` | 17 | 2 |
| `src/content/agents/qwen-code.md` | 17 | 2 |

## 数据站同步

`data/docs/agents/{10}.md`：①Underlying Models 由纯文本列表改为链到 `../models/{slug}.md` 实体页；②新增 `## API Platform` 关系小节，链到对应 `../apis/{slug}.md`（Agent→API 关系补齐）。与主站 frontmatter `underlying_models`/company.api 真值一致，不矛盾。辅助脚本 `data/scripts/b2a_agent_relations.py` 新增。

---

# China AI Hub — Phase 2 Change Log（B1 实体关系一致性全库审计 + 修复）

**日期**：2026-09-29 · **范围**：主站 `china-ai-hub` + 数据站 `china-ai-hub-data`
**依据**：`phase2/39-chinaaihub-upgrade-plan.md` P0 + `phase2/38-chinaaihub-audit-report.md` §23
**验证方式**：程序化交叉审计脚本 `scripts/entity-consistency-audit.py`（六向核对 Company↔Model↔Agent↔API↔Pricing↔Benchmark）+ `npm run build` 121 页通过 + 修后复扫 0 矛盾

| File | Problem | Change | Source | Verification date |
|---|---|---|---|---|
| `src/content/companies/{6}.md` | frontmatter `agents`/`api` 字段全空，与 agent.company / api.provider 反向指针矛盾（审计 §23 MiniMax「0 APIs」类，全库 6 家全中） | 补 `agents` + `api` 字段（值取反向指针真值） | agent/api 实体页反向指针 | 2026-09-29 |
| `src/content/companies/zhipu-ai.md` | `foundation_models` 漏列活跃兄弟 SKU `glm-5.3-flashx` | 补 `glm-5.3-flashx` | Z.ai docs（既有 source） | 2026-09-29 |
| `data/docs/companies/{6}.md` | 数据站 company 页缺 `## Agents` / `## API` 关系小节，与主站语义层不同步 | 补 `## Agents` + `## API` 小节（链接到实体页）；同步 zhipu Foundation Models | 主站 frontmatter 真值 | 2026-09-29 |
| `data/docs/companies/bytedance.md` | 悬空 `## Related Entities → volcengine`（非 company 实体） | 移除该小节（Ark 已由 `api: ark` + `cloud_distribution` 覆盖） | — | 2026-09-29 |
| `scripts/entity-consistency-audit.py` | （新增）无审计基础设施 | 新建六向一致性审计脚本（含 superseded 不计入当前模型口径） | — | 2026-09-29 |

**审计结论**：修复前 26 处矛盾（Company→API 6 + Company→Agent 6 + Company→Model 2 + DataSite Company→API 6 + DataSite Company→Agent 6）；修复后 0 矛盾。详见 `docs/entity-consistency-report.md`。

---

# China AI Hub — Phase 2 Change Log（P0-a 核心模型页深化 + D 级页治理）

**日期**：2026-09-28 · **范围**：主站 `china-ai-hub` 模型页
**依据**：`phase2/37-chinaaihub-content-upgrade-strategy.md` §2/§8/§10/§11 + `docs/content-audit.md` P0 清单
**验证方式**：官方源已在前序批次核实（2026-09-20/27）+ `npm run build` 121 页通过 + 内链逐条核对

---

## A · 8 个核心模型页深化（FACTS → INTERPRETATION → IMPLICATIONS）

每页正文从 <120 词事实段扩至 800–1,400 词，新增答案前置块（§3）＋ 架构/参数/MoE 含义 · context window 实际意义 · 定价含义 · API/coding/agent/部署含义 · open-weight/license 含义 · benchmark 解读 + 「benchmark 不能证明什么」· 适用/不适用负载 ＋ 四层标签贯穿（Official fact / Vendor-reported claim / Third-party evidence / China AI Hub analysis）。**零编造**：全部数值取自既有 frontmatter 事实与官方源；无源数字保持原文或标「Not publicly documented」。

| File | Problem | Change | Source | Verification date |
|---|---|---|---|---|
| `src/content/models/deepseek-v4-pro.md` | B 级，正文 <120 词事实段，无 why-it-matters、无四层标签 | 扩至 ~1,250 词：答案前置块 + 架构/MoE/context/pricing/API/agent/open-weight/benchmark 解读/负载适用性 + China AI Hub analysis；保留全部 source；内链 technology/comparison/research/agents/pricing | DeepSeek API docs + HF card（既有 source） | 2026-09-28 |
| `src/content/models/deepseek-v4-1-flash.md` | C 级，纯事实概述 | 扩至 ~1,300 词：同上结构；补 peak/off-peak 含义、vendor-harness benchmark 警示、非对称架构 cost 逻辑 | DeepSeek API docs + HF card（既有 source） | 2026-09-28 |
| `src/content/models/kimi-k3.md` | B 级，信息密度高但缺解读层 | 扩至 ~1,350 词：补 1M/1M 输入输出唯一性、KDA/Gated MLA 长上下文含义、$20M license 阈值、固定 sampling 限制 | Moonshot GitHub + platform docs（既有 source） | 2026-09-28 |
| `src/content/models/qwen3.8-max.md` | C 级，纯事实概述 | 扩至 ~1,300 词：补 Gated DeltaNet 含义、区域差价、open A95B 与 closed Max 差异、no fine-tuning 约束 | Model Studio + HF card（既有 source） | 2026-09-28 |
| `src/content/models/glm-5.3.md` | B 级，缺分析 | 扩至 ~1,300 词：补 post-training-only 增益含义、open-weight 1M 独特性、always-on reasoning、私有 Code Bench 警示 | Z.ai docs + GitHub（既有 source） | 2026-09-28 |
| `src/content/models/minimax-m3.md` | B 级，缺分析 | 扩至 ~1,300 词：补 MSA 速度声明（vendor claim）、512K 计费分界、max output 未公开、最低旗舰价定位 | MiniMax platform + HF card（既有 source） | 2026-09-28 |
| `src/content/models/doubao-seed-2-1-pro.md` | B 级，缺分析 | 扩至 ~1,250 词：补零架构披露（闭源策略）、cn-beijing-only、5x 输入输出比、单条 preview benchmark 证据薄弱 | Ark docs + Seed blog（既有 source） | 2026-09-28 |
| `src/content/models/glm-5.2.md` | C 级，deprecated 但缺语境 | 扩至 ~1,150 词：补 superseded 语境、MIT「pure open」vs 5.3 Apache-2.0 差异、同价停用决策、历史基线定位 | Z.ai docs + HF card（既有 source） | 2026-09-28 |

## B · 5 个 D 级页面治理

### 兄弟 SKU / 速度变体页（3 个）—— canonical 指向父页，差异化小节重写

| File | Problem | Change | Source | Verification date |
|---|---|---|---|---|
| `src/content/models/glm-5.3-flashx.md` | D 级，与 glm-5.3-flash 近重复（仅 1 source、无 context/benchmark、正文 53 词） | 加 `canonical_model: glm-5.3-flash`；重写为「How it differs」差异化小节（吞吐 200 t/s + 2.5x 价格）+ 说明父页为 canonical | Z.ai pricing（既有 source） | 2026-09-28 |
| `src/content/models/minimax-m2.7-highspeed.md` | D 级，正文即「同模型 2x 计价更快吞吐」近重复 | 加 `canonical_model: minimax-m2.7`；重写为差异化小节（~60 vs ~100 t/s、2x 价格、相同 204,800 context/license） | MiniMax platform docs（既有 source） | 2026-09-28 |
| `src/content/models/kimi-k2.7-code-highspeed.md` | D 级，与 kimi-k2.7-code 近重复（45 词、无 benchmark） | 加 `canonical_model: kimi-k2.7-code`；重写为差异化小节（~180–260 t/s、2x 价格、相同 256K context/API-only） | Kimi platform docs（既有 source） | 2026-09-28 |

### discontinued / superseded 页（2 个）—— 补语境 + 既有字段（只补有据的）

| File | Problem | Change | Source | Verification date |
|---|---|---|---|---|
| `src/content/models/deepseek-v3-2.md` | D 级，discontinued 且 context/pricing/benchmark 三字段全缺 | 加 `superseded_by: deepseek-v4-pro`；补「discontinued + 被 V4 家族取代」语境 + 「release 页无数值 score」如实标注 + 历史定位小节（DSA 架构）；**未编造** context/pricing/benchmark | DeepSeek release + HF config.json（既有 source） | 2026-09-28 |
| `src/content/models/qwen3.7-plus.md` | D 级，被 qwen3.8 取代、仅 1 source、无 context/benchmark | 加 `superseded_by: qwen3.8-max`；补 superseded-but-billable 语境 + 双区价格已补齐（既有）+ context/capability/benchmark 如实标注「not publicly documented」；**未编造** 缺失字段 | Alibaba Model Studio pricing（既有 source） | 2026-09-28 |

## 基础设施变更（支撑 canonical / superseded 渲染）

| File | Problem | Change | Source | Verification date |
|---|---|---|---|---|
| `src/content.config.ts` | 模型 schema 无 canonical 目标字段 | 加 `canonical_model: z.string().optional()` | — | 2026-09-28 |
| `src/layouts/BaseLayout.astro` | canonical 硬编码当前路径 | 加 `canonicalPath` prop（可覆盖 canonical/og:url） | — | 2026-09-28 |
| `src/pages/models/[...id].astro` | 无 superseded/canonical 渲染 | 解析 `superseded_by`/`canonical_model` → 渲染 amber 提示条（canonical 页另传 canonicalPath 至 BaseLayout） | — | 2026-09-28 |

## 审计结论

| 项 | 结果 |
|---|---|
| Pages modified | 13 模型页（8 深化 + 5 治理）+ 3 基础设施文件 |
| Pages added / removed | 0（无路由增删） |
| Internal links added | 8 页共 ~60 条（technology/comparison/research/guides/agents/pricing/同族模型），逐条核对存在 |
| 四层标签 | 13 页正文全部贯穿（Official fact / Vendor-reported claim / Third-party evidence / China AI Hub analysis） |
| Fabricated data | 0（deepseek-v3-2 / qwen3.7-plus 缺失字段如实标注，未补造） |
| Build | 121 页通过；canonical/og:url 覆盖验证通过 |
| Remaining | 6 个 comparison 页深度升级（P0 续）、14 research 页统一四层标签措辞（P0 续）|

---

# China AI Hub — Phase 2 Change Log（P0-b 对比页深化 + Research 页微调）

**日期**：2026-09-28 · **范围**：主站 `china-ai-hub` 对比页 + Research 页
**依据**：`docs/content-audit.md` P0 清单 + 战略 §4/§5/§8/§10
**验证方式**：官方源沿用既有 source 引用（零编造）+ `npm run build` 121 页通过 + 内链逐条 grep 核对存在

## A · 6 个对比页深化（规格表驱动 → 逐维解读）

每页补：逐维「差异为何重要」分析（不重排规格表）、benchmark 可比性限制节、证据化语言（better suited to / more relevant when / has an advantage in / has a limitation in）、四层标签（Official fact / Vendor-reported claim / China AI Hub analysis）、内部链接到模型页。保留全部既有规格表与 source 引用。

| File | 新增维度分析数 | 绝对胜者表述清除 | 内链新增 |
|---|---|---|---|
| `comparisons/deepseek-v4-1-flash-vs-glm-5.3-flash.md` | 7（cost/long-context/reasoning/coding/agent-GUI/deployment/API） | 0（原文已无） | 2（两模型页） |
| `comparisons/deepseek-v4-pro-vs-kimi-k3.md` | 7 | 0 | 2 |
| `comparisons/deepseek-v4-pro-vs-qwen3.8-max.md` | 7 | 0 | 2 |
| `comparisons/doubao-seed-2-1-pro-vs-minimax-m3.md` | 7 | 0 | 2 |
| `comparisons/kimi-k3-vs-minimax-m3.md` | 7 | 0 | 2 |
| `comparisons/qwen3.8-max-vs-glm-5.3.md` | 7 | 0 | 2 |

每页均新增 **Benchmark comparability is limited** 明确声明（不同 test configuration，不可按 headline scores 排名）＋ 文末四层标签说明。

## B · 14 个 Research 页微调（纯增量，不动标题/URL/结构/数据）

| File | 标签统一 | 补 Limitations | 内链新增 |
|---|---|---|---|
| `benchmark-methodology-divergence.md` | ✓（China AI Hub analysis indicates） | ✓（新增 Limitations 段） | 2（deepseek-v4-pro、qwen38-max） |
| `open-weight-vs-api-structural-analysis.md` | ✓ | ✓（新增 Limitations 段） | 2（deepseek-v4-pro、qwen38-max） |
| `chinese-ai-context-windows.md` | ✓ | 已有 | 2（kimi-k3、technology/long-context） |
| `chinese-ai-apis-compared.md` | ✓ | 已有 | 2（deepseek-v4-pro、companies/alibaba-cloud） |
| `chinese-ai-coding-models.md` | ✓ | 已有 | 2（glm-53、kimi-k3） |
| `chinese-ai-model-companies-explained.md` | ✓ | 已有 | 6（六公司页） |
| `chinese-ai-model-licensing-explained.md` | ✓ | 已有 | 4（deepseek-v4-pro、kimi-k3、minimax-m3、qwen38-max） |
| `chinese-ai-model-pricing-changed.md` | ✓ | 已有 | 1（deepseek-v4-1-flash） |
| `chinese-ai-moe-architectures.md` | ✓ | 已有 | 2（deepseek-v4-1-flash、glm-53-flash） |
| `chinese-ai-multimodal-capabilities.md` | ✓ | 已有 | 2（deepseek-v4-1-flash、glm-53-flash） |
| `glm-agent-oriented-ai.md` | ✓ | 已有 | 1（glm-53-flash） |
| `how-deepseek-changed-chinas-ai-market.md` | ✓ | 已有 | 1（deepseek-v4-pro） |
| `rise-of-chinese-ai-agents.md` | ✓ | 已有 | 5（autoglm、deepseek-harness、glm-coding-plan、kimi-code、qwen-code） |
| `state-of-chinas-ai-models-2026.md` | ✓ | 已有 | 1（kimi-k3） |

## 审计结论

| 项 | 结果 |
|---|---|
| Pages modified | 20（6 对比 + 14 Research） |
| Pages added / removed | 0 |
| 维度分析新增 | 42（6 页 × 7 维） |
| 绝对胜者表述清除 | 0（对比页原文已符合「不宣判胜者」，未发现 universal winner / overall best 类表述） |
| 四层标签 | 6 对比页文末补标签说明 + 14 Research 页统一「China AI Hub analysis indicates」措辞 |
| Limitations 新增 | 2（benchmark-methodology-divergence、open-weight-vs-api-structural-analysis） |
| Internal links added | 对比 12 条 + Research 33 条（全部 grep 核对目标页存在） |
| Fabricated data | 0（所有数值沿用既有 source） |
| Build | 121 页通过 |
| Remaining | P1（18 technology 页加深 + 6 company/10 agent/6 API 页加答案前置 + 3 guides 轻量优化） |

---

# China AI Hub — Phase 2 Change Log（P1 Technology 页加深 + Company/Agent/API 页升级 + 指南轻量）

**日期**：2026-09-28 · **范围**：主站 `china-ai-hub`
**依据**：战略 §7/§2/§3/§8/§10 + `docs/content-audit.md` P1 清单
**验证方式**：零编造（全部数值取自既有 frontmatter 事实与官方源）+ `npm run build` 121 页通过 + 内链逐条 grep 核对存在

## A · 18 个 Technology 页深化（B 级，不重写已达标页）

每页增量（不重写结构）：补「What the available evidence actually shows」诚实证据小结节 + 加深中国 AI 证据密度（引具体模型/公司/benchmark/价格锚点）+ 补 related_models/companies 双向内链 + 文末四层标签。全部数值沿用既有实体页已刊载事实。

| File | 证据锚点 | 内链 | 说明 |
|---|---|---|---|
| `a2a.md` | 1 | 3（companies） | 无 A2A 采用为数据缺口非趋势；MCP 7/10 不对称 |
| `ai-agents.md` | 9 | 已有 | 补定价锚点（GLM Coding Plan ¥118–1078、Kimi K3 2.8T）|
| `ai-chips.md` | 2 | 2 | MLA/FlashMLA/DeepGEMM/MSA 效率工程为硬件压力代理 |
| `ai-infrastructure.md` | 3 | 2 | $0.15/1M 价格地板为基础设施成就 |
| `computer-use.md` | 4 | 已有 | Doubao Work 订阅定价 + AutoGLM 安全模式 |
| `deep-research.md` | 4 | 3+3 | 无专用产品；393K/1M 输出为构件能力 |
| `distillation.md` | 2 | 2+2 | Qwen 35B-A3B/2.4T-A95B 蒸馏产品锚点 |
| `function-calling.md` | 5 | 2+2 | 五 API 平台 OpenAI 兼容 tool 面 |
| `inference.md` | 3 | 1+1 | off-peak 2x 为容量管理决策 |
| `long-context.md` | 7 | 已有 | 11 模型 1M；输入/输出不对称 131K→1M |
| `mcp.md` | 2 | 3+5 | 7/10 开源 agent 采用 vs 3 闭源不列 |
| `mixture-of-experts.md` | 6 | 4+3 | 五公司旗舰 MoE；3.1% 激活比成本逻辑 |
| `multimodal-ai.md` | 7 | 已有 | V4-Pro 无视觉 vs V4.1-Flash 有视觉 |
| `quantization.md` | 3 | 已有 | 30B 4-bit 单卡 + MoE 量化不均 |
| `rag.md` | 3 | 已有 | 长上下文替代检索的设计选择 |
| `reasoning-models.md` | 6 | 已有 | 旗舰价差 $0.30→$6.00；vendor 分数 |
| `synthetic-data.md` | 5 | 3+3 | R1 配方 + A3B 产品线；无逐模型数据构成字段 |
| `tool-calling.md` | 5 | 已有 | 五 API 平台 tool 面；可用性普遍/可靠性无证 |

## B · 22 个实体页升级（6 Company + 10 Agent + 6 API，C 级）

每页补：答案前置块（§3 首 100–180 词 What/Why/Characteristics/Professional should know）+ 文末四层标签 +「Why it matters」分析段（公司结构性角色 / agent 与底层模型关系 / API 兼容性与成本取舍）+ 内链到相关模型/公司/技术页。22 页全部覆盖（answer-first=1、labels=1、why-it-matters=1）。

## C · 3 个指南轻量（A/B 级）

| File | 改动 |
|---|---|
| `how-to-choose-a-chinese-ai-model.md` | 补 7 行 Selection matrix 表（需求→最佳匹配模型/API→已验证字段）|
| `how-to-read-vendor-reported-benchmarks.md` | 补 6 行 Benchmark reference 表（benchmark→task type→分数说明什么）|
| `open-weight-vs-api.md` | 补 6 行 Decision matrix 表（约束→API/open-weight→已验证字段）|

## 审计结论

| 项 | 结果 |
|---|---|
| Pages modified | 43（18 technology + 6 company + 10 agent + 6 API + 3 guides）|
| Pages added / removed | 0 |
| 四层标签 | 18 tech 页 + 22 实体页文末全部补「China AI Hub analysis indicates」标签说明 |
| 答案前置块 | 22 实体页全部补齐 |
| Why-it-matters 分析 | 22 实体页全部补齐 |
| Internal links | 18 tech 页 frontmatter 双向内链（related_models/companies）+ 22 实体页内链（全部 grep 核对目标存在）|
| Fabricated data | 0（所有数值沿用既有 frontmatter/source，缺失字段如实标注）|
| Build | 121 页通过 |
| Remaining | P2（数据站历史维度：price/release/benchmark history + 逐字段 verification-date）|
