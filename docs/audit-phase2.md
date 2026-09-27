# China AI Hub — Phase 2 审计报告（audit-phase2）

**日期**：2026-09-27 · **流程**：SCAN → AUDIT → FIX → BUILD → RE-SCAN → VERIFY

---

## P0 — Factual / Data Conflicts

### 扫描范围
- 实体集合：models 19→21、companies 6、apis 6、agents 10、pricing 6、benchmarks 10、technologies 18、comparisons 6、research 14
- 关系检查：Company↔Model / Company↔API / Model↔API / Model↔Pricing / Model↔Benchmark / Agent↔Model / Pricing↔Model

### 发现并修复的冲突（2 个，均已官方源核实）

| # | 冲突 | 核实结果 | 修复 |
|---|---|---|---|
| 1 | `pricing/alibaba-cloud.md` 引用 `qwen3.7-plus`，但 models 库无此实体 | 官方定价页确认存在：等价 qwen3.7-plus-2026-05-26，国际区 $0.4/$1.6（≤256K）、$1.2/$4.8（256K–1M），北京区 $0.276/$1.101；限时 20% 折扣 | 创建主站 + Data Hub 实体页，pricing 数据保持 |
| 2 | `pricing/zhipu-ai.md` 引用 `glm-5.3-flashx`，但 models 库无此实体；且 `glm-5.3-flash` 实体把 FlashX 当作 alias | 官方 Z.ai 定价页确认：FlashX 是独立计费 SKU（$0.37/$1.25 vs Flash $0.15/$0.50），官方导航标注「GLM-5.3-Flash/FlashX New」 | 创建独立实体页 + 清理 glm-5.3-flash 的 FlashX alias（version 改回 Flash）|

### 任务书点名问题核查
- ✅ DeepSeek 公司页「no API currently listed」矛盾：已不存在（6 家公司页 grep 无残留；DeepSeek 描述已含 API platform）
- ✅ Model↔API：17 条 api_available=true 均有 provider 级 API 条目（首轮扫描误报源于 apis 库无 models 列表字段，校准后为 0）

### RE-SCAN 结果
- 数据一致性冲突：**0**
- 孤儿页：**0**（全站 116 页）
- 断链：**0**

## P1 — Content Quality

- 检查项：generic AI filler、无来源数字、重复段落——本轮未发现新增问题；实体页全部 source-backed
- 新实体页（qwen3.7-plus、glm-5.3-flashx）：官方定价页未公布的字段（context/capabilities/benchmark）已如实标注「not publicly documented」，零编造

## P1 — Entity Relationships

- ✅ Company↔Model：6 家公司的 foundation/open models 列表全部指向真实实体
- ✅ Agent↔Model：underlying_models 全部有效
- ✅ Pricing↔Model：本轮修复后全部有效
- ✅ Benchmark↔Model（P3 批次）：10 页 25 条反向关系
- 新增：glm-5.3-flashx 与 glm-5.3-flash 的实体分离（同族不同 SKU，独立计费）

## P1 — SEO / AIO

- ✅ canonical/robots/sitemap 全 pages.dev（P0 续批次已修）
- ✅ 断链 0 / 孤儿 0
- ✅ 首页 Dataset JSON-LD、模型页 SoftwareApplication+FAQPage
- ⏳ GSC 数据不足，query-driven 长尾页留待观察后决策

## P2 — Optional Improvements

1. Technology 页「China AI Implementation」深度扩展（当前已含相关模型/公司链接，可逐篇深化）
2. Comparison 页「Key differences」绑定 source 的逐条检查
3. Research 篇「Observed Data vs Analysis」显式分段标记
4. 历史价格数据积累后的 price history 展示

---

**状态**：P0 全部修复，RE-SCAN 通过。详见 phase2-changelog.md。
