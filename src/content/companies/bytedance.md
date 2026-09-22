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
ai_products:
  - Doubao (consumer AI assistant)
  - Volcengine Ark (AI API platform)
  - Seedance (video generation)
  - Seedream (image generation)
foundation_models:
  - doubao-seed-2-1-pro
  - doubao-seed-evolving
  - doubao-seed-2-1-turbo
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
related_entities:
  - volcengine
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

ByteDance is a Chinese technology company and the provider of the Doubao (豆包) AI assistant and the
Doubao Seed family of foundation models. Its API platform is Volcengine Ark (火山方舟), operated by
Beijing Volcano Engine Technology Co., Ltd. The ByteDance Seed research team publishes the official
Seed blog and maintains the ByteDance-Seed GitHub organization, which hosts open-source training
tooling such as VeOmni and Triton-distributed (but no Doubao LLM weights).

Doubao Seed models are closed-API: they are served through Ark in the cn-beijing region. The current
flagship text models are Doubao Seed 2.1 Pro (1M-token context as of September 2026), Doubao Seed
Evolving (a rolling model updated at least weekly for agent and coding use), and Doubao Seed 2.1 Turbo.
Video generation (Seedance) and image generation (Seedream) are separate dedicated models.
