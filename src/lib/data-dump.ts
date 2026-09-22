/* Shared helper for machine-readable JSON outputs (audit P1-7). */
import { getCollection, type CollectionKey } from 'astro:content';

export async function dumpCollection(name: CollectionKey, label: string) {
  const entries = await getCollection(name);
  const records = entries.map((e) => ({ id: e.id, ...e.data }));
  return {
    name: `China AI Hub ${label} collection`,
    description: `Machine-readable dump of the China AI Hub ${label} collection. Every record keeps its verified fields, source-type labels and last_verified date.`,
    generated: new Date().toISOString().slice(0, 10),
    count: records.length,
    records,
  };
}

export function jsonResponse(body: unknown) {
  return new Response(JSON.stringify(body, null, 2), {
    headers: { 'Content-Type': 'application/json; charset=utf-8' },
  });
}
