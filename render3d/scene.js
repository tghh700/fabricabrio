// Brio 3D — v3: personagem com malha contínua, fibras do peitoral, linha do tempo amarrada à narração.
import * as THREE from "three";
import { RoundedBoxGeometry } from "three/addons/geometries/RoundedBoxGeometry.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";
import { OutputPass } from "three/addons/postprocessing/OutputPass.js";
import { makeCharacter, poseCharacter, poseFibers } from "./body.js";

const W = 1080, H = 1920, FPS = 30;
const P = new URLSearchParams(location.search);
const SCALE = parseFloat(P.get("scale") || "1");
const RW = Math.round(W * SCALE), RH = Math.round(H * SCALE);
const TL = await (await fetch(P.get("tempos") || "roteiros/brio3d_01_tempos.json")).json();
const DUR = TL.dur + 0.5, ST = TL.starts;
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lerp = (a, b, t) => a + (b - a) * t;
const ease = (x) => { x = clamp(x); return x * x * (3 - 2 * x); };
const eo = (x) => { x = clamp(x); return 1 - (1 - x) ** 3; };
const bo = (x) => { x = clamp(x); const c = 1.7; return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2; };
const prog = (t, s, d) => clamp((t - s) / d);
const C = { coral: 0xff5c3d, cream: 0xefe6da, navy: 0x2b2f5c, ink: 0x15151c, steel: 0xc9ccd4, rubber: 0x1d1e24, bench: 0x1b1c22, lilac: 0x9c8cff };
const beatAt = (t) => { let i = 0; while (i < ST.length - 1 && t >= ST[i + 1]) i++; return i; };

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
  const J = Pp(0, 50), S = Pp(290, 52), head = Pp(378, 64), K = [J[0] + 170, J[1] - 60], F = [K[0] + 45, 1340];
  const hand = [S[0] + (inclDeg < 10 ? 60 : 38), S[1] - lerp(70, 238, u)];
  return { H: Hp, J, S, head, K, F, hand, E: ik(S, hand, 132, 125), back: Pp(430, 0), mid: Pp(300, 0), seat: [Hp[0] + 150, Hp[1]], n };
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

// ------------------------------------------------------------------ personagem e equipamentos
const PAL = { skin: 0xc98d6a, hair: 0x231917, top: 0x272c5c, shorts: 0x4a4d5c, accent: C.coral };
const ch = makeCharacter(scene, PAL);
const matte = new THREE.MeshStandardMaterial({ color: 0x8a8d96, metalness: 0.5, roughness: 0.55 });
const seat = add(new THREE.Mesh(new RoundedBoxGeometry(0.85, 0.2, 0.8, 5, 0.08), M.pad));
const back = add(new THREE.Mesh(new RoundedBoxGeometry(2.2, 0.2, 0.8, 5, 0.08), M.pad));
const legF = add(new THREE.Mesh(new THREE.CylinderGeometry(0.055, 0.055, 1, 16), matte));
const legB = add(new THREE.Mesh(new THREE.CylinderGeometry(0.055, 0.055, 1, 16), matte));
const footF = add(new THREE.Mesh(new RoundedBoxGeometry(0.14, 0.07, 0.95, 2, 0.025), matte));
const footB = add(new THREE.Mesh(new RoundedBoxGeometry(0.14, 0.07, 0.95, 2, 0.025), matte));
const bar = new THREE.Group(); const plates = [];
{ const shaft = new THREE.Mesh(new THREE.CylinderGeometry(0.033, 0.033, 3.2, 20), M.steel); shaft.rotation.x = Math.PI / 2; bar.add(shaft);
  for (const z of [-1.2, 1.2]) {
    for (const [r, th, dz, outer] of [[0.5, 0.1, 0, 0], [0.4, 0.08, 0.1, 1]]) {
      const g = new THREE.Group();
      const pl = new THREE.Mesh(new THREE.CylinderGeometry(r, r, th, 64), M.rubber); pl.rotation.x = Math.PI / 2; g.add(pl);
      const lip = new THREE.Mesh(new THREE.TorusGeometry(r * 0.8, 0.012, 8, 64), new THREE.MeshBasicMaterial({ color: new THREE.Color(C.coral).multiplyScalar(0.9) }));
      lip.position.z = Math.sign(z) * (th / 2 + 0.002); g.add(lip);
      g.position.z = z + Math.sign(z) * dz; g.userData = { z0: g.position.z, outer, s: Math.sign(z) }; bar.add(g); plates.push(g);
    }
    const col = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.06, 0.08, 20), M.steel); col.rotation.x = Math.PI / 2; col.position.z = z - Math.sign(z) * 0.1; bar.add(col);
  }
  bar.traverse((o) => { o.castShadow = o.receiveShadow = true; }); scene.add(bar); }
