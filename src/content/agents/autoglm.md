---
image: "/images/ai/agents-autoglm.webp"
image_credit: "AI-generated illustration (Seedream)"
agent_id: autoglm
agent_name: AutoGLM
company: zhipu-ai
description: "Zhipu AI's open-source phone-use autonomous agent (repo Open-AutoGLM). The VLM sees the phone screen, plans a chain-of-thought action sequence, and executes it via ADB (Android), HDC (HarmonyOS NEXT) or WebDriverAgent (iOS). First phone agent with true Phone Use capabilities (2024-10-25); AutoGLM 2.0 commercial product runs agents in cloud virtual phones. Research/learning use."
agent_type: autonomous
underlying_models: []
framework: "Python framework (PhoneAgent API + CLI); model AutoGLM-Phone-9B built on the GLM-4.1V-9B family"
tool_calling: true
computer_use: true
memory: false
planning: true
api: true
pricing: "Open-source framework free. AutoGLM-Phone API (BigModel model id autoglm-phone) limited-time free as of 2026-09-20; paid price after promotion not publicly disclosed."
deployment: both
open_source: true
license: "Apache-2.0 (code); MIT (models)"
github: https://github.com/zai-org/Open-AutoGLM
documentation: https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone.md
use_cases:
  - Food delivery ordering and reordering
  - Product purchase and cross-platform price comparison
  - Travel planning (routes, flights/trains, hotels)
  - News, music, video playback and social interactions
  - Cloud-phone batch operations - notifications, likes, customer-service and attendance workflows
  - AI-native phone research and GUI agent development
limitations:
  - Research/learning use only; prohibited for illegal information gathering
  - Sensitive pages (payment, password, banking) cannot be screenshotted - agent auto-detects and requests human takeover
  - Android 7.0+ with developer mode + USB debugging required; ADB Keyboard needed for Android text input
  - iOS support requires separate WebDriverAgent setup
  - Local deployment needs ~24GB+ VRAM GPU
  - No persistent-memory feature documented in the README
last_verified: "2026-09-20"
sources:
  - source_name: Open-AutoGLM GitHub repository
    source_url: https://github.com/zai-org/Open-AutoGLM
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: AutoGLM Goes Open Source blog
    source_url: https://autoglm.z.ai/blog
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: AutoGLM-Phone model card (Hugging Face)
    source_url: https://huggingface.co/zai-org/AutoGLM-Phone-9B
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: BigModel AutoGLM-Phone API docs
    source_url: https://docs.bigmodel.cn/cn/guide/models/vlm/autoglm-phone.md
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
**What it is.** AutoGLM is Zhipu AI's open-source phone-use agent: a vision-language model reads the phone screen, plans a chain-of-thought action sequence, and executes it over ADB (Android), HDC (HarmonyOS NEXT) or WebDriverAgent (iOS). **Why it matters.** It was the first phone agent with true Phone Use capabilities (2024-10-25) and is the only tracked Chinese agent built specifically around GUI phone operation. **Key characteristics.** Ships as a Python framework built on the AutoGLM-Phone-9B VLM (GLM-4.1V-9B family); free framework, Apache-2.0 code / MIT models; a hosted API on BigModel was free during its promotional period as of 2026-09-20. **What a professional should know.** It is research/learning-only by license, auto-detects sensitive screens (payment, password, banking) and requests human takeover, and needs ~24GB+ VRAM for local deployment.

AutoGLM is Zhipu AI's open-source phone-use agent ([Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)): the vision-language model reads the phone screen, plans a chain-of-thought action sequence, and executes it over ADB (Android), HDC (HarmonyOS NEXT) or WebDriverAgent (iOS). It was the first phone agent with true Phone Use capabilities (2024-10-25); the commercial AutoGLM 2.0 product runs the same approach on cloud virtual phones.

The framework ships as a Python package (PhoneAgent API + CLI) built around AutoGLM-Phone-9B, a 9B VLM from the GLM-4.1V-9B family. The open-source framework is free, and the hosted AutoGLM-Phone API on BigModel was free during its promotional period as of 2026-09-20.

Local deployment needs a GPU with roughly 24GB+ VRAM; Android use requires developer mode and USB debugging, and iOS needs a separate WebDriverAgent setup. See the [Zhipu AI](/companies/zhipu-ai/) profile for the wider GLM ecosystem.

## Why it matters

AutoGLM is the purest demonstration of [computer use](/technology/computer-use/) as a product in the Chinese ecosystem: its capability is inseparable from the underlying VLM's screen-reading and action-planning ability, rather than from any API or tool registry. That makes it the reference for how GUI operation depends on a vision model's grounding quality — a relationship the database captures by tying the agent to Zhipu AI while the GLM-4.1V-9B lineage sits outside the tracked flagship models. China AI Hub analysis indicates AutoGLM matters less as a production tool (it is research/learning-licensed) and more as the clearest evidence that phone-level computer use is technically mature in China's open ecosystem.

## Field reference

| Field | Value | Evidence type |
|---|---|---|
| Underlying model | AutoGLM-Phone-9B (GLM-4.1V-9B family) | Official |
| Target users | Researchers and developers (research/learning use) | Official |
| Platform | Python framework (PhoneAgent API + CLI); AutoGLM 2.0 cloud product | Official |
| OS | Android (ADB), HarmonyOS NEXT (HDC), iOS (WebDriverAgent) | Official |
| Browser / computer use | Phone GUI computer use | Vendor-reported |
| Coding | Not publicly documented | Not publicly documented |
| Autonomous task execution | Yes (chain-of-thought planning) | Vendor-reported |
| MCP | Not publicly documented | Not publicly documented |
| Tool calling | Yes | Official |
| Memory | No | Official |
| Workflow | Screen reading → chain-of-thought planning → action execution | Vendor-reported |
| API | Yes (BigModel `autoglm-phone`) | Official |
| Pricing | Framework free; API limited-time free as of 2026-09-20 | Vendor-reported |
| Region | China (BigModel) | Official |
| Open-source | Yes — Apache-2.0 (code), MIT (models) | Official |
| Deployment | Cloud and self-hosted | Official |
| Limitations | Research/learning only; ~24GB+ VRAM for local; sensitive screens need human takeover | Official |
| Source | [Open-AutoGLM GitHub](https://github.com/zai-org/Open-AutoGLM) | Official |
| Last verified | 2026-09-20 | Official |

*Labels used above: **Official fact** (from the Open-AutoGLM GitHub repo, AutoGLM blog and model card), **Vendor-reported claim** (capability and pricing statements by Zhipu AI), and **China AI Hub analysis** (our synthesis, always introduced as such).*
