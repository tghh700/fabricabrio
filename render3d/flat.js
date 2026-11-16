// Brio 3D "flat": cena 3D de verdade (câmera, perspectiva, profundidade) com cores chapadas, sem luz nem textura.
// Estilo da referência: corpo em formas lisas, membros do lado de lá mais escuros, sem rosto, chão com grade, cortes de câmera.
import * as THREE from "three";
import { Tube, profile } from "./body.js";

const W = 1080, H = 1920, FPS = 30;
const P = new URLSearchParams(location.search);
const TL = await (await fetch(P.get("tempos") || "roteiros/brio3d_01_tempos.json")).json();
const DUR = TL.dur + 0.5, ST = TL.starts;
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lerp = (a, b, t) => a + (b - a) * t;
const ease = (x) => { x = clamp(x); return x * x * (3 - 2 * x); };
const eo = (x) => { x = clamp(x); return 1 - (1 - x) ** 3; };
const bo = (x) => { x = clamp(x); const c = 1.7; return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2; };
const prog = (t, s, d) => clamp((t - s) / d);
const beatAt = (t) => { let i = 0; while (i < ST.length - 1 && t >= ST[i + 1]) i++; return i; };

const COL = { bg: 0x0d0e12, floor: 0x121318, grid: 0x262833, body: 0xe7e1d5, near: 0xb8b1a5, far: 0x847e74,
  bench: 0x2a2c35, benchTop: 0x34363f, steel: 0xb9bcc4, plate: 0x24262d, coral: 0xff5c3d, yel: 0xf6b81a, rival: 0x4a4e5c, rivalN: 0x5d6272, rivalF: 0x3a3d48 };
const flat = (c) => new THREE.MeshBasicMaterial({ color: c, side: THREE.DoubleSide });

// ------------------------------------------------------------------ cena
const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
renderer.setPixelRatio(1); renderer.setSize(W, H); renderer.outputColorSpace = THREE.SRGBColorSpace;
const scene = new THREE.Scene(); scene.background = new THREE.Color(COL.bg); scene.fog = new THREE.Fog(COL.bg, 7, 19);
const camera = new THREE.PerspectiveCamera(38, W / H, 0.05, 80); camera.setViewOffset(W, H, 0, -H * 0.13, W, H);
const floor = new THREE.Mesh(new THREE.PlaneGeometry(80, 80), flat(COL.floor)); floor.rotation.x = -Math.PI / 2; scene.add(floor);
const grid = new THREE.GridHelper(80, 80, COL.grid, COL.grid); grid.position.y = 0.002; scene.add(grid);

// ------------------------------------------------------------------ pose lateral (px) → mundo
function ik(s, h, L1, L2) {
  const dx = h[0] - s[0], dy = h[1] - s[1];
  const d = Math.max(Math.min(Math.hypot(dx, dy), L1 + L2 - 1), Math.abs(L1 - L2) + 1);
  const a = Math.atan2(dy, dx), b = Math.acos((L1 * L1 + d * d - L2 * L2) / (2 * L1 * d));
  const c1 = [s[0] + L1 * Math.cos(a + b), s[1] + L1 * Math.sin(a + b)], c2 = [s[0] + L1 * Math.cos(a - b), s[1] + L1 * Math.sin(a - b)];
  return c1[1] > c2[1] ? c1 : c2;
}
function pose(inclDeg, u) {
  const a = inclDeg * Math.PI / 180, dx = -Math.cos(a), dy = -Math.sin(a), n = [Math.sin(a), -Math.cos(a)];
  const Hp = [560, 1180], Pp = (d, o) => [Hp[0] + dx * d + n[0] * o, Hp[1] + dy * d + n[1] * o];
  const J = Pp(0, 50), S = Pp(290, 52), head = Pp(382, 66), K = [J[0] + 170, J[1] - 60], F = [K[0] + 45, 1340];
  const hand = [S[0] + (inclDeg < 10 ? 60 : 38), S[1] - lerp(70, 238, u)];
  return { H: Hp, J, S, head, K, F, hand, E: ik(S, hand, 132, 125), back: Pp(430, 0), mid: Pp(300, 0), seat: [Hp[0] + 150, Hp[1]], n };
}
const V = (p, z = 0, ox = 0, oz = 0) => new THREE.Vector3((p[0] - 540) / 200 + ox, (1340 - p[1]) / 200, z + oz);

