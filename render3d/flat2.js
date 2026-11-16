// Brio 3D flat v2: personagem em pé com esqueleto completo (rosca, agachamento, caminhada, flexão de braço, joinha),
// várias cenas, cortes com transição (faixa coral) e câmera com empurrão e balanço.
import * as THREE from "three";
import { Tube, profile } from "./body.js";

const W = 1080, H = 1920, FPS = 30;
const P = new URLSearchParams(location.search);
const TL = await (await fetch(P.get("tempos") || "roteiros/brio3d_02_tempos.json")).json();
const DUR = TL.dur + 0.4, ST = TL.starts;
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lerp = (a, b, t) => a + (b - a) * t;
const ease = (x) => { x = clamp(x); return x * x * (3 - 2 * x); };
const eo = (x) => { x = clamp(x); return 1 - (1 - x) ** 3; };
const bo = (x) => { x = clamp(x); const c = 1.7; return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2; };
const prog = (t, s, d) => clamp((t - s) / d);
const beatAt = (t) => { let i = 0; while (i < ST.length - 1 && t >= ST[i + 1]) i++; return i; };
const v3 = (x, y, z) => new THREE.Vector3(x, y, z);

const COL = { bg: 0x0c0d11, floor: 0x111217, grid: 0x23252e, body: 0xe9e3d7, armN: 0x8f887c, armF: 0x6d685f, legN: 0xc3bcb0, legF: 0x9b9489,
  steel: 0xbfc2ca, iron: 0x24262d, coral: 0xff5c3d, yel: 0xf6b81a, bread: 0xd9a35a, breadD: 0xb27a35, table: 0x2b2d36 };
const flat = (c) => new THREE.MeshBasicMaterial({ color: c, side: THREE.DoubleSide });

const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(1); renderer.setSize(W, H); renderer.outputColorSpace = THREE.SRGBColorSpace;
const scene = new THREE.Scene(); scene.background = new THREE.Color(COL.bg); scene.fog = new THREE.Fog(COL.bg, 8, 20);
const camera = new THREE.PerspectiveCamera(36, W / H, 0.05, 80); camera.setViewOffset(W, H, W * 0.11, -H * 0.13, W, H);
const floor = new THREE.Mesh(new THREE.PlaneGeometry(80, 80), flat(COL.floor)); floor.rotation.x = -Math.PI / 2; scene.add(floor);
const grid = new THREE.GridHelper(80, 80, COL.grid, COL.grid); grid.position.y = 0.002; scene.add(grid);
// faixas de luz ao fundo (coral/amarelo, como as cordas da referência)
for (let i = 0; i < 3; i++) { const r = new THREE.Mesh(new THREE.BoxGeometry(30, 0.025, 0.025), new THREE.MeshBasicMaterial({ color: i === 1 ? COL.yel : COL.coral, transparent: true, opacity: 0.55 }));
  r.position.set(0, 1.1 + i * 0.55, -4.5); scene.add(r); }

