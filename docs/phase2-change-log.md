# China AI Hub — Phase 2 Change Log（2B-P3 Authority 层六件：E-E-A-T 治理页 + author 字段补挂）

**日期**：2026-09-29 · **范围**：主站 `china-ai-hub`（新增 5 治理页 + 补全 1 既有页 + 68 页 author 字段回填）
**依据**：`phase2/40-sinoaihub-phase2b-audit.md` P3 9-14（Author/Researcher · Methodology · Data policy · Corrections · Update history · Editorial standards）
**验证方式**：零夸大（全部如实描述站点实际运作，无虚构个人简历、无编造数字——45/14 分布与 168 evidence rows 从数据站 entity-template.md/evidence-layer.md 读取）· `npm run build` 150 页通过（+5）· 六页 slug 逐一 grep dist 确认存在 · sitemap 含 6 治理页 · `npm run check:counts` 0 矛盾 · `git fetch` 后 `git rev-list --left-right --count HEAD...origin/main` = `0 0`

## A · 六页清单（slug / 词数 / 与既有页去重）

| # | 治理页 | slug | 正文词数 | 去重结果 |
|---|---|---|---|---|
| 1 | Author/Researcher | `/authors/` | ~360 | **新建**（既有 about.astro 是站点定位，非作者实体页；无重复）|
| 2 | Methodology | `/methodology/` | ~620 | **新建**（about.astro 仅一句「How data is sourced」，方法论独立成页；分工互链 editorial-standards）|
| 3 | Data policy | `/data-policy/` | ~520 | **新建**（与 terms.astro 互链不重复：terms=法律条款，data-policy=数据许可/复用/主站与数据站分工/更新频率）|
| 4 | Corrections | `/corrections/` | ~380 | **补全既有页**（已存在 corrections.astro；本批补 GitHub issue 渠道 + 「No corrections issued to date」历史更正记录区）|
| 5 | Update history | `/updates/` | ~520 | **新建**（从 git 64 commits + phase2-change-log.md 生成结构化记录：日期/范围/类型；无既有页）|
| 6 | Editorial standards | `/editorial-standards/` | ~540 | **新建**（质量门槛独立成页；与 methodology 分工互链）|

## B · author 字段补挂

- 编辑类集合（research 18 + guides 11 + comparisons 18 + technologies 18 + news 3 = **68 页**）frontmatter 补 `author: SinoAI Hub Research Team`（团队化署名，无虚构个人简历）。
- `src/content.config.ts` 五集合 schema 加 `author: z.string().optional()`（comparisons/guides/research/technologies/news）。
- 实体数据集合（models/companies/agents/apis/pricing/benchmarks）为数据记录，非编辑署名，未加 author（证据层由 source/last_verified 承载，见 methodology）。
- 作者实体页如实说明：团队化署名、无虚构个人简历；未来若有个体署名会真实挂载姓名与资质（当前不存在）。

## C · 数据口径（全部从数据站读取，零编造）

- **verification_status 45/14 分布**：45 verified / 14 partially_verified（13 模型 + 1 API 未披露核心字段），源：数据站 `docs/entity-template.md` 字段存在矩阵。
- **Evidence Layer 八字段**：evidence_id / source_name / source_url / source_type / published / verified / confidence / conflict，源：`docs/evidence-layer.md`。
- **168 evidence rows** + 7 类 source_type 枚举，源：`docs/evidence-layer.md` backfill 结果。
- **四层标签**：Official fact / Vendor-reported claim / Third-party evidence / China AI Hub analysis（全站既有措辞，本批页内复述定义）。

## D · 基础设施

| File | Change |
|---|---|
| `src/layouts/BaseLayout.astro` | footer 补 9 治理页链接（Updates 并入 legal 行 + Authors/Methodology/Data Policy/Editorial Standards 新行）|
| `src/pages/llms.txt.ts` | Core pages 补 7 治理页条目 |
| `src/pages/corrections.astro` | 补 GitHub issue 渠道 + Correction record 区（No corrections issued to date）|