// ------------------------------------------------------------------ personagem chapado
const TORSO = profile([[0, 0.25, 0.34], [0.15, 0.25, 0.35], [0.4, 0.22, 0.31], [0.66, 0.26, 0.4], [0.82, 0.25, 0.44], [0.93, 0.19, 0.42], [1, 0.12, 0.2]]);
const LEG = (sk) => profile([[0, 0.16, 0.16], [0.25, 0.15, 0.15], [sk - 0.02, 0.1, 0.1], [sk + 0.15, 0.11, 0.11], [0.96, 0.068, 0.068], [1, 0.065, 0.065]]);
const ARM = (se) => profile([[0, 0.12, 0.12], [0.1, 0.125, 0.12], [se - 0.02, 0.085, 0.085], [se + 0.12, 0.09, 0.088], [0.97, 0.064, 0.064], [1, 0.062, 0.062]]);
class Fig {
  constructor(c) {
    this.torso = new Tube(flat(c.body), { nr: 28, nl: 24 }); this.head = new THREE.Mesh(new THREE.SphereGeometry(0.24, 32, 20), flat(c.body));
    this.neck = new Tube(flat(c.body), { nr: 16, nl: 4 });
    this.legs = [new Tube(flat(c.far), { nr: 18, nl: 30 }), new Tube(flat(c.near), { nr: 18, nl: 30 })];
    this.arms = [new Tube(flat(c.far), { nr: 18, nl: 30 }), new Tube(flat(c.near), { nr: 18, nl: 30 })];
    this.feet = [0, 1].map((i) => new THREE.Mesh(new THREE.CapsuleGeometry(0.065, 0.16, 6, 12), flat(i ? c.near : c.far)));
    this.hands = [0, 1].map((i) => new THREE.Mesh(new THREE.SphereGeometry(0.085, 20, 14), flat(i ? c.near : c.far)));
    this.g = new THREE.Group();
    for (const o of [this.torso.mesh, this.head, this.neck.mesh, ...this.legs.map((x) => x.mesh), ...this.arms.map((x) => x.mesh), ...this.feet, ...this.hands]) this.g.add(o);
    scene.add(this.g);
  }
  set(p, ox = 0, oz = 0) {
    const J = V(p.J, 0, ox, oz), S = V(p.S, 0, ox, oz), nrm = new THREE.Vector3(p.n[0], -p.n[1], 0), axis = S.clone().sub(J).normalize();
    this.torso.update([J.clone().addScaledVector(axis, -0.1), J.clone().lerp(S, 0.5), S.clone().addScaledVector(axis, 0.1)], TORSO, nrm);
    const hd = V(p.head, 0, ox, oz); this.head.position.copy(hd);
    this.neck.update([S, S.clone().lerp(hd, 0.5), hd.clone().addScaledVector(axis, -0.12)], profile([[0, 0.1, 0.1], [1, 0.09, 0.09]]), nrm);
    [-1, 1].forEach((s, i) => {
      const hip = V(p.J, s * 0.18, ox, oz), knee = V(p.K, s * 0.3, ox, oz), ank = V([p.F[0], p.F[1] - 22], s * 0.38, ox, oz);
      const sk = hip.distanceTo(knee) / (hip.distanceTo(knee) + knee.distanceTo(ank));
      this.legs[i].update([hip, hip.clone().lerp(knee, 0.5), knee, knee.clone().lerp(ank, 0.5), ank], LEG(sk), new THREE.Vector3(0, 1, 0));
      this.feet[i].position.set(ank.x + 0.08, 0.07, ank.z); this.feet[i].rotation.z = Math.PI / 2;
      const sh = V(p.S, s * 0.34, ox, oz), el = V(p.E, s * 0.72, ox, oz), wr = V(p.hand, s * 0.76, ox, oz);
      const se = sh.distanceTo(el) / (sh.distanceTo(el) + el.distanceTo(wr));
      this.arms[i].update([sh, sh.clone().lerp(el, 0.5), el, el.clone().lerp(wr, 0.5), wr], ARM(se), new THREE.Vector3(0, 0, s));
      this.hands[i].position.copy(wr);
    });
    this.p = p; this.ox = ox; this.oz = oz;
  }
}
const me = new Fig({ body: COL.body, near: COL.near, far: COL.far });
const rival = new Fig({ body: COL.rival, near: COL.rivalN, far: COL.rivalF });