// ------------------------------------------------------------------ personagem
const TORSO = (belly) => profile([[0, 0.22, 0.27], [0.18, 0.23 + belly, 0.28], [0.42, 0.24 + belly * 0.7, 0.29], [0.7, 0.26, 0.34], [0.86, 0.24, 0.36], [0.96, 0.17, 0.3], [1, 0.1, 0.14]]);
const LIMB = (r0, r1, rk, kn) => profile([[0, r0, r0], [0.18, r0 * 0.97, r0 * 0.97], [kn - 0.02, rk, rk], [kn + 0.14, rk * 1.06, rk * 1.06], [0.97, r1, r1], [1, r1 * 0.96, r1 * 0.96]]);
class Fig {
  constructor() {
    this.torso = new Tube(flat(COL.body), { nr: 32, nl: 24 }); this.head = new THREE.Mesh(new THREE.SphereGeometry(0.21, 36, 24), flat(COL.body));
    this.legs = [new Tube(flat(COL.legF), { nr: 20, nl: 28 }), new Tube(flat(COL.legN), { nr: 20, nl: 28 })];
    this.arms = [new Tube(flat(COL.armF), { nr: 20, nl: 28 }), new Tube(flat(COL.armN), { nr: 20, nl: 28 })];
    this.feet = [0, 1].map((i) => new THREE.Mesh(new THREE.CapsuleGeometry(0.075, 0.17, 6, 14), flat(i ? COL.legN : COL.legF)));
    this.hands = [0, 1].map((i) => new THREE.Mesh(new THREE.SphereGeometry(0.075, 20, 14), flat(i ? COL.armN : COL.armF)));
    this.parts = [this.torso.mesh, this.head, ...this.legs.map((x) => x.mesh), ...this.arms.map((x) => x.mesh), ...this.feet, ...this.hands];
    this.parts.forEach((o) => scene.add(o)); this.belly = 0; this.armK = 1;
  }
  set visible(v) { this.parts.forEach((o) => (o.visible = v)); }
  // j: juntas em coordenadas locais (x frente, y cima, z direita); M: matriz do mundo
  apply(j, M, fwd) {
    const w = (p) => p.clone().applyMatrix4(M);
    const pel = w(j.pelvis), neck = w(j.neck), front = fwd.clone().transformDirection(M);
    const ax = neck.clone().sub(pel).normalize();
    this.torso.update([pel.clone().addScaledVector(ax, -0.1), pel.clone().lerp(neck, 0.5), neck.clone().addScaledVector(ax, 0.06)], TORSO(this.belly), front);
    this.head.position.copy(w(j.head));
    [0, 1].forEach((i) => {
      const h = w(j.hip[i]), k = w(j.knee[i]), a = w(j.ankle[i]), kn = h.distanceTo(k) / (h.distanceTo(k) + k.distanceTo(a));
      this.legs[i].update([h, h.clone().lerp(k, 0.5), k, k.clone().lerp(a, 0.5), a], LIMB(0.135, 0.07, 0.095, kn), front);
      this.feet[i].position.copy(a).add(front.clone().multiplyScalar(0.09)).setY(0.075);
      this.feet[i].quaternion.setFromUnitVectors(v3(0, 1, 0), front.clone().setY(0).normalize());
      const s = w(j.sh[i]), e = w(j.el[i]), r = w(j.wr[i]), se = s.distanceTo(e) / (s.distanceTo(e) + e.distanceTo(r)), K = this.armK;
      this.arms[i].update([s, s.clone().lerp(e, 0.5), e, e.clone().lerp(r, 0.5), r], LIMB(0.105 * K, 0.06, 0.075 * K, se), front);
      this.hands[i].position.copy(r);
    });
    this.W = { pel, neck, head: w(j.head), wr: [w(j.wr[0]), w(j.wr[1])], sh: [w(j.sh[0]), w(j.sh[1])] };
  }
}
// cinemática 2D (plano sagital): joelho/cotovelo dobram para o lado "bend" (+1 frente)
function ik2(a, b, L1, L2, bend) {
  const d = Math.max(Math.min(a.distanceTo(b), L1 + L2 - 1e-3), Math.abs(L1 - L2) + 1e-3);
  const dir = b.clone().sub(a).normalize(), x = (L1 * L1 - L2 * L2 + d * d) / (2 * d), h = Math.sqrt(Math.max(0, L1 * L1 - x * x));
  const perp = v3(-dir.y, dir.x, 0).multiplyScalar(bend);
  return a.clone().addScaledVector(dir, x).addScaledVector(perp, h).setZ(a.z);
}
// esqueleto base
function skel({ drop = 0, back = 0, lean = 0, walk = null, arms }) {
  const pelvis = v3(-back, 0.95 - drop, 0);
  const up = v3(Math.sin(lean), Math.cos(lean), 0);
  const neck = pelvis.clone().addScaledVector(up, 0.66), head = pelvis.clone().addScaledVector(up, 0.93);
  const j = { pelvis, neck, head, hip: [], knee: [], ankle: [], sh: [], el: [], wr: [] };
  [-1, 1].forEach((s, i) => {
    const hip = pelvis.clone().add(v3(0, 0, s * 0.14));
    let ank = v3(0.02, 0.08, s * 0.17);
    if (walk !== null) { const ph = walk + (i ? Math.PI : 0); ank = v3(0.28 * Math.sin(ph), 0.08 + Math.max(0, 0.12 * Math.cos(ph)), s * 0.15); }
    j.hip.push(hip); j.ankle.push(ank); j.knee.push(ik2(hip, ank, 0.47, 0.47, 1).setZ(s * 0.16));
    const sh = neck.clone().addScaledVector(up, -0.1).add(v3(0, 0, s * 0.33));
    j.sh.push(sh);
    const [el, wr] = arms(i, s, sh, up); j.el.push(el); j.wr.push(wr);
  });
  return j;
}
const hang = (i, s, sh, sw = 0) => [sh.clone().add(v3(0.04 + sw, -0.36, s * 0.06)), sh.clone().add(v3(0.08 + sw * 1.6, -0.7, s * 0.08))];
function curl(u) { return (i, s, sh) => { const el = sh.clone().add(v3(0.02, -0.36, s * 0.04)); const a = lerp(-0.15, 2.4, u); return [el, el.clone().add(v3(0.33 * Math.sin(a), -0.33 * Math.cos(a), 0))]; }; }
function squatArms() { return (i, s, sh) => [sh.clone().add(v3(-0.3, -0.05, s * 0.12)), sh.clone().add(v3(-0.18, 0.12, s * 0.28))]; }
function flex(u) { return (i, s, sh) => { const el = sh.clone().add(v3(0.02, 0.02, s * 0.34)); const a = lerp(0.5, 1.25, u); return [el, el.clone().add(v3(0.0, 0.33 * Math.sin(a), s * 0.33 * Math.cos(a)))]; }; }
function thumbs() { return (i, s, sh) => i === 1 ? [sh.clone().add(v3(0.3, -0.16, s * 0.05)), sh.clone().add(v3(0.42, 0.14, s * 0.05))] : hang(i, s, sh); }
function shrug(u) { return (i, s, sh) => [sh.clone().add(v3(0.12, -0.3, s * 0.18)), sh.clone().add(v3(0.38, -0.2 + 0.08 * u, s * 0.32))]; }

