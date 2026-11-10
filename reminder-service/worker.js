/* A-Z reminder service: a Cloudflare Worker with a D1 database.
   It stores only a push address, a time zone and reminder times like "06:40|12345".
   No names, no task words, nothing about children. Once a minute it sends an empty
   push to each device that has a reminder due; the device shows the details itself. */
export default {
  async fetch(req, env) {
    const cors = { 'Access-Control-Allow-Origin': env.ALLOW_ORIGIN || '*', 'Access-Control-Allow-Methods': 'POST, OPTIONS', 'Access-Control-Allow-Headers': 'content-type' };
    if (req.method === 'OPTIONS') return new Response(null, { headers: cors });
    const url = new URL(req.url);
    try {
      if (req.method === 'POST' && url.pathname === '/subscribe') {
        const b = await req.json(), sub = b && b.sub;
        if (!sub || typeof sub.endpoint !== 'string' || !/^https:\/\//.test(sub.endpoint) || sub.endpoint.length > 1000) return new Response('bad request', { status: 400, headers: cors });
        const times = (Array.isArray(b.times) ? b.times : []).filter(t => /^\d\d:\d\d\|[0-6]{1,7}$/.test(t)).slice(0, 200);
        const tz = String(b.tz || 'UTC').slice(0, 64);
        try { new Intl.DateTimeFormat('en-US', { timeZone: tz }); } catch (e) { return new Response('bad time zone', { status: 400, headers: cors }); }
        await env.DB.prepare('INSERT INTO subs (endpoint, tz, times, updated) VALUES (?1, ?2, ?3, ?4) ON CONFLICT(endpoint) DO UPDATE SET tz = ?2, times = ?3, updated = ?4')
          .bind(sub.endpoint, tz, JSON.stringify(times), Date.now()).run();
        return new Response('ok', { headers: cors });
      }
      if (req.method === 'POST' && url.pathname === '/unsubscribe') {
        const b = await req.json();
        await env.DB.prepare('DELETE FROM subs WHERE endpoint = ?1').bind(String((b && b.endpoint) || '')).run();
        return new Response('ok', { headers: cors });
      }
      return new Response('A-Z reminders', { headers: cors });
    } catch (e) { return new Response('error', { status: 500, headers: cors }); }
  },
  async scheduled(event, env, ctx) {
    const now = new Date(event.scheduledTime);
    const { results } = await env.DB.prepare('SELECT endpoint, tz, times FROM subs').all();
    const jobs = [];
    for (const r of results || []) {
      if (!isDue(r.tz, JSON.parse(r.times || '[]'), now)) continue;
      jobs.push(sendPush(r.endpoint, env).then(st => (st === 404 || st === 410) ? env.DB.prepare('DELETE FROM subs WHERE endpoint = ?1').bind(r.endpoint).run() : null).catch(() => null));
    }
    ctx.waitUntil(Promise.all(jobs));
  }
};
export function isDue(tz, times, now) {
  const p = Object.fromEntries(new Intl.DateTimeFormat('en-US', { timeZone: tz, hour12: false, hour: '2-digit', minute: '2-digit', weekday: 'short' }).formatToParts(now).map(x => [x.type, x.value]));
  const hm = `${p.hour === '24' ? '00' : p.hour}:${p.minute}`, dow = String(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'].indexOf(p.weekday));
  return times.some(t => { const [h, days] = t.split('|'); return h === hm && days.includes(dow); });
}
async function sendPush(endpoint, env) {
  const jwt = await vapidJwt(new URL(endpoint).origin, env.VAPID_SUBJECT || 'mailto:reminders@example.com', env.VAPID_PRIVATE_JWK);
  const res = await fetch(endpoint, { method: 'POST', headers: { TTL: '600', Urgency: 'high', Authorization: `vapid t=${jwt}, k=${env.VAPID_PUBLIC}`, 'Content-Length': '0' } });
  return res.status;
}
const b64u = buf => btoa(String.fromCharCode(...new Uint8Array(buf))).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
const txt = s => b64u(new TextEncoder().encode(s));
export async function vapidJwt(aud, sub, jwkText) {
  const key = await crypto.subtle.importKey('jwk', JSON.parse(jwkText), { name: 'ECDSA', namedCurve: 'P-256' }, false, ['sign']);
  const head = txt(JSON.stringify({ typ: 'JWT', alg: 'ES256' })), body = txt(JSON.stringify({ aud, exp: Math.floor(Date.now() / 1000) + 12 * 3600, sub }));
  const sig = await crypto.subtle.sign({ name: 'ECDSA', hash: 'SHA-256' }, key, new TextEncoder().encode(head + '.' + body));
  return `${head}.${body}.${b64u(sig)}`;
}
