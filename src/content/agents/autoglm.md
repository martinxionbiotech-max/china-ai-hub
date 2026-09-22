---
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
AutoGLM is Zhipu AI's open-source phone-use agent ([Open-AutoGLM](https://github.com/zai-org/Open-AutoGLM)): the vision-language model reads the phone screen, plans a chain-of-thought action sequence, and executes it over ADB (Android), HDC (HarmonyOS NEXT) or WebDriverAgent (iOS). It was the first phone agent with true Phone Use capabilities (2024-10-25); the commercial AutoGLM 2.0 product runs the same approach on cloud virtual phones.

The framework ships as a Python package (PhoneAgent API + CLI) built around AutoGLM-Phone-9B, a 9B VLM from the GLM-4.1V-9B family. The open-source framework is free, and the hosted AutoGLM-Phone API on BigModel was free during its promotional period as of 2026-09-20.

Local deployment needs a GPU with roughly 24GB+ VRAM; Android use requires developer mode and USB debugging, and iOS needs a separate WebDriverAgent setup. See the [Zhipu AI](/companies/zhipu-ai/) profile for the wider GLM ecosystem.
