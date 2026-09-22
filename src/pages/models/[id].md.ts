import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export async function getStaticPaths() {
  const models = await getCollection('models');
  return models.map((m) => ({ params: { id: m.id }, props: { model: m } }));
}

export const GET: APIRoute = async ({ props, site }) => {
  const m = (props as { model: { id: string; data: Record<string, unknown> } }).model;
  const d = m.data;
  const base = (site?.origin ?? 'https://chinaaihub.com').replace(/\/$/, '');
  const yesNo = (v: unknown) => (v === true ? 'Yes' : v === false ? 'No' : 'Unknown');
  const rows: string[] = [];
  const push = (k: string, v: unknown) => { if (v != null && v !== '') rows.push(`| ${k} | ${v} |`); };
  push('Model ID', d.model_id);
  push('Provider', d.provider);
  push('Model family', d.model_family);
  push('Release date', d.release_date);
  push('Status', d.status);
  push('Architecture', d.architecture);
  push('Context window', d.context_window != null ? `${d.context_window} tokens` : null);
  push('Open weights', yesNo(d.open_weight));
  push('License', d.license);
  push('Self-hosting', yesNo(d.self_hosting));
  push('API available', yesNo(d.api_available));
  const pricing = d.pricing as Record<string, unknown> | undefined;
  if (pricing?.input_price_per_1m != null) {
    push('API pricing', `$${pricing.input_price_per_1m} input / $${pricing.output_price_per_1m ?? '—'} output per 1M tokens (${pricing.currency})`);
  }
  push('Last verified', d.last_verified);
  const body = [
    `# ${d.model_name}`,
    '',
    `Source: [${base}/models/${m.id}/](${base}/models/${m.id}/)`,
    '',
    '| Field | Value |',
    '| --- | --- |',
    ...rows,
    '',
  ].join('\n');
  return new Response(body, { headers: { 'Content-Type': 'text/markdown; charset=utf-8' } });
};