// arco do ângulo do banco
const arc = new THREE.Mesh(new THREE.TorusGeometry(0.9, 0.018, 8, 48, Math.PI / 6), new THREE.MeshBasicMaterial({ color: new THREE.Color(C.coral).multiplyScalar(1.4), transparent: true, opacity: 0 }));
scene.add(arc);

// ------------------------------------------------------------------ roteiro visual (por beat)
// inclinação do banco, ritmo da repetição, peso (anilha externa sai), ativação baixo/cima
function state(t) {
  const [s0, s1, s2, s3, s4, s5, s6] = ST;
  let inc = 30 * ease((t - (s2 + 0.15)) / 1.0);
  if (t > s5) inc = 30 * (1 - ease((t - (s5 + 0.4)) / 0.8)) + 30 * ease((t - (s5 + 2.8)) / 0.8);
  const speed = t > s3 && t < s4 ? 2.0 : 2.7;
  const plateOff = ease((t - (s4 + 0.6)) / 0.8);
  const up = inc > 15;
  const flash = (a) => eo(prog(t, a, 0.4));
  const low = up ? 0.15 : 0.35 + 0.6 * (t > s1 ? flash(s1) : 0.4);
  const upp = up ? 0.4 + 0.6 * flash(s2 + 1.0) : 0.1;
  return { inc, speed, plateOff, low, upp };
}
let phase = 0, lastT = 0;
const keys = () => { const [s0, s1, s2, s3, s4, s5, s6] = ST; return [
  // t, ângulo, distância, altura, alvo x, alvo y
  [0, -0.85, 11.4, 4.6, -0.3, 1.95], [s1, -0.55, 10.4, 4.4, -0.35, 1.95], [s1 + 3.5, -0.35, 7.6, 4.3, -0.75, 2.05],
  [s2 + 0.2, -0.2, 9.8, 3.6, -0.45, 1.95], [s3, -0.45, 9.2, 4.3, -0.6, 2.0], [s3 + 0.6, -0.55, 5.2, 6.0, -1.05, 1.95], [s4, -0.45, 4.8, 5.8, -1.1, 2.0],
  [s4 + 0.5, -0.15, 9.6, 3.8, -0.4, 1.95], [s5, -0.3, 10.2, 4.2, -0.4, 1.95], [s6, -0.75, 11.0, 4.8, -0.35, 1.95], [DUR, -0.5, 12.6, 5.6, -0.3, 2.05]]; };
function cam(t) {
  const K = keys(); let i = 0; while (i < K.length - 2 && t > K[i + 1][0]) i++;
  const [t0, ...a] = K[i], [t1, ...b] = K[i + 1], k = ease((t - t0) / (t1 - t0));
  const [ang, d, h, tx, ty] = a.map((v, j) => lerp(v, b[j], k));
  camera.position.set(tx + d * Math.sin(ang), h, d * Math.cos(ang)); camera.lookAt(tx, ty, 0);
}

const composer = new EffectComposer(renderer);
composer.addPass(new RenderPass(scene, camera));
composer.addPass(new UnrealBloomPass(new THREE.Vector2(RW, RH), 0.5, 0.45, 0.92));
composer.addPass(new OutputPass());

// ------------------------------------------------------------------ texto
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
    const p = eo(prog(t, t0 + i * 0.1, 0.3)); let size = 150;
    ctx.font = `${size}px Anton`; while (ctx.measureText(s).width > 950 && size > 90) { size -= 6; ctx.font = `${size}px Anton`; }
    ctx.globalAlpha = p; ctx.fillStyle = col; ctx.shadowColor = "rgba(0,0,0,.5)"; ctx.shadowBlur = 24;
    ctx.fillText(s, 70 - (1 - p) * 90, 450 + i * 158);
  });
  ctx.globalAlpha = 1; ctx.shadowBlur = 0;
}
const PILLS = [null, ["PEITO TODO", "#f6b81a", "#15151c"], null, ["PARTE DE CIMA", "#ff5c3d", "#ffffff"], ["MENOS PESO", "#f5f2eb", "#15151c"],
  ["OS DOIS CRESCEM O PEITO", "#f6b81a", "#15151c"], ["COMENTA RETO OU INCLINADO", "#ff5c3d", "#ffffff"]];
