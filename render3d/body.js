// Corpo do personagem Brio: malhas contínuas (tubos com perfil de raio) reconstruídas a cada quadro.
// Assim joelho, cotovelo e ombro dobram de forma suave, sem emendas de esferas.
import * as THREE from "three";
import { RoundedBoxGeometry } from "three/addons/geometries/RoundedBoxGeometry.js";

const sstep = (a, b, x) => { const t = Math.max(0, Math.min(1, (x - a) / (b - a))); return t * t * (3 - 2 * t); };
export function profile(keys) { // keys: [[s, ry, rz], ...] → função s → [ry, rz] suave
  return (s) => {
    if (s <= keys[0][0]) return [keys[0][1], keys[0][2]];
    for (let i = 0; i < keys.length - 1; i++) {
      const [s0, a0, b0] = keys[i], [s1, a1, b1] = keys[i + 1];
      if (s <= s1) { const k = sstep(s0, s1, s); return [a0 + (a1 - a0) * k, b0 + (b1 - b0) * k]; }
    }
    const l = keys[keys.length - 1]; return [l[1], l[2]];
  };
}

// Tubo com seção elíptica ao longo de uma curva; tampas arredondadas opcionais.
export class Tube {
  constructor(mat, { nr = 28, nl = 56, caps = true, capRings = 8 } = {}) {
    this.nr = nr; this.nl = nl; this.caps = caps; this.cr = caps ? capRings : 0;
    const rings = nl + 1 + 2 * this.cr; this.rings = rings;
    const g = new THREE.BufferGeometry();
    this.pos = new Float32Array(rings * (nr + 1) * 3);
    g.setAttribute("position", new THREE.BufferAttribute(this.pos, 3));
    const idx = [];
    for (let i = 0; i < rings - 1; i++) for (let j = 0; j < nr; j++) {
      const a = i * (nr + 1) + j, b = a + nr + 1; idx.push(a, b, a + 1, b, b + 1, a + 1);
    }
    g.setIndex(idx); this.g = g;
    this.mesh = new THREE.Mesh(g, mat); this.mesh.castShadow = this.mesh.receiveShadow = true; this.mesh.frustumCulled = false;
    this.frames = [];
  }
  update(points, prof, up) {
    const curve = new THREE.CatmullRomCurve3(points, false, "centripetal", 0.5);
    const nl = this.nl, nr = this.nr, cr = this.cr;
    const P = [], T = [], N = [], B = [];
    for (let i = 0; i <= nl; i++) { const s = i / nl; P.push(curve.getPointAt(s)); T.push(curve.getTangentAt(s).normalize()); }
    let n = up.clone().addScaledVector(T[0], -up.dot(T[0])).normalize();
    for (let i = 0; i <= nl; i++) {
      if (i > 0) { const q = new THREE.Quaternion().setFromUnitVectors(T[i - 1], T[i]); n = n.clone().applyQuaternion(q); n.addScaledVector(T[i], -n.dot(T[i])).normalize(); }
      N.push(n.clone()); B.push(new THREE.Vector3().crossVectors(T[i], n).normalize());
    }
    this.frames = { P, T, N, B, prof };
    let k = 0; const pos = this.pos;
    const ring = (c, t, nn, bb, ry, rz) => {
      for (let j = 0; j <= nr; j++) {
        const a = (j / nr) * Math.PI * 2, ca = Math.cos(a), sa = Math.sin(a);
        pos[k++] = c.x + nn.x * ry * ca + bb.x * rz * sa; pos[k++] = c.y + nn.y * ry * ca + bb.y * rz * sa; pos[k++] = c.z + nn.z * ry * ca + bb.z * rz * sa;
      }
    };
    const [r0y, r0z] = prof(0), [r1y, r1z] = prof(1);
    for (let c = cr; c >= 1; c--) { const ph = (c / cr) * Math.PI / 2, e = Math.sin(ph), f = Math.cos(ph);
      ring(P[0].clone().addScaledVector(T[0], -Math.max(r0y, r0z) * e * 0.9), T[0], N[0], B[0], r0y * f + 1e-4, r0z * f + 1e-4); }
    for (let i = 0; i <= nl; i++) { const [ry, rz] = prof(i / nl); ring(P[i], T[i], N[i], B[i], ry, rz); }
    for (let c = 1; c <= cr; c++) { const ph = (c / cr) * Math.PI / 2, e = Math.sin(ph), f = Math.cos(ph);
      ring(P[nl].clone().addScaledVector(T[nl], Math.max(r1y, r1z) * e * 0.9), T[nl], N[nl], B[nl], r1y * f + 1e-4, r1z * f + 1e-4); }
    this.g.attributes.position.needsUpdate = true; this.g.computeVertexNormals(); this.g.computeBoundingSphere();
  }
  // ponto na superfície: s ∈ [0,1] ao longo, ang = 0 na direção N (frente), lift = afastamento extra
  surface(s, ang, lift = 0) {
    const { P, N, B, prof } = this.frames; const f = s * this.nl, i = Math.max(0, Math.min(this.nl - 1, Math.floor(f))), k = f - i;
    const c = P[i].clone().lerp(P[i + 1], k), nn = N[i].clone().lerp(N[i + 1], k).normalize(), bb = B[i].clone().lerp(B[i + 1], k).normalize();
    const [ry, rz] = prof(s);
    return c.addScaledVector(nn, (ry + lift) * Math.cos(ang)).addScaledVector(bb, (rz + lift) * Math.sin(ang));
  }
}

