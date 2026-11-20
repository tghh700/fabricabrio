// Brio 2,5D: esqueleto e câmera em 3D, mas tudo DESENHADO em 2D (formas chapadas no canvas), como a referência.
// Membros = traços grossos de ponta redonda com espessura pela perspectiva; tronco = feijão chapado; chão e cenário em linhas 3D.
import * as THREE from "three";

const W = 1080, H = 1920, FPS = 30;
const P = new URLSearchParams(location.search);
const TL = await (await fetch(P.get("tempos") || "roteiros/brio_chain_01_tempos.json")).json();
const DUR = TL.dur + 0.5, ST = TL.starts;
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lerp = (a, b, t) => a + (b - a) * t;
const ease = (x) => { x = clamp(x); return x * x * (3 - 2 * x); };
const eo = (x) => { x = clamp(x); return 1 - (1 - x) ** 3; };
const bo = (x) => { x = clamp(x); const c = 1.7; return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2; };
const prog = (t, s, d) => clamp((t - s) / d);
const beatAt = (t) => { let i = 0; while (i < ST.length - 1 && t >= ST[i + 1]) i++; return i; };
const v3 = (x, y, z) => new THREE.Vector3(x, y, z);

const HERO = { body: "#efe9de", head: "#f3eee4", armN: "#d9d2c6", armF: "#a9a296", legN: "#cfc8bc", legF: "#a39c90" };
const DARK = { body: "#4d5262", head: "#575c6c", armN: "#464a58", armF: "#343743", legN: "#4a4e5c", legF: "#363945" };
const CORAL = "#ff5c3d", YEL = "#ff5c3d", GOLD = "#f6b81a", CREAM = "#f2ede3", GREY = "#8a8d96";

const cv = document.createElement("canvas"); cv.width = W; cv.height = H; document.body.appendChild(cv);
const ctx = cv.getContext("2d");
const camera = new THREE.PerspectiveCamera(34, W / H, 0.05, 80);
let CY = 0; // deslocamento vertical do quadro (personagem abaixo dos títulos)

function proj(v) { const c = v.clone().applyMatrix4(camera.matrixWorldInverse); const depth = -c.z; const q = v.clone().project(camera);
  const f = (H / 2) / Math.tan(THREE.MathUtils.degToRad(camera.fov / 2));
  return { x: (q.x + 1) / 2 * W, y: (1 - q.y) / 2 * H + CY, s: f / Math.max(depth, 0.05), d: depth }; }

// ------------------------------------------------------------------ esqueleto (mesmo do flat2, com base afastada)
function ik2(a, b, L1, L2, bend) {
  const d = Math.max(Math.min(a.distanceTo(b), L1 + L2 - 1e-3), Math.abs(L1 - L2) + 1e-3);
  const dir = b.clone().sub(a).normalize(), x = (L1 * L1 - L2 * L2 + d * d) / (2 * d), h = Math.sqrt(Math.max(0, L1 * L1 - x * x));
  return a.clone().addScaledVector(dir, x).addScaledVector(v3(-dir.y, dir.x, 0).multiplyScalar(bend), h).setZ(a.z);
}
function skel({ drop = 0, back = 0, lean = 0, walk = null, stance = 0.16, bob = 0, arms }) {
  const pelvis = v3(-back, 0.97 - drop + bob, 0), up = v3(Math.sin(lean), Math.cos(lean), 0);
  const neck = pelvis.clone().addScaledVector(up, 0.64), head = pelvis.clone().addScaledVector(up, 0.9);
  const j = { pelvis, neck, head, hip: [], knee: [], ankle: [], sh: [], el: [], wr: [], up };
  [-1, 1].forEach((s, i) => {
    const hip = pelvis.clone().add(v3(0, 0, s * 0.13));
    let ank = v3(s * stance, 0.06, s * 0.2);
    if (walk !== null) { const ph = walk + (i ? Math.PI : 0); ank = v3(0.3 * Math.sin(ph), 0.06 + Math.max(0, 0.13 * Math.cos(ph)), s * 0.14); }
    j.hip.push(hip); j.ankle.push(ank); j.knee.push(ik2(hip, ank, 0.48, 0.48, 1).setZ(s * 0.17));
    const sh = neck.clone().addScaledVector(up, -0.08).add(v3(0, 0, s * 0.27)); j.sh.push(sh);
    const [el, wr] = arms(i, s, sh, up); j.el.push(el); j.wr.push(wr);
  });
  return j;
}
const hang = (sw = 0) => (i, s, sh) => [sh.clone().add(v3(0.03 + sw, -0.35, s * 0.05)), sh.clone().add(v3(0.07 + sw * 1.7, -0.68, s * 0.07))];
const curl = (u) => (i, s, sh) => { const el = sh.clone().add(v3(0.03, -0.35, s * 0.03)); const a = lerp(-0.1, 2.45, i ? u : clamp(1 - u)); return [el, el.clone().add(v3(0.33 * Math.sin(a), -0.33 * Math.cos(a), 0))]; };
const squatArms = () => (i, s, sh) => [sh.clone().add(v3(-0.26, -0.06, s * 0.14)), sh.clone().add(v3(-0.16, 0.1, s * 0.3))];
const flex = (u) => (i, s, sh) => { const el = sh.clone().add(v3(0.02, 0.02, s * 0.33)); const a = lerp(0.55, 1.3, u); return [el, el.clone().add(v3(0, 0.33 * Math.sin(a), s * 0.33 * Math.cos(a)))]; };
const thumbs = () => (i, s, sh) => i === 1 ? [sh.clone().add(v3(0.3, -0.18, s * 0.05)), sh.clone().add(v3(0.42, 0.12, s * 0.05))] : hang()(i, s, sh);
const shrug = (u) => (i, s, sh) => [sh.clone().add(v3(0.12, -0.28, s * 0.18)), sh.clone().add(v3(0.36, -0.2 + 0.08 * u, s * 0.3))];
const run = (ph) => (i, s, sh) => { const a = 0.9 * Math.sin(ph + (i ? 0 : Math.PI)); const el = sh.clone().add(v3(0.3 * Math.sin(a), -0.3 * Math.cos(a), s * 0.04)); return [el, el.clone().add(v3(0.3, 0.12, 0))]; };

