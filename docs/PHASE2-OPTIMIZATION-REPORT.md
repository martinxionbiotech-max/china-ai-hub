# China AI Hub — 优化实施报告（P0 续 + P1）

**日期**：2026-09-27 · **范围**：主站 `china-ai-hub` + Data Hub `china-ai-hub-data`
**生产环境**：`https://china-ai-hub.pages.dev` / `https://china-ai-hub-data.pages.dev`（无自定义域名，全部引用已统一）

---

## FINAL DELIVERABLES

### 1. Files changed
**主站（4 个 commit，`2ba7925..73074b7`）**：
- `astro.config.mjs`（site → pages.dev）
- `src/layouts/BaseLayout.astro`（域名 + extraJsonLd prop + Data Hub 链接）
- `src/pages/{robots,llms.txt}.ts`、`src/pages/{models/[id].md,models/[id].json}.ts`、`src/pages/{comparisons,guides,technology}/[...slug].astro`（域名）
- `src/pages/news/[...slug].astro`（trigger_updates 用 modelHref 解析）
- `src/content/guides/*.md` ×3（source_url 域名）
- `src/content/companies/bytedance.md`（related_entities 清空）
- `src/pages/index.astro`（首页 Dataset JSON-LD）
- `README.md`、`docs/*.md` ×5（文档域名）

**Data Hub（3 个 commit，`3d2b12a..37362a6`）**：
- `mkdocs.yml`（site_url → pages.dev）
- `docs/**/*.md` 68 文件（@id/mainEntityOfPage/链接文本域名统一）
- `docs/models/*.md` ×6（新增 Related Agents/Related Technologies 章节）

### 2-4. Routes added / modified / removed
- Added：0 条新路由（无内容扩张）
- Modified：全部既有路由的 canonical/JSON-LD 域名
- Removed/merged：0

### 5. SEO fixes
- ✅ 生产域名统一（此前 canonical/robots/sitemap/@id 指向未启用域名 chinaaihub.com）
- ✅ 2 条断链修复（qwen3.8-max slug 解析、volcengine 无实体页）
- ✅ 断链复查 **0 条**、孤儿页 **0 个**
- ✅ sitemap/robots/canonical 全量指向 pages.dev，build 114 页通过

### 6. Schema fixes
- ✅ 首页新增 **Dataset JSON-LD**（动态计数：models/companies/agents）
- ✅ BaseLayout 新增 `extraJsonLd` prop（任意页可注入额外 JSON-LD 块）
- 既有 schema 健康：SoftwareApplication（模型页）/ Organization / WebSite / FAQPage / OfferCatalog（定价页）

### 7. Entity Graph improvements
- ✅ 全量关系字段校验（companies/technologies/agents/news/guides/research 的 related_* 字段）：**0 无效引用**
- ✅ Data Hub 模型页补关系章节：Related Agents（4 页）、Related Technologies（6 页）——数据 join 自 agents 的 underlying_models 与主站 technologies 的 related_models，**零编造**
- 修复 Related Technologies 链接指向（Data Hub 无 technologies 目录 → 指向主站技术页）

### 8. Data Hub improvements
- ✅ 域名统一 + 字段覆盖核对（见 E 节缺口清单）
- ✅ 模型实体关系章节补齐

### 9. Internal-linking improvements
- ✅ 断链 0 / 孤儿 0（全站 114 页扫描）
- news 模板模型链接改用 ID 解析器（防 Astro slug 化点号歧义）

### 10. AIO/GEO improvements
- ✅ 首页 Dataset schema（AI 可识别「这是一个数据库」）
- ✅ llms.txt 已有且域名正确；模型页 Quick Facts/Last verified/Sources/表格齐全

### 11. Remaining technical issues
- 无 CRITICAL/HIGH 遗留
- Data Hub 本地 mkdocs 构建未运行（本机无 pip/mkdocs）——Markdown 结构变更均为纯章节增补，线上构建由 Cloudflare Pages 执行

### 12. Recommended Phase 3 work
1. Data Hub 字段缺口回填（见 E 节，需逐实体查证官方源）
2. 首页 FAQ schema（需真实高频问题支撑，不伪造）
3. Benchmark 页「Relevant models」反向关系章节（同 agents join 模式）
4. GSC 数据积累后做 query-driven 长尾页（任务书 PHASE 16）

---

## A. Main Site entity coverage
models 19 · agents 10 · apis 6 · benchmarks 10 · companies 6 · technologies 18 · comparisons 6 · guides 3 · research 14 · news 3 —— 全部集合有索引页 + 详情页，0 孤儿。

## B. Data Hub entity coverage
models 20 · companies 7 · agents 11 · apis 7 · pricing 7 · benchmarks 11 —— 全部实体有 JSON-LD @id 锚定主站实体。

## C. Missing relationships
- Data Hub models → Related Agents：20 篇中 4 篇有（其余 16 篇的模型未被任何 agent 声明为 underlying model——属真实数据状态，非缺链）
- Data Hub companies → Related Entities：1/7（主站 related_entities 多为空数组，待 Phase 3 从 foundation_models/open_models 反向派生）
- Benchmark → Relevant models：0（待 Phase 3 反向 join）

## D. Missing structured data
- 首页 FAQPage（无真实 FAQ 区，未伪造）✅ 合理缺省
- Benchmark 页无 JSON-LD（目前仅 Data Hub markdown）→ Phase 3 候选

## E. Important pages still requiring manual source verification
Data Hub 字段缺口（主站数据同步后仍缺，需逐实体官方源查证，**不得编造**）：
- **models**：Version 6/20、Architecture 9/20、Parameter Information 9/20、Maximum Output 10/20、Benchmark Results 9/20
- **apis**：Rate Limits 3/7、Regions 4/7、Structured Output 4/7
- **agents**：Underlying Models 6/11、Framework 6/11、Github 6/11
- **companies**：Cloud Distribution 1/7、Related Entities 1/7

---

**状态**：全部提交已推送 main；两站工作树干净；主站 build 114 页通过；断链/孤儿 0。
