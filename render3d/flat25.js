// Brio 2,5D: esqueleto e câmera em 3D, mas tudo DESENHADO em 2D (formas chapadas no canvas), como a referência.
// Membros = traços grossos de ponta redonda com espessura pela perspectiva; tronco = feijão chapado; chão e cenário em linhas 3D.
import * as THREE from "three";

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

const HERO = { body: "#ebe6dc", head: "#efeae1", armN: "#8f887d", armF: "#6c675f", legN: "#c6bfb3", legF: "#a39c90" };
const DARK = { body: "#4b4f5c", head: "#555a68", armN: "#3c3f4a", armF: "#2f323b", legN: "#454956", legF: "#353843" };
const CORAL = "#ff5c3d", YEL = "#f6b81a", CREAM = "#f2ede3", GREY = "#8a8d96";

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
function figure(J, pal, alpha = 1, opts = {}) {
  const D = (v) => proj(v).d;
  const nearArm = D(J.sh[0]) < D(J.sh[1]) ? 0 : 1, nearLeg = D(J.hip[0]) < D(J.hip[1]) ? 0 : 1;
  const leg = (i) => { const c = i === nearLeg ? pal.legN : pal.legF; poly3([J.hip[i], J.knee[i], J.ankle[i]], 0.16, c, alpha);
    line(J.ankle[i], J.ankle[i].clone().addScaledVector(J.fwd, 0.16), 0.11, c, alpha); };
  const arm = (i) => { const c = i === nearArm ? pal.armN : pal.armF; poly3([J.sh[i], J.el[i], J.wr[i]], 0.125, c, alpha);
    if (opts.gloves) glove(J.wr[i], 0.1, opts.gloves); else disc(J.wr[i], 0.075, c, alpha); if (opts.hand) opts.hand(i, J.wr[i]); };
  leg(1 - nearLeg); leg(nearLeg); arm(1 - nearArm);
  const ax = J.neck.clone().sub(J.pelvis).normalize();
  torso(J.pelvis.clone().addScaledVector(ax, -0.02), J.neck.clone().addScaledVector(ax, -0.03), [0.3, 0.46, 0.3], pal.body, alpha);
  disc(J.head.clone().addScaledVector(ax, 0.06), 0.18, pal.head, alpha);
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
function barbell(c) { seg3(c.clone().add(v3(0, 0, -1.15)), c.clone().add(v3(0, 0, 1.15)), "#c0c3cb", 8);
  [-0.95, -1.05, 0.95, 1.05].forEach((z, k) => { const p = c.clone().add(v3(0, 0, z)), Cc = proj(p), r = (k % 3 === 0 ? 0.42 : 0.34) * Cc.s;
    ctx.fillStyle = "#24262d"; ctx.beginPath(); ctx.ellipse(Cc.x, Cc.y, r * 0.5, r, 0, 0, 7); ctx.fill(); ctx.strokeStyle = YEL; ctx.lineWidth = 3; ctx.beginPath(); ctx.ellipse(Cc.x, Cc.y, r * 0.38, r * 0.78, 0, 0, 7); ctx.stroke(); }); }
function bread(c, rot) { const A = proj(c.clone().add(v3(Math.cos(rot) * 0.2, 0, Math.sin(rot) * 0.2))), B = proj(c.clone().add(v3(-Math.cos(rot) * 0.2, 0, -Math.sin(rot) * 0.2)));
  ctx.strokeStyle = "#d9a35a"; ctx.lineCap = "round"; ctx.lineWidth = 0.2 * (A.s + B.s) / 2; ctx.beginPath(); ctx.moveTo(A.x, A.y); ctx.lineTo(B.x, B.y); ctx.stroke();
  ctx.strokeStyle = "#a8722f"; ctx.lineWidth = 0.025 * A.s; for (let k = -1; k <= 1; k++) { const m = { x: lerp(A.x, B.x, 0.5 + k * 0.25), y: lerp(A.y, B.y, 0.5 + k * 0.25) };
    ctx.beginPath(); ctx.moveTo(m.x - 0.04 * A.s, m.y - 0.05 * A.s); ctx.lineTo(m.x + 0.04 * A.s, m.y - 0.09 * A.s); ctx.stroke(); } }
function table(c) { const q = [v3(-0.7, 0.8, -0.4), v3(0.7, 0.8, -0.4), v3(0.7, 0.8, 0.4), v3(-0.7, 0.8, 0.4)].map((p) => p.add(c));
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
function bg() { ctx.fillStyle = "#0c0d11"; ctx.fillRect(0, 0, W, H); const g = ctx.createRadialGradient(560, 1150, 120, 560, 1150, 1100); g.addColorStop(0, "rgba(60,62,78,.35)"); g.addColorStop(1, "rgba(0,0,0,0)"); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H); }
function vignette() { const g = ctx.createRadialGradient(540, 1100, 320, 540, 1100, 1250); g.addColorStop(0, "rgba(0,0,0,0)"); g.addColorStop(1, "rgba(0,0,0,.55)"); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H); }