function world(j, pos, yaw) { const M = new THREE.Matrix4().makeRotationY(yaw).setPosition(pos); const w = (p) => p.clone().applyMatrix4(M);
  return { pelvis: w(j.pelvis), neck: w(j.neck), head: w(j.head), hip: j.hip.map(w), knee: j.knee.map(w), ankle: j.ankle.map(w), sh: j.sh.map(w), el: j.el.map(w), wr: j.wr.map(w),
    fwd: v3(1, 0, 0).applyAxisAngle(v3(0, 1, 0), yaw) }; }

// ------------------------------------------------------------------ desenho
function line(a, b, wm, col, alpha = 1) { const A = proj(a), B = proj(b); ctx.globalAlpha = alpha; ctx.strokeStyle = col; ctx.lineCap = "round"; ctx.lineJoin = "round";
  ctx.lineWidth = wm * (A.s + B.s) / 2; ctx.beginPath(); ctx.moveTo(A.x, A.y); ctx.lineTo(B.x, B.y); ctx.stroke(); ctx.globalAlpha = 1; }
function poly3(pts, wm, col, alpha = 1) { const Q = pts.map(proj); ctx.globalAlpha = alpha; ctx.strokeStyle = col; ctx.lineCap = "round"; ctx.lineJoin = "round";
  ctx.lineWidth = wm * Q.reduce((a, q) => a + q.s, 0) / Q.length; ctx.beginPath(); Q.forEach((q, i) => (i ? ctx.lineTo(q.x, q.y) : ctx.moveTo(q.x, q.y))); ctx.stroke(); ctx.globalAlpha = 1; }
function disc(c, rm, col, alpha = 1) { const C = proj(c); ctx.globalAlpha = alpha; ctx.fillStyle = col; ctx.beginPath(); ctx.arc(C.x, C.y, rm * C.s, 0, 7); ctx.fill(); ctx.globalAlpha = 1; return C; }
function torso(pel, neck, widths, col, alpha = 1) { // "ovo": união de discos ao longo do eixo (largo no peito, afina no quadril)
  ctx.globalAlpha = alpha; ctx.fillStyle = col; ctx.beginPath();
  for (let i = 0; i <= 24; i++) { const t = i / 24, p = proj(pel.clone().lerp(neck, t));
    const w = t < 0.62 ? lerp(widths[0], widths[1], Math.sin(t / 0.62 * Math.PI / 2)) : lerp(widths[1], widths[2], (t - 0.62) / 0.38);
    ctx.moveTo(p.x + w * p.s / 2, p.y); ctx.arc(p.x, p.y, w * p.s / 2, 0, 7); }
  ctx.fill(); ctx.globalAlpha = 1;
}
function shadow(c, r) { const C = proj(v3(c.x, 0, c.z)), E = proj(v3(c.x + r, 0, c.z)), F = proj(v3(c.x, 0, c.z + r));
  ctx.save(); ctx.translate(C.x, C.y); ctx.scale(Math.max(8, Math.hypot(E.x - C.x, E.y - C.y)), Math.max(4, Math.hypot(F.x - C.x, F.y - C.y)));
  const g = ctx.createRadialGradient(0, 0, 0, 0, 0, 1); g.addColorStop(0, "rgba(0,0,0,.55)"); g.addColorStop(1, "rgba(0,0,0,0)"); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(0, 0, 1, 0, 7); ctx.fill(); ctx.restore(); }
function glove(c, rm, col) { const C = disc(c, rm, col); ctx.strokeStyle = "rgba(255,255,255,.45)"; ctx.lineWidth = rm * C.s * 0.18; ctx.lineCap = "round";
  ctx.beginPath(); ctx.arc(C.x, C.y, rm * C.s * 0.62, -2.4, -1.3); ctx.stroke(); }

// personagem: pernas atrás, braço de lá, tronco, cabeça, braço de cá (como a referência)
function figure(J, pal, alpha = 1, opts = {}) { const K = opts.bulk || 1;
  const D = (v) => proj(v).d;
  const nearArm = D(J.sh[0]) < D(J.sh[1]) ? 0 : 1, nearLeg = D(J.hip[0]) < D(J.hip[1]) ? 0 : 1;
  const leg = (i) => { const c = i === nearLeg ? pal.legN : pal.legF; poly3([J.hip[i], J.knee[i], J.ankle[i]], 0.17 * (0.85 + 0.15 * K), c, alpha);
    line(J.ankle[i], J.ankle[i].clone().addScaledVector(J.fwd, 0.16), 0.11, c, alpha); };
  const arm = (i) => { const c = i === nearArm ? pal.armN : pal.armF; poly3([J.sh[i], J.el[i], J.wr[i]], 0.13 * K, c, alpha);
    if (opts.gloves) glove(J.wr[i], 0.1, opts.gloves); else disc(J.wr[i], 0.075, c, alpha); if (opts.hand) opts.hand(i, J.wr[i]); };
  leg(1 - nearLeg); leg(nearLeg); arm(1 - nearArm);
  const ax = J.neck.clone().sub(J.pelvis).normalize();
  torso(J.pelvis.clone().addScaledVector(ax, -0.06), J.neck.clone().addScaledVector(ax, 0.0), [0.44, 0.5 * (0.8 + 0.2 * K), 0.42 * K], pal.body, alpha);
  disc(J.head.clone().addScaledVector(ax, 0.04), 0.2, pal.head, alpha);
  arm(nearArm);
}

