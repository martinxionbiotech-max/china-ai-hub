# SinoAIHub 全站内容审计（Phase 1 — AUDIT ONLY）

> 审计日期：2026-09-28
> 范围：主站 `china-ai-hub`（Astro）+ 数据站 `china-ai-hub-data`（MkDocs）
> 依据：`phase2/37-chinaaihub-content-upgrade-strategy.md` §1（分级标准）+ §12（优先级）
> 状态：**本批只审计与分级，未修改任何页面 / 内容 / 数据 / URL。**

---

## 0. 审计方法与范围

- 逐页读取正文（剥离 YAML frontmatter 后的正文词数作为"正文量"口径），并抽查每类集合的代表样本全文。
- 数据源（frontmatter 结构化字段）与正文分开评估：`models`/`companies`/`agents`/`apis`/`benchmarks`/`pricing` 等集合以结构化字段承载事实，正文承载解读。
- 分级维度（§1 十维）：factual completeness / source quality / originality / analytical depth / evidence / usefulness / search intent / AIO 抽取潜力 / 重复度 / 是否解释 "why it matters"。
- 数据站页面为结构化事实层（§6 定位），用独立口径评估，不与主站编辑页混排。

---

## 1. 页面清单（Inventory）

### 1.1 主站内容页（`src/content/`，共 103 页）

正文量 = 剥离 frontmatter 后的单词数。

| 集合 | 数量 | 正文量区间 | 代表 URL 模式 |
|---|---|---|---|
| models | 21 | 39–117 | `/models/{slug}` |
| companies | 6 | 72–130 | `/companies/{slug}` |
| agents | 10 | 67–133 | `/agents/{slug}` |
| apis | 6 | 66–103 | `/api/{slug}` |
| comparisons | 6 | 420–522 | `/comparisons/{slug}` |
| technologies | 18 | 332–485 | `/technology/{slug}` |
| research | 14 | 666–1991 | `/research/{slug}` |
| guides | 3 | 400–446 | `/guides/{slug}` |
| news | 3 | 100–141 | `/news/{slug}` |
| pricing | 6 | 51–56 | `/pricing/{slug}` |
| benchmarks | 10 | 44–60 | `/benchmarks/{slug}` |

静态/工具页（`about`、`corrections`、`disclosure`、`privacy`、`terms`、`cookies`、`index`、`llms.txt`、`robots.txt`）不纳入本次"重要页面"分级，单独记录但不打级。

### 1.2 数据站（`docs/`，结构化事实层）

| 集合 | 实体记录数 | 备注 |
|---|---|---|
| models | 21（+index） | 与主站同名实体，带 JSON-LD + canonical 指向主站 |
| companies | 6（+index） | |
| agents | 10（+index） | |
| apis | 6（+index） | |
| benchmarks | 10（+index） | |
| pricing | 6（+index） | |

数据站每条实体含 `last_verified` / `sources`（source_type + confidence）/ benchmark 表（source_type）/ 已知限制，为结构化事实 + 来源标注。**缺失**：价格历史 / 发布历史 / benchmark 历史 / 版本变更时间线（§6 明确要求，见 P2）。

---

## 2. 分级表（Grading）

分级定义（§1）：
- **A** = 强页，仅需微调
- **B** = 有用但需更深分析
- **C** = 薄 / 重复 / 纯数据库式
- **D** = 不准确 / 过时 / 重复 / 结构问题

### 2.1 Models（21 页）— 全集合正文 <120 词，无 A

事实层完整（frontmatter 字段齐），但正文均为一到两段事实概述，**无 why-it-matters、无 benchmark 解读、无"benchmark 不能证明什么"、无适用/不适用负载、无 China AI Hub analysis、无四层标签**。

| 分级 | 页面 | 判定依据 |
|---|---|---|
| **B** | deepseek-v4-pro | 正文含 deprecated 冲突标注 + known_limitations 4 条（官方页相互矛盾、峰值/谷值计价 2x、checkpoint 存疑），是模型页中唯一接近"解读"的；但仍无 why-it-matters。 |
| **B** | kimi-k3 | 正文含 license 义务细节（$20M MAS 条款、MAU/收入 UI 署名）与 API 参数（固定 temperature/top_p、max_completion_tokens 上限），信息密度最高；缺解读层。 |
| **B** | minimax-m3 / glm-5.3 / glm-5.3-flash / doubao-seed-2-1-pro | 正文含架构/计价/模态差异等实质信息，可作为 B 级改造起点；缺分析。 |
| **C** | deepseek-v4-1-flash / doubao-seed-2-1-turbo / doubao-seed-evolving / glm-5.2 / qwen3.8-max / qwen3.8-flash / minimax-m2.7 / qwen3.8-2.4t-a95b / kimi-k2.6 / kimi-k2.7-code | 纯事实概述，无解读；部分（qwen3.8-flash、kimi-k2.7-code、doubao-turbo）benchmark_results 为空，数据层亦不全。 |
| **D** | glm-5.3-flashx | 与 glm-5.3-flash 近重复的"兄弟 SKU"页，仅 1 个 source、无 context_window、无 benchmark；正文 53 词。 |
| **D** | minimax-m2.7-highspeed | 正文即"同一模型 2x 计价、更快吞吐"，无独立内容，近重复页。 |
| **D** | kimi-k2.7-code-highspeed | 与 kimi-k2.7-code 近重复的 highspeed 兄弟页，正文 45 词、无 benchmark。 |
| **D** | deepseek-v3-2 | 已 discontinued，且 context_window / pricing / benchmark_results 三字段全缺，结构不完整。 |
| **D** | qwen3.7-plus | 被 qwen3.8 取代，仅 1 source、无 context_window、无 benchmark，结构不完整。 |