## 审计结论

| 项 | 结果 |
|---|---|
| 治理页 | 6（新建 5 + 补全 1） |
| author 字段补挂 | 68 页（编辑类 5 集合全量） |
| 虚构个人简历 | 0（团队化署名，明示无个体作者） |
| 夸大/编造 | 0（45/14、168 rows 等口径从数据站读取） |
| build | 150 页通过（+5） |
| 内链 | 六页互链 + 与 terms/disclosure/about 交叉链接，grep dist 确认存在 |
| check:counts | 0 矛盾（六集合四面对齐） |
| 同步 | origin/main `0 0` |

---

# China AI Hub — Phase 2 Change Log（2B-P2b Decision Guides：8 数据驱动决策指南页）

**日期**：2026-09-29 · **范围**：主站 `china-ai-hub`（新增 8 指南页）
**依据**：`phase2/40-sinoaihub-phase2b-audit.md` P2-8（增加 Decision Guides：coding · agent · API · self-hosting · enterprise · long context · multimodal · pricing）
**验证方式**：零编造（全部数值从实体页 frontmatter + 数据站记录读取，未手写数字）· 每页结构 Short answer → Decision criteria 矩阵表（Criteria | Relevance/Notes）→ Entity routing 场景路由表 → What the evidence shows → Selection procedure → Limitations → Sources → 四层标签 footer · 正文 1,222–1,363 词 · `npm run build` 145 页通过（+8）· 内链逐一 grep dist 确认存在 · 数据站一致性抽查（下述）· `git fetch` 后 `git rev-list --left-right --count HEAD...origin/main` = `0 0`

## A · 8 指南概览

| slug | 主题 | 正文词数 | 决策矩阵行数 | 路由链接数 |
|---|---|---|---|---|
| `choosing-a-coding-model` | 编程模型选择（SWE 证据/工具调用/上下文）| 1,252 | 8 | 9 |
| `choosing-an-agent` | Agent 搭建（模型依赖/tool calling/MCP）| 1,288 | 7 | 10 |
| `choosing-an-api-platform` | API 选型（兼容/价格/区域/rate limits）| 1,333 | 7 | 7 |
| `self-hosting-chinese-open-weights` | 自托管（open weights/license/硬件/量化）| 1,272 | 8 | 10 |
| `enterprise-deployment` | 企业部署（区域/SLA/数据驻留/合规）| 1,289 | 7 | 7 |
| `long-context-model-selection` | 长上下文（1M context 与适用负载）| 1,351 | 6 | 7 |
| `multimodal-model-selection` | 多模态（vision/audio/video 矩阵）| 1,222 | 6 | 7 |
| `choosing-by-price` | 价格选型（price_history/阶梯/订阅）| 1,363 | 7 | 7 |

## B · 数据源一致性抽查

主站 frontmatter 与数据站 `china-ai-hub-data/docs/` 逐字段核对，全部一致。代表项：kimi-k3 $3.00/$15.00 · 1M/1M · GPQA 93.5 · DeepSWE 67.5 · TB2.1 88.3；glm-5.3 TB3.0 28.3 · DeepSWE v1.1 66.9 · CyberGym 84.5；minimax-m3 $0.30/$1.20 · price_history 0.6→0.3 / 2.4→1.2 / 0.12→0.06。价格史仅 3 条有据事件（DeepSeek billing-structure 08-16、V4.1-Flash 降价 09-10、MiniMax M3 永久 50% 折扣），未造新历史。

## C · 关键诚实标注

- enterprise 指南显式标注 SLA/合规认证「未公开」——6 平台均无公开 SLA/合规条款，诚实记录而非推断。
- 四层标签 footer 全 8 页；`Third-party` 无据不硬挂（benchmark 全为 vendor_reported）。
- 内链发现并修正 2 处 slug 错误（kimi-k2.6→kimi-k26、minimax-m2.7→minimax-m27，点号剥除规则）。

---

