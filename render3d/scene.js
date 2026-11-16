// Brio — piloto 3D em tempo real (Three.js). Cada quadro é calculado só a partir de t (determinístico),
// então o render é quadro a quadro, sem depender de relógio nem de placa de vídeo.
import * as THREE from "three";
import { RoundedBoxGeometry } from "three/addons/geometries/RoundedBoxGeometry.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";
import { OutputPass } from "three/addons/postprocessing/OutputPass.js";

const W = 1080, H = 1920, FPS = 30, DUR = 10;
const P = new URLSearchParams(location.search);
const SCALE = parseFloat(P.get("scale") || "1");     // 0.5 = prévia rápida
const RW = Math.round(W * SCALE), RH = Math.round(H * SCALE);

// ------------------------------------------------------------------ util
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lerp = (a, b, t) => a + (b - a) * t;
const ease = (x) => { x = clamp(x); return x * x * (3 - 2 * x); };
const eo = (x) => { x = clamp(x); return 1 - (1 - x) ** 3; };
const bo = (x) => { x = clamp(x); const c = 1.7; return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2; };
const prog = (t, s, d) => clamp((t - s) / d);
const C = { coral: 0xff5c3d, cream: 0xefe6da, navy: 0x2b2f5c, ink: 0x15151c, steel: 0xc9ccd4, rubber: 0x1d1e24, bench: 0x1b1c22, lilac: 0x9c8cff };

// ------------------------------------------------------------------ pose (vista lateral em px → mundo em m)
function ik(s, h, L1, L2) {
  const dx = h[0] - s[0], dy = h[1] - s[1];
  const d = Math.max(Math.min(Math.hypot(dx, dy), L1 + L2 - 1), Math.abs(L1 - L2) + 1);
  const a = Math.atan2(dy, dx), b = Math.acos((L1 * L1 + d * d - L2 * L2) / (2 * L1 * d));
  const c1 = [s[0] + L1 * Math.cos(a + b), s[1] + L1 * Math.sin(a + b)], c2 = [s[0] + L1 * Math.cos(a - b), s[1] + L1 * Math.sin(a - b)];
  return c1[1] > c2[1] ? c1 : c2;
}
function pose(inclDeg, u) {
  const a = inclDeg * Math.PI / 180, dx = -Math.cos(a), dy = -Math.sin(a), n = [Math.sin(a), -Math.cos(a)];
  const Hp = [560, 1180];
  const Pp = (d, o) => [Hp[0] + dx * d + n[0] * o, Hp[1] + dy * d + n[1] * o];
  const J = Pp(0, 38), S = Pp(300, 42), head = Pp(395, 62), K = [J[0] + 175, J[1] - 55], F = [K[0] + 40, 1340];
  const hand = [S[0] + (inclDeg < 10 ? 75 : 50), S[1] - lerp(85, 245, u)];
  return { H: Hp, J, S, head, K, F, hand, E: ik(S, hand, 140, 130), musc: Pp(inclDeg < 10 ? 262 : 285, 72),
           back: Pp(430, 0), mid: Pp(300, 0), seat: [Hp[0] + 150, Hp[1]], n, ang: Math.atan2(dy, dx) };
}
const V = (p, z = 0) => new THREE.Vector3((p[0] - 540) / 200, (1340 - p[1]) / 200, z);

// ------------------------------------------------------------------ renderer
const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(1); renderer.setSize(RW, RH);
renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 0.82;
renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x0d0d12);
scene.fog = new THREE.Fog(0x0d0d12, 9, 22);
const pmrem = new THREE.PMREMGenerator(renderer);
scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
scene.environmentIntensity = 0.35;
const camera = new THREE.PerspectiveCamera(36, W / H, 0.1, 60);

