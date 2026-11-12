# BRIO_21 — canal de treino (BRIO) · lote adiantado 09/11
TITLE = 'Dá pra ganhar músculo sem peso?'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"
GATILHO = 'Time academia ou time treino em casa? Comenta.'
GATILHO_TIPO = 4

NARRATION = {'file': 'audio_tight/roteiro_brio_21.mp3', 'starts': [0.0, 4.361, 9.157, 14.509, 18.853, 23.401, 27.461, 33.787, 38.245, 43.01, 48.369]}  # narração enxuta (tighten.py)

BEATS = [
    dict(vis='hook', k='', t1='SEM PESO', t2='DÁ MÚSCULO?',
         text='Dá pra ganhar músculo sem pegar em peso nenhum? A resposta surpreende muita gente.'),
    dict(vis='yes', k='', t1='A RESPOSTA', t2='SIM, DÁ.',
         text='Dá sim. O músculo não sabe se a força vem de uma barra ou do seu próprio corpo.'),
    dict(vis='rule', k='', t1='A CONDIÇÃO', t2='PERTO DO LIMITE.',
         text='A condição é a mesma da academia: levar a série perto do limite, sem sobrar muita repetição.'),
    dict(vis='problem', k='', t1='O PROBLEMA', t2='FICA FÁCIL.',
         text='O problema é que o corpo fica forte rápido, e vinte flexões viram fácil demais.'),
    dict(vis='harder', k='', t1='O SEGREDO', t2='DEIXAR MAIS DIFÍCIL.',
         text='O segredo é deixar mais difícil. Pé no alto na flexão, uma perna só no agachamento.'),
    dict(vis='slow', k='', t1='OUTRO TRUQUE', t2='MAIS DEVAGAR.',
         text='Outro truque: descer bem devagar, e segurar alguns segundos na parte de baixo.'),
    dict(vis='limit', k='', t1='O LIMITE', t2='PERNA E COSTAS.',
         text='O mais difícil sem peso é perna e costas. Pra isso, uma mochila cheia ou uma barra fixa ajudam muito.'),
    dict(vis='gym', k='', t1='E A ACADEMIA?', t2='É MAIS FÁCIL.',
         text='A academia facilita, porque é só colocar mais peso. Mas não é obrigatória pra começar.'),
    dict(vis='count', k='', t1='O QUE CONTA', t2='PROGREDIR.',
         text='Em casa ou na academia, o que conta é a mesma coisa: progredir um pouco a cada semana.'),
    dict(vis='start', k='', t1='PRA COMEÇAR', t2='TRÊS EXERCÍCIOS.',
         text='Pra começar em casa: flexão, agachamento e remada com mochila. Três séries de cada, perto do limite.'),
    dict(vis='cta', k='', t1='COMENTA', t2='SEU TIME.',
         text='Time academia ou time treino em casa? Comenta. No Bríu dá pra registrar as repetições de qualquer treino. Registre e acompanhe seus treinos gratuitamente. Link na bio.',
         marks={'ponte': 2.623, 'fixa': 5.468, 'link': 8.061}),
]
