---
image: "/images/ai/companies-zhipu-ai.webp"
image_credit: "AI-generated illustration (Seedream)"
company_id: zhipu-ai
company_name: Zhipu AI
description: "Zhipu AI (Beijing; international operator Z.AI in Singapore): Z.ai / GLM assistant, BigModel platform, GLM Coding Plan, AutoGLM phone agent, GLM-Image / CogView and CogVideoX. Foundation models GLM-5.3, GLM-5.3-Flash and GLM-5.2."
aliases:
  - 智谱
  - Z.ai
  - BigModel
  - Zhipu
headquarters: "China platform: Beijing Zhipu Huazhang Technology Co., Ltd. (北京智谱华章科技股份有限公司), Beijing, China; international Z.ai operator: JINGSHENG HENGXING TECHNOLOGY PTE.LTD, 10 Anson Road, #26-03 International Plaza, Singapore 079903"
funding: "No official funding disclosure located as of 2026-09-22 (IPO/funding reports circulate in media but are not confirmed on official channels)."
ai_products:
  - Z.ai / GLM chat assistant
  - BigModel platform (China)
  - GLM Coding Plan
  - AutoGLM phone agent
  - GLM-Image / CogView (image)
  - CogVideoX (video)
foundation_models:
  - glm-5.3
  - glm-5.3-flash
  - glm-5.3-flashx
  - glm-5.2
agents:
  - autoglm
  - glm-coding-plan
api:
  - zai
open_models:
  - glm-5.3
major_releases:
  - name: GLM-5.3-Flash / FlashX
    date: "2026-08-26"
    type: model_release
  - name: GLM-5.3
    date: "2026-08-18"
    type: model_release
  - name: GLM-5.2
    date: "2026-06-16"
    type: model_release
open_source_projects:
  - GLM-5.3 (Apache-2.0)
  - GLM-5.3-Flash (Apache-2.0)
  - GLM-5.2 (Apache-2.0)
  - GLM-OCR
  - GLM-V
  - GLM-Image
  - GLM-ASR
  - CogVideo
  - Open-AutoGLM
official_documentation: https://docs.z.ai/
official_website: https://z.ai/
related_entities: []
last_verified: "2026-09-20"
sources:
  - source_name: Z.ai docs — GLM-5.3 model page
    source_url: https://docs.z.ai/guides/llm/glm-5.3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Z.ai docs — GLM-5.3-Flash model page
    source_url: https://docs.z.ai/guides/vlm/glm-5.3-flash
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Z.ai release notes
    source_url: https://docs.z.ai/release-notes/new-released
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: GLM-5 GitHub repository
    source_url: https://github.com/zai-org/GLM-5
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---

**What it is.** Zhipu AI is the company behind the GLM model family, sold internationally as Z.ai and in China as BigModel. **Why it matters.** Zhipu ships genuinely open Apache-2.0 weights ([GLM-5.3](/models/glm-53/), [GLM-5.3-Flash](/models/glm-53-flash/), GLM-5.2) while pairing them with an unusually broad agent surface ([AutoGLM](/agents/autoglm/), [GLM Coding Plan](/agents/glm-coding-plan/)). **Key characteristics.** GLM-5.3 is a 744B/40B-active MoE with 1M-token context and always-on reasoning; GLM-5.3-Flash was the first open frontier model combining sparse and linear attention. **What a professional should know.** The Apache-2.0 labeling comes from GitHub metadata — the README has no separate weights-license section, so verify the per-model Hugging Face card before commercial reuse.

Zhipu AI (智谱) develops the GLM model family, sold internationally as Z.ai and in China as BigModel
(open.bigmodel.cn). The current flagship is GLM-5.3 (released 2026-08-18, 1M context, open weights on
Hugging Face), alongside the multimodal coding model GLM-5.3-Flash/FlashX (2026-08-26).

The international operator is JINGSHENG HENGXING TECHNOLOGY PTE.LTD (Singapore); the China platform is
run by 北京智谱华章科技股份有限公司. The company also offers the GLM Coding Plan subscription and the
Open-AutoGLM phone-agent framework. A founding date is not stated on the official pages fetched.

## Why it matters

Zhipu AI's structural role is the open-weight-plus-agents combination: it is the only major lab pairing Apache-2.0 open weights with a first-party phone-use agent (AutoGLM) and a coding-plan product that routes third-party tools (Claude Code, Codex, Cursor, OpenClaw) onto GLM models. That positions it as the strongest open alternative for builders who want both downloadable weights and a managed agent layer. China AI Hub analysis indicates Zhipu's distinctive bet is breadth of *surface* — models, phone agents, coding plans, image/video — unified by the GLM family, with openness (Apache-2.0) as the shared thread.

## Entity hub

### Models

- [GLM-5.3](/models/glm-53/)
- [GLM-5.3-Flash](/models/glm-53-flash/)
- [GLM-5.3-FlashX](/models/glm-53-flashx/)
- [GLM-5.2](/models/glm-52/)

### Products

- [GLM Coding Plan](/agents/glm-coding-plan/)
- [AutoGLM](/agents/autoglm/)
- [BigModel platform](/api/zai/)

### API

- [Z.ai](/api/zai/)

### Agents

- [AutoGLM](/agents/autoglm/)
- [GLM Coding Plan](/agents/glm-coding-plan/)

### Research / Technology

- [AI Agents](/technology/ai-agents/)
- [Computer Use](/technology/computer-use/)
- [Mixture of Experts](/technology/mixture-of-experts/)
- [Reasoning Models](/technology/reasoning-models/)
- [GLM and Agent-Oriented AI](/research/glm-agent-oriented-ai/)

### Comparisons

- [DeepSeek-V4.1-Flash vs GLM-5.3-Flash](/comparisons/deepseek-v4-1-flash-vs-glm-53-flash/)
- [Qwen3.8-Max vs GLM-5.3](/comparisons/qwen38-max-vs-glm-53/)

### Pricing

- [Zhipu AI pricing](/pricing/zhipu-ai/)

### Benchmarks

- [AutomationBench](/benchmarks/automationbench/)
- [CyberGym](/benchmarks/cybergym/)
- [DeepSWE](/benchmarks/deepswe/)
- [Terminal-Bench](/benchmarks/terminal-bench/)

*Labels used above: **Official fact** (from Z.ai docs and the GLM-5 GitHub repository), **Vendor-reported claim** (model capabilities and pricing published by Zhipu AI), and **China AI Hub analysis** (our synthesis, always introduced as such).*