// materiais
const M = {
  skin: new THREE.MeshPhysicalMaterial({ color: 0xd9cfc2, roughness: 0.6, sheen: 0.4, sheenRoughness: 0.6, sheenColor: 0xffd9c8 }),
  short: new THREE.MeshStandardMaterial({ color: C.navy, roughness: 0.7 }),
  pad: new THREE.MeshPhysicalMaterial({ color: C.bench, roughness: 0.35, clearcoat: 0.6, clearcoatRoughness: 0.4 }),
  steel: new THREE.MeshStandardMaterial({ color: C.steel, metalness: 1.0, roughness: 0.25 }),
  rubber: new THREE.MeshStandardMaterial({ color: C.rubber, roughness: 0.6 }),
  coral: new THREE.MeshStandardMaterial({ color: C.coral, roughness: 0.4, emissive: C.coral, emissiveIntensity: 0.6 }),
  floor: new THREE.MeshStandardMaterial({ color: 0x17171e, roughness: 0.32, metalness: 0.15 }),
  wall: new THREE.MeshStandardMaterial({ color: 0x1b1b26, roughness: 0.9 }),
  stripC: new THREE.MeshBasicMaterial({ color: new THREE.Color(C.coral).multiplyScalar(2.2) }),
  stripL: new THREE.MeshBasicMaterial({ color: new THREE.Color(C.lilac).multiplyScalar(1.6) }),
  rack: new THREE.MeshStandardMaterial({ color: 0x2c2e38, metalness: 0.6, roughness: 0.4 }),
};
const add = (m) => { m.castShadow = true; m.receiveShadow = true; scene.add(m); return m; };

// cenário
const floor = new THREE.Mesh(new THREE.PlaneGeometry(60, 60), M.floor); floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true; scene.add(floor);
const wall = new THREE.Mesh(new THREE.PlaneGeometry(60, 20), M.wall); wall.position.set(0, 10, -5.5); wall.receiveShadow = true; scene.add(wall);
for (let i = -6; i <= 6; i++) {   // faixas de luz na parede (identidade: coral e lilás)
  const s = new THREE.Mesh(new THREE.BoxGeometry(0.06, 2.2, 0.02), i % 3 === 0 ? M.stripC : M.stripL);
  s.position.set(i * 1.6, 1.7, -5.45); scene.add(s);
}
function rack(x, z) {
  const g = new THREE.Group();
  for (const dx of [-0.6, 0.6]) { const u = new THREE.Mesh(new THREE.BoxGeometry(0.12, 3.2, 0.12), M.rack); u.position.set(dx, 1.6, 0); g.add(u); }
  const top = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.1, 0.12), M.rack); top.position.set(0, 3.1, 0); g.add(top);
  for (let k = 0; k < 4; k++) {
    const pl = new THREE.Mesh(new THREE.CylinderGeometry(0.42 - k * 0.05, 0.42 - k * 0.05, 0.07, 40), M.rubber);
    pl.rotation.x = Math.PI / 2; pl.position.set(0, 0.6 + k * 0.5, 0.12); g.add(pl);
  }
  g.position.set(x, 0, z); g.traverse((o) => { o.castShadow = o.receiveShadow = true; }); scene.add(g);
}
rack(-4.2, -3.2); rack(3.6, -3.6); rack(6.2, -2.2);
for (let k = 0; k < 6; k++) { // anilhas empilhadas no chão
  const pl = add(new THREE.Mesh(new THREE.CylinderGeometry(0.45, 0.45, 0.08, 40), M.rubber)); pl.position.set(2.6, 0.04 + k * 0.085, -1.6);
}

// luzes
scene.add(new THREE.HemisphereLight(0xb9b4ff, 0x14121a, 0.35));
const key = new THREE.DirectionalLight(0xfff1e6, 1.7); key.position.set(-3, 7, 5); key.castShadow = true;
key.shadow.mapSize.set(2048, 2048); key.shadow.radius = 6; key.shadow.bias = -0.0004;
Object.assign(key.shadow.camera, { left: -5, right: 5, top: 5, bottom: -3, near: 1, far: 20 }); scene.add(key);
const rim = new THREE.PointLight(C.coral, 30, 12, 2); rim.position.set(1.5, 3.2, -2.6); scene.add(rim);
const fill = new THREE.PointLight(C.lilac, 12, 12, 2); fill.position.set(-4, 2.5, 3); scene.add(fill);

