import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

/* llms.txt for AI crawlers and LLM-oriented tooling (llmstxt.org spec). */
export const GET: APIRoute = async ({ site }) => {
  const base = (site?.origin ?? 'https://chinaaihub.com').replace(/\/$/, '');
  const [models, agents, companies, apis, pricing, benchmarks] = await Promise.all([
    getCollection('models'),
    getCollection('agents'),
    getCollection('companies'),
    getCollection('apis'),
    getCollection('pricing'),
    getCollection('benchmarks'),
  ]);

  const L: string[] = [];
  L.push('# China AI Hub');
  L.push('');
  L.push(
    '> Independent English-language database and analysis of China AI models, agents, APIs, pricing and benchmarks. All facts are sourced, date-stamped and labeled by source type (vendor-reported vs independent); analysis is kept separate from data.'
  );
  L.push('');
  L.push('## Core pages');
  L.push(`- [Home](${base}/): Overview of the China AI Hub database and what it covers.`);
  L.push(`- [Models](${base}/models/): Filterable database of Chinese AI models.`);
  L.push(`- [Agents](${base}/agents/): Chinese AI coding and general-purpose agents.`);
  L.push(`- [Companies](${base}/companies/): Chinese AI companies and their products.`);
  L.push(`- [API](${base}/api/): Chinese AI API endpoints and their capabilities.`);
  L.push(`- [Pricing](${base}/pricing/): Normalized API pricing across providers.`);
  L.push(`- [Benchmarks](${base}/benchmarks/): Benchmark evaluations of Chinese AI models.`);
  L.push(`- [About](${base}/about/): Sourcing policy, source tiers and methodology.`);
  L.push('');
  L.push('## Models');
  for (const m of models) {
    const d = m.data;
    const parts = [`${d.model_name} by ${d.provider}`];
    if (d.context_window != null) parts.push(`${d.context_window.toLocaleString()}-token context`);
    if (d.open_weight != null) parts.push(d.open_weight ? 'open weights' : 'closed weights');
    parts.push(`last verified ${d.last_verified}`);
    L.push(`- [${d.model_name}](${base}/models/${m.id}/): ${parts.join(', ')}.`);
  }
  L.push('');
  L.push('## Agents');
  for (const a of agents) {
    const d = a.data;
    const parts = [d.agent_type];
    if (d.open_source != null) parts.push(d.open_source ? 'open source' : 'proprietary');
    parts.push(`last verified ${d.last_verified}`);
    L.push(`- [${d.agent_name}](${base}/agents/${a.id}/): ${d.description} ${parts.join(' · ')}.`);
  }
  L.push('');
  L.push('## Companies');
  for (const c of companies) {
    const d = c.data;
    const parts: string[] = [];
    if (d.headquarters) parts.push(`based ${d.headquarters}`);
    if (d.foundation_models.length) parts.push(`models: ${d.foundation_models.join(', ')}`);
    L.push(`- [${d.company_name}](${base}/companies/${c.id}/): Chinese AI company${parts.length ? ` — ${parts.join(' · ')}` : ''}.`);
  }
  L.push('');
  L.push('## API');
  for (const a of apis) {
    const d = a.data;
    const parts = [`${d.api_type}`, d.endpoint ? d.endpoint : 'endpoint not listed'];
    L.push(`- [${d.api_id} API](${base}/api/${a.id}/): API by ${d.provider} — ${parts.join(' · ')}.`);
  }
  L.push('');
  L.push('## Pricing');
  for (const p of pricing) {
    const d = p.data;
    L.push(
      `- [${d.provider_id} API pricing](${base}/pricing/${p.id}/): ${d.models.length} model${
        d.models.length === 1 ? '' : 's'
      } listed in ${d.currency}, last verified ${d.last_verified}.`
    );
  }
  L.push('');
  L.push('## Benchmarks');
  for (const b of benchmarks) {
    const d = b.data;
    L.push(
      `- [${d.benchmark_name}${d.version ? ` v${d.version}` : ''}](${base}/benchmarks/${b.id}/): ${
        d.description ?? 'Benchmark evaluation of Chinese AI models'
      }.`
    );
  }
  L.push('');
  L.push('## Optional');
  L.push(`- [Sitemap](${base}/sitemap-index.xml): Full sitemap of all China AI Hub pages.`);
  L.push(`- [Data Hub](https://data.chinaaihub.com/): Structured data layer with entity records.`);

  return new Response(`${L.join('\n')}\n`, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