const me = new Fig();
function place(fig, j, pos, yaw) { const M = new THREE.Matrix4().makeRotationY(yaw).setPosition(pos); fig.apply(j, M, v3(1, 0, 0)); }

// ------------------------------------------------------------------ objetos
function dumbbell() { const g = new THREE.Group(); const h = new THREE.Mesh(new THREE.CylinderGeometry(0.025, 0.025, 0.34, 12), flat(COL.steel)); h.rotation.x = Math.PI / 2; g.add(h);
  for (const z of [-0.15, 0.15]) { const d = new THREE.Mesh(new THREE.CylinderGeometry(0.11, 0.11, 0.07, 28), flat(COL.coral)); d.rotation.x = Math.PI / 2; d.position.z = z; g.add(d); }
  scene.add(g); return g; }
const dbs = [dumbbell(), dumbbell()];
const barbell = new THREE.Group(); { const s = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 2.4, 14), flat(COL.steel)); s.rotation.x = Math.PI / 2; barbell.add(s);
  for (const z of [-0.95, 0.95]) for (const [r, dz] of [[0.42, 0], [0.33, 0.09]]) { const d = new THREE.Mesh(new THREE.CylinderGeometry(r, r, 0.08, 40), flat(COL.iron)); d.rotation.x = Math.PI / 2; d.position.z = z + Math.sign(z) * dz; barbell.add(d);
    const rim = new THREE.Mesh(new THREE.RingGeometry(r * 0.74, r * 0.8, 40), new THREE.MeshBasicMaterial({ color: COL.yel, side: THREE.DoubleSide })); rim.position.z = d.position.z + Math.sign(z) * 0.042; barbell.add(rim); } }
scene.add(barbell);
// pães franceses
function bread() { const g = new THREE.Group(); const b = new THREE.Mesh(new THREE.CapsuleGeometry(0.11, 0.3, 8, 20), flat(COL.bread)); b.rotation.z = Math.PI / 2; b.scale.set(1, 1, 0.85); g.add(b);
  for (let k = -1; k <= 1; k++) { const c = new THREE.Mesh(new THREE.BoxGeometry(0.03, 0.012, 0.13), flat(COL.breadD)); c.position.set(k * 0.1, 0.105, 0); c.rotation.y = 0.5; g.add(c); }
  scene.add(g); return g; }
