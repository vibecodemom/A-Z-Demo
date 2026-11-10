// Makes the pair of keys the reminder service uses to sign its pushes. Run once: node make-keys.mjs
const { subtle } = globalThis.crypto;
const kp = await subtle.generateKey({ name: 'ECDSA', namedCurve: 'P-256' }, true, ['sign', 'verify']);
const raw = new Uint8Array(await subtle.exportKey('raw', kp.publicKey));
const b64u = u8 => Buffer.from(u8).toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
console.log('VAPID_PUBLIC (goes in wrangler.toml and in the app):\n' + b64u(raw));
console.log('\nVAPID_PRIVATE_JWK (keep secret; paste when wrangler asks):\n' + JSON.stringify(await subtle.exportKey('jwk', kp.privateKey)));