// ------------------------------------------------------------------ cenário em linhas 3D
function floorGrid(cx = 0, cz = 0, n = 10, alpha = 1) {
  ctx.strokeStyle = `rgba(255,255,255,${0.045 * alpha})`; ctx.lineWidth = 2;
  for (let i = -n; i <= n; i++) { [[v3(cx + i, 0, cz - n), v3(cx + i, 0, cz + n)], [v3(cx - n, 0, cz + i), v3(cx + n, 0, cz + i)]].forEach(([a, b]) => {
    const A = proj(a), B = proj(b); if (A.d < 0.1 || B.d < 0.1) return; ctx.beginPath(); ctx.moveTo(A.x, A.y); ctx.lineTo(B.x, B.y); ctx.stroke(); }); }
}
function seg3(a, b, col, px, alpha = 1) { const A = proj(a), B = proj(b); if (A.d < 0.1 || B.d < 0.1) return; ctx.globalAlpha = alpha; ctx.strokeStyle = col; ctx.lineWidth = px; ctx.lineCap = "round";
  ctx.beginPath(); ctx.moveTo(A.x, A.y); ctx.lineTo(B.x, B.y); ctx.stroke(); ctx.globalAlpha = 1; }
function gymFrame(alpha = 1) { // estrutura de rack/"gaiola" com faixas amarelas (como as cordas do ringue)
  const pts = [[-2.2, -1.6], [2.2, -1.6], [2.2, 1.6], [-2.2, 1.6]];
  pts.forEach(([x, z]) => { seg3(v3(x, 0, z), v3(x, 2.5, z), "#9aa0ab", 9, alpha); disc(v3(x, 2.5, z), 0.06, YEL, alpha); });
  [0.9, 1.4, 1.9].forEach((y) => { [[0, 1], [1, 2], [3, 0]].forEach(([a, b]) => seg3(v3(pts[a][0], y, pts[a][1]), v3(pts[b][0], y, pts[b][1]), YEL, 4, alpha * 0.85)); });
}
// objetos
function dumbbell(c, axis) { seg3(c.clone().addScaledVector(axis, -0.16), c.clone().addScaledVector(axis, 0.16), "#c0c3cb", 6); [-0.15, 0.15].forEach((k) => disc(c.clone().addScaledVector(axis, k), 0.11, CORAL)); }
function ring3(c, r, fill, stroke) { // círculo no plano XY (anilha vista em perspectiva real)
  const Q = []; for (let a = 0; a < 40; a++) { const t = a / 40 * Math.PI * 2; Q.push(proj(c.clone().add(v3(Math.cos(t) * r, Math.sin(t) * r, 0)))); }
  ctx.beginPath(); Q.forEach((q, i) => (i ? ctx.lineTo(q.x, q.y) : ctx.moveTo(q.x, q.y))); ctx.closePath();
  if (fill) { ctx.fillStyle = fill; ctx.fill(); } if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = 3; ctx.stroke(); } }
function barbell(c) { seg3(c.clone().add(v3(0, 0, -1.15)), c.clone().add(v3(0, 0, 1.15)), "#c0c3cb", 8);
  const zs = [-1.05, -0.95, 0.95, 1.05].sort((a, b) => proj(c.clone().add(v3(0, 0, b))).d - proj(c.clone().add(v3(0, 0, a))).d);
  zs.forEach((z) => { const p = c.clone().add(v3(0, 0, z)), r = Math.abs(z) > 1 ? 0.34 : 0.42; ring3(p, r, "#24262d", null); ring3(p, r * 0.78, null, CORAL); }); }
function bread(c, rot) { const A = proj(c.clone().add(v3(Math.cos(rot) * 0.2, 0, Math.sin(rot) * 0.2))), B = proj(c.clone().add(v3(-Math.cos(rot) * 0.2, 0, -Math.sin(rot) * 0.2)));
  ctx.strokeStyle = "#d9a35a"; ctx.lineCap = "round"; ctx.lineWidth = 0.2 * (A.s + B.s) / 2; ctx.beginPath(); ctx.moveTo(A.x, A.y); ctx.lineTo(B.x, B.y); ctx.stroke();
  ctx.strokeStyle = "#a8722f"; ctx.lineWidth = 0.025 * A.s; for (let k = -1; k <= 1; k++) { const m = { x: lerp(A.x, B.x, 0.5 + k * 0.25), y: lerp(A.y, B.y, 0.5 + k * 0.25) };
    ctx.beginPath(); ctx.moveTo(m.x - 0.04 * A.s, m.y - 0.05 * A.s); ctx.lineTo(m.x + 0.04 * A.s, m.y - 0.09 * A.s); ctx.stroke(); } }
function table(c) { const q = [v3(-0.55, 0.92, -0.4), v3(0.75, 0.92, -0.4), v3(0.75, 0.92, 0.4), v3(-0.55, 0.92, 0.4)].map((p) => p.add(c));
  q.forEach((p) => seg3(p, p.clone().setY(0), "#3a3c46", 10)); const Q = q.map(proj); ctx.fillStyle = "#2c2e37"; ctx.beginPath(); Q.forEach((p, i) => (i ? ctx.lineTo(p.x, p.y) : ctx.moveTo(p.x, p.y))); ctx.fill(); }