function overlay(t, st, arcPos) {
  const b = beatAt(t), B = TL.beats[b];
  title(B.t1, B.t2, t, ST[b] - 0.05);
  const pl = PILLS[b]; if (pl) pill(pl[0], pl[1], pl[2], bo(prog(t, ST[b] + 0.5, 0.3)));
  if (arcPos && st.inc > 2) { // rótulo do ângulo, preso ao arco no 3D
    const v = arcPos.clone().project(camera); const x = (v.x + 1) / 2 * W, y = (1 - v.y) / 2 * H;
    ctx.globalAlpha = clamp(st.inc / 20) * (b === 2 || b === 5 ? 1 : 0); ctx.font = "84px Anton"; ctx.fillStyle = "#ff5c3d"; ctx.textAlign = "center";
    ctx.shadowColor = "rgba(0,0,0,.6)"; ctx.shadowBlur = 16; ctx.fillText(`${Math.round(st.inc)}°`, x, y); ctx.globalAlpha = 1; ctx.shadowBlur = 0;
  }
}

// ------------------------------------------------------------------ quadro
window.renderFrame = (f, fmt = "image/jpeg", q = 0.93) => {
  const t = f / FPS, st = state(t);
  // fase da repetição integrada (velocidade muda sem saltos)
  if (f === 0 || t < lastT) { phase = 0; lastT = 0; for (let k = 0; k < f; k++) { const tk = k / FPS; phase += state(tk).speed / FPS; } lastT = t; }
  else { for (let tk = lastT; tk < t - 1e-6; tk += 1 / FPS) phase += state(tk).speed / FPS; lastT = t; }
  const u = 0.5 - 0.5 * Math.cos(phase);
  const p = pose(st.inc, u);
  const nrm = new THREE.Vector3(p.n[0], -p.n[1], 0);
  const legs = [-1, 1].map((s) => [V(p.J, s * 0.22), V(p.K, s * 0.34), V([p.F[0], p.F[1] - 30], s * 0.42)]);
  const arms = [-1, 1].map((s) => [V(p.S, s * 0.36), V(p.E, s * 0.74), V(p.hand, s * 0.78)]);
  poseCharacter(ch, V(p.J), V(p.S), nrm, legs, arms, V(p.head), t, clamp(u * 1.4 - 0.2));
  poseFibers(ch, t, st.low * (0.6 + 0.4 * u), st.upp * (0.6 + 0.4 * u));
  // banco
  const Hw = V(p.H), Bw = V(p.back), Sw = V(p.seat), tilt = Math.atan2(Bw.y - Hw.y, Bw.x - Hw.x);
  back.position.copy(Hw).lerp(Bw, 0.5).add(new THREE.Vector3(Math.sin(tilt) * 0.1, -Math.cos(tilt) * 0.1, 0)); back.rotation.z = tilt + Math.PI;
  seat.position.set((Hw.x + Sw.x) / 2 + 0.05, Hw.y - 0.1, 0);
  const lf = Sw.x - 0.08; legF.position.set(lf, (Hw.y - 0.2) / 2, 0); legF.scale.y = Hw.y - 0.2; footF.position.set(lf, 0.035, 0);
  const mid = V(p.mid), lb = st.inc < 5 ? Bw.x + 0.25 : mid.x + 0.05, topy = st.inc < 5 ? Hw.y - 0.2 : lerp(Hw.y, mid.y, 0.8) - 0.2;
  legB.position.set(lb, topy / 2, 0); legB.scale.y = topy; footB.position.set(lb, 0.035, 0);
  // barra e anilhas externas saindo
  const hp = V(p.hand); bar.position.set(hp.x, hp.y, 0);
  for (const g of plates) if (g.userData.outer) { g.position.z = g.userData.z0 + g.userData.s * 1.4 * st.plateOff; g.visible = st.plateOff < 0.98; g.scale.setScalar(1 - 0.3 * st.plateOff); }
  // arco do ângulo no pivô do banco
  arc.position.copy(Hw).add(new THREE.Vector3(0, 0.02, 0.45)); arc.rotation.set(0, 0, Math.PI - tilt * 0 - Math.PI / 6 * (st.inc / 30));
  arc.geometry.dispose(); arc.geometry = new THREE.TorusGeometry(0.9, 0.02, 8, 48, Math.max(0.01, st.inc * Math.PI / 180)); arc.rotation.set(0, 0, Math.PI - st.inc * Math.PI / 180);
  const b = beatAt(t); arc.material.opacity = (b === 2 || b === 5) ? clamp(st.inc / 15) : 0;
  const arcMid = Hw.clone().add(new THREE.Vector3(-Math.cos(st.inc * Math.PI / 360) * 1.25, Math.sin(st.inc * Math.PI / 360) * 1.25 + 0.05, 0.45));
  cam(t); rim.intensity = 16 + 10 * u;
  composer.render();
  ctx.drawImage(renderer.domElement, 0, 0, W, H);
  overlay(t, st, arcMid);
  return out.toDataURL(fmt, q);
};
window.FRAMES = Math.round(DUR * FPS); window.FPS = FPS;
window.ready = document.fonts.load("150px Anton").then(() => document.fonts.ready).then(() => true);
renderer.domElement.style.display = "none"; document.body.appendChild(renderer.domElement);