### 2.2 Companies（6 页）— 全 C

| 分级 | 页面 | 判定依据 |
|---|---|---|
| **C** | alibaba-cloud / bytedance / deepseek / minimax / moonshot-ai / zhipu-ai | 结构化事实齐（founded/headquarters/funding/model 清单），正文为 72–130 词事实概述，含少量战略注记（如 bytedance "纯闭源策略"、deepseek "开源+低价"），但无分析层、无四层标签、无 why-it-matters。bytedance / alibaba-cloud 相对更厚（C+）。 |

### 2.3 Agents（10 页）— 全 C

| 分级 | 页面 | 判定依据 |
|---|---|---|
| **C** | autoglm / deepseek-harness / doubao-app / glm-coding-plan / kimi-code / minimax-agent / minimax-code / qoder / qwen-agent / qwen-code | 正文 67–133 词，多为产品定位 + 定价 + underlying models 清单；qwen-agent（67）、minimax-code（68）最薄。无评测证据、无与底层模型能力的关系解读、无四层标签。 |

### 2.4 APIs（6 页）— 全 C

| 分级 | 页面 | 判定依据 |
|---|---|---|
| **C** | ark / deepseek / minimax / model-studio / moonshot / zai | 正文 66–103 词，端点到鉴权到能力的事实概述（如 ark 的 Responses/Chat 双端点、AK/SK）；纯数据库式，无兼容性/成本/取舍解读。 |

### 2.5 Comparisons（6 页）— 全 B

| 分级 | 页面 | 判定依据 |
|---|---|---|
| **B** | deepseek-v4-1-flash-vs-glm-5.3-flash / deepseek-v4-pro-vs-kimi-k3 / deepseek-v4-pro-vs-qwen3.8-max / doubao-seed-2-1-pro-vs-minimax-m3 / kimi-k3-vs-minimax-m3 / qwen3.8-max-vs-glm-5.3 | 已有证据式语言（"listed"、"we do not rank"）、at-a-glance 表 + 定价/上下文/能力/许可分节 + trade-off summary + "choose by workload"；**不宣判胜者**（符合 §4）。但仍是规格表驱动，缺：逐对 benchmark 可比性限制、cost/coding/reasoning/agent 的逐维影响展开、以及"该差异为何重要"的结论化表达。 |

### 2.6 Technologies（18 页）— 全 B（部分 B+）

| 分级 | 页面 | 判定依据 |
|---|---|---|
| **B** | a2a / ai-agents / ai-chips / ai-infrastructure / computer-use / deep-research / distillation / function-calling / inference / long-context / mcp / mixture-of-experts / multimodal-ai / quantization / rag / reasoning-models / synthetic-data / tool-calling | 18 页均含 "why it matters"（grep 证实）+ how-it-works + Chinese adoption + limitations + deployment 结构，是中国 AI 语境化写法，明显优于百科式。差距：个别页证据密度与"现有证据实际说明了什么"的表达仍偏弱；reasoning-models（485）、mixture-of-experts、ai-agents 最接近 A。 |

### 2.7 Research（14 页）— 站内最强集合

| 分级 | 页面 | 判定依据 |
|---|---|---|
| **A** | benchmark-methodology-divergence | 完整走 §5 结构（问题→方法→证据→数据→分析→反例/限制→China AI Hub view→结论），含 5 个"比较性杠杆"的原创方法学分析（版本/工具/子集/产品错位/未公开），是站内标杆。 |
| **A** | how-deepseek-changed-chinas-ai-market | Executive Summary + What We Know/Data Shows/Changed + Why It Matters + 四轴 Detailed Analysis + 证据表，跨源综合 + 原创解读（MIT 授权→能力价格地板、峰值计价→需求塑造）。 |
| **A** | state-of-chinas-ai-models-2026 | 19 模型/6 实验室的聚合快照，openness/context/price 三结构事实 + 分层表 + 明确"snapshot 非 ranking"。 |
| **B** | chinese-ai-model-companies-explained / chinese-ai-model-licensing-explained / chinese-ai-model-pricing-changed / chinese-ai-moe-architectures / chinese-ai-multimodal-capabilities / glm-agent-oriented-ai / chinese-ai-apis-compared / chinese-ai-context-windows / chinese-ai-coding-models / rise-of-chinese-ai-agents / open-weight-vs-api-structural-analysis | 同套方法论（Exec Summary + 数据表 + 解读），质量高但证据密度/原创深度略逊于 A；open-weight-vs-api-structural-analysis（666）最薄。 |