const sphG = new THREE.SphereGeometry(1, 40, 24);
// ------------------------------------------------------------------ personagem "Brio" (corpo esculpido por primitivas)
const PAL = { skin: 0xd8a07c, hair: 0x2a1e1a, top: 0x262a52, shorts: 0x5b5e70, shoe: 0xf1efea, sole: 0xff5c3d, band: 0xff5c3d };
const MC = {
  skin: new THREE.MeshPhysicalMaterial({ color: PAL.skin, roughness: 0.5, sheen: 0.5, sheenRoughness: 0.5, sheenColor: 0xffc9a8, clearcoat: 0.08 }),
  hair: new THREE.MeshStandardMaterial({ color: PAL.hair, roughness: 0.85 }),
  top: new THREE.MeshPhysicalMaterial({ color: PAL.top, roughness: 0.75, sheen: 0.6, sheenColor: 0x6a6fd0 }),
  shorts: new THREE.MeshStandardMaterial({ color: PAL.shorts, roughness: 0.8 }),
  shoe: new THREE.MeshStandardMaterial({ color: PAL.shoe, roughness: 0.55 }),
  sole: new THREE.MeshStandardMaterial({ color: PAL.sole, roughness: 0.5 }),
  band: new THREE.MeshStandardMaterial({ color: PAL.band, roughness: 0.7 }),
  eye: new THREE.MeshStandardMaterial({ color: 0x141418, roughness: 0.2 }),
  glow: new THREE.MeshBasicMaterial({ color: new THREE.Color(C.coral).multiplyScalar(1.6), transparent: true, opacity: 0.6, blending: THREE.AdditiveBlending, depthWrite: false }),
};
const Y = new THREE.Vector3(0, 1, 0);
const mk = (geo, mat) => add(new THREE.Mesh(geo, mat));
class Seg { // segmento afinado (cilindro de raio r1→r2) + juntas esféricas + músculo opcional
  constructor(r1, r2, mat, bulge = null) {
    this.c = mk(new THREE.CylinderGeometry(r2, r1, 1, 32, 1, true), mat);
    this.j1 = mk(sphG, mat); this.j1.scale.setScalar(r1); this.j2 = mk(sphG, mat); this.j2.scale.setScalar(r2);
    this.b = bulge ? mk(sphG, bulge.mat || mat) : null; this.bulge = bulge;
  }
  set(p1, p2) {
    const d = new THREE.Vector3().subVectors(p2, p1), L = d.length(); const q = new THREE.Quaternion().setFromUnitVectors(Y, d.clone().normalize());
    this.c.position.copy(p1).addScaledVector(d, 0.5); this.c.scale.set(1, L, 1); this.c.quaternion.copy(q);
    this.j1.position.copy(p1); this.j2.position.copy(p2);
    if (this.b) { const B = this.bulge; this.b.position.copy(p1).addScaledVector(d, B.f); if (B.off) this.b.position.add(B.off.clone().applyQuaternion(q));
      this.b.quaternion.copy(q); this.b.scale.set(B.r[0], L * B.len, B.r[1]); }
  }
}
const char = {
  thighL: new Seg(0.185, 0.165, MC.shorts), thighR: new Seg(0.185, 0.165, MC.shorts),
  thigh2L: new Seg(0.15, 0.115, MC.skin), thigh2R: new Seg(0.15, 0.115, MC.skin),
  shinL: new Seg(0.115, 0.075, MC.skin, { f: 0.32, len: 0.5, r: [0.13, 0.125] }), shinR: new Seg(0.115, 0.075, MC.skin, { f: 0.32, len: 0.5, r: [0.13, 0.125] }),
  uarmL: new Seg(0.13, 0.1, MC.skin, { f: 0.5, len: 0.62, r: [0.135, 0.13] }), uarmR: new Seg(0.13, 0.1, MC.skin, { f: 0.5, len: 0.62, r: [0.135, 0.13] }),
  farmL: new Seg(0.1, 0.075, MC.skin, { f: 0.3, len: 0.55, r: [0.108, 0.104] }), farmR: new Seg(0.1, 0.075, MC.skin, { f: 0.3, len: 0.55, r: [0.108, 0.104] }),
  neck: new Seg(0.15, 0.14, MC.skin),
  torso: new THREE.Group(), head: new THREE.Group(),
  fists: [mk(new RoundedBoxGeometry(0.2, 0.2, 0.22, 4, 0.08), MC.skin), mk(new RoundedBoxGeometry(0.2, 0.2, 0.22, 4, 0.08), MC.skin)],
  bands: [mk(new THREE.CylinderGeometry(0.1, 0.1, 0.09, 24), MC.band), mk(new THREE.CylinderGeometry(0.1, 0.1, 0.09, 24), MC.band)],
  shoes: [new THREE.Group(), new THREE.Group()],
  pecs: [new THREE.Mesh(sphG, MC.glow), new THREE.Mesh(sphG, MC.glow), new THREE.Mesh(sphG, MC.glow), new THREE.Mesh(sphG, MC.glow)],
};
// tronco esculpido em coordenadas locais (x = do quadril ao ombro, y = frente do peito, z = largura); L = 1,5
const TL = 1.5;
for (const [x, s, mat] of [
  [0.02, [0.34, 0.3, 0.44], MC.shorts],      // quadril/short
  [0.42, [0.42, 0.27, 0.42], MC.top],        // cintura
  [0.92, [0.5, 0.31, 0.5], MC.top],          // peito
  [1.3, [0.3, 0.27, 0.56], MC.top],          // ombros/trapézio
]) { const m = new THREE.Mesh(sphG, mat); m.position.x = x; m.scale.set(...s); m.castShadow = m.receiveShadow = true; char.torso.add(m); }
for (const z of [-1, 1]) { // deltoides
  const d = new THREE.Mesh(sphG, MC.skin); d.position.set(1.38, 0.0, z * 0.6); d.scale.set(0.2, 0.19, 0.19); d.castShadow = true; char.torso.add(d);
}
scene.add(char.torso);
// cabeça: x = topo da cabeça, y = para onde o rosto olha
{
  const g = char.head;
  const sk = new THREE.Mesh(sphG, MC.skin); sk.scale.set(0.36, 0.34, 0.31); g.add(sk); g.scale.setScalar(0.86);
  const hair = new THREE.Mesh(new THREE.SphereGeometry(1, 32, 20, 0, Math.PI * 2, 0, 1.75), MC.hair);
  hair.scale.set(0.375, 0.355, 0.325); hair.quaternion.setFromUnitVectors(Y, new THREE.Vector3(0.75, -0.66, 0).normalize()); g.add(hair);
  for (const z of [-1, 1]) {
    const e = new THREE.Mesh(sphG, MC.eye); e.position.set(0.06, 0.31, z * 0.11); e.scale.set(0.05, 0.03, 0.034); g.add(e); e.name = "eye";
    const b = new THREE.Mesh(new RoundedBoxGeometry(0.035, 0.03, 0.12, 2, 0.012), MC.hair); b.position.set(0.15, 0.3, z * 0.11); b.name = z < 0 ? "browL" : "browR"; g.add(b);
    const ear = new THREE.Mesh(sphG, MC.skin); ear.position.set(-0.02, 0.0, z * 0.31); ear.scale.set(0.08, 0.06, 0.04); g.add(ear);
  }
  const nose = new THREE.Mesh(sphG, MC.skin); nose.position.set(-0.03, 0.34, 0); nose.scale.set(0.06, 0.05, 0.045); g.add(nose);
  const mouth = new THREE.Mesh(new RoundedBoxGeometry(0.03, 0.02, 0.1, 2, 0.008), MC.eye); mouth.position.set(-0.15, 0.3, 0); mouth.name = "mouth"; g.add(mouth);
  g.traverse((o) => { o.castShadow = true; o.receiveShadow = true; }); scene.add(g);
}
for (const sh of char.shoes) {
  const up = new THREE.Mesh(new RoundedBoxGeometry(0.4, 0.17, 0.2, 4, 0.07), MC.shoe); up.position.set(0.06, 0.1, 0); sh.add(up);
  const so = new THREE.Mesh(new RoundedBoxGeometry(0.43, 0.05, 0.22, 3, 0.02), MC.sole); so.position.set(0.06, 0.025, 0); sh.add(so);
  sh.traverse((o) => { o.castShadow = true; o.receiveShadow = true; }); scene.add(sh);
}
for (const p of char.pecs) scene.add(p);

