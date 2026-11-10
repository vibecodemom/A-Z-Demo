/* A-Z service worker: keeps the app working offline and shows reminder notifications.
   Reminder words (names, task names) are saved on this device by the app. The reminder
   service only sends an empty "it's time" signal, and this file decides what to show. */
const CACHE = 'az-v1';
const SHELL = ['./', './index.html', './manifest.webmanifest', './icon-192.png', './icon-512.png', './apple-touch-icon.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE && k !== 'az-remind').map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const r = e.request; if (r.method !== 'GET') return;
  const u = new URL(r.url); if (u.origin !== location.origin) return;
  if (r.mode === 'navigate' || u.pathname.endsWith('/') || u.pathname.endsWith('.html')) {
    e.respondWith(fetch(r).then(res => { const cp = res.clone(); caches.open(CACHE).then(c => c.put(r, cp)); return res; })
      .catch(() => caches.match(r).then(m => m || caches.match('./index.html'))));
    return;
  }
  e.respondWith(caches.match(r).then(m => m || fetch(r)));
});
self.addEventListener('push', e => {
  e.waitUntil((async () => {
    let list = [];
    try { const c = await caches.open('az-remind'); const res = await c.match('az-reminders.json'); if (res) list = await res.json(); } catch (x) {}
    const now = new Date(), mins = now.getHours() * 60 + now.getMinutes(), dow = now.getDay();
    const due = list.filter(it => { const [h, m] = String(it.t).split(':').map(Number); const at = h * 60 + m - (it.b || 0); return (it.d || []).includes(dow) && Math.abs(at - mins) <= 3; });
    const opts = { icon: 'icon-192.png', badge: 'icon-192.png', renotify: true };
    if (!due.length) return self.registration.showNotification('A-Z', { ...opts, body: 'Time to check the list!', tag: 'az' });
    for (const it of due) await self.registration.showNotification(it.title, { ...opts, body: it.body || '', tag: 'az-' + it.t + '-' + it.title });
  })());
});
self.addEventListener('notificationclick', e => {
  e.notification.close();
  e.waitUntil(self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then(cs => { for (const c of cs) if ('focus' in c) return c.focus(); return self.clients.openWindow('./'); }));
});