### 2.8 Guides（3 页）

| 分级 | 页面 | 判定依据 |
|---|---|---|
| **A** | how-to-read-vendor-reported-benchmarks | 答案前置 + 六步 reading procedure + bottom line，直接服务专业读者的易错点，是优秀实操指南。 |
| **B** | how-to-choose-a-chinese-ai-model / open-weight-vs-api | 结构好、答案前置，但可进一步补"按负载/预算/合规的选择矩阵"与更多数据库锚点。 |

### 2.9 News（3 页）— 全 C

| 分级 | 页面 | 判定依据 |
|---|---|---|
| **C** | deepseek-v4-1-flash-release / deepseek-v4-pro-retirement-reversed / qwen3-8-max-0902-snapshot | 100–141 词新闻条目，事实当前、有来源，属合理短篇；非本次升级重点。 |

### 2.10 Pricing（6 页）— 全 C

| 分级 | 页面 | 判定依据 |
|---|---|---|
| **C** | alibaba-cloud / bytedance / deepseek / minimax / moonshot-ai / zhipu-ai | 正文 51–56 词，均为"下表列出 N 个模型的价目 + 官方源链接"的纯数据壳，无价格解读/历史/对比。 |

### 2.11 Benchmarks（10 页）— 全 C

| 分级 | 页面 | 判定依据 |
|---|---|---|
| **C** | automationbench / browsecomp / cybergym / deepswe / gpqa-diamond / hle / mmmu-pro / swe-bench / terminal-bench / video-mme | 正文 44–60 词，均为"下表列出 N 条评测 + 详见 Limitations"的纯数据壳；benchmark 定义/方法学/污染说明落在 frontmatter 字段，正文无解读。 |

### 2.12 数据站（结构化事实层）— 全 C（定位使然，非缺陷）

| 分级 | 说明 |
|---|---|
| **C** | 每条实体含 JSON-LD（SoftwareApplication/Organization）+ canonical 指向主站 + sources（source_type/confidence）+ last_verified + benchmark 表（source_type）+ known_limitations，结构化事实与来源标注已达标。**按 §6 评估仍缺**：价格历史 / 发布历史 / benchmark 历史 / 版本变更时间线 / 逐字段 verification-date。数据站是"结构化事实 + 证据 + 历史"里"历史"维度缺失。 |

---

## 3. 专项检查（Special Checks）

### 3.1 四层标签（Official fact / Vendor-reported / Third-party / China AI Hub analysis）— **系统性缺失**

全站 grep 结果（`src/content/`）：

| 标签 | 出现文件数 |
|---|---|
| "Official fact" | **0** |
| "Vendor-reported" | 1（仅 how-deepseek… 一处正文） |
| "Third-party" | 3 |
| "China AI Hub analysis" | **0**（research 用近似词 "China AI Hub view"/"China AI Hub analysis indicates" 表述，但未统一为 §2 规定的四层标签） |

**结论**：四层标签体系（§2 硬性要求）在所有实体页（models/companies/agents/apis）正文中完全缺失；benchmark 的 source_type 只在数据字段里存在，正文未升格为"官方事实 vs 厂商自报 vs 第三方 vs 本站分析"的可视区分。这是本次审计发现的第一优先级系统性缺口。

### 3.2 无 source 标注的数字

- **context_window**：schema 无 source 字段，为裸数字；正文亦不注来源。
- **model 级 pricing**：仅 `pricing_ref`（provider id，非 URL）；`pricing` 集合页有逐行 `official_source` URL，但模型页无直链。
- **benchmark 分数**：`benchmark_results.source_url` 为可选，多数有，少数（如 deepseek-v4-pro 的 "Agents' Last Exam" 行）缺失。
- **结论**：context window 与模型级价格为"无源数字"重灾区；benchmark 部分缺失 source_url。

### 3.3 答案前置（首 100–180 词）缺失

- **达标**：research（Exec Summary）、guides、technologies（definition + why-it-matters）开头即可独立回答 "what/why/characteristics"。
- **缺失**：models / companies / agents / apis 以密集事实段开头，无结构化 "what is it → why it matters → key characteristics → what a professional should know" 答案块；comparisons 有 at-a-glance 表可接受，但缺一句结论式 "the key difference is…"。

