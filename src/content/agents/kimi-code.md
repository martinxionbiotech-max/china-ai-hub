---
agent_id: kimi-code
agent_name: Kimi Code
company: moonshot-ai
description: "Moonshot AI's coding agent - open-source terminal CLI with Desktop app and VS Code extension, built on the Kimi K3 model. One subscription, code anywhere."
agent_type: coding
underlying_models:
  - kimi-k3
  - kimi-k2.7-code
  - kimi-k2.7-code-highspeed
  - kimi-k2.6
framework: "TypeScript terminal agent (pi-tui); succeeds the deprecated Python kimi-cli"
tool_calling: true
browser_use: true
computer_use: true
mcp: true
memory: true
planning: true
multi_agent: true
api: true
pricing: "Included in Kimi membership Plus and above (Plus $15 / Pro $31 / Max $79 / Ultra $159 per month); free tier has no coding quota. Pay-as-you-go Open Platform API available separately."
deployment: both
open_source: true
license: "MIT (kimi-code); Apache-2.0 (legacy kimi-cli)"
github: https://github.com/MoonshotAI/kimi-code
documentation: https://moonshotai.github.io/kimi-code/en/
use_cases:
  - Understanding unfamiliar codebases
  - Feature implementation and bug fixing
  - Writing tests and refactoring
  - Batch file processing
  - Long-horizon whole-repo work via 1M-token context
  - Video-input tasks (screen recording to code)
  - Scheduled and background tasks
  - IDE-driven sessions (VS Code, Zed, JetBrains via ACP)
limitations:
  - kimi-cli (previous generation) is being wound down; Kimi Code CLI auto-migrates its config and sessions
  - No dedicated sandboxing; runs on the local machine with approval gates (manual / yolo / auto modes)
  - Cloud inference only (managed endpoints api.kimi.com/coding/v1 and api.kimi.ai/coding/v1); not self-hostable as a model service
  - macOS Computer Use requires Accessibility and Screen Recording permissions
  - Windows install requires Git for Windows
  - Coding quota shared across devices; devices inactive over 30 days are unbound
last_verified: "2026-09-20"
sources:
  - source_name: MoonshotAI/kimi-code GitHub repository
    source_url: https://github.com/MoonshotAI/kimi-code
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi Code documentation (moonshotai.github.io)
    source_url: https://moonshotai.github.io/kimi-code/en/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi Code product docs (kimi.com)
    source_url: https://www.kimi.com/code/docs/en/
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: Kimi membership pricing page
    source_url: https://www.kimi.ai/membership/pricing
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
