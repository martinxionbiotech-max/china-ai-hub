---
benchmark_id: browsecomp
benchmark_name: BrowseComp
description: "Benchmark of browsing and retrieval ability: locating obscure information using web search and browsing."
evaluations:
  - benchmark: BrowseComp
    model: kimi-k3
    score: "91.2 (90.4 with full 1M context, no compaction)"
    metric: accuracy
    date: "2026-07"
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K3
  - benchmark: BrowseComp
    model: kimi-k2.5
    score: "60.6 (74.9 with context management; 78.4 Agent Swarm)"
    metric: accuracy
    source_type: vendor_reported
    source_url: https://github.com/MoonshotAI/Kimi-K2.5
  - benchmark: BrowseComp
    model: minimax-m3
    score: 83.5
    metric: accuracy
    date: "2026-06-01"
    source_type: vendor_reported
    source_url: https://www.minimax.cn/models/text/m3
limitations: "All scores are vendor-reported and not independently verified. Evaluation setups (context management, agent scaffolding) differ between vendors."
last_verified: "2026-09-20"
sources:
  - source_name: Kimi K3 GitHub README
    source_url: https://github.com/MoonshotAI/Kimi-K3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
  - source_name: MiniMax official M3 model page
    source_url: https://www.minimax.cn/models/text/m3
    source_type: official
    last_verified: "2026-09-20"
    confidence: high
---
Benchmark of browsing and retrieval ability: locating obscure information using web search and browsing. The table below lists 3 recorded evaluations across 3 models: kimi-k3, kimi-k2.5, minimax-m3. All entries are labeled by source type (vendor_reported) with links to the original publication. See the Limitations section for comparability caveats before citing any score.