// destaque do peito: elipse chapada coral sobre a superfície + halo
const glowTex = (() => { const c = document.createElement("canvas"); c.width = c.height = 128; const x = c.getContext("2d");
  const g = x.createRadialGradient(64, 64, 4, 64, 64, 64); g.addColorStop(0, "rgba(255,92,61,0.9)"); g.addColorStop(1, "rgba(255,92,61,0)"); x.fillStyle = g; x.fillRect(0, 0, 128, 128);
  return new THREE.CanvasTexture(c); })();
function chestMark() {
  const m = new THREE.Mesh(new THREE.CircleGeometry(1, 40), new THREE.MeshBasicMaterial({ color: COL.coral, transparent: true, side: THREE.DoubleSide, depthTest: true }));
  const halo = new THREE.Sprite(new THREE.SpriteMaterial({ map: glowTex, transparent: true, blending: THREE.AdditiveBlending, depthWrite: false }));
  scene.add(m); scene.add(halo); return { m, halo };
}
const marks = { low: [chestMark(), chestMark()], up: [chestMark(), chestMark()] };
function placeMarks(fig, lowA, upA, t) {
  const tor = fig.torso;
  const put = (mk, s, ang, sx, sy, a) => {
    const pt = tor.surface(s, ang, 0.012), c = tor.surface(s, ang, -0.2);
    mk.m.position.copy(pt); mk.m.lookAt(pt.clone().add(pt.clone().sub(c)));
    mk.m.scale.set(sx, sy, 1); mk.m.material.opacity = a; mk.m.visible = a > 0.01;
    mk.halo.position.copy(tor.surface(s, ang, 0.08)); mk.halo.scale.setScalar(0.75 * (0.8 + 0.4 * a)); mk.halo.material.opacity = a * 0.6; mk.halo.visible = a > 0.01;
  };
  const pulse = 0.75 + 0.25 * Math.sin(t * 6);
  [-1, 1].forEach((s, i) => {
    put(marks.low[i], 0.7, s * 0.42, 0.17, 0.13, lowA * pulse);
    put(marks.up[i], 0.87, s * 0.38, 0.12, 0.075, upA * pulse);
  });
}