const breads = [bread(), bread(), bread()];
const table = new THREE.Mesh(new THREE.BoxGeometry(1.4, 0.06, 0.8), flat(COL.table)); scene.add(table);
const tlegs = [0, 1, 2, 3].map(() => { const l = new THREE.Mesh(new THREE.BoxGeometry(0.06, 0.8, 0.06), flat(COL.iron)); scene.add(l); return l; });
// partículas de energia (gasto calórico)
const sparks = Array.from({ length: 26 }, (_, i) => { const m = new THREE.Mesh(new THREE.OctahedronGeometry(0.035), new THREE.MeshBasicMaterial({ color: i % 3 ? COL.coral : COL.yel, transparent: true })); scene.add(m); return m; });
// celular
const phoneC = document.createElement("canvas"); phoneC.width = 600; phoneC.height = 1220; const px = phoneC.getContext("2d");
const phoneTex = new THREE.CanvasTexture(phoneC); phoneTex.colorSpace = THREE.SRGBColorSpace;
const phone = new THREE.Group(); phone.add(new THREE.Mesh(new THREE.BoxGeometry(0.72, 1.45, 0.05), flat(0x1b1c22)));
const scr = new THREE.Mesh(new THREE.PlaneGeometry(0.66, 1.34), new THREE.MeshBasicMaterial({ map: phoneTex })); scr.position.z = 0.026; phone.add(scr); scene.add(phone);
function drawPhone(t) {
  px.fillStyle = "#121318"; px.fillRect(0, 0, 600, 1220); px.fillStyle = "#8a8d96"; px.font = "bold 26px SpaceMono"; px.fillText("HOJE · TREINO A", 40, 110);
  px.fillStyle = "#f5f2eb"; px.font = "64px Anton"; px.fillText("Brio", 40, 195);
  [["AGACHAMENTO", "80 KG × 8"], ["ROSCA DIRETA", "14 KG × 10"], ["SUPINO", "60 KG × 8"]].forEach(([a, b], i) => {
    const p = eo(prog(t, 0.3 + i * 0.35, 0.3)); px.globalAlpha = p; px.fillStyle = "#1e2028"; px.beginPath(); px.roundRect(30, 260 + i * 175, 540, 150, 24); px.fill();
    px.fillStyle = i === 2 ? "#ff5c3d" : "#f6b81a"; px.fillRect(30, 260 + i * 175, 12, 150); px.fillStyle = "#c9ccd4"; px.font = "bold 26px SpaceMono"; px.fillText(a, 70, 315 + i * 175);
    px.fillStyle = "#f5f2eb"; px.font = "64px Anton"; px.fillText(b, 70, 388 + i * 175); px.globalAlpha = 1; });
  const p = eo(prog(t, 1.4, 1.0)); px.globalAlpha = p; px.fillStyle = "#ff5c3d"; px.beginPath(); px.roundRect(30, 1040, 540, 110, 55); px.fill();
  px.fillStyle = "#fff"; px.font = "52px Anton"; px.textAlign = "center"; px.fillText("TREINO REGISTRADO", 300, 1115); px.textAlign = "left"; px.globalAlpha = 1;
  phoneTex.needsUpdate = true;
}

// ------------------------------------------------------------------ cenas
// cada cena: ação do personagem + câmera (pos0,pos1,alvo) + objetos visíveis
const SC = [
  { cam: [v3(1.6, 0.6, 2.6), v3(2.4, 1.0, 1.4), v3(0, 1.15, 0)], act: "curl" },          // 0 gancho: baixo, girando
  { cam: [v3(4.6, 1.3, 2.4), v3(4.2, 1.6, 3.2), v3(0, 0.95, 0)], act: "squat" },        // 1 kcal sobem: agachamento
  { cam: [v3(2.4, 2.4, 3.6), v3(2.0, 2.1, 3.9), v3(0.35, 1.05, 0)], act: "shrug" },        // 2 pães na mesa
  { cam: [v3(0, 1.3, 5.6), v3(0, 1.3, 5.6), v3(0, 1.0, 0)], act: "walk", track: 1 },     // 3 caminhando com faíscas
  { cam: [v3(3.2, 1.0, 0.4), v3(-0.4, 1.3, 3.2), v3(0, 1.45, 0)], act: "flex", orbit: 1 }, // 4 conclusão: órbita
  { cam: [v3(1.5, 1.5, 3.2), v3(1.2, 1.4, 2.6), v3(0.55, 1.3, 0)], act: "thumbs" },      // 5 CTA: celular
];