// ------------------------------------------------------------------ texto e HUD
function title(l1, l2, t, t0) { ctx.textAlign = "left";
  [[l1, CREAM], [l2, YEL]].forEach(([s, col], i) => { const p = eo(prog(t, t0 + 0.1 + i * 0.08, 0.28)); let size = 138; ctx.font = `${size}px Anton`;
    while (ctx.measureText(s).width > 950 && size > 90) { size -= 6; ctx.font = `${size}px Anton`; }
    ctx.save(); ctx.beginPath(); ctx.rect(0, 270 + i * 148, W, 195); ctx.clip(); ctx.fillStyle = col; ctx.fillText(s, 66, 420 + i * 148 + (1 - p) * 150); ctx.restore(); }); }
function big(s, x, y, size, col, a = 1, al = "center") { if (a <= 0) return; ctx.globalAlpha = a; ctx.font = `${size}px Anton`; ctx.fillStyle = col; ctx.textAlign = al; ctx.fillText(s, x, y); ctx.globalAlpha = 1; }
function mono(s, x, y, size, col, a = 1, al = "center") { if (a <= 0) return; ctx.globalAlpha = a; ctx.font = `bold ${size}px SpaceMono`; ctx.fillStyle = col; ctx.textAlign = al; ctx.fillText(s, x, y); ctx.globalAlpha = 1; }
function tag3(s, v, col, a = 1, dy = 40) { const q = proj(v); mono(s, q.x, q.y + dy, 26, col, a); }
function hud(x, y, w, h, head, foot, a) { if (a <= 0) return; ctx.globalAlpha = a; ctx.strokeStyle = YEL; ctx.lineWidth = 4; const c = 34;
  [[x, y, 1, 1], [x + w, y, -1, 1], [x, y + h, 1, -1], [x + w, y + h, -1, -1]].forEach(([px, py, sx, sy]) => { ctx.beginPath(); ctx.moveTo(px + sx * c, py); ctx.lineTo(px, py); ctx.lineTo(px, py + sy * c); ctx.stroke(); });
  ctx.fillStyle = YEL; ctx.fillRect(x + 22, y + 26, 10, 10); mono(head, x + 44, y + 36, 24, YEL, 1, "left");
  if (foot) { ctx.fillStyle = "rgba(20,21,27,.92)"; ctx.beginPath(); ctx.roundRect(x + 18, y + h - 74, w - 36, 54, 14); ctx.fill(); mono(foot[0], x + 42, y + h - 38, 24, YEL, 1, "left"); mono(foot[1], x + 120, y + h - 38, 24, CREAM, 1, "left"); }
  ctx.globalAlpha = 1; }
function bar(x, y, w, v, label, col, a) { if (a <= 0) return; ctx.globalAlpha = a; mono(label, x, y - 14, 24, CREAM, 1, "left"); ctx.fillStyle = "#2a2c35"; ctx.fillRect(x, y, w, 10); ctx.fillStyle = col; ctx.fillRect(x, y, w * v, 10); ctx.globalAlpha = 1; }
function wipe(t) { for (let b = 1; b < ST.length; b++) { const k = (t - (ST[b] - 0.16)) / 0.32; if (k < 0 || k > 1) continue; const x = lerp(-1300, 1500, ease(k));
  ctx.save(); ctx.translate(x, 0); ctx.transform(1, 0, -0.32, 1, 0, 0); ctx.fillStyle = "#16171d"; ctx.fillRect(0, 0, 860, H); ctx.fillStyle = YEL; ctx.fillRect(860, 0, 22, H); ctx.restore(); } }
function bg() { ctx.fillStyle = "#16171d"; ctx.fillRect(0, 0, W, H); const g = ctx.createRadialGradient(560, 1150, 120, 560, 1150, 1100); g.addColorStop(0, "rgba(60,62,78,.35)"); g.addColorStop(1, "rgba(0,0,0,0)"); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H); }
function vignette() { const g = ctx.createRadialGradient(540, 1100, 320, 540, 1100, 1250); g.addColorStop(0, "rgba(0,0,0,0)"); g.addColorStop(1, "rgba(0,0,0,.55)"); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H); }

function cam(pos, tgt, fov = 34) { camera.fov = fov; camera.updateProjectionMatrix(); camera.position.copy(pos); camera.lookAt(tgt); camera.updateMatrixWorld(); }
let CYv=0;
// ritmo de repetição: sobe rápido, segura, desce controlado, pausa (u: 0 embaixo → 1 em cima)
function rep(ph, up = 0.28, hold = 0.12, down = 0.45) { const c = (ph / (2 * Math.PI)) % 1;
  if (c < up) return eo(c / up); if (c < up + hold) return 1; if (c < up + hold + down) return 1 - ease((c - up - hold) / down); return 0; }
// rosca alternada com punho por fora do corpo (halter não encosta no tronco)
const curlA = (ph) => (i, s, sh) => { const u = rep(ph + (i ? 0 : Math.PI)), el = sh.clone().add(v3(0.03, -0.34, s * 0.07));
  const a = lerp(-0.08, 2.35, u); return [el, el.clone().add(v3(0.32 * Math.sin(a), -0.32 * Math.cos(a), s * (0.1 - 0.03 * u)))]; };
// agachamento: mãos na barra, pegada larga, atrás do pescoço
const barArms = (bar) => (i, s, sh) => { const wr = bar.clone().add(v3(0, 0, s * 0.5)), mid = sh.clone().lerp(wr, 0.5).add(v3(-0.05, -0.2, s * 0.12)); return [mid, wr]; };
// caminhada natural
const swing = (ph) => (i, s, sh) => { const a = 0.45 * Math.sin(ph + (i ? Math.PI : 0)), el = sh.clone().add(v3(0.33 * Math.sin(a), -0.33 * Math.cos(a), s * 0.06));
  return [el, el.clone().add(v3(0.33 * Math.sin(a + 0.35), -0.33 * Math.cos(a + 0.35), s * 0.02))]; };