// ------------------------------------------------------------------ banco, barra, anilhas
function Bench() {
  const g = { seat: new THREE.Mesh(new THREE.BoxGeometry(0.85, 0.18, 0.62), flat(COL.benchTop)), back: new THREE.Mesh(new THREE.BoxGeometry(2.2, 0.18, 0.62), flat(COL.benchTop)),
    legF: new THREE.Mesh(new THREE.BoxGeometry(0.1, 1, 0.1), flat(COL.bench)), legB: new THREE.Mesh(new THREE.BoxGeometry(0.1, 1, 0.1), flat(COL.bench)),
    footF: new THREE.Mesh(new THREE.BoxGeometry(0.12, 0.06, 0.8), flat(COL.bench)), footB: new THREE.Mesh(new THREE.BoxGeometry(0.12, 0.06, 0.8), flat(COL.bench)) };
  Object.values(g).forEach((o) => scene.add(o)); return g;
}
function placeBench(b, p, inc, ox = 0, oz = 0) {
  const Hw = V(p.H, 0, ox, oz), Bw = V(p.back, 0, ox, oz), Sw = V(p.seat, 0, ox, oz), tilt = Math.atan2(Bw.y - Hw.y, Bw.x - Hw.x);
  b.back.position.copy(Hw).lerp(Bw, 0.5).add(new THREE.Vector3(Math.sin(tilt) * 0.09, -Math.cos(tilt) * 0.09, 0)); b.back.rotation.z = tilt + Math.PI;
  b.seat.position.set((Hw.x + Sw.x) / 2 + 0.05, Hw.y - 0.09, oz);
  const lf = Sw.x - 0.08; b.legF.position.set(lf, (Hw.y - 0.18) / 2, oz); b.legF.scale.y = Hw.y - 0.18; b.footF.position.set(lf, 0.03, oz);
  const mid = V(p.mid, 0, ox, oz), lb = inc < 5 ? Bw.x + 0.25 : mid.x + 0.05, top = inc < 5 ? Hw.y - 0.18 : lerp(Hw.y, mid.y, 0.8) - 0.18;
  b.legB.position.set(lb, top / 2, oz); b.legB.scale.y = top; b.footB.position.set(lb, 0.03, oz);
}
function Bar() {
  const g = new THREE.Group(); const sh = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 3.0, 16), flat(COL.steel)); sh.rotation.x = Math.PI / 2; g.add(sh);
  const plates = [];
  for (const z of [-1.1, 1.1]) for (const [r, th, dz, outer] of [[0.46, 0.09, 0, 0], [0.37, 0.08, 0.1, 1]]) {
    const pg = new THREE.Group(); const pl = new THREE.Mesh(new THREE.CylinderGeometry(r, r, th, 48), flat(COL.plate)); pl.rotation.x = Math.PI / 2; pg.add(pl);
    const rim = new THREE.Mesh(new THREE.RingGeometry(r * 0.74, r * 0.8, 48), new THREE.MeshBasicMaterial({ color: COL.coral, side: THREE.DoubleSide }));
    rim.position.z = Math.sign(z) * (th / 2 + 0.003); pg.add(rim);
    const rim2 = rim.clone(); rim2.position.z = -rim.position.z; pg.add(rim2);
    pg.position.z = z + Math.sign(z) * dz; pg.userData = { z0: pg.position.z, outer, s: Math.sign(z) }; g.add(pg); plates.push(pg);
  }
  scene.add(g); return { g, plates };
}
const bench = Bench(), bench2 = Bench(), bar = Bar(), bar2 = Bar();
const arc = new THREE.Mesh(new THREE.RingGeometry(0.95, 1.0, 48, 1, 0, 0.5), new THREE.MeshBasicMaterial({ color: COL.coral, side: THREE.DoubleSide, transparent: true }));
scene.add(arc);

