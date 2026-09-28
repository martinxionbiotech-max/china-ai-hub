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