const out = document.createElement("canvas"); out.width = W; out.height = H; document.body.appendChild(out);
const ctx = out.getContext("2d");
function title(l1, l2, t, t0) {
  ctx.textAlign = "left";
  [[l1, "#f2ede3"], [l2, "#ff5c3d"]].forEach(([s, col], i) => {
    const p = eo(prog(t, t0 + 0.12 + i * 0.08, 0.28)); let size = 140; ctx.font = `${size}px Anton`;
    while (ctx.measureText(s).width > 950 && size > 90) { size -= 6; ctx.font = `${size}px Anton`; }
    ctx.save(); ctx.beginPath(); ctx.rect(0, 270 + i * 150, W, 195); ctx.clip();
    ctx.fillStyle = col; ctx.fillText(s, 70, 430 + i * 150 + (1 - p) * 150); ctx.restore();
  });
}
function big(s, x, y, size, col, a = 1) { if (a <= 0) return; ctx.globalAlpha = a; ctx.font = `${size}px Anton`; ctx.fillStyle = col; ctx.textAlign = "center"; ctx.fillText(s, x, y); ctx.globalAlpha = 1; }
function label(s, v, col, size, a, dy = 0) { if (a <= 0) return; const q = v.clone().project(camera); const x = (q.x + 1) / 2 * W, y = (1 - q.y) / 2 * H + dy;
  ctx.globalAlpha = a; ctx.font = `bold ${size}px SpaceMono`; ctx.fillStyle = col; ctx.textAlign = "center"; ctx.fillText(s, x, y); ctx.globalAlpha = 1; }
function wipe(t) { // faixa coral diagonal cobrindo cada corte
  for (let b = 1; b < ST.length; b++) { const k = (t - (ST[b] - 0.18)) / 0.36; if (k < 0 || k > 1) continue;
    const x = lerp(-1400, 1500, ease(k)); ctx.save(); ctx.translate(x, 0); ctx.transform(1, 0, -0.35, 1, 0, 0);
    ctx.fillStyle = "#ff5c3d"; ctx.fillRect(0, 0, 900, H); ctx.fillStyle = "#f6b81a"; ctx.fillRect(900, 0, 70, H); ctx.restore(); }
}
function vignette() { const g = ctx.createRadialGradient(540, 1100, 280, 540, 1100, 1250); g.addColorStop(0, "rgba(0,0,0,0)"); g.addColorStop(1, "rgba(0,0,0,0.6)"); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H); }