// banco
const seat = add(new THREE.Mesh(new RoundedBoxGeometry(0.85, 0.2, 0.78, 5, 0.08), M.pad));
const back = add(new THREE.Mesh(new RoundedBoxGeometry(2.2, 0.2, 0.78, 5, 0.08), M.pad));
const matte = new THREE.MeshStandardMaterial({ color: 0x8a8d96, metalness: 0.5, roughness: 0.55 });
const legF = add(new THREE.Mesh(new THREE.CylinderGeometry(0.055, 0.055, 1, 16), matte));
const legB = add(new THREE.Mesh(new THREE.CylinderGeometry(0.055, 0.055, 1, 16), matte));
const footF = add(new THREE.Mesh(new RoundedBoxGeometry(0.14, 0.07, 0.9, 2, 0.025), matte));
const footB = add(new THREE.Mesh(new RoundedBoxGeometry(0.14, 0.07, 0.9, 2, 0.025), matte));
// barra olímpica
const bar = new THREE.Group();
const shaft = new THREE.Mesh(new THREE.CylinderGeometry(0.035, 0.035, 3.2, 20), M.steel); shaft.rotation.x = Math.PI / 2; bar.add(shaft);
for (const z of [-1.22, 1.22]) {
  for (const [r, th, dz, mat] of [[0.5, 0.1, 0, M.rubber], [0.4, 0.08, 0.1, M.rubber]]) {
    const pl = new THREE.Mesh(new THREE.CylinderGeometry(r, r, th, 56), mat); pl.rotation.x = Math.PI / 2; pl.position.z = z + Math.sign(z) * dz; bar.add(pl);
    const lip = new THREE.Mesh(new THREE.TorusGeometry(r * 0.8, 0.012, 8, 48), new THREE.MeshBasicMaterial({ color: new THREE.Color(C.coral).multiplyScalar(0.9) }));
    lip.position.z = pl.position.z + Math.sign(z) * (th / 2 + 0.002); bar.add(lip);
  }
  const col = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.06, 0.08, 20), M.steel); col.rotation.x = Math.PI / 2; col.position.z = z - Math.sign(z) * 0.1; bar.add(col);
}
bar.traverse((o) => { o.castShadow = o.receiveShadow = true; }); scene.add(bar);

