---
image: "/images/ai/companies-bytedance.webp"
image_credit: "AI-generated illustration (Seedream)"
company_id: bytedance
company_name: ByteDance
description: "ByteDance (Doubao): the consumer AI assistant Doubao, Volcengine Ark AI API platform, Seedance video and Seedream image generation. Foundation models Doubao Seed 2.1 Pro / Evolving / Turbo."
aliases:
  - 字节跳动
  - Doubao
  - 豆包
headquarters: "No. 1 Building, Dazhongsi Plaza, No. 18A North Third Ring Road West, Haidian District, Beijing, China"
funding: "Privately held; funding rounds not officially disclosed as of 2026-09-22."
ai_products:
  - Doubao (consumer AI assistant)
  - Volcengine Ark (AI API platform)
  - Seedance (video generation)
  - Seedream (image generation)
foundation_models:
  - doubao-seed-2-1-pro
  - doubao-seed-evolving
  - doubao-seed-2-1-turbo
agents:
  - doubao-app
  - coze
  - trae
api:
  - ark
cloud_distribution:
  - Volcengine Ark (cn-beijing)
major_releases:
  - name: Doubao Seed 2.1 family
    date: "2026-06-23"
    type: model_release
  - name: Doubao Seed 2.1 Pro with 1M context (260915)
    date: "2026-09"
    type: model_release
  - name: Doubao Seed Evolving (rolling weekly-updated model)
    date: "2026-06"
    type: model_release
open_source_projects:
  - VeOmni (ByteDance-Seed, scaling multimodal model training)
  - Triton-distributed (ByteDance-Seed)
official_documentation: https://docs.volcengine.com/docs/ark
official_website: https://www.bytedance.com/
related_entities: []
last_verified: "2026-09-20"
sources:
  - source_name: Ark (Volcengine) official documentation
    source_url: https://docs.volcengine.com/docs/ark/product-overview?lang=zh
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Ark official model list
    source_url: https://docs.volcengine.com/docs/ark/model-list?lang=zh
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Ark model release announcements
    source_url: https://docs.volcengine.com/docs/ark/model-release-announcement
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: ByteDance Seed official blog — Seed 2.1 release
    source_url: https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity
    source_type: official
    published_date: "2026-06-23"
    last_verified: "2026-09-20"
    confidence: high
  - source_name: ByteDance Seed GitHub organization
    source_url: https://github.com/ByteDance-Seed
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** ByteDance is the Chinese technology company behind the Doubao (豆包) consumer assistant and the [Doubao Seed](/models/doubao-seed-2-1-pro/) family of foundation models, served through the Volcengine Ark AI API platform. **Why it matters.** Doubao is the largest-scale example of a closed-API strategy in China — no Doubao LLM weights are public, so every user routes through ByteDance's own infrastructure. **Key characteristics.** Flagship text models Doubao Seed 2.1 Pro (1M context), Evolving (rolling weekly updates) and Turbo; separate Seedance video and Seedream image generation models. **What a professional should know.** Serving is cn-beijing-only via [Ark](/api/ark/), and the premium pricing (¥6.00/¥30.00 per 1M tokens for Seed 2.1 Pro) is the highest in the database — so it is a China-region, generation-premium offering rather than a budget or self-hosting option.

ByteDance is a Chinese technology company and the provider of the Doubao (豆包) AI assistant and the
Doubao Seed family of foundation models. Its API platform is Volcengine Ark (火山方舟), operated by
Beijing Volcano Engine Technology Co., Ltd. The ByteDance Seed research team publishes the official
Seed blog and maintains the ByteDance-Seed GitHub organization, which hosts open-source training
tooling such as VeOmni and Triton-distributed (but no Doubao LLM weights).

Doubao Seed models are closed-API: they are served through Ark in the cn-beijing region. The current
flagship text models are Doubao Seed 2.1 Pro (1M-token context as of September 2026), Doubao Seed
Evolving (a rolling model updated at least weekly for agent and coding use), and Doubao Seed 2.1 Turbo.
Video generation (Seedance) and image generation (Seedream) are separate dedicated models.

## Why it matters

China AI Hub analysis: ByteDance is the purest expression of the closed-API model in the database — it publishes open training *tooling* (VeOmni, Triton-distributed) but no open model weights, in deliberate contrast to DeepSeek, Alibaba Cloud and Zhipu AI, and that position shapes its structural role — ByteDance competes on consumer reach ([Doubao App](/agents/doubao-app/)) and on generation (Seedance/Seedream), not on the open-weight or price-floor axis. China AI Hub analysis indicates Doubao's distinctiveness is the consumer-to-model vertical integration: the same Seed models that power the Doubao assistant are sold through Ark, which is why its pricing reflects a generation-premium strategy rather than a cost-minimization one. China AI Hub analysis indicates ByteDance's open-tooling-but-closed-weights posture (VeOmni and Triton-distributed open, Doubao weights closed) is a deliberate line — it shares training infrastructure to recruit researchers while keeping serving economics fully proprietary.

## Entity hub

### Models

- [Doubao Seed 2.1 Pro](/models/doubao-seed-2-1-pro/)
- [Doubao Seed 2.1 Turbo](/models/doubao-seed-2-1-turbo/)
- [Doubao Seed Evolving](/models/doubao-seed-evolving/)

### Products

- [Doubao (consumer AI assistant)](/agents/doubao-app/)
- [Volcengine Ark (AI API platform)](/api/ark/)

### API

- [Volcengine Ark](/api/ark/)

### Agents

- [Doubao](/agents/doubao-app/)
- [Coze](/agents/coze/)
- [Trae](/agents/trae/)

### Research / Technology

- [AI Agents](/technology/ai-agents/)
- [Computer Use](/technology/computer-use/)
- [Long Context](/technology/long-context/)
- [Multimodal AI](/technology/multimodal-ai/)
- [Tool Calling](/technology/tool-calling/)

### Comparisons

- [Doubao Seed 2.1 Pro vs MiniMax M3](/comparisons/doubao-seed-2-1-pro-vs-minimax-m3/)

### Pricing

- [ByteDance pricing](/pricing/bytedance/)

## What is uncertain

- Funding rounds are not officially disclosed.
- No Doubao LLM weights are public — every user routes through ByteDance's own infrastructure.

## Sources

| evidence_id | source_name | source_url | source_type | published | verified | confidence | conflict |
|---|---|---|---|---|---|---|---|
| src-companies-bytedance-1 | Ark (Volcengine) official documentation | https://docs.volcengine.com/docs/ark/product-overview?lang=zh | Official documentation | — | 2026-09-20 | high | — |
| src-companies-bytedance-2 | Ark official model list | https://docs.volcengine.com/docs/ark/model-list?lang=zh | Official documentation | — | 2026-09-20 | high | — |
| src-companies-bytedance-3 | Ark model release announcements | https://docs.volcengine.com/docs/ark/model-release-announcement | Official documentation | — | 2026-09-20 | high | — |
| src-companies-bytedance-4 | ByteDance Seed official blog — Seed 2.1 release | https://seed.bytedance.com/en/blog/seed2-1-officially-released-advancing-ai-productivity | Official | 2026-06-23 | 2026-09-20 | high | — |
| src-companies-bytedance-5 | ByteDance Seed GitHub organization | https://github.com/ByteDance-Seed | Official documentation | — | 2026-09-20 | high | — |

*Labels used above: **Official fact** (from Ark documentation and ByteDance Seed's official blog/GitHub), **Vendor-reported claim** (model capabilities and pricing published by ByteDance), and **China AI Hub analysis** (our synthesis, always introduced as such).*
