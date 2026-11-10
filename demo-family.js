/* ============================== Demo: a pretend family, saved only in this browser ==============================
   build.py adds this to the demo page, just before the app starts.
   Maya (code 1 1 1 1) and Leo (code 🍎 🐶 ⭐ 🚗). The grown-up passcode is 1 2 3 4. */
const DEMO_PIN = 'cc7d0b64da5fa9cefef6f91407ddabb93e1705ebf15176bb49cea3c30b0b26df';
function demoSeed() {
  try { if (localStorage.getItem(LS_KEY)) return; } catch (e) { return; }
  const kidsList = [
    { id: 'demo_maya', name: 'Maya', mode: 'kids', avatar: '🦊', color: 'ocean', codeType: 'numbers', code: '1|1|1|1', buddy: 'rocket', font: 'standard', order: 0 },
    { id: 'demo_leo', name: 'Leo', mode: 'little', avatar: '🦖', color: 'grass', codeType: 'pictures', code: '🍎|🐶|⭐|🚗', buddy: 'dino', font: 'standard', order: 1 }
  ];
  const data = { 'app/settings': { appName: 'A-Z', children: kidsList, setupDone: true, demo: true, pinHash: DEMO_PIN, sound: true, warnMin: 5, warnStyle: 'both', devoOn: true, allowRemove: true, playMin: 15, createdAt: todayStr() } };
  for (const k of kidsList) {
    const ch = makeChart(k.mode, true);
    const brush = ch.sections[0].steps.find(st => /brush/i.test(st.l)); if (brush) brush.time = k.mode === 'little' ? '06:50' : '06:40';
    const hw = ch.sections[1].steps.find(st => /homework/i.test(st.l)); if (hw) hw.time = '15:30';
    ch.sections[2].steps.unshift(S_('🚿', 'Shower', { time: '19:00', mins: [15] }));
    data['charts/' + k.id] = ch;
    for (let i = 1; i <= 6; i++) {
      const date = addDays(todayStr(), -i), dow = parseDs(date).getDay(), day = { done: {}, faces: {} };
      let n = 0;
      for (const s of ch.sections) if ((s.days || ALLDAYS).includes(dow)) for (const st of s.steps) {
        n++;
        if ((n + i) % 5 === 0) continue;
        if (st.type === 'checkin') day.faces[st.id] = (n + i) % 3 ? 'good' : 'notyet'; else day.done[st.id] = parseDs(date).getTime() + (7 + n) * 3600000;
      }
      day.feel = { [parseDs(date).getTime() + 16 * 3600000]: i % 3 ? 'calm' : 'wiggly' };
      const key = k.id + '_' + ymOf(date), m = data['months/' + key] || (data['months/' + key] = { childId: k.id, month: ymOf(date), days: {} });
      m.days[date] = day;
    }
  }
  data['play/demo_maya'] = { pet: { state: 'pet', style: 'cute', species: 'dragon', color: '#C3A6FF', name: 'Sparkle', food: 85, fun: 85, last: Date.now(), xp: 40, hatchCoins: 0, own: ['crown', 'cape'], worn: { head: 'crown', body: 'cape' }, seen: 'kid' }, spent: 0,
    world: { cells: { '2,2': { o: 'castle' }, '3,5': { o: 'tree' }, '5,1': { g: 'water', o: 'boat' }, '6,6': { h: ['brick', 'brick'] }, '1,7': { o: 'cow' } } } };
  try { localStorage.setItem(LS_KEY, JSON.stringify(data)); } catch (e) {}
}
function demoBanner() {
  if (!S.store) return '';
  const isDemo = S.settings && S.settings.demo;
  return `<div class="card demo stack"><p><b>👋 Welcome to the A-Z demo</b></p>
    <p class="small muted">${isDemo ? 'This is a pretend family. Tap Maya (code 1 1 1 1) or Leo (code 🍎 🐶 ⭐ 🚗). The grown-up passcode is 1 2 3 4.' : 'This is your own copy of A-Z.'} Everything saves only in this browser, and nothing is sent anywhere.</p>
    <div class="row">${confirmBtn('demo-reset', 'demoReset', 'Reset demo')}</div></div>`;
}
ACT.demoReset = () => { try { localStorage.removeItem(LS_KEY); localStorage.removeItem('az_wx'); } catch (e) {} location.reload(); };
demoSeed();