// celular (CTA)
const phoneC = document.createElement("canvas"); phoneC.width = 600; phoneC.height = 1220; const pctx = phoneC.getContext("2d");
const phoneTex = new THREE.CanvasTexture(phoneC); phoneTex.colorSpace = THREE.SRGBColorSpace;
const phone = new THREE.Group();
phone.add(new THREE.Mesh(new THREE.BoxGeometry(1.42, 2.86, 0.08), flat(0x1c1d23)));
const screen = new THREE.Mesh(new THREE.PlaneGeometry(1.3, 2.64), new THREE.MeshBasicMaterial({ map: phoneTex })); screen.position.z = 0.041; phone.add(screen);
phone.position.set(30, 1.8, 0); scene.add(phone);
function drawPhone(t, t0) {
  const x = pctx; x.fillStyle = "#121318"; x.fillRect(0, 0, 600, 1220);
  x.fillStyle = "#8a8d96"; x.font = "bold 26px SpaceMono"; x.fillText("SEU TREINO · PEITO", 40, 110);
  x.fillStyle = "#f5f2eb"; x.font = "64px Anton"; x.fillText("Brio", 40, 200);
  const rows = [["SUPINO RETO", "60 KG × 8", "#f6b81a"], ["SUPINO INCLINADO", "50 KG × 8", "#ff5c3d"]];
  rows.forEach(([a, b, c], i) => { const p = eo(prog(t, t0 + 0.3 + i * 0.4, 0.35)); x.globalAlpha = p;
    x.fillStyle = "#1e2028"; x.beginPath(); x.roundRect(30, 270 + i * 190, 540, 160, 26); x.fill();
    x.fillStyle = c; x.fillRect(30, 270 + i * 190, 12, 160); x.fillStyle = "#c9ccd4"; x.font = "bold 28px SpaceMono"; x.fillText(a, 70, 330 + i * 190);
    x.fillStyle = "#f5f2eb"; x.font = "70px Anton"; x.fillText(b, 70, 410 + i * 190); x.globalAlpha = 1; });
  // gráfico de evolução
  const p = eo(prog(t, t0 + 1.2, 1.2)); x.strokeStyle = "#ff5c3d"; x.lineWidth = 8; x.lineJoin = "round"; x.beginPath();
  const pts = [[60, 1060], [160, 1020], [260, 1030], [360, 960], [460, 930], [540, 860]]; const n = Math.max(2, Math.ceil(pts.length * p));
  pts.slice(0, n).forEach(([a, b], i) => (i ? x.lineTo(a, b) : x.moveTo(a, b))); x.stroke();
  x.fillStyle = "#8a8d96"; x.font = "bold 24px SpaceMono"; x.fillText("EVOLUÇÃO · 8 SEMANAS", 40, 760);
  phoneTex.needsUpdate = true;
}

// ------------------------------------------------------------------ roteiro visual
// cada beat: câmera inicial → final (posição, alvo), com corte seco entre beats
function shot(b, k, p) {
  const hand = V(p.hand), chest = V(p.S).lerp(V(p.J), 0.25), headP = V(p.head);
  const S = [
    [[-3.6, 1.2, 2.4], [-3.1, 1.5, 3.1], [-0.9, 1.3, 0], [-0.8, 1.35, 0]],          // 0 gancho: baixo, perto, girando
    [[-0.9, 6.4, 0.9], [-0.9, 5.6, 0.5], [-0.8, 0.9, 0], [-0.8, 0.9, 0]],           // 1 reto: de cima
    [[0.2, 1.5, 6.4], [2.6, 2.1, 5.4], [-0.6, 1.3, 0], [-0.7, 1.4, 0]],             // 2 inclina: lateral orbitando
    [[-3.4, 3.3, 1.5], [-3.0, 3.0, 1.9], [chest.x, chest.y, 0.2], [chest.x, chest.y, 0.2]], // 3 clavícula: close alto
    [[hand.x + 2.2, 2.9, 3.2], [hand.x + 1.6, 2.6, 3.0], [hand.x + 0.2, hand.y - 0.6, 0.5], [hand.x + 0.2, hand.y - 0.6, 0.5]], // 4 carga: anilha
    [[3.6, 3.6, 7.4], [3.0, 3.2, 6.8], [-0.6, 1.2, 0], [-0.6, 1.2, 0]],             // 5 os dois
    [[31.6, 2.3, 3.6], [30.9, 2.0, 3.0], [30, 1.8, 0], [30, 1.8, 0]],              // 6 celular
  ][b];
  const kk = ease(k), M = [2.3, 1.45, 1.55, 2.0, 2.2, 1.4, 1.75][b];
  const tg = new THREE.Vector3(...S[2]).lerp(new THREE.Vector3(...S[3]), kk);
  const ps = new THREE.Vector3(...S[0]).lerp(new THREE.Vector3(...S[1]), kk);
  return [tg.clone().add(ps.sub(tg).multiplyScalar(M)), tg];
}
function state(t) {
  const b = beatAt(t), k = (t - ST[b]) / ((ST[b + 1] ?? DUR) - ST[b]);
  let inc = b < 2 ? 0 : b === 2 ? 30 * ease((k - 0.15) / 0.45) : 30;
  if (b >= 5) inc = 0;
  const speed = b === 3 ? 1.9 : 2.7;
  const plateOff = b === 4 ? ease((k - 0.25) / 0.4) : b > 4 ? 1 : 0;
  const lowA = b === 1 ? eo(prog(k, 0.15, 0.25)) : b === 0 ? 0.55 : b >= 2 && b <= 4 ? 0.25 : 0.7;
  const upA = b >= 2 && b <= 4 ? eo(prog(t, ST[2] + 1.2, 0.5)) : 0;
  return { b, k, inc, speed, plateOff, lowA, upA };
}

