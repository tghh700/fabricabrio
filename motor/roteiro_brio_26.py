# BRIO_26 — canal de treino (BRIO) · lote adiantado 09/11
TITLE = 'O joelho pode passar da ponta do pé no agachamento?'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"
GATILHO = 'Time joelho pode passar ou time não pode? Comenta.'
GATILHO_TIPO = 4

NARRATION = {'file': 'audio_tight/roteiro_brio_26.mp3', 'starts': [0.0, 4.189, 7.514, 11.286, 15.732, 20.739, 25.699, 30.333, 35.718, 40.513, 46.129]}  # narração enxuta (tighten.py)

BEATS = [
    dict(vis='hook', k='', t1='O JOELHO', t2='PODE PASSAR?',
         text='Te disseram que o joelho nunca pode passar da ponta do pé no agachamento? Vamos ver isso direito.'),
    dict(vis='myth', k='', t1='O MITO', t2='JOELHO PRA TRÁS.',
         text='A ideia era proteger o joelho, travando ele atrás da ponta do pé.'),
    dict(vis='body', k='', t1='O CORPO', t2='NÃO FUNCIONA ASSIM.',
         text='Só que pra descer fundo, com o tronco em pé, o joelho naturalmente vai pra frente.'),
    dict(vis='back', k='', t1='O PROBLEMA', t2='A LOMBAR PAGA.',
         text='Quando você trava o joelho, o tronco deita pra frente, e quem paga é a lombar e o quadril.'),
    dict(vis='daily', k='', t1='NO DIA A DIA', t2='VOCÊ JÁ FAZ.',
         text='E no dia a dia você já faz isso. Subir escada e sentar no chão passam o joelho da ponta do pé.'),
    dict(vis='what', k='', t1='O QUE IMPORTA', t2='O PÉ INTEIRO NO CHÃO.',
         text='O que importa é o pé inteiro no chão, o calcanhar firme, e o joelho na direção dos dedos.'),
    dict(vis='secret', k='', t1='O SEGREDO', t2='CONTROLE.',
         text='O segredo é controle: descer devagar, sem deixar o joelho cair pra dentro.'),
    dict(vis='pain', k='', t1='ATENÇÃO', t2='SE DOER.',
         text='Mas se o seu joelho dói, a regra muda. Diminui a amplitude e procura um fisioterapeuta.'),
    dict(vis='progress', k='', t1='E A CARGA', t2='SOBE DEVAGAR.',
         text='E a carga sobe aos poucos, só quando a técnica estiver firme em todas as repetições.'),
    dict(vis='stance', k='', t1='A BASE', t2='PÉS NA LARGURA.',
         text='Os pés ficam mais ou menos na largura dos ombros, com as pontas um pouco pra fora. Ajusta até ficar confortável.'),
    dict(vis='cta', k='', t1='COMENTA', t2='SEU TIME.',
         text='Time joelho pode passar ou time não pode? Comenta. No Bríu você registra cada série do seu agachamento. Registre e acompanhe seus treinos gratuitamente. Link na bio.',
         marks={'ponte': 2.587, 'fixa': 5.184, 'link': 7.744}),
]