// pegar o pão na mesa e levantar para mostrar
const reach = (target, lift) => (i, s, sh) => i === 1 ? (() => { const wr = target.clone(); const el = sh.clone().lerp(wr, 0.5).add(v3(-0.05, -0.12 + 0.1 * lift, s * 0.1)); return [el, wr]; })() : hang()(i, s, sh);
// bíceps duplo com "pulso" de contração
const flexA = (ph) => (i, s, sh) => { const u = 0.75 + 0.25 * Math.sin(ph * 1.5), el = sh.clone().add(v3(0.04, 0.03, s * 0.34)); const a = lerp(0.6, 1.35, u);
  return [el, el.clone().add(v3(0.02, 0.32 * Math.sin(a), s * 0.32 * Math.cos(a)))]; };
const pointPhone = (k) => (i, s, sh) => i === 1 ? [sh.clone().add(v3(0.3, -0.12, s * 0.12)), sh.clone().add(v3(0.6, 0.0 + 0.04 * Math.sin(k * 20), s * 0.22))] : hang()(i, s, sh);

// colisão: empurra cotovelo e punho (com o raio do objeto na mão) para fora do tronco e da cabeça
function closestOnSeg(p, a, b) { const ab = b.clone().sub(a), t = clamp(p.clone().sub(a).dot(ab) / ab.lengthSq()); return a.clone().addScaledVector(ab, t); }
function collide(j, extra = 0) {
  const top = j.neck.clone().addScaledVector(j.up, -0.06), R = 0.26;
  [0, 1].forEach((i) => {
    for (const [key, r] of [["el", 0.07], ["wr", 0.07 + extra]]) {
      const p = j[key][i], c = closestOnSeg(p, j.pelvis, top), d = p.clone().sub(c), L = d.length(), need = R + r;
      if (L < need) { if (L < 1e-4) d.set(0, 0, i ? 1 : -1); p.copy(c.addScaledVector(d.normalize(), need)); }
      const h = j.head, dh = p.clone().sub(h), Lh = dh.length(), nh = 0.2 + r;
      if (Lh < nh) p.copy(h.clone().addScaledVector(dh.normalize(), nh));
    }
    // antebraço não atravessa o tronco: se o meio do antebraço está dentro, empurra o cotovelo
    const m = j.el[i].clone().lerp(j.wr[i], 0.5), cm = closestOnSeg(m, j.pelvis, top), dm = m.clone().sub(cm);
    if (dm.length() < R + 0.06) j.el[i].add(dm.normalize().multiplyScalar(R + 0.06 - dm.length() + 0.02));
  });
  return j;
}

// ------------------------------------------------------------------ cadeia "erro → consequência → volta"
// frases: 0 erro1 | 1 conserto1 | 2 erro2 | 3 conserto2 | 4 erro3 | 5 conserto3 | 6 resultado | 7 CTA
const RW = [1, 3, 5], RWD = 0.5;           // voltas de fita no início destas frases
const phraseAt = (t) => { let i = 0; while (i < ST.length - 1 && t >= ST[i + 1]) i++; return i; };
const LOC = { plate: v3(1.15, 0, 0.9), rack: v3(-1.4, 0, -0.6), cal: v3(0.2, 0, -1.4) };

function rep2(ph, up, hold, down) { return rep(ph, up, hold, down); }
// volume do corpo ao longo do vídeo (cresce com os acertos, murcha nos erros)
function bulkAt(t) { const f = phraseAt(t), lt = t - ST[f];
  const B = [0.82, 0.88, 0.86, 0.98, 0.84, 1.0, 1.3, 1.3]; const prev = f ? B[f - 1] : 0.82;
  if (f === 5) return lerp(0.84, 1.22, ease(lt / (ST[6] - ST[5]))); if (f === 6) return lerp(1.22, 1.3, eo(lt / 0.6));
  return lerp(prev, B[f], ease(lt / 0.8)); }

// pílula de rótulo (como a referência): ponto colorido + texto
function pill(s, x, y, ok, a = 1) { if (a <= 0) return; ctx.save(); ctx.globalAlpha = a; ctx.font = "bold 30px SpaceMono"; const w = ctx.measureText(s).width + 70;
  ctx.translate(x, y); ctx.scale(bo(a), bo(a)); ctx.fillStyle = "#f4f1ea"; ctx.beginPath(); ctx.roundRect(-w / 2, -30, w, 60, 12); ctx.fill();
  ctx.fillStyle = ok ? "#2f9cff" : "#e8363a"; ctx.beginPath(); ctx.arc(-w / 2 + 26, 0, 9, 0, 7); ctx.fill(); ctx.fillStyle = "#1b1c22"; ctx.textAlign = "left"; ctx.fillText(s, -w / 2 + 46, 10); ctx.restore(); }
function pill3(s, v, ok, a, dy = -40) { const q = proj(v); pill(s, q.x, q.y + dy, ok, a); }
// legenda de uma palavra por vez
const KEY = new Set(["material", "estímulo", "falha", "nada", "oito", "constância", "quilo", "QUILO", "comida", "esforço"]);
function caption(t) { let w = null; for (const x of TL.words) { if (x[1] <= t + 0.03) w = x; else break; } if (!w) return;
  const k = eo(prog(t, w[1], 0.12)), w0 = w[0].replace(/Bríu/gi, "Brio"), word = w0.charAt(0).toUpperCase() + w0.slice(1), hot = KEY.has(w[0]);
  ctx.save(); ctx.translate(540, 1470); ctx.scale(0.85 + 0.15 * k, 0.85 + 0.15 * k); ctx.font = "92px Anton"; ctx.textAlign = "center";
  ctx.lineWidth = 14; ctx.strokeStyle = "rgba(0,0,0,.75)"; ctx.lineJoin = "round"; ctx.strokeText(word, 0, 0); ctx.fillStyle = hot ? "#ffc43d" : "#ffffff"; ctx.fillText(word, 0, 0); ctx.restore(); }
