# Guia para animar um short (fábrica de vídeos)

Pasta: /home/claude/fabrica. Você recebe um ROTEIRO pronto (roteiro_XXX.py) com a narração JÁ GERADA (cache em audio_cache/).
**NUNCA chame o ElevenLabs / tts.py diretamente e nunca altere o texto (`text`) dos beats** — isso gasta créditos pagos. Você só escreve o arquivo de cenas e renderiza.

## O que entregar
1. Criar `scenes_XXX.py` com uma função por `vis` do roteiro (roteiros agora têm 10 a 12 cenas e ≈ 1 min: varie bastante os visuais, nada de repetir a mesma composição em cenas seguidas) + dicionários `VIS` e `SFX` (veja modelo em scenes_short02.py, scenes_short03.py, scenes_gym01.py).
2. Gerar quadros de conferência: `python3 build2.py roteiro_XXX scenes_XXX --stills` (salva em out/roteiro_XXX_stills/NN_35.png e NN_85.png). Monte uma folha de contato com PIL e OLHE as imagens com a ferramenta Read. Corrija sobreposições.
3. Renderizar: `python3 build2.py roteiro_XXX scenes_XXX` → out/roteiro_XXX.mp4 (~1 min).
4. NÃO edite engine2.py, build2.py, tts.py nem cenas de outros vídeos (outros agentes estão trabalhando em paralelo). Se precisar de um objeto novo, desenhe dentro do seu scenes_XXX.py.

## Assinatura de cena
```python
from engine2 import *
from scenes_short02 import chip   # chip(c, texto, x, y, cor_fundo, cor_texto=WHITE, size=66, t=t, start=seg)
def minha_cena(c, t, d, b):       # t = segundos desde o início da cena, d = duração da cena, b = dict do beat
    with Cam(c, t, punch=0.06):   # zoom de entrada; shake=px para tremer
        ...
VIS = {"minha_cena": minha_cena, ...}
SFX = {"minha_cena": [(0.0, "whoosh"), ("0.5d", "pop")], ...}   # tempos em s ou fração de d ("0.5d+0.3")
```
Efeitos disponíveis: whoosh, swish, pop, click, tick, clack, boom, ding, buzz, shutter, zip.
Use `boom` no gancho (1ª cena) e `whoosh` no início das demais.

## Layout (tela 1080x1920)
- O título (2 linhas Anton; o kicker/quadradinho não é mais desenhado) é desenhado automaticamente no topo e ocupa até y≈650 (títulos de 3 linhas: até ≈780). **Todo o conteúdo da cena deve ficar entre y≈820 e y≈1800.**
- Chão: `FLOOR_Y = 1640`. Personagem em pé: `chunky(c, x, FLOOR_Y, s, pose, face=1|-1, dark=False|True, helmet=..., bob=...)` → retorna (x,y) da mão da frente. Altura ≈ 615*s px. Use s 0.7–0.95.
- Barra de progresso e marca d'água são desenhadas automaticamente (marca no canto superior direito, y≈80–140: não coloque nada lá).
- Margens laterais: 60 px.

## Estética
Fundo escuro com grade (automático). Bonecos gordinhos sem rosto: claro (protagonista) e escuro (`dark=True`, coadjuvante). Cor de destaque: `YEL` (no tema BRIO vira coral automaticamente — use sempre `YEL`, nunca um amarelo fixo). Verde = certo, vermelho = errado/perigo, azul = água/neutro.
Movimento sempre: algo entra/pulsa/anima em toda cena (pop com back_out, ring pulsando, arrow animada com p=prog(...), check_mark/x_mark com p). Nada parado por mais de ~1 s.
**Ordem de desenho (10/11):** o que precisa ficar na frente é desenhado por último. Seta de gráfico passa ACIMA das barras e só cresce depois que elas aparecem; nenhuma seta ou linha atravessa texto/rótulo; elemento que surge depois não pode cobrir outro que ainda está na tela. Confira isso nos stills 35 e 85 de cada cena.
Ritmo: o elemento principal aparece até 0.4 s após o início; o "chip"/label de reforço aparece por volta de 0.4–0.6·d.

## Poses (POSES em engine2)
idle, reach, reach_low, point_up, scratch, shrug, laugh, phone_up, thumb, cheer, push, guard, shock, walk1, walk2,
bar_back, squat_half, squat_deep, curl_down, curl_up, flex, tired. Misture com `pose_mix("idle", "reach", prog(t, 0.2, 0.4))`.

## Primitivas úteis (engine2)
clamp, ease, ease_out, back_out, lerp, prog(t,start,dur), mix(cor1,cor2,t)
cap_line, poly, disk, rrect(c,x,y,w,h,r,cor,alpha), draw_text(c,s,x,y,size,cor,"Anton"|"Space Mono",alpha,align,spacing), label(c,s,x,y,cor,size)
wall, outlet (padrão BR NBR 14136), module_back, wall_box, wires, breaker_panel, screwdriver, phone, phone_screen(lines=[(texto,cor)],title,logo), dr_flat, finger
check_mark, x_mark, spark, bolt, ring, arrow, plane, resistor, shower, snowflake, pizza, barbell, bed, chart_up
brio_mark(c,x,y,s,trail,t), brio_wordmark(c,x,y,size), fioterra_mark(c,x,y,s)
Para escalar algo com pop: `p = back_out(prog(t, start, 0.3)); c.save(); c.translate(x,y); c.scale(max(p,.001), max(p,.001)); ...; c.restore()` (nunca escala 0).

## Regras de conteúdo
- Padrão brasileiro sempre (tomada sextavada de 3 furos, fios: azul-claro neutro, verde/verde-amarelo terra).
- O visual deve ilustrar exatamente o que a narração diz naquele beat.
- No canal BRIO: a última cena mostra a marca do BRIO (brio_mark + brio_wordmark, cores oficiais coral #FF4D2E e lilás #C9B8FF) e um chip "LINK NA BIO", com uma linha curta de reforço em Space Mono pequena (ex.: "REGISTRE E ACOMPANHE SEUS / TREINOS GRATUITAMENTE"; pode adaptar ao fechamento falado). Use o helper cta_brio.py. Telas do app são estilizadas e genéricas (sem nomes ou dados de usuários reais).
