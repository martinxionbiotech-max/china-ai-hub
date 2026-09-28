---
image: "/images/ai/technologies-function-calling.webp"
image_credit: "AI-generated illustration (Seedream)"
slug: function-calling
title: Function Calling
definition: "Function calling is OpenAI's term for tool calling: a model capability in which the model produces a structured request (name plus arguments) to invoke a developer-defined function, so applications can execute real code in response to natural language."
related_models:
  - deepseek-v4-pro
  - deepseek-v4-1-flash
  - qwen3.8-max
  - kimi-k3
related_companies:
  - deepseek
  - alibaba-cloud
  - moonshot-ai
related_technologies:
  - tool-calling
related_guides: [how-to-choose-a-chinese-ai-model]
last_verified: "2026-09-22"
sources:
  - source_name: "OpenAI — Function calling guide"
    source_url: "https://platform.openai.com/docs/guides/function-calling"
    source_type: official
  - source_name: "DeepSeek — Function calling documentation"
    source_url: "https://api-docs.deepseek.com/guides/function_calling"
    source_type: official
---

## Technical background

"Function calling" and "tool calling" describe the same mechanism; the terminology split is historical. OpenAI introduced "function calling" in June 2023 in the Chat Completions API; Anthropic used "tool use"; the industry has since converged on "tools" as the umbrella term. Understanding both terms matters when reading vendor docs.

## How it works

Functions are declared as JSON Schema definitions. When the model decides a function is needed, it returns a structured object: function name plus a JSON arguments payload. The application executes the function and sends the result back as a function/tool message, after which the model continues. This round trip is the unit of an agent loop.

## Why it matters

Function calling converts language into structured, executable intent — the difference between a model that describes an action and one that triggers it. It underpins data extraction, database operations, and every agent framework.

## Chinese adoption

In the China AI Hub database (last verified 2026-09-22), DeepSeek documents function calling most explicitly: DeepSeek-V4-Pro and V4.1-Flash both list the capability, and DeepSeek maintains dedicated function-calling documentation compatible with OpenAI-style schemas. Other Chinese providers implement the equivalent under "tools" — Qwen3.8-Max, Kimi K3, MiniMax M3 and Doubao Seed 2.1 Pro all list tool calling. The API layer confirms this is the practical surface: Ark, Model Studio, Kimi and Z.ai each expose OpenAI-compatible function/tool calling with structured output on at least their flagship models.

## Major Chinese companies and models

- **DeepSeek** — V4-Pro and V4.1-Flash list function calling and structured output; official docs describe OpenAI-compatible invocation.

## Practical applications

Natural-language interfaces to internal APIs, structured data extraction from documents, CRM/ERP automation, and compatibility layers for applications built on OpenAI-style tool schemas.

## Limitations

JSON argument validity still needs validation (the model can emit malformed or wrong-typed arguments); schemas with many functions degrade selection accuracy; and nested or long argument payloads are error-prone.

## Deployment considerations

Validate and coerce arguments before execution; keep function sets small per request; prefer enums and tight schemas; and version your function definitions since models are sensitive to description changes.

## What the available evidence actually shows

The database records function/tool calling as a capability flag on the flagship models of all six tracked companies, and as an API surface on Ark, Model Studio, DeepSeek, Kimi and Z.ai — so the claim "function calling is broadly available across Chinese providers" is well evidenced. What is not evidenced is the reliability of schema adherence: no independent benchmark in the database measures structured-output validity or function-selection accuracy across these models. China AI Hub analysis indicates function calling is now a table-stakes compatibility layer — the meaningful differentiator has moved from "does it support it" to "how reliably does it emit valid arguments," which the database cannot yet answer.

## Future development

The distinction between function calling, tool use and MCP tools is collapsing into one capability surface; expect schema standards and tool registries to keep converging.

*Labels used above: **Official fact** (from OpenAI's and DeepSeek's function-calling docs and the China AI Hub database), **Vendor-reported claim** (capability flags), and **China AI Hub analysis** (our synthesis, always introduced as such).*