function rewindFx(k) {  // linhas de fita + ◀◀ desenhado
  ctx.fillStyle = "rgba(255,255,255,.08)"; ctx.fillRect(0, 0, W, H);
  for (let y = 0; y < H; y += 34) { const yy = (y + k * 900) % H; ctx.fillStyle = "rgba(255,255,255,.22)"; ctx.fillRect(0, yy, W, 3); }
  ctx.fillStyle = "#fff"; for (let i = 0; i < 2; i++) { const x = 820 + i * 62; ctx.beginPath(); ctx.moveTo(x, 240); ctx.lineTo(x + 58, 202); ctx.lineTo(x + 58, 278); ctx.closePath(); ctx.fill(); } }
function ffFx(t) { ctx.fillStyle = "#ffc43d"; for (let i = 0; i < 2; i++) { const x = 860 + i * 56; ctx.globalAlpha = 0.6 + 0.4 * Math.sin(t * 12); ctx.beginPath(); ctx.moveTo(x + 52, 240); ctx.lineTo(x, 206); ctx.lineTo(x, 274); ctx.closePath(); ctx.fill(); } ctx.globalAlpha = 1; }

// ------------------------------------------------------------------ objetos do mundo
function plate(c, fill) { const r = 0.32; const Q = []; for (let a = 0; a < 32; a++) { const t = a / 32 * Math.PI * 2; Q.push(proj(c.clone().add(v3(Math.cos(t) * r, 0, Math.sin(t) * r)))); }
  ctx.fillStyle = "#e9e6df"; ctx.beginPath(); Q.forEach((q, i) => (i ? ctx.lineTo(q.x, q.y) : ctx.moveTo(q.x, q.y))); ctx.fill();
  const items = [["#f1d9a6", -0.12, -0.05, 0.11], ["#7a4b2e", 0.1, -0.08, 0.1], ["#4fa65b", 0.0, 0.12, 0.09], ["#f1d9a6", 0.16, 0.1, 0.08], ["#c24a33", -0.14, 0.12, 0.08]];
  items.forEach(([col, dx, dz, r], i) => { const a = clamp(fill * 5 - i); if (a <= 0) return; disc(c.clone().add(v3(dx, 0.05 + 0.02 * i, dz)), r * bo(a) * (i < 1 ? 1 : 1), col); }); }
function stand(c) { seg3(c.clone(), c.clone().add(v3(0, 0.9, 0)), "#3a3c46", 10); const top = [v3(-0.45, 0.9, -0.35), v3(0.45, 0.9, -0.35), v3(0.45, 0.9, 0.35), v3(-0.45, 0.9, 0.35)].map((p) => p.add(c)).map(proj);
  ctx.fillStyle = "#2c2e37"; ctx.beginPath(); top.forEach((p, i) => (i ? ctx.lineTo(p.x, p.y) : ctx.moveTo(p.x, p.y))); ctx.fill(); }
function dbH(c, axis, s = 1) { seg3(c.clone().addScaledVector(axis, -0.17 * s), c.clone().addScaledVector(axis, 0.17 * s), "#c0c3cb", 6); [-0.16, 0.16].forEach((k) => disc(c.clone().addScaledVector(axis, k * s), 0.1 * s, CORAL)); }
function meter(x, y, v, label, col) { ctx.fillStyle = "rgba(20,21,27,.9)"; ctx.beginPath(); ctx.roundRect(x - 26, y - 220, 52, 240, 16); ctx.fill();
  ctx.fillStyle = col; ctx.beginPath(); ctx.roundRect(x - 16, y + 10 - 220 * v + 10, 32, 220 * v - 10, 10); ctx.fill(); mono(label, x, y + 52, 22, CREAM); }
function weeks(x, y, n, total, failAt = -1) { const cw = 74; for (let i = 0; i < total; i++) { const cx = x + (i % 4) * (cw + 12), cy = y + Math.floor(i / 4) * (cw + 12), on = i < n;
  ctx.fillStyle = on ? (failAt >= 0 && i >= failAt ? "#e8363a" : "#4fa65b") : "rgba(255,255,255,.08)"; ctx.beginPath(); ctx.roundRect(cx, cy, cw, cw, 14); ctx.fill();
  mono(`S${i + 1}`, cx + cw / 2, cy + cw / 2 + 8, 22, on ? "#fff" : GREY); } }