# China AI Hub — Phase 2 Change Log（2B-P2a Comparison 规模化：12 数据驱动 Entity-vs-Entity 对比页）

**日期**：2026-09-29 · **范围**：主站 `china-ai-hub`（新增 12 对比页 + 1 基础设施微调）
**依据**：`phase2/40-sinoaihub-phase2b-audit.md` P2-7（大规模增加 Comparison，自动关联 pricing/context/coding/vision/agent/license/deployment/benchmark）+ 数据站统一模板 `docs/entity-template.md`
**验证方式**：零编造（全部数值从两实体主站 frontmatter + 数据站记录读取，未手写数字）· 每页 8 维覆盖 + 每维差异值 + 1 句「差异为何重要」条件化表述（无胜者）· `npm run build` 137 页通过（+12）· 内链 13 个模型 slug 逐一 grep dist 确认存在 · 数据站一致性抽查（下述表）· `git fetch` 后 `git rev-list --left-right --count HEAD...origin/main` = `0 0`

## A · 候选对选择（12 对，排除既有 6 对比页）

优先级落地：同厂商变体对（6 对）+ 跨厂商同档对（4 对）+ 用途导向对（2 对，长上下文/编码）。排除既有 6 对（deepseek-v4-1-flash-vs-glm-5.3-flash、deepseek-v4-pro-vs-kimi-k3、deepseek-v4-pro-vs-qwen3.8-max、doubao-seed-2-1-pro-vs-minimax-m3、kimi-k3-vs-minimax-m3、qwen3.8-max-vs-glm-5.3）。

| # | slug | 实体对 | 类型 | 正文词数 |
|---|---|---|---|---|
| 1 | `deepseek-v4-pro-vs-deepseek-v4-1-flash` | DeepSeek-V4-Pro / V4.1-Flash | 同厂商（旗舰→flash） | 1,332 |
| 2 | `kimi-k3-vs-glm-5.3` | Kimi K3 / GLM-5.3 | 跨厂商同档（开源 1M 旗舰） | 1,368 |
| 3 | `qwen3.8-max-vs-doubao-seed-2-1-pro` | Qwen3.8-Max / Doubao Seed 2.1 Pro | 跨厂商同档（闭源旗舰） | 1,334 |
| 4 | `qwen3.8-max-vs-qwen3.8-flash` | Qwen3.8-Max / Qwen3.8-Flash | 同厂商（旗舰→flash） | 1,212 |
| 5 | `glm-5.3-vs-glm-5.3-flash` | GLM-5.3 / GLM-5.3-Flash | 同厂商（旗舰→flash） | 1,212 |
| 6 | `kimi-k3-vs-kimi-k2.7-code` | Kimi K3 / Kimi K2.7 Code | 同厂商（旗舰→coding 专家） | 1,249 |
| 7 | `minimax-m3-vs-minimax-m2.7` | MiniMax-M3 / MiniMax-M2.7 | 同厂商（旗舰→自进化） | 1,271 |
| 8 | `doubao-seed-2-1-pro-vs-doubao-seed-2-1-turbo` | Doubao Pro / Doubao Turbo | 同厂商（pro→turbo） | 1,220 |
| 9 | `deepseek-v4-1-flash-vs-qwen3.8-flash` | DeepSeek-V4.1-Flash / Qwen3.8-Flash | 跨厂商同档（flash 开源 vs 闭源） | 1,225 |
| 10 | `glm-5.3-flash-vs-qwen3.8-flash` | GLM-5.3-Flash / Qwen3.8-Flash | 跨厂商同档（flash） | 1,205 |
| 11 | `kimi-k3-vs-qwen3.8-max` | Kimi K3 / Qwen3.8-Max | 跨厂商同档（长输出 vs 多区） | 1,265 |
| 12 | `qwen3.8-max-vs-qwen3.8-2.4t-a95b` | Qwen3.8-Max / 2.4T-A95B | 同厂商（闭源 API vs 开源权重） | 1,212 |

## B · 数据驱动构建（8 维自动关联）

