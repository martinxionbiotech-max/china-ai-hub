---
image: "/images/ai/technologies-tool-calling.webp"
image_credit: "AI-generated illustration (Seedream)"
slug: tool-calling
title: Tool Calling
definition: "Tool calling is a model capability where the model, instead of only writing text, emits structured requests to invoke external tools — search, calculators, code execution, APIs — and incorporates their results into its response."
related_models:
  - deepseek-v4-pro
  - deepseek-v4-1-flash
  - qwen3.8-max
  - kimi-k3
  - minimax-m3
  - doubao-seed-2-1-pro
related_companies:
  - deepseek
  - alibaba-cloud
  - moonshot-ai
  - minimax
  - bytedance
related_technologies:
  - function-calling
  - mcp
  - ai-agents
related_guides: [how-to-choose-a-chinese-ai-model]
last_verified: "2026-09-22"
sources:
  - source_name: "OpenAI — Function calling guide"
    source_url: "https://platform.openai.com/docs/guides/function-calling"
    source_type: official
  - source_name: "Anthropic — Tool use documentation"
    source_url: "https://docs.anthropic.com/en/docs/build-with-claude/tool-use"
    source_type: official
---

## Technical background

Tool calling arrived with the 2023 wave of chat APIs (OpenAI function calling, then Anthropic tool use) and quickly became the backbone of agentic systems: the model decides what to call, the runtime executes, the result returns to context. It is now a standard capability column in every model database.

## How it works

The developer declares tools as JSON schemas (name, description, parameters). The API may accept tools in the request; the model responds either with text or with a structured tool-call object; the runtime executes the tool and appends the result as a tool message. The model then continues, possibly issuing further calls in a loop. Some APIs support parallel tool calls.

## Why it matters

Tool calling is the primitive that turns models into actors: without it, no browser control, no code execution, no database writes. It also improves factual reliability — a model that can call a calculator or a search API makes fewer arithmetic and knowledge errors.

## Chinese adoption

Tool calling is broadly listed across the China AI Hub database (last verified 2026-09-22). Models listing it include DeepSeek-V4-Pro and V4.1-Flash, Qwen3.8-Max, Kimi K3, MiniMax M3 (and M2.7), and the Doubao Seed 2.1 series. On the agent side, seven of ten tracked Chinese agents list MCP support, and coding agents such as Qwen Code, Kimi Code and MiniMax Code implement tool loops as their core design.

## Major Chinese companies and models

- **DeepSeek** — V4-Pro and V4.1-Flash list tool calling plus structured output.
- **Alibaba Cloud** — Qwen3.8-Max lists tool calling.
- **Moonshot AI** — Kimi K3 lists tool calling and structured output.
- **MiniMax** — M3 and M2.7 list tool calling.
- **ByteDance** — Doubao Seed 2.1 Pro lists tool calling and computer use.

## Practical applications

Agent frameworks, coding assistants (file edit, test run, git), data pipelines (SQL, HTTP APIs), search grounding, and structured data extraction.

## Limitations

Tool reliability varies with schema design and model tier; long loops drift and burn tokens; parallel call support is inconsistent across vendors; and each tool is new attack surface.

## Deployment considerations

Keep tool descriptions precise (models read them literally); validate arguments before execution; add loop budgets and approval gates for irreversible actions; test tool choice on your real schemas, not demo ones.

## Future development

Tool calling is merging with computer use (operating arbitrary software through screens), standardized tool registries via MCP, and model-native tool selection improvements.