// ------------------------------------------------------------------ pose por frase
function poseAt(f, ph, lt, k) {
  const u = rep(ph, 0.3, 0.1, 0.45);
  if (f === 0) return { j: collide(skel({ arms: curlA(ph), stance: 0.16 }), 0.24), pos: v3(0, 0, 0), yaw: 0.25, db: 0.7 };
  if (f === 1) { const tgt = v3(0.75, 0.95, 0.55).lerp(v3(0.2, 1.4, 0.25), ease(prog(k, 0.55, 0.35)));
    return { j: collide(skel({ arms: (i, s, sh) => i === 1 ? [sh.clone().lerp(tgt, 0.5).add(v3(0, -0.15, s * 0.1)), tgt] : hang()(i, s, sh), stance: 0.14, lean: 0.12 })), pos: v3(0.2, 0, 0.3), yaw: 0.6 }; }
  if (f === 2) { const j = collide(skel({ arms: curlA(ph * 1.6), stance: 0.16 }), 0.18); j.head.y += 0.03 * Math.sin(ph * 0.8); return { j, pos: v3(-0.6, 0, -0.1), yaw: -0.2, db: 0.55 }; }
  if (f === 3) { const j = collide(skel({ arms: curlA(ph * 0.75), stance: 0.2, lean: -0.05 * u }), 0.3); j.head.x -= 0.03 * u; return { j, pos: v3(-0.6, 0, -0.1), yaw: -0.2, db: 1.25, shake: u > 0.6 }; }
  if (f === 4) { const s = eo(prog(k, 0.45, 0.4)); return { j: collide(skel({ walk: s > 0 ? ph : null, lean: 0.05, arms: swing(ph * s), stance: 0.14 })), pos: v3(lerp(0, 1.5, s), 0, 0.2), yaw: lerp(0, -0.2, s) }; }
  if (f === 5) return { j: collide(skel({ arms: curlA(ph), stance: 0.18 }), 0.28), pos: v3(0, 0, 0), yaw: 0.15, db: 1.15 };
  if (f === 6) return { j: collide(skel({ arms: flexA(ph), stance: 0.22 })), pos: v3(0, 0, 0), yaw: -0.25 };
  return { j: collide(skel({ arms: pointPhone(k), stance: 0.14 })), pos: v3(-0.7, 0, 0), yaw: 0.35 };
}
function camFor(f, k, J, t) {
  const sh = v3(0.025 * Math.sin(t * 1.7), 0.02 * Math.sin(t * 2.3), 0.025 * Math.cos(t * 1.3)), push = 1 + 0.15 * (1 - eo(clamp(k * 4)));
  const orbit = (a0, a1, d0, h, tgt) => { const d = d0 * 1.3, a = lerp(a0, a1, ease(k)); cam(v3(tgt.x + d * Math.sin(a) * push, h, tgt.z + d * Math.cos(a) * push).add(sh), tgt, 34); };
  if (f === 0) orbit(-0.2, 0.25, 7.2, 1.6, v3(0.25, 1.0, 0.2));
  if (f === 1) orbit(0.7, 0.95, 6.4, 2.6, v3(0.6, 0.85, 0.5));
  if (f === 2) orbit(-0.55, -0.35, 6.8, 1.2, v3(-0.4, 1.05, -0.1));
  if (f === 3) orbit(-0.35, -0.15, 6.4, 1.1, v3(-0.45, 1.15, -0.1));
  if (f === 4) orbit(0.15, 0.4, 8.2, 2.2, v3(lerp(0, 0.9, ease(k)), 0.9, 0.1));
  if (f === 5) orbit(0.2, -0.3, 7.6, 1.4, v3(0.0, 1.0, 0.0));
  if (f === 6) orbit(-0.9, 0.6, 6.8, 0.6, v3(0, 1.2, 0));
  if (f === 7) cam(v3(0.2, 1.3, 7.6).add(sh), v3(-0.05, 1.1, 0), 34);
}