每页 `dimensions` frontmatter 固定 8 维：pricing / context / coding / vision / agent / license / deployment / benchmark。正文结构：`At a glance`（Criterion|A|B 表）+ 逐维分节（每维差异值 + 「差异为何重要」）+ `Why each difference matters`（8 维条件化结论）+ `Trade-off summary` + `Decision context`（4 情境）+ `What is uncertain` + `Sources` + 四层标签 footer。全部数值取自两实体主站 frontmatter（pricing/context_window/maximum_output/capabilities/open_weight/license/self_hosting/api_available/benchmark_results）与数据站记录，零手写数字。

**关键条件化处理（无胜者宣判）**：
- 跨币种对（qwen3.8-max vs doubao-seed-2-1-pro）显式声明「USD vs CNY，不声明孰贵」。
- 基准版本分歧（Terminal-Bench 2.1 vs 3.0、DeepSWE vs v1.1）逐页标注「不可直接比较」。
- 0 基准记录模型（qwen3.8-flash、kimi-k2.7-code、qwen3.8-2.4t-a95b、doubao-turbo）标注「无基准证据，非能力缺失」。
- 缺字段（max output 未公开、架构未披露）逐页标「Not publicly disclosed / Not stated」。

## C · 基础设施微调

| File | Change |
|---|---|
| `src/pages/comparisons/[...slug].astro` | `dimensionLabels` 补 `benchmark: 'Benchmark records'`（8 维含 benchmark，原映射缺失此标签） |

## 数据站一致性抽查（每页数值与数据站一致）

抽查覆盖 12 页涉及的 13 个模型实体，主站 frontmatter 与数据站 `china-ai-hub-data/docs/models/*.md` 逐字段核对（pricing / context_window / maximum_output / capabilities / open_weight / license / benchmark 计数），全部一致。代表项：kimi-k3 $3.00/$15.00 · 1M/1M · 6 基准；glm-5.3 $1.40/$4.40 · 1M/131,072 · 4 基准；qwen3.8-max $2.00/$6.00 · 1M/131,072 · 5 基准；doubao-pro ¥6.00/¥30.00(CNY) · 1M/262,144 · 1 基准；minimax-m3 $0.30/$1.20 · 1M · 5 基准。

## 审计结论

| 项 | 结果 |
|---|---|
| 新增对比页 | 12 |
| 8 维覆盖 | 12/12 页（96 维格） |
| 绝对胜者宣判 | 0（全部 better suited to / more relevant when / has an advantage in） |
| 四层标签 | 12/12 页文末 footer |
| 双实体互链 | 12/12 页（At a glance 前后 + Why 节内链到两模型页） |
| 内链验证 | 13 个模型 slug 全存在于 dist |
| Fabricated data | 0 |
| build | 137 页通过（+12） |
| 同步 | origin/main `0 0` |

---

# China AI Hub — Phase 2 Change Log（B5 P4 决策情境层 + P5 过度推断格式统一）

**日期**：2026-09-29 · **范围**：主站 `china-ai-hub`（6 对比页 + 6 公司页 + 7 模型页 + 4 research 页）
**依据**：`phase2/39-chinaaihub-upgrade-plan.md` P4（§9 决策情境对比层）+ P5（§24 过度推断格式统一）+ `phase2/38-chinaaihub-audit-report.md` §9/§24
**验证方式**：零编造（决策情境只写页内既有事实，缺据维度标 Not publicly documented / not publicly documented; confirm with vendor）· 分析句统一加前缀不改事实结论 · `npm run build` 125 页通过（无增删页）· 终检 grep 过度推断短语无标注残留 = 0

## A · P4 决策情境层（6 对比页，§9）

对 6 个对比页各加 `## Decision context` 分节，按四类情境分块（每块 2-4 句 + 条件化表述，不宣判胜者）：

