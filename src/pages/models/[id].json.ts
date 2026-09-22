import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { jsonResponse } from '../../lib/data-dump';

export async function getStaticPaths() {
  const models = await getCollection('models');
  return models.map((m) => ({ params: { id: m.id }, props: { model: m } }));
}

export const GET: APIRoute = async ({ props, site }) => {
  const m = (props as { model: { id: string; data: Record<string, unknown> } }).model;
  const base = (site?.origin ?? 'https://chinaaihub.com').replace(/\/$/, '');
  const [allBenchmarks, allAgents] = await Promise.all([
    getCollection('benchmarks'),
    getCollection('agents'),
  ]);
  const mid = String(m.data.model_id ?? '');
  const relatedBenchmarks = allBenchmarks
    .filter((b) => b.data.evaluations.some((e) => e.model === mid))
    .map((b) => ({ id: b.id, name: b.data.benchmark_name, url: `${base}/benchmarks/${b.id}/` }));
  const relatedAgents = allAgents
    .filter((a) => (a.data.underlying_models ?? []).includes(mid))
    .map((a) => ({ id: a.id, name: a.data.agent_name, url: `${base}/agents/${a.id}/` }));
  return jsonResponse({
    id: m.id,
    url: `${base}/models/${m.id}/`,
    ...m.data,
    _relations: {
      provider: `${base}/companies/${String(m.data.provider)}/`,
      benchmarks: relatedBenchmarks,
      agents: relatedAgents,
    },
  });
};