function basis(x, y) { // quaternion de uma base ortonormal (x, y)
  const X = x.clone().normalize(), Z = new THREE.Vector3().crossVectors(X, y).normalize(), Yv = new THREE.Vector3().crossVectors(Z, X);
  return new THREE.Quaternion().setFromRotationMatrix(new THREE.Matrix4().makeBasis(X, Yv, Z));
}
function placeBody(t, inclDeg, u) {
  const p = pose(inclDeg, u);
  const nrm = new THREE.Vector3(p.n[0], -p.n[1], 0);
  const J = V(p.J), S = V(p.S);
  const axis = new THREE.Vector3().subVectors(S, J);
  char.torso.position.copy(J); char.torso.quaternion.copy(basis(axis, nrm)); char.torso.scale.setScalar(axis.length() / TL);
  // pernas (pés afastados, firmes no chão)
  for (const [i, s] of [[0, -1], [1, 1]]) {
    const hip = V(p.J, s * 0.24), knee = V(p.K, s * 0.36), ank = V([p.F[0], p.F[1] - 34], s * 0.44);
    const mid = hip.clone().lerp(knee, 0.55);
    (i ? char.thighR : char.thighL).set(hip, mid); (i ? char.thigh2R : char.thigh2L).set(mid, knee); (i ? char.shinR : char.shinL).set(knee, ank);
    char.shoes[i].position.set(ank.x - 0.02, 0, ank.z); char.shoes[i].rotation.y = -s * 0.15;
  }
  // braços: pegada mais larga que os ombros, cotovelos abertos
  const grip = 0.78;
  for (const [i, s] of [[0, -1], [1, 1]]) {
    const sh = V(p.S, s * 0.58), el = V(p.E, s * 0.76), hd = V(p.hand, s * grip);
    (i ? char.uarmR : char.uarmL).set(sh, el); (i ? char.farmR : char.farmL).set(el, hd);
    char.fists[i].position.copy(hd); char.fists[i].quaternion.copy(basis(new THREE.Vector3().subVectors(hd, el), new THREE.Vector3(0, 0, 1)));
    char.bands[i].position.copy(el).lerp(hd, 0.82); char.bands[i].quaternion.setFromUnitVectors(Y, new THREE.Vector3().subVectors(hd, el).normalize());
  }
  // cabeça e pescoço
  const hc = V(p.head); const top = axis.clone().normalize();
  char.neck.set(S.clone().addScaledVector(top, 0.05), hc.clone().addScaledVector(top, -0.12));
  char.head.position.copy(hc).addScaledVector(top, -0.04); char.head.quaternion.copy(basis(top, nrm));
  const effort = clamp(u * 1.4 - 0.2);
  char.head.children.forEach((o) => {
    if (o.name === "browL") o.rotation.y = 0.35 * effort; if (o.name === "browR") o.rotation.y = -0.35 * effort;
    if (o.name === "eye") o.scale.y = 0.03 * (1 - 0.6 * effort); if (o.name === "mouth") o.scale.z = 1 + 0.6 * effort;
  });
  // músculo trabalhado (holograma coral por cima da regata)
  const upper = inclDeg > 15;
  const glow = upper ? 0.35 + 0.65 * u : 0.25 + 0.5 * u;
  MC.glow.opacity = glow;
  const pos = (f, h, z) => J.clone().addScaledVector(axis, f).addScaledVector(nrm, h).add(new THREE.Vector3(0, 0, z));
  const q = basis(axis, nrm);
  [[0.66, -1], [0.66, 1], [0.8, -1], [0.8, 1]].forEach(([f, s], k) => {
    const pc = char.pecs[k]; const isUp = k >= 2;
    pc.visible = upper ? true : !isUp || true;
    pc.position.copy(pos(f, isUp ? 0.25 : 0.27, s * (isUp ? 0.24 : 0.25))); pc.quaternion.copy(q);
    const k2 = isUp ? (upper ? 1.0 : 0.45) : (upper ? 0.35 : 1.0);
    pc.scale.set(isUp ? 0.17 : 0.24, 0.07, isUp ? 0.2 : 0.23); pc.material = MC.glow; pc.userData.k = k2;
    pc.scale.multiplyScalar(0.85 + 0.15 * k2);
  });
  // banco
  const Hw = V(p.H), Bw = V(p.back), Sw = V(p.seat);
  const tilt = Math.atan2(Bw.y - Hw.y, Bw.x - Hw.x);
  back.position.copy(Hw).lerp(Bw, 0.5).add(new THREE.Vector3(Math.sin(tilt) * 0.1, -Math.cos(tilt) * 0.1, 0)); back.rotation.z = tilt + Math.PI;
  seat.position.set((Hw.x + Sw.x) / 2 + 0.05, Hw.y - 0.1, 0);
  const lf = Sw.x - 0.08; legF.position.set(lf, (Hw.y - 0.2) / 2, 0); legF.scale.y = Hw.y - 0.2; footF.position.set(lf, 0.035, 0);
  const mid = V(p.mid); const lb = inclDeg < 5 ? Bw.x + 0.25 : mid.x + 0.05; const topy = inclDeg < 5 ? Hw.y - 0.2 : lerp(Hw.y, mid.y, 0.8) - 0.2;
  legB.position.set(lb, topy / 2, 0); legB.scale.y = topy; footB.position.set(lb, 0.035, 0);
  const hp = V(p.hand); bar.position.set(hp.x, hp.y, 0);
  return p;
}