### 3.4 重复 / 近重复组

1. **模型兄弟 SKU 近重复**：`glm-5.3-flash` ↔ `glm-5.3-flashx`；`minimax-m2.7` ↔ `minimax-m2.7-highspeed`；`kimi-k2.7-code` ↔ `kimi-k2.7-code-highspeed`。
2. **主站 ↔ 数据站同名实体**：`models/companies/agents/apis` 六类实体两站各存一份（数据站以 canonical 指向主站，属设计内，但需确保二者字段一致、无漂移）。
3. **跨集合主题重叠（非重复，需内链治理）**：`chinese-ai-apis-compared` vs 各 API 页；`chinese-ai-coding-models` vs `kimi-code`/`qwen-code` 等 agent 页；`chinese-ai-model-licensing-explained` vs 各 model 页 license 字段。

---

## 4. 升级清单（Upgrade List，按 §12）

### P0 — 重要模型/实体页 + 重要对比页 + Research 页

| 页面 | 现状 | 升级方向 |
|---|---|---|
| 核心模型页（deepseek-v4-pro、deepseek-v4-1-flash、kimi-k3、qwen3.8-max、glm-5.3、minimax-m3、doubao-seed-2-1-pro、glm-5.2） | B/C，正文 <120 词事实段 | 按 §2 从 FACTS→INTERPRETATION→IMPLICATIONS 补：答案前置块、架构/参数/MoE 含义、context window 实际意义、定价含义、API/agent/coding/部署含义、benchmark 解读 + "不能证明什么"、适用/不适用负载、license 含义、China AI Hub analysis；并加四层标签 + source 标注。 |
| 6 个对比页 | B，规格表驱动 | 补逐对 benchmark 可比性限制、cost/coding/reasoning/agent/部署逐维"差异为何重要"；保留"choose by workload"不宣判胜者。 |
| 14 个 Research 页 | A/B，已强 | 仅微调：统一为四层标签（"China AI Hub analysis" 措辞）、补 benchmark 方法学反例、内链到实体页。不重写 A 页。 |
| 重复/结构问题模型页（glm-5.3-flashx、minimax-m2.7-highspeed、kimi-k2.7-code-highspeed、deepseek-v3-2、qwen3.7-plus） | D | 兄弟 SKU 页合并或补差异化独立内容；discontinued/superseded 页补齐 context/pricing/benchmark 字段或合并进父模型。 |

### P1 — Technology 页 + Company/Agent/API 页 + 指南

| 页面 | 现状 | 升级方向 |
|---|---|---|
| 18 个 Technology 页 | B | 加深中国 AI 证据密度（引具体模型/benchmark/价格锚点）、补 related_models/companies 双向内链、"现有证据实际说明什么"的表达；不重写已达标页。 |
| 6 Company + 10 Agent + 6 API 页 | C | 加答案前置块 + 四层标签 + "why it matters"（如：该公司在生态中的结构性角色 / 该 agent 与底层模型能力的关系 / 该 API 的兼容性与成本取舍）。 |
| 3 个指南 | A/B | 轻量：补选择矩阵/更多数据库锚点。 |

### P2 — 历史数据集 + 跨实体研究机会

| 机会 | 现状 | 方向 |
|---|---|---|
| 数据站历史维度（§6） | 无 price/release/benchmark history | 新增：价格历史、发布历史、benchmark 历史、模型演进、公司时间线、逐字段 verification-date；schema 已预留 `price_history` 字段（pricing 集合）可扩展。 |
| 跨实体原创研究 | 已有 14 篇 | 新研究选题：benchmark 方法学可比性矩阵、模型价格演进时间线、context-window 演进、open-weight 趋势、API 兼容性矩阵（OpenAI/Anthropic 兼容）、授权条款横向对比扩展。 |

---

## 5. 统计小结（主站 103 页）

| 分级 | 数量 | 占比 |
|---|---|---|
| A | 4 | 3.9% |
| B | 43 | 41.7% |
| C | 51 | 49.5% |
| D | 5 | 4.9% |

（数据站 59 条实体 + 6 index 另计，全 C，属结构化事实层定位，问题为"历史维度缺失"而非"错误"。）

**核心结论**：站内最强资产是 Research（14 篇，A/B）与 Technologies（18 篇，B），已体现 evidence-driven + 中国语境 + 原创综合。最弱资产是作为"数据库→知识库"转型核心的**实体页**（models/companies/agents/apis，共 43 页，全 C/B-），表现为：正文薄（<130 词）、四层标签全缺失、无 why-it-matters、context window 与模型级价格为无源数字。升级重心应放在实体页的 FACTS→INTERPRETATION→IMPLICATIONS 改造，而非扩量。
