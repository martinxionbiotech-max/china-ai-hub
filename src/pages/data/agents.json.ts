import { dumpCollection, jsonResponse } from '../../lib/data-dump';

export async function GET() {
  const body = await dumpCollection('agents', 'agents');
  return jsonResponse(body);
}