// ------------------------------------------------------------------ câmera (planos)
const keys = [ // t, ângulo (rad, 0 = de lado), distância, altura, alvo x, alvo y
  [0.0, -0.75, 11.6, 4.8, -0.25, 1.95], [3.6, -0.45, 10.9, 4.6, -0.3, 1.9],
  [4.8, -0.5, 9.6, 4.9, -0.55, 1.95], [8.2, -0.3, 8.6, 4.6, -0.7, 2.0],
  [10.0, -0.75, 11.8, 5.4, -0.35, 2.05],
];
function cam(t) {
  let i = 0; while (i < keys.length - 2 && t > keys[i + 1][0]) i++;
  const [t0, ...a] = keys[i], [t1, ...b] = keys[i + 1], k = ease((t - t0) / (t1 - t0));
  const [ang, d, h, tx, ty] = a.map((v, j) => lerp(v, b[j], k));
  camera.position.set(tx + d * Math.sin(ang), h, d * Math.cos(ang));
  camera.lookAt(tx, ty, 0);
}

// pós-processamento
const composer = new EffectComposer(renderer);
composer.addPass(new RenderPass(scene, camera));
const bloom = new UnrealBloomPass(new THREE.Vector2(RW, RH), 0.45, 0.5, 0.97); composer.addPass(bloom);
composer.addPass(new OutputPass());