// ------------------------------------------------------------------ texto
const out = document.createElement("canvas"); out.width = W; out.height = H; document.body.appendChild(out);
const ctx = out.getContext("2d");
function title(l1, l2, t, t0) {
  ctx.textAlign = "left";
  [[l1, "#f2ede3"], [l2, "#ff5c3d"]].forEach(([s, col], i) => {
    const p = eo(prog(t, t0 + i * 0.08, 0.28)); let size = 142; ctx.font = `${size}px Anton`;
    while (ctx.measureText(s).width > 950 && size > 90) { size -= 6; ctx.font = `${size}px Anton`; }
    ctx.globalAlpha = p; ctx.fillStyle = col; ctx.fillText(s, 70, 430 + i * 150 + (1 - p) * 30);
  });
  ctx.globalAlpha = 1;
}
function label(s, v, col = "#c9ccd4", size = 30, a = 1, dy = 0) {
  if (a <= 0) return; const q = v.clone().project(camera); if (q.z > 1) return;
  const x = (q.x + 1) / 2 * W, y = (1 - q.y) / 2 * H + dy;
  ctx.globalAlpha = a; ctx.font = `bold ${size}px SpaceMono`; ctx.fillStyle = col; ctx.textAlign = "center";
  ctx.fillText(s, x, y); ctx.globalAlpha = 1; return [x, y];
}
function big(s, x, y, size, col, a) { if (a <= 0) return; ctx.globalAlpha = a; ctx.font = `${size}px Anton`; ctx.fillStyle = col; ctx.textAlign = "center"; ctx.fillText(s, x, y); ctx.globalAlpha = 1; }
function vignette() { const g = ctx.createRadialGradient(540, 1050, 300, 540, 1050, 1250); g.addColorStop(0, "rgba(0,0,0,0)"); g.addColorStop(1, "rgba(0,0,0,0.55)"); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H); }

