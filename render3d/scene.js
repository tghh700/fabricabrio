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
const C = { coral: 0xff5c3d, cream: 0xefe6da, navy: 0x2b2f5c, ink: 0x15151c, steel: 0xc9ccd4, rubber: 0x1d1e24, bench: 0x262833, lilac: 0x9c8cff };

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

// ------------------------------------------------------------------ peças do boneco
const cylG = new THREE.CylinderGeometry(1, 1, 1, 28, 1, true), sphG = new THREE.SphereGeometry(1, 32, 20);
class Limb {
  constructor(r, mat) { this.r = r; this.c = add(new THREE.Mesh(cylG, mat)); this.a = add(new THREE.Mesh(sphG, mat)); this.b = add(new THREE.Mesh(sphG, mat));
    this.a.scale.setScalar(r); this.b.scale.setScalar(r); }
  set(p1, p2) {
    const d = new THREE.Vector3().subVectors(p2, p1), L = d.length();
    this.c.position.copy(p1).addScaledVector(d, 0.5); this.c.scale.set(this.r, L, this.r);
    this.c.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), d.normalize());
    this.a.position.copy(p1); this.b.position.copy(p2);
  }
}
const body = {
  torso: new Limb(0.3, M.skin), head: add(new THREE.Mesh(sphG, M.skin)),
  thighL: new Limb(0.17, M.short), thighR: new Limb(0.17, M.short), shinL: new Limb(0.125, M.skin), shinR: new Limb(0.125, M.skin),
  uarmL: new Limb(0.12, M.skin), uarmR: new Limb(0.12, M.skin), farmL: new Limb(0.105, M.skin), farmR: new Limb(0.105, M.skin),
  pecL: add(new THREE.Mesh(sphG, M.coral)), pecR: add(new THREE.Mesh(sphG, M.coral)),
  shorts: add(new THREE.Mesh(sphG, M.short)),
};
body.head.scale.setScalar(0.34);
// banco
const seat = add(new THREE.Mesh(new RoundedBoxGeometry(0.85, 0.18, 0.62, 4, 0.06), M.pad));
const back = add(new THREE.Mesh(new RoundedBoxGeometry(2.2, 0.18, 0.62, 4, 0.06), M.pad));
const legF = add(new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 1, 16), M.steel));
const legB = add(new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 1, 16), M.steel));
const footF = add(new THREE.Mesh(new RoundedBoxGeometry(0.12, 0.06, 0.7, 2, 0.02), M.steel));
const footB = add(new THREE.Mesh(new RoundedBoxGeometry(0.12, 0.06, 0.7, 2, 0.02), M.steel));
// barra
const bar = new THREE.Group();
const shaft = new THREE.Mesh(new THREE.CylinderGeometry(0.035, 0.035, 2.6, 20), M.steel); shaft.rotation.x = Math.PI / 2; bar.add(shaft);
for (const z of [-1.0, 1.0]) for (const [r, th, dz] of [[0.44, 0.09, 0], [0.34, 0.07, 0.08]]) {
  const pl = new THREE.Mesh(new THREE.CylinderGeometry(r, r, th, 48), M.rubber); pl.rotation.x = Math.PI / 2; pl.position.z = z + Math.sign(z) * dz; bar.add(pl);
  const hub = new THREE.Mesh(new THREE.CylinderGeometry(0.07, 0.07, th + 0.01, 20), M.steel); hub.rotation.x = Math.PI / 2; hub.position.z = pl.position.z; bar.add(hub);
}
bar.traverse((o) => { o.castShadow = o.receiveShadow = true; }); scene.add(bar);

function placeBody(t, inclDeg, u) {
  const p = pose(inclDeg, u);
  const J = V(p.J), S = V(p.S), K = V(p.K), F = V(p.F);
  body.torso.set(J, S);
  body.shorts.position.copy(J); body.shorts.scale.set(0.32, 0.31, 0.33);
  for (const [s, th, sh] of [[-1, body.thighL, body.shinL], [1, body.thighR, body.shinR]]) {
    th.set(V(p.J, s * 0.17), V(p.K, s * 0.22)); sh.set(V(p.K, s * 0.22), V(p.F, s * 0.26));
  }
  for (const [s, ua, fa] of [[-1, body.uarmL, body.farmL], [1, body.uarmR, body.farmR]]) {
    ua.set(V(p.S, s * 0.36), V(p.E, s * 0.56)); fa.set(V(p.E, s * 0.56), V(p.hand, s * 0.5));
  }
  body.head.position.copy(V(p.head));
  const m = V(p.musc), nrm = new THREE.Vector3(p.n[0], -p.n[1], 0);
  const glow = 1.2 + 3.5 * u * (inclDeg > 15 ? 1.4 : 1.0);
  M.coral.emissiveIntensity = glow;
  for (const [s, pec] of [[-1, body.pecL], [1, body.pecR]]) {
    pec.position.copy(m).addScaledVector(nrm, 0.07); pec.position.z = s * 0.15;
    pec.scale.set(0.27, 0.12, 0.15); pec.rotation.set(0, 0, p.ang + Math.PI);
  }
  // banco
  const Hw = V(p.H), Bw = V(p.back), Sw = V(p.seat);
  const tilt = Math.atan2(Bw.y - Hw.y, Bw.x - Hw.x);
  back.position.copy(Hw).lerp(Bw, 0.5).add(new THREE.Vector3(Math.sin(tilt) * 0.09, -Math.cos(tilt) * 0.09, 0)); back.rotation.z = tilt + Math.PI;
  seat.position.set((Hw.x + Sw.x) / 2 + 0.05, Hw.y - 0.09, 0);
  const lf = Sw.x - 0.08; legF.position.set(lf, (Hw.y - 0.18) / 2, 0); legF.scale.y = Hw.y - 0.18; footF.position.set(lf, 0.03, 0);
  const mid = V(p.mid); const lb = inclDeg < 5 ? Bw.x + 0.25 : mid.x + 0.05; const top = inclDeg < 5 ? Hw.y - 0.18 : lerp(Hw.y, mid.y, 0.8) - 0.18;
  legB.position.set(lb, top / 2, 0); legB.scale.y = top; footB.position.set(lb, 0.03, 0);
  // barra nas mãos
  const hp = V(p.hand); bar.position.set(hp.x, hp.y, 0);
  return p;
}

// ------------------------------------------------------------------ câmera (planos)
const keys = [ // t, ângulo (rad, 0 = de lado), distância, altura, alvo x, alvo y
  [0.0, -0.8, 11.6, 4.0, -0.25, 2.05], [3.6, -0.5, 10.9, 3.8, -0.3, 2.0],
  [4.8, -1.15, 10.6, 4.1, -0.45, 2.2], [8.2, -0.95, 9.4, 3.8, -0.6, 2.2],
  [10.0, -0.55, 12.4, 4.6, -0.3, 2.3],
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
  rim.intensity = 30 + 18 * u;
  composer.render();
  ctx.drawImage(renderer.domElement, 0, 0, W, H);
  overlay(t);
  return out.toDataURL(fmt, q);
};
window.FRAMES = FPS * DUR; window.FPS = FPS;
window.ready = document.fonts.load("150px Anton").then(() => document.fonts.ready).then(() => true);
renderer.domElement.style.display = "none"; document.body.appendChild(renderer.domElement);