let phase = 0, lastF = -1;
const speedAt = (t) => [3.2, 2.0, 4.2, 2.0, 5.5, 3.6, 3.0, 1.6][phraseAt(t)];
function drawWorld(t) {
  const f = phraseAt(t), lt = t - ST[f], k = lt / ((ST[f + 1] ?? DUR) - ST[f]);
  const PO = poseAt(f, phase, lt, k), J = world(PO.j, PO.pos, PO.yaw);
  camFor(f, k, J, t); CY = 210;
  bg(); floorGrid(0, 0, 12);
  for (const [rx, rz] of [[-2.6, -2.4], [2.4, -2.8]]) { // racks ao fundo
    for (const dx of [-0.55, 0.55]) seg3(v3(rx + dx, 0, rz), v3(rx + dx, 2.3, rz), "#3b3e49", 10);
    seg3(v3(rx - 0.6, 2.25, rz), v3(rx + 0.6, 2.25, rz), "#3b3e49", 8); seg3(v3(rx - 0.75, 1.35, rz), v3(rx + 0.75, 1.35, rz), "#9aa0ab", 5);
    for (const dx of [-0.65, 0.65]) { ring3(v3(rx + dx, 1.35, rz), 0.3, "#24262d", null); ring3(v3(rx + dx, 1.35, rz), 0.22, null, CORAL); } }
  // prato fica no mundo o tempo todo (vazio → cheio a partir do conserto 1)
  const fill = f === 0 ? 0.15 : f === 1 ? eo(prog(lt, 0.2, 1.0)) * 0.85 + 0.15 : 1;
  if (f <= 3) { stand(LOC.plate.clone().setY(0)); plate(LOC.plate.clone().setY(0.92), fill); }
  shadow(J.pelvis, 0.5);
  let bulk = bulkAt(t); if (f === 0 || f === 2 || f === 4) bulk *= 1 - 0.06 * eo(prog(k, 0.55, 0.3)) * (0.6 + 0.4 * Math.sin(t * 9));
  const axis = v3(0, 0, 1).applyAxisAngle(v3(0, 1, 0), PO.yaw);
  let shk = PO.shake ? 4 * Math.sin(t * 60) : 0; ctx.save(); ctx.translate(shk, 0);
  figure(J, f === 4 && k > 0.5 ? { ...HERO, body: "#cfcac0" } : HERO, 1, { bulk, hand: (i, w) => { if (PO.db) dbH(w, axis, PO.db); } });
  ctx.restore();
  return { f, lt, k, J, PO };
}
window.renderFrame = (fr) => {
  if (fr !== lastF + 1) { phase = 0; for (let q = 0; q < fr; q++) phase += speedAt(q / FPS) / FPS; }
  const t = fr / FPS; phase += speedAt(t) / FPS; lastF = fr;
  let f = phraseAt(t), lt = t - ST[f];
  // volta da fita: nos primeiros RWD s das frases 1,3,5 mostra o fim da frase anterior andando para trás
  const inRW = RW.includes(f) && lt < RWD;
  const tv = inRW ? ST[f] - 0.02 - (lt / RWD) * Math.min(1.6, ST[f] - ST[f - 1] - 0.05) : t;
  if (inRW) { const save = phase; phase -= (t - tv) * 3; drawWorld(tv); phase = save; } else drawWorld(t);
  const W2 = { f: phraseAt(tv), lt: tv - ST[phraseAt(tv)] }; W2.k = W2.lt / ((ST[W2.f + 1] ?? DUR) - ST[W2.f]);
  const g = W2.f, gl = W2.lt, gk = W2.k;
  // HUD por frase (pílulas como a referência)
  if (g === 0) { pill("COMEU POUCO", 540, 470, false, eo(prog(gl, 0.6, 0.25))); pill("SEM MATERIAL", 540, 550, false, eo(prog(gk, 0.62, 0.2))); }
  if (g === 1) pill("COMIDA", 540, 470, true, eo(prog(gl, 0.3, 0.25)));
  if (g === 2) { meter(960, 1180, lerp(0.15, 0.25, 0.5 + 0.5 * Math.sin(t * 3)), "ESFORÇO", "#e8363a"); pill("SEM ESTÍMULO", 540, 470, false, eo(prog(gk, 0.55, 0.2))); }
  if (g === 3) { meter(960, 1180, lerp(0.25, 0.92, eo(prog(gl, 0.1, 0.8))), "ESFORÇO", "#4fa65b"); pill("PERTO DA FALHA", 540, 470, true, eo(prog(gl, 0.4, 0.25))); }
  if (g === 4) { weeks(370, 300, Math.min(3, Math.floor(gl * 3)) + (gk > 0.45 ? 0 : 0), 8, gk > 0.45 ? 2 : -1); pill("DESISTIU", 540, 520, false, eo(prog(gk, 0.5, 0.2))); }
  if (g === 5) { weeks(370, 300, Math.min(8, Math.floor(gl * 4) + 1), 8); ffFx(t); pill("CONSTÂNCIA", 540, 520, true, eo(prog(gl, 0.4, 0.25))); }
  if (g === 6) { ["COMIDA", "ESFORÇO", "CONSTÂNCIA"].forEach((s, i) => pill(s, 220 + i * 320, 420, true, eo(prog(gl, 0.6 + i * 0.35, 0.25))));
    big("+1 KG", 540, 640, 150, "#4fa65b", eo(prog(gl, 2.2, 0.3))); mono("DE MÚSCULO", 540, 690, 28, CREAM, eo(prog(gl, 2.3, 0.3)));
    for (let i = 0; i < 40 && gl > 2.2; i++) { const p = (gl - 2.2) * 0.6 + i * 0.137, x = (i * 263) % W, y = ((p % 1) * H * 0.8) + 200; ctx.fillStyle = ["#ff5c3d", "#ffc43d", "#4fa65b", "#2f9cff"][i % 4]; ctx.save(); ctx.translate(x, y); ctx.rotate(p * 9 + i); ctx.fillRect(-8, -4, 16, 8); ctx.restore(); } }
  if (g === 7) { const a = eo(prog(gl, 0.1, 0.4)), x = 580, y = 560 + (1 - a) * 80; ctx.globalAlpha = a; ctx.fillStyle = "#1b1c22"; ctx.beginPath(); ctx.roundRect(x, y, 400, 700, 48); ctx.fill();
    ctx.fillStyle = "#121318"; ctx.beginPath(); ctx.roundRect(x + 16, y + 16, 368, 668, 36); ctx.fill(); mono("SUA EVOLUÇÃO", x + 40, y + 80, 20, GREY, a, "left"); big("Brio", x + 40, y + 140, 50, CREAM, a, "left");
    ctx.strokeStyle = "#4fa65b"; ctx.lineWidth = 8; ctx.beginPath(); const p = eo(prog(gl, 0.4, 1.2)), pts = [[60, 560], [130, 520], [200, 530], [270, 450], [340, 400]];
    pts.slice(0, Math.max(2, Math.ceil(pts.length * p))).forEach(([px, py], i) => (i ? ctx.lineTo(x + px, y + py) : ctx.moveTo(x + px, y + py))); ctx.stroke();
    [["ROSCA", "10 KG → 14 KG"], ["SUPINO", "40 KG → 52 KG"]].forEach(([n, v], i) => { ctx.fillStyle = "#1e2028"; ctx.beginPath(); ctx.roundRect(x + 30, y + 180 + i * 120, 340, 100, 18); ctx.fill();
      mono(n, x + 56, y + 218 + i * 120, 18, "#c9ccd4", a, "left"); big(v, x + 56, y + 262 + i * 120, 40, CREAM, a, "left"); }); ctx.globalAlpha = 1;
    pill("LINK NA BIO", 780, 1340, true, eo(prog(gl, 1.2, 0.25))); }
  vignette();
  if (inRW) rewindFx(lt / RWD);
  caption(t);
  mono("@briotreino", 960, 1600, 24, "rgba(255,255,255,.55)", 1, "right");
  return cv.toDataURL("image/jpeg", 0.93);
};
window.FRAMES = Math.round(DUR * FPS); window.FPS = FPS;
window.ready = document.fonts.load("140px Anton").then(() => document.fonts.load("bold 30px SpaceMono")).then(() => true);