// textura de tecido (ruído fino) para o relevo da regata e do short
function fabricTex() {
  const c = document.createElement("canvas"); c.width = c.height = 256; const x = c.getContext("2d");
  const img = x.createImageData(256, 256);
  for (let i = 0; i < 256 * 256; i++) { const v = 128 + ((i * 2654435761) % 997) / 997 * 60 - 30 + ((i % 256) % 4 < 2 ? 12 : -12); img.data.set([v, v, v, 255], i * 4); }
  x.putImageData(img, 0, 0); const t = new THREE.CanvasTexture(c); t.wrapS = t.wrapT = THREE.RepeatWrapping; t.repeat.set(6, 6); return t;
}

export function makeCharacter(scene, PAL) {
  const fab = fabricTex();
  const MC = {
    skin: new THREE.MeshPhysicalMaterial({ color: PAL.skin, roughness: 0.42, specularIntensity: 0.6, sheen: 0.15, sheenColor: 0xff9f80, clearcoat: 0.12, clearcoatRoughness: 0.55 }),
    top: new THREE.MeshPhysicalMaterial({ color: PAL.top, roughness: 0.82, bumpMap: fab, bumpScale: 0.6, sheen: 0.4, sheenColor: 0x7d82e0, side: THREE.DoubleSide }),
    shorts: new THREE.MeshPhysicalMaterial({ color: PAL.shorts, roughness: 0.78, bumpMap: fab, bumpScale: 0.5, side: THREE.DoubleSide }),
    hair: new THREE.MeshStandardMaterial({ color: PAL.hair, roughness: 0.7 }),
    shoe: new THREE.MeshStandardMaterial({ color: 0xf1efea, roughness: 0.5 }), sole: new THREE.MeshStandardMaterial({ color: PAL.accent, roughness: 0.5 }),
    band: new THREE.MeshStandardMaterial({ color: PAL.accent, roughness: 0.75 }), eye: new THREE.MeshStandardMaterial({ color: 0x15151a, roughness: 0.15 }),
    white: new THREE.MeshStandardMaterial({ color: 0xf4f1ec, roughness: 0.3 }),
  };
  const add = (o) => { scene.add(o); return o; };
  const ch = { MC };
  ch.torso = new Tube(MC.skin, { nr: 36, nl: 40 }); add(ch.torso.mesh);
  ch.shirt = new Tube(MC.top, { nr: 36, nl: 30, caps: false }); add(ch.shirt.mesh);
  ch.pants = new Tube(MC.shorts, { nr: 36, nl: 12, caps: false }); add(ch.pants.mesh);
  ch.legT = [new Tube(MC.skin, { nr: 24, nl: 48 }), new Tube(MC.skin, { nr: 24, nl: 48 })]; ch.legT.forEach((t) => add(t.mesh));
  ch.legS = [new Tube(MC.shorts, { nr: 24, nl: 16, caps: false }), new Tube(MC.shorts, { nr: 24, nl: 16, caps: false })]; ch.legS.forEach((t) => add(t.mesh));
  ch.armT = [new Tube(MC.skin, { nr: 24, nl: 48 }), new Tube(MC.skin, { nr: 24, nl: 48 })]; ch.armT.forEach((t) => add(t.mesh));
  ch.neck = new Tube(MC.skin, { nr: 20, nl: 8 }); add(ch.neck.mesh);
  // cabeça
  const head = new THREE.Group();
  const skull = new THREE.Mesh(new THREE.SphereGeometry(1, 48, 32), MC.skin); skull.scale.set(0.3, 0.29, 0.26); head.add(skull);
  const jaw = new THREE.Mesh(new THREE.SphereGeometry(1, 40, 24), MC.skin); jaw.position.set(-0.11, 0.06, 0); jaw.scale.set(0.2, 0.21, 0.21); head.add(jaw);
  const hair = new THREE.Mesh(new THREE.SphereGeometry(1, 48, 32, 0, Math.PI * 2, 0, 1.55), MC.hair);
  hair.scale.set(0.315, 0.3, 0.272); hair.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), new THREE.Vector3(0.8, -0.6, 0).normalize()); head.add(hair);
  const tuft = new THREE.Mesh(new THREE.SphereGeometry(1, 32, 20), MC.hair); tuft.position.set(0.2, 0.12, 0); tuft.scale.set(0.12, 0.12, 0.22); head.add(tuft);
  for (const z of [-1, 1]) {
    const w = new THREE.Mesh(new THREE.SphereGeometry(1, 24, 16), MC.white); w.position.set(0.05, 0.255, z * 0.095); w.scale.set(0.045, 0.02, 0.05); head.add(w);
    const e = new THREE.Mesh(new THREE.SphereGeometry(1, 24, 16), MC.eye); e.position.set(0.05, 0.268, z * 0.095); e.scale.set(0.028, 0.014, 0.028); e.name = "eye"; head.add(e);
    const b = new THREE.Mesh(new RoundedBoxGeometry(0.035, 0.03, 0.11, 2, 0.012), MC.hair); b.position.set(0.13, 0.255, z * 0.1); b.name = z < 0 ? "browL" : "browR"; head.add(b);
    const ear = new THREE.Mesh(new THREE.SphereGeometry(1, 20, 14), MC.skin); ear.position.set(0.0, 0.0, z * 0.26); ear.scale.set(0.07, 0.055, 0.035); head.add(ear);
  }
  const nose = new THREE.Mesh(new THREE.SphereGeometry(1, 20, 14), MC.skin); nose.position.set(-0.03, 0.275, 0); nose.scale.set(0.055, 0.045, 0.04); head.add(nose);
  const mouth = new THREE.Mesh(new RoundedBoxGeometry(0.025, 0.018, 0.09, 2, 0.008), MC.eye); mouth.position.set(-0.14, 0.235, 0); mouth.name = "mouth"; head.add(mouth);
  head.traverse((o) => { o.castShadow = o.receiveShadow = true; }); ch.head = add(head);
  ch.fists = [0, 1].map(() => { const g = new THREE.Group();
    const palm = new THREE.Mesh(new RoundedBoxGeometry(0.17, 0.17, 0.2, 4, 0.07), MC.skin); g.add(palm);
    const th = new THREE.Mesh(new THREE.CapsuleGeometry(0.035, 0.07, 6, 12), MC.skin); th.position.set(0.04, 0.0, 0.1); th.rotation.x = Math.PI / 2; g.add(th);
    g.traverse((o) => { o.castShadow = true; }); return add(g); });
  ch.bands = [0, 1].map(() => { const m = new THREE.Mesh(new THREE.CylinderGeometry(0.088, 0.088, 0.08, 28), MC.band); m.castShadow = true; return add(m); });
  ch.shoes = [0, 1].map(() => { const g = new THREE.Group();
    const up = new THREE.Mesh(new RoundedBoxGeometry(0.36, 0.15, 0.17, 4, 0.06), MC.shoe); up.position.set(0.06, 0.1, 0); g.add(up);
    const so = new THREE.Mesh(new RoundedBoxGeometry(0.39, 0.045, 0.19, 3, 0.02), MC.sole); so.position.set(0.06, 0.025, 0); g.add(so);
    g.traverse((o) => { o.castShadow = o.receiveShadow = true; }); return add(g); });
  // fibras do peitoral (ativação): tubos finos sobre o peito, com pulso
  ch.fibers = [];
  for (const side of [-1, 1]) for (let k = 0; k < 14; k++) {
    const upper = k >= 9;
    const mat = new THREE.MeshBasicMaterial({ color: new THREE.Color(PAL.accent).multiplyScalar(1.6), transparent: true, opacity: 0, blending: THREE.AdditiveBlending, depthWrite: false });
    const m = new THREE.Mesh(new THREE.BufferGeometry(), mat); m.frustumCulled = false; add(m);
    ch.fibers.push({ m, side, k, upper });
  }
  return ch;
}