// ------------------------------------------------------------------ texto por cima (2D)
const out = document.createElement("canvas"); out.width = W; out.height = H; document.body.appendChild(out);
const ctx = out.getContext("2d");
function pill(txt, col, fg, p, y = 1490) {
  if (p <= 0) return;
  ctx.save(); ctx.translate(540, y); ctx.scale(p, p); ctx.font = "68px Anton"; const w = ctx.measureText(txt).width + 70;
  ctx.fillStyle = col; ctx.beginPath(); ctx.roundRect(-w / 2, -54, w, 100, 24); ctx.fill();
  ctx.fillStyle = fg; ctx.textAlign = "center"; ctx.fillText(txt, 0, 22); ctx.restore();
}
function title(l1, l2, t, t0) {
  ctx.font = "150px Anton"; ctx.textAlign = "left";
  [[l1, "#f5f2eb"], [l2, "#ff5c3d"]].forEach(([s, col], i) => {
    const p = eo(prog(t, t0 + i * 0.12, 0.35));
    ctx.globalAlpha = p; ctx.fillStyle = col; ctx.shadowColor = "rgba(0,0,0,.45)"; ctx.shadowBlur = 24;
    ctx.fillText(s, 70 - (1 - p) * 90, 450 + i * 158);
  });
  ctx.globalAlpha = 1; ctx.shadowBlur = 0;
}
function overlay(t) {
  if (t < 4.0) title("SUPINO RETO", "OU INCLINADO?", t, 0.05);
  else if (t < 8.4) title("INCLINADO:", "PARTE DE CIMA.", t, 4.1);
  else title("QUAL VOCÊ", "FAZ MAIS?", t, 8.45);
  if (t < 3.9) pill("RETO = PEITO TODO", "#f6b81a", "#15151c", bo(prog(t, 0.8, 0.3)));
  else if (t < 8.4) pill("INCLINADO = PARTE DE CIMA", "#ff5c3d", "#ffffff", bo(prog(t, 4.6, 0.3)));
  else pill("COMENTA RETO OU INCLINADO", "#f5f2eb", "#15151c", bo(prog(t, 8.6, 0.3)));
}

// ------------------------------------------------------------------ quadro
function incl(t) { return 30 * ease((t - 3.8) / 1.0); }
window.renderFrame = (f, fmt = "image/jpeg", q = 0.93) => {
  const t = f / FPS, a = incl(t), u = 0.5 - 0.5 * Math.cos(t * 2.7);
  placeBody(t, a, u); cam(t);
  rim.intensity = 16 + 10 * u;
  composer.render();
  ctx.drawImage(renderer.domElement, 0, 0, W, H);
  overlay(t);
  return out.toDataURL(fmt, q);
};
window.FRAMES = FPS * DUR; window.FPS = FPS;
window.ready = document.fonts.load("150px Anton").then(() => document.fonts.ready).then(() => true);
renderer.domElement.style.display = "none"; document.body.appendChild(renderer.domElement);