let phase = 0, lastF = -1;
const speedAt = (t) => [2.9, 2.4, 1.6, 6.0, 2.2, 1.5][beatAt(t)];
window.renderFrame = (f, fmt = "image/jpeg", q = 0.93) => {
  if (f !== lastF + 1) { phase = 0; for (let k = 0; k < f; k++) phase += speedAt(k / FPS) / FPS; }
  const t = f / FPS; phase += speedAt(t) / FPS; lastF = f;
  const b = beatAt(t), lt = t - ST[b], k = lt / ((ST[b + 1] ?? DUR) - ST[b]), u = 0.5 - 0.5 * Math.cos(phase), S = SC[b];
  // personagem
  let j, pos = v3(0, 0, 0), yaw = 0.0;
  me.belly = 0; me.armK = 1;
  if (S.act === "curl") j = skel({ arms: curl(u) });
  if (S.act === "squat") { const d = 0.38 * u; j = skel({ drop: d, back: d * 0.55, lean: 0.5 * u + 0.1, arms: squatArms() }); }
  if (S.act === "shrug") { j = skel({ arms: shrug(u) }); pos = v3(-0.35, 0, 0); yaw = -0.25; }
  if (S.act === "walk") { j = skel({ walk: phase, lean: 0.06, arms: (i, s, sh) => hang(i, s, sh, 0.18 * Math.sin(phase + (i ? 0 : Math.PI))) }); pos = v3(lerp(-1.6, 1.6, k), 0, 0); yaw = 0; me.armK = lerp(1, 1.25, ease(k)); }
  if (S.act === "flex") { j = skel({ arms: flex(u) }); yaw = Math.PI / 2; me.armK = 1.25; }
  if (S.act === "thumbs") { j = skel({ arms: thumbs() }); yaw = 0.35; }
  j.head.y += 0.015 * Math.sin(t * 3);
  place(me, j, pos, yaw);
  // objetos por cena
  dbs.forEach((d, i) => { d.visible = b === 0; d.position.copy(me.W.wr[i]); d.rotation.y = yaw; });
  barbell.visible = b === 1; if (b === 1) { barbell.position.copy(me.W.neck).add(v3(-0.2, -0.02, 0)); }
  const showT = b === 2; table.visible = showT; tlegs.forEach((l) => (l.visible = showT)); breads.forEach((br) => (br.visible = showT));
  if (showT) { table.position.set(0.9, 0.8, 0); [[-0.6, -0.33], [0.6, -0.33], [-0.6, 0.33], [0.6, 0.33]].forEach(([x, z], i) => tlegs[i].position.set(0.9 + x, 0.4, z));
    breads.forEach((br, i) => { const d = bo(prog(lt, 0.25 + i * 0.35, 0.35)); br.position.set(0.55 + i * 0.36, 0.9 + (1 - d) * 1.6, 0.05 * (i - 1)); br.rotation.y = 0.3 * i - 0.2 + (1 - d) * 2; br.visible = lt > 0.25 + i * 0.35; }); }
  sparks.forEach((s, i) => { s.visible = b === 3 || b === 1; const ph = (t * 0.6 + i / sparks.length) % 1;
    const base = b === 1 ? me.W.pel : me.W.pel; s.position.set(base.x + Math.sin(i * 7.1) * 0.5, 0.4 + ph * 2.0, Math.cos(i * 3.3) * 0.45); s.material.opacity = (1 - ph) * (b === 1 ? 0.5 + 0.5 * k : 1); s.rotation.set(t * 3 + i, t * 2, 0); });
  phone.visible = b === 5; if (b === 5) { phone.position.set(1.05, 1.35, -0.55); phone.rotation.y = 0.55 + 0.08 * Math.sin(t); phone.scale.setScalar(0.85); drawPhone(lt); }
  // câmera: trilho + empurrão inicial + balanço de mão
  const kk = ease(k), push = 1 + 0.22 * (1 - eo(prog(lt, 0, 0.5)));
  let tgt = S.cam[2].clone(), cp = S.cam[0].clone().lerp(S.cam[1], kk);
  if (S.track) { tgt.x = pos.x * 0.8; cp.x = pos.x * 0.6; }
  if (S.orbit) { const a = lerp(0.1, Math.PI * 0.95, kk); cp = v3(6.2 * Math.cos(a), 1.6 + 0.5 * kk, 6.2 * Math.sin(a)); }
  cp = tgt.clone().add(cp.sub(tgt).multiplyScalar(push * [2.2, 1.7, 1.85, 1.6, 1.15, 2.2][b]));
  cp.add(v3(0.03 * Math.sin(t * 1.7), 0.025 * Math.sin(t * 2.3), 0.03 * Math.cos(t * 1.3)));
  if (b === 0 || b === 1) cp.y += 0.012 * Math.sin(t * 40) * u; // tremor no esforço
  camera.position.copy(cp); camera.lookAt(tgt);
  renderer.render(scene, camera);
  ctx.drawImage(renderer.domElement, 0, 0, W, H); vignette();
  // gráficos por cena
  if (b === 0) { big("60", 860, 1000, 170, "#f6b81a", eo(prog(lt, 0.5, 0.3))); big("MIN", 860, 1070, 50, "#8a8d96", eo(prog(lt, 0.5, 0.3))); }
  if (b === 1) { const n = Math.round(lerp(0, 400, eo(prog(lt, 0.3, 3.2)))); big(`${n}`, 860, 1000, 170, n >= 200 ? "#ff5c3d" : "#f2ede3"); big("KCAL", 860, 1070, 50, "#8a8d96"); }
  if (b === 2) { breads.forEach((br, i) => br.visible && label(`${i + 1}`, br.position.clone().add(v3(0, 0.32, 0)), "#f6b81a", 44, eo(prog(lt, 0.45 + i * 0.35, 0.2)))); big("≈ 140 KCAL CADA", 540, 1560, 58, "#c9ccd4", eo(prog(lt, 1.2, 0.3))); }
  if (b === 3) { big("24 H", 860, 1000, 150, "#ff5c3d", eo(prog(lt, 0.4, 0.3))); big("MAIS MÚSCULO,", 860, 1080, 46, "#f6b81a", eo(prog(lt, 1.6, 0.3))); big("MAIS GASTO", 860, 1135, 46, "#f6b81a", eo(prog(lt, 1.9, 0.3))); }
  if (b === 4) { big("NÃO É QUEIMAR.", 540, 730, 60, "#8a8d96", eo(prog(lt, 0.4, 0.3))); big("É CONSTRUIR.", 540, 820, 80, "#f6b81a", eo(prog(lt, 1.6, 0.3))); }
  if (b === 5) big("LINK NA BIO", 540, 1560, 58, "#c9ccd4", eo(prog(lt, 1.0, 0.3)));
  const B = TL.beats[b]; title(B.t1, B.t2, t, ST[b] - 0.05);
  wipe(t);
  return out.toDataURL(fmt, q);
};
window.FRAMES = Math.round(DUR * FPS); window.FPS = FPS;
window.ready = document.fonts.load("140px Anton").then(() => document.fonts.load("bold 30px SpaceMono")).then(() => true);
renderer.domElement.style.display = "none"; document.body.appendChild(renderer.domElement);