// ------------------------------------------------------------------ quadro
let phase = 0, lastF = -1;
window.renderFrame = (f, fmt = "image/jpeg", q = 0.93) => {
  if (f !== lastF + 1) { phase = 0; for (let k = 0; k < f; k++) phase += state(k / FPS).speed / FPS; }
  const t = f / FPS, st = state(t); phase += st.speed / FPS; lastF = f;
  const u = 0.5 - 0.5 * Math.cos(phase);
  const p = pose(st.inc, u);
  me.set(p); placeBench(bench, p, st.inc);
  bar.g.position.copy(V(p.hand));
  for (const g of bar.plates) if (g.userData.outer) { g.position.z = g.userData.z0 + g.userData.s * 1.6 * st.plateOff; g.visible = st.plateOff < 0.97; }
  placeMarks(me, st.lowA * (0.6 + 0.4 * u), st.upA * (0.6 + 0.4 * u), t);
  // segundo personagem só no beat 5 (reto x inclinado lado a lado)
  const two = st.b === 5; const oz = two ? 1.9 : 0;
  if (two) {
    const pA = pose(0, u); me.set(pA, 0, oz); placeBench(bench, pA, 0, 0, oz); bar.g.position.copy(V(pA.hand, 0, 0, oz));
    const u2 = 0.5 - 0.5 * Math.cos(phase + 1.3), pB = pose(30, u2); rival.set(pB, 0, -1.9); placeBench(bench2, pB, 30, 0, -1.9); bar2.g.position.copy(V(pB.hand, 0, 0, -1.9));
    for (const g of bar.plates) g.visible = true, g.userData.outer && (g.position.z = g.userData.z0);
    placeMarks(me, 0.8 * (0.6 + 0.4 * u), 0, t);
  }
  rival.g.visible = two; for (const o of Object.values(bench2)) o.visible = two; bar2.g.visible = two;
  // arco do ângulo
  const Hw = V(p.H); arc.visible = st.b === 2 && st.inc > 1;
  arc.geometry.dispose(); arc.geometry = new THREE.RingGeometry(0.95, 1.02, 48, 1, Math.PI - st.inc * Math.PI / 180, Math.max(0.01, st.inc * Math.PI / 180));
  arc.position.set(Hw.x, Hw.y + 0.02, 0.42);
  // câmera
  const [cp, ct] = shot(st.b, st.k, p); camera.position.copy(cp); camera.lookAt(ct);
  if (st.b === 6) { drawPhone(t, ST[6]); phone.rotation.y = -0.25 + 0.15 * ease(st.k); }
  renderer.render(scene, camera);
  ctx.drawImage(renderer.domElement, 0, 0, W, H); vignette();
  const B = TL.beats[st.b]; title(B.t1, B.t2, t, ST[st.b] - 0.05);
  // rótulos presos ao 3D
  const lt = t - ST[st.b];
  if (st.b === 1) label("PEITO INTEIRO", V(p.S).lerp(V(p.J), 0.3).add(new THREE.Vector3(0, 0.2, 0.9)), "#f6b81a", 32, eo(prog(lt, 0.6, 0.3)));
  if (st.b === 2) label(`${Math.round(st.inc)}°`, Hw.clone().add(new THREE.Vector3(-1.2, 0.45, 0.42)), "#ff5c3d", 64, clamp(st.inc / 10));
  if (st.b === 3) label("PARTE DE CIMA", V(p.S).add(new THREE.Vector3(0.2, 1.25, 0.2)), "#ff5c3d", 38, eo(prog(lt, 0.5, 0.3)));
  if (st.b === 4) { ctx.fillStyle = "rgba(13,14,18,.82)"; ctx.beginPath(); ctx.roundRect(140, 1440, 800, 170, 30); ctx.fill(); big("60 KG", 330, 1570, 120, "#8a8d96", 1 - st.plateOff * 0.6); big("→", 540, 1565, 100, "#c9ccd4", st.plateOff); big("50 KG", 760, 1570, 120, "#ff5c3d", st.plateOff); }
  if (two) {
    label("RETO", V(pose(0, 0).H, 0, 0.3, oz).setY(0.05), "#f6b81a", 40, eo(prog(lt, 0.4, 0.3)), 70);
    label("INCLINADO", V(pose(30, 0).H, 0, 0.3, -1.9).setY(0.05), "#ff5c3d", 40, eo(prog(lt, 0.7, 0.3)), 70);
  }
  if (st.b === 6) { ctx.globalAlpha = eo(prog(lt, 0.8, 0.3)); ctx.font = "bold 30px SpaceMono"; ctx.fillStyle = "#c9ccd4"; ctx.textAlign = "center"; ctx.fillText("LINK NA BIO", 540, 1600); ctx.globalAlpha = 1; }
  return out.toDataURL(fmt, q);
};
window.FRAMES = Math.round(DUR * FPS); window.FPS = FPS;
window.ready = document.fonts.load("140px Anton").then(() => document.fonts.load("bold 30px SpaceMono")).then(() => true);
renderer.domElement.style.display = "none"; document.body.appendChild(renderer.domElement);