// perfis (s de 0 a 1)
const TORSO = profile([[0, 0.27, 0.4], [0.12, 0.27, 0.41], [0.35, 0.245, 0.37], [0.62, 0.29, 0.45], [0.78, 0.29, 0.5], [0.9, 0.23, 0.52], [0.97, 0.15, 0.3], [1, 0.12, 0.14]]);
const SHIRT = (s) => { const v = TORSO(0.1 + s * 0.83); return [v[0] + 0.018, v[1] + 0.018]; };
const PANTS = (s) => { const v = TORSO(s * 0.16); return [v[0] + 0.02, v[1] + 0.02]; };

export function poseCharacter(ch, J, S, nrm, legs, arms, head, t, effort) {
  // tronco: do quadril ao pescoço, frente = normal do peito
  const axis = new THREE.Vector3().subVectors(S, J).normalize(), L = J.distanceTo(S);
  const pts = [J.clone().addScaledVector(axis, -0.12), J.clone().addScaledVector(axis, L * 0.45), J.clone().addScaledVector(axis, L * 0.85), S.clone().addScaledVector(axis, 0.16)];
  ch.torso.update(pts, TORSO, nrm);
  const sp = (s) => ch.torso.surface(s, 0, 0);
  const seg = (a, b) => { const out = []; for (let i = 0; i <= 3; i++) out.push(new THREE.CatmullRomCurve3(pts, false, "centripetal").getPointAt(a + (b - a) * i / 3)); return out; };
  ch.shirt.update(seg(0.1, 0.93), SHIRT, nrm);
  ch.pants.update(seg(0.0, 0.16), PANTS, nrm);
  // pernas: quadril → joelho → tornozelo (uma malha só)
  legs.forEach(([hip, knee, ank], i) => {
    const L1 = hip.distanceTo(knee), L2 = knee.distanceTo(ank), sk = L1 / (L1 + L2);
    const pr = profile([[0, 0.19, 0.19], [0.3, 0.175, 0.175], [sk - 0.03, 0.12, 0.12], [sk + 0.03, 0.115, 0.115], [sk + 0.16, 0.13, 0.125], [sk + 0.32, 0.11, 0.105], [0.97, 0.075, 0.075], [1, 0.07, 0.07]]);
    const kneeOut = new THREE.Vector3().subVectors(knee, hip.clone().lerp(ank, sk)).normalize();
    ch.legT[i].update([hip, hip.clone().lerp(knee, 0.5), knee, knee.clone().lerp(ank, 0.5), ank], pr, kneeOut.lengthSq() > 0 ? kneeOut : new THREE.Vector3(0, 1, 0));
    const ps = (s) => { const v = pr(s * sk * 0.6); return [v[0] + 0.022, v[1] + 0.022]; };
    const a = hip.clone(), b = hip.clone().lerp(knee, 0.6);
    ch.legS[i].update([a, a.clone().lerp(b, 0.5), b], ps, kneeOut);
    ch.shoes[i].position.set(ank.x - 0.02, 0, ank.z); ch.shoes[i].rotation.y = (i ? 1 : -1) * 0.12;
  });
  // braços: de dentro do ombro → cotovelo → punho (deltoide faz parte do perfil)
  arms.forEach(([sh, el, wr], i) => {
    const L1 = sh.distanceTo(el), L2 = el.distanceTo(wr), se = L1 / (L1 + L2);
    const pr = profile([[0, 0.15, 0.15], [0.08, 0.165, 0.16], [0.2, 0.135, 0.13], [se * 0.62, 0.13, 0.125], [se - 0.02, 0.095, 0.095], [se + 0.03, 0.095, 0.095], [se + 0.14, 0.105, 0.1], [0.95, 0.07, 0.07], [1, 0.068, 0.068]]);
    const out = new THREE.Vector3().subVectors(el, sh.clone().lerp(wr, se)).normalize();
    ch.armT[i].update([sh, sh.clone().lerp(el, 0.5), el, el.clone().lerp(wr, 0.5), wr], pr, out.lengthSq() > 0 ? out : new THREE.Vector3(0, 1, 0));
    const d = new THREE.Vector3().subVectors(wr, el).normalize();
    ch.fists[i].position.copy(wr).addScaledVector(d, 0.06);
    ch.fists[i].quaternion.setFromRotationMatrix(new THREE.Matrix4().makeBasis(d, new THREE.Vector3(0, 0, 1).cross(d).normalize(), new THREE.Vector3(0, 0, 1)));
    ch.bands[i].position.copy(wr).addScaledVector(d, -0.07); ch.bands[i].quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), d);
  });
  // pescoço e cabeça
  const nb = S.clone().addScaledVector(axis, 0.08);
  ch.neck.update([nb, nb.clone().lerp(head, 0.5), head.clone().addScaledVector(axis, -0.05)], profile([[0, 0.13, 0.13], [1, 0.11, 0.11]]), nrm);
  ch.head.position.copy(head);
  const X = axis.clone(), Z = new THREE.Vector3().crossVectors(X, nrm).normalize(), Yv = new THREE.Vector3().crossVectors(Z, X);
  ch.head.quaternion.setFromRotationMatrix(new THREE.Matrix4().makeBasis(X, Yv, Z));
  ch.head.children.forEach((o) => {
    if (o.name === "browL") o.rotation.y = 0.35 * effort; if (o.name === "browR") o.rotation.y = -0.35 * effort;
    if (o.name === "eye") o.scale.y = 0.014 * (1 - 0.65 * effort); if (o.name === "mouth") o.scale.z = 1 + 0.7 * effort;
  });
}

// fibras: da linha do esterno (frente) até a inserção perto da axila; superiores saem da clavícula
export function poseFibers(ch, t, lowAct, upAct) {
  for (const f of ch.fibers) {
    const { side, k, upper } = f;
    let s0, a0;
    if (!upper) { s0 = 0.5 + (k / 8) * 0.28; a0 = side * 0.08; } else { const kk = (k - 9) / 4; s0 = 0.86; a0 = side * (0.15 + kk * 0.5); }
    const s1 = 0.86, a1 = side * 1.02;
    const pts = [];
    for (let i = 0; i <= 14; i++) { const u = i / 14; pts.push(ch.torso.surface(s0 + (s1 - s0) * u * u, a0 + (a1 - a0) * u, 0.03)); }
    const curve = new THREE.CatmullRomCurve3(pts);
    f.m.geometry.dispose(); f.m.geometry = new THREE.TubeGeometry(curve, 24, 0.017, 6, false);
    const act = upper ? upAct : lowAct;
    const pulse = 0.5 + 0.5 * Math.sin(t * 7 - k * 0.6);
    f.m.material.opacity = Math.min(1, act * (0.55 + 0.75 * pulse));
  }
}