| 对比页 | For API developers | For self-hosting | For coding agents | For enterprise |
|---|---|---|---|---|
| deepseek-v4-1-flash-vs-glm-5.3-flash | ✅ | ✅ | ✅ | ✅ |
| deepseek-v4-pro-vs-kimi-k3 | ✅ | ✅ | ✅ | ✅ |
| deepseek-v4-pro-vs-qwen3.8-max | ✅ | ✅ | ✅ | ✅ |
| doubao-seed-2-1-pro-vs-minimax-m3 | ✅ | ✅ | ✅ | ✅ |
| kimi-k3-vs-minimax-m3 | ✅ | ✅ | ✅ | ✅ |
| qwen3.8-max-vs-glm-5.3 | ✅ | ✅ | ✅ | ✅ |

四类情境覆盖维度（只写页内既有事实，缺据如实标）：
- **For API developers**：price/tool calling/structured output/API 兼容性——按页内既有字段；latency 全 6 页均「Not publicly documented on this page」（页内无 latency 数据）。
- **For self-hosting**：weights/license——按页内既有；hardware requirements/quantization/inference ecosystem 全 6 页均「Not publicly documented」（页内无此三维数据）。
- **For coding agents**：SWE/terminal 分项均「not broken out on this page」（对比页只有 aggregate benchmark 计数），只写页内 tool calling/agent capability/context 既有事实。
- **For enterprise**：region/SLA/data residency/compliance 全 6 页均「not publicly documented — confirm with the vendor」。

每块开头统一 `China AI Hub analysis indicates the following decision-context implications, drawn from the listed facts above.` 标注为分析；全节零编造、零胜者宣判（用 better suited to / more relevant when / has an advantage in）。

## B · P5 过度推断格式统一（§24，全站 19 句补前缀）

扫描全站分析性语句（grep 关键词：natural default / distinctive bet / structural role is / is the purest / signaling a / reflecting the premium / clearest market position / deliberate closed-strategy / a genuine moat / is itself a structural fact / the closest thing / positions … as / makes the pair a clean / This makes both candidates 等），统一补 `China AI Hub analysis: ` 前缀，共 **19 句**：

| 文件 | 补前缀句数 | 代表性分析句 |
|---|---|---|
| companies/（6 页） | 6 | "China AI Hub analysis: Alibaba Cloud occupies a structurally unique position…"（原 "That makes Qwen the natural default"）· MiniMax/Zhipu/ByteDance/DeepSeek/Moonshot 各 structural role 句 |
| models/（7 页） | 8 | doubao-seed-2-1-pro「deliberate closed-strategy」「signaling a generation-premium」「purest closed strategy」· kimi-k3「reflecting the premium」· glm-5.2「makes the pair a clean」· glm-5.3「distinguishing factor」· minimax-m3「clearest market position」· deepseek-v4-1-flash「architectural logic is cost」 |
| comparisons/（1 页） | 1 | deepseek-v4-1-flash「This makes both candidates for local deployment」 |
| research/（4 页） | 4 | chinese-ai-apis-compared「closest thing to a Chinese model router」· how-deepseek「pattern is clear / genuine moat」· rise-of-chinese-ai-agents「structural shift visible / positions Zhipu as infrastructure」· agent-ecosystem「concentration is itself a structural fact」 |

原则：不改任何事实与结论，只加标注；每结论证据链（Evidence → Reasoning → Interpretation）在原文已成立，本批只补标注前缀。research 页既有「China AI Hub View」「Our interpretation:」正确标注不动。

终检：`grep -rn "natural default|distinctive bet|structural role is|…" src/content/ | grep -v "China AI Hub analysis" | grep -v "Our interpretation"` 返回 0 残留。

## 审计结论

| 项 | 结果 |
|---|---|
| 对比页决策情境节 | 6（每页 4 块全覆盖 = 24 块） |
| 未公开标注（Not publicly documented / confirm with vendor） | 每页 self-hosting 3 维 + enterprise 4 维 + API latency 1 维，全如实标注 |
| P5 分析句补前缀 | 19 句（company 6 + model 8 + comparison 1 + research 4） |
| 残留未标注分析句 | 0 |
| build | 125 页通过（无增删页） |
| Fabricated data | 0 |

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