// ------------------------------------------------------------------ cenas
function cam(pos, tgt, fov = 34) { camera.fov = fov; camera.updateProjectionMatrix(); camera.position.copy(pos); camera.lookAt(tgt); camera.updateMatrixWorld(); }
let phase = 0, lastF = -1;
const speedAt = (t) => [3.0, 2.5, 1.6, 6.2, 2.4, 1.6][beatAt(t)];
function poseAt(b, ph, k) { const u = 0.5 - 0.5 * Math.cos(ph);
  if (b === 0) return { j: skel({ arms: curl(u), stance: 0.18 }), pos: v3(0, 0, 0), yaw: 0.0 };
  if (b === 1) { const d = 0.4 * u; return { j: skel({ drop: d, back: d * 0.55, lean: 0.5 * u + 0.1, stance: 0.03, arms: squatArms() }), pos: v3(0, 0, 0), yaw: 0 }; }
  if (b === 2) return { j: skel({ arms: shrug(u), stance: 0.12 }), pos: v3(-0.6, 0, 0), yaw: -0.3 };
  if (b === 3) return { j: skel({ walk: ph, lean: 0.08, bob: -0.03 * Math.abs(Math.sin(ph)), arms: run(ph) }), pos: v3(lerp(-2.2, 2.2, k), 0, 0), yaw: 0 };
  if (b === 4) return { j: skel({ arms: flex(u), stance: 0.2 }), pos: v3(0.55, 0, 0.35), yaw: -1.2 };
  return { j: skel({ arms: thumbs(), stance: 0.14 }), pos: v3(-0.75, 0, 0), yaw: 0.35 };
}
window.renderFrame = (f) => {
  if (f !== lastF + 1) { phase = 0; for (let k = 0; k < f; k++) phase += speedAt(k / FPS) / FPS; }
  const t = f / FPS; phase += speedAt(t) / FPS; lastF = f;
  const b = beatAt(t), lt = t - ST[b], k = lt / ((ST[b + 1] ?? DUR) - ST[b]), kk = ease(k), push = 1 + 0.18 * (1 - eo(prog(lt, 0, 0.5)));
  const { j, pos, yaw } = poseAt(b, phase, k), J = world(j, pos, yaw);
  // câmera de cada cena
  const shake = v3(0.025 * Math.sin(t * 1.7), 0.02 * Math.sin(t * 2.3), 0.025 * Math.cos(t * 1.3));
  CY = 170;
  if (b === 0) { const a = lerp(-0.55, -0.2, kk); cam(v3(7.6 * Math.sin(a) * push, 0.9, 7.6 * Math.cos(a) * push).add(shake), v3(0.1, 1.1, 0), 36); }
  if (b === 1) { const a = lerp(0.95, 0.6, kk); cam(v3(9.4 * Math.sin(a) * push, 3.6, 9.4 * Math.cos(a) * push).add(shake), v3(0, 0.9, 0), 34); }
  if (b === 2) { cam(v3(lerp(2.8, 2.2, kk), 7.2 * push, lerp(6.2, 6.6, kk)), v3(0.2, 0.55, 0), 36); }
  if (b === 3) { cam(v3(J.pelvis.x * 0.7 + 0.4, 1.05, 8.4 * push).add(shake), v3(J.pelvis.x * 0.85, 1.0, 0), 34); }
  if (b === 4) { const a = lerp(-0.9, 0.5, kk); cam(v3(9.2 * Math.sin(a) * push, 0.6, 9.2 * Math.cos(a) * push).add(shake), v3(0, 1.15, 0), 32); }
  if (b === 5) { cam(v3(0.2, 1.3, 7.6 * push).add(shake), v3(-0.05, 1.1, 0), 34); }
  bg(); floorGrid(0, 0, 12);
  if (b === 0 || b === 4) gymFrame(0.9);
  // segundo personagem (conclusão): só queima (correndo, escuro) x constrói (herói)
  if (b === 4) { const ph2 = phase * 2.2, J2 = world(skel({ walk: ph2, lean: 0.12, arms: run(ph2) }), v3(-0.6, 0, -0.55), 0.5); shadow(J2.pelvis, 0.45); figure(J2, DARK, 0.95);
    tag3("SÓ QUEIMAR", v3(J2.pelvis.x, 0, J2.pelvis.z), GREY, eo(prog(lt, 0.5, 0.3))); }
  if (b === 2) { table(v3(0.9, 0, 0)); }
  // rastro de movimento (como a referência): poses anteriores semitransparentes
  if (b === 0 || b === 3) { for (const back of [0.12, 0.06]) { const P2 = poseAt(b, phase - speedAt(t) * back * 1.0, k), J3 = world(P2.j, P2.pos, P2.yaw); figure(J3, HERO, 0.12); } }
  shadow(J.pelvis, 0.5);
  if (b === 1) { /* barra atrás do corpo primeiro */ }
  figure(J, HERO, 1, { hand: (i, w) => { if (b === 0) dumbbell(w, v3(0, 0, 1).applyAxisAngle(v3(0, 1, 0), yaw)); } });
  if (b === 1) barbell(J.neck.clone().add(v3(-0.16, 0.0, 0)));
  if (b === 2) [0, 1, 2].forEach((i) => { const d = bo(prog(lt, 0.2 + i * 0.32, 0.32)); if (lt < 0.2 + i * 0.32) return;
    const c = v3(0.55 + i * 0.36, 0.86 + (1 - d) * 1.4, 0.04 * (i - 1)); bread(c, 0.3 * i - 0.2 + (1 - d) * 2); tag3(`${i + 1}`, c.clone().add(v3(0, 0.3, 0)), YEL, eo(prog(lt, 0.4 + i * 0.32, 0.2)), 0); });
  if (b === 3) for (let i = 0; i < 18; i++) { const ph = (t * 0.7 + i / 18) % 1, c = J.pelvis.clone().add(v3(Math.sin(i * 7.1) * 0.5 - 0.3, -0.55 + ph * 1.9, Math.cos(i * 3.3) * 0.4)), C = proj(c);
    ctx.globalAlpha = 1 - ph; ctx.fillStyle = i % 3 ? CORAL : YEL; ctx.save(); ctx.translate(C.x, C.y); ctx.rotate(t * 3 + i); ctx.fillRect(-6, -6, 12, 12); ctx.restore(); ctx.globalAlpha = 1; }
  if (b === 4) tag3("CONSTRUIR", v3(J.pelvis.x, 0, J.pelvis.z), YEL, eo(prog(lt, 0.9, 0.3)));
  vignette();
  // HUD e números
  if (b === 0) { big("60", 900, 1010, 170, YEL, eo(prog(lt, 0.4, 0.3))); mono("MINUTOS", 900, 1060, 26, GREY, eo(prog(lt, 0.4, 0.3))); }
  if (b === 1) { const n = Math.round(lerp(0, 400, eo(prog(lt, 0.3, 3.4)))); hud(70, 690, 940, 900, "CONTANDO O GASTO", ["01/03", `${n} KCAL EM 1 HORA`], eo(prog(lt, 0.1, 0.3)));
    bar(110, 790, 400, n / 400, "KCAL", n >= 200 ? CORAL : YEL, eo(prog(lt, 0.2, 0.3))); big(`${n}`, 940, 900, 150, n >= 200 ? CORAL : CREAM, 1, "right"); }
  if (b === 2) { hud(70, 690, 940, 900, "EM PÃO FRANCÊS", ["02/03", "≈ 140 KCAL CADA"], eo(prog(lt, 0.1, 0.3))); }
  if (b === 3) { const h = Math.floor(lerp(0, 23, eo(prog(lt, 0.2, 4.6)))), m = Math.floor(lerp(0, 59, (lt * 3) % 1));
    big(`${String(h).padStart(2, "0")}:${String(m).padStart(2, "0")}`, 940, 900, 120, CORAL, eo(prog(lt, 0.2, 0.3)), "right"); mono("GASTANDO ATÉ PARADO", 940, 950, 24, GREY, eo(prog(lt, 0.4, 0.3)), "right");
    hud(70, 690, 940, 900, "MAIS MÚSCULO", ["03/03", "MAIS GASTO, O DIA INTEIRO"], eo(prog(lt, 0.1, 0.3))); }
  if (b === 5) { // celular 2D com a tela do Brio
    const a = eo(prog(lt, 0.1, 0.4)), x = 560, y = 760 + (1 - a) * 80; ctx.globalAlpha = a; ctx.fillStyle = "#1b1c22"; ctx.beginPath(); ctx.roundRect(x, y, 400, 780, 48); ctx.fill();
    ctx.fillStyle = "#121318"; ctx.beginPath(); ctx.roundRect(x + 16, y + 16, 368, 748, 36); ctx.fill(); mono("HOJE · TREINO A", x + 40, y + 80, 20, GREY, a, "left"); big("Brio", x + 40, y + 140, 50, CREAM, a, "left");
    [["AGACHAMENTO", "80 KG × 8", YEL], ["ROSCA DIRETA", "14 KG × 10", YEL], ["SUPINO", "60 KG × 8", CORAL]].forEach(([n, v, c], i) => { const p = eo(prog(lt, 0.5 + i * 0.3, 0.3)); ctx.globalAlpha = p;
      ctx.fillStyle = "#1e2028"; ctx.beginPath(); ctx.roundRect(x + 30, y + 180 + i * 140, 340, 116, 18); ctx.fill(); ctx.fillStyle = c; ctx.fillRect(x + 30, y + 180 + i * 140, 8, 116);
      mono(n, x + 56, y + 222 + i * 140, 18, "#c9ccd4", p, "left"); big(v, x + 56, y + 278 + i * 140, 46, CREAM, p, "left"); });
    const p = eo(prog(lt, 1.6, 0.3)); ctx.globalAlpha = p; ctx.fillStyle = CORAL; ctx.beginPath(); ctx.roundRect(x + 30, y + 640, 340, 80, 40); ctx.fill(); big("TREINO REGISTRADO", x + 200, y + 694, 36, "#fff", p); ctx.globalAlpha = 1;
    mono("LINK NA BIO", 540, 1600, 28, CREAM, eo(prog(lt, 1.0, 0.3))); }
  const B = TL.beats[b]; title(B.t1, B.t2, t, ST[b] - 0.05);
  wipe(t);
  return cv.toDataURL("image/jpeg", 0.93);
};
window.FRAMES = Math.round(DUR * FPS); window.FPS = FPS;
window.ready = document.fonts.load("140px Anton").then(() => document.fonts.load("bold 30px SpaceMono")).then(() => true);
