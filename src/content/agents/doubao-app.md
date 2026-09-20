---
agent_id: doubao-app
agent_name: Doubao
company: bytedance
description: "ByteDance's consumer AI assistant app (life & work companion) with multimodal chat, office task automation, desktop agent control, image/video creation, and Feishu integration. Mainland-China focused."
agent_type: platform
underlying_models: []
framework: "Built-in autonomous planning/executing agent; desktop virtual-desktop control (Doubao Work)"
tool_calling: true
browser_use: null
computer_use: true
mcp: null
memory: null
planning: true
multi_agent: null
api: false
pricing: "Free Basic tier; paid memberships: Standard 68 CNY/month (688/yr), Enhanced 200 CNY/month (2048/yr), Professional 500 CNY/month (5088/yr). Quota-based; extra creation packs and cloud storage sold separately."
deployment: cloud
open_source: false
license: null
github: null
documentation: https://www.doubao.com/download/desktop
use_cases:
  - Daily Q&A, explanations and life organization
  - "Study help: homework grading, concept learning"
  - "Office automation: documents, spreadsheets, PPTs, data analysis, code"
  - Agentic desktop automation (Doubao Work virtual desktop)
  - Image generation (Seedream 5.0) and video generation (Seedance 2.5)
  - Voice calls and photo recognition
  - Enterprise work via Feishu integration
limitations:
  - Consumer chat LLM is not publicly named in official sources; only creation models (Seedream 5.0 / Seedance 2.5) are stated for the Professional tier
  - Web/app is mainland-China focused; non-logged-in overseas sessions are redirected to Dola (which is itself geo-restricted)
  - Membership is quota-based; free tier quotas are limited; creation packs expire and do not roll over
  - "Official disclaimer: as an AI it may misunderstand or mislead; users advised to cross-check"
  - No public consumer API; developer access to Doubao models is via Volcengine Ark
last_verified: "2026-09-20"
sources:
  - source_name: Doubao official site (desktop/web features)
    source_url: https://www.doubao.com/download/desktop
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Apple App Store CN listing (iTunes API)
    source_url: https://itunes.apple.com/search?term=豆包&country=cn&entity=software
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Doubao paid-service agreement
    source_url: https://www.doubao.com/legal/ey01
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Volcengine Doubao LLM platform page
    source_url: https://www.volcengine.com/product/doubao
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
