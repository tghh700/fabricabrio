# BRIO_13 — canal de treino (BRIO) · lote adiantado 09/11
TITLE = 'Quantas repetições pra crescer? Não é só 8 a 12'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"
GATILHO = 'Salva pro próximo treino, testa uma série mais longa e volta pra comentar como foi.'
GATILHO_TIPO = 5

NARRATION = {'file': 'audio_tight/roteiro_brio_13.mp3', 'starts': [0.0, 3.869, 8.191, 13.147, 18.244, 23.574, 28.634, 33.185, 38.337, 43.845, 49.736]}  # narração enxuta (tighten.py)

BEATS = [
    dict(vis='hook', k='', t1='8 A 12', t2='REPETIÇÕES?',
         text='Te disseram que pra crescer tem que ser de oito a doze repetições? Isso está incompleto.'),
    dict(vis='myth', k='', t1='A REGRA', t2='QUE TODO MUNDO REPETE.',
         text='Oito a doze virou regra de academia. Funciona, mas não é a única faixa que funciona.'),
    dict(vis='science', k='', t1='O QUE OS ESTUDOS', t2='MOSTRAM.',
         text='Os estudos mostram que de seis até umas trinta repetições, o músculo cresce de forma parecida.'),
    dict(vis='catch', k='', t1='A CONDIÇÃO', t2='PERTO DO LIMITE.',
         text='A condição é uma só: terminar a série perto do limite, com no máximo umas três repetições sobrando.'),
    dict(vis='light', k='', t1='SÉRIE LONGA', t2='QUEIMA MAIS.',
         text='Com peso leve e muita repetição, a série cansa e queima mais. Mas o músculo trabalha do mesmo jeito.'),
    dict(vis='heavy', k='', t1='SÉRIE CURTA', t2='PESA NA ARTICULAÇÃO.',
         text='Com peso alto e poucas repetições, você ganha mais força, mas cansa mais a articulação.'),
    dict(vis='mix', k='', t1='O SEGREDO', t2='MISTURAR.',
         text='O segredo é misturar. Exercícios grandes com menos repetições, e os pequenos com mais.'),
    dict(vis='example', k='', t1='EXEMPLO', t2='NA PRÁTICA.',
         text='Agachamento com seis a dez. Elevação lateral com quinze a vinte. Tudo levado perto do limite.'),
    dict(vis='track', k='', t1='O QUE MANDA', t2='É PROGREDIR.',
         text='E em qualquer faixa, o que faz crescer é progredir. Uma repetição a mais, ou um pouco mais de peso.'),
    dict(vis='rest', k='', t1='E O DESCANSO', t2='ACOMPANHA.',
         text='E o descanso acompanha: série curta e pesada pede mais descanso, série longa e leve pede menos.'),
    dict(vis='cta', k='', t1='SALVA', t2='E TESTA.',
         text='Salva pro próximo treino, testa uma série mais longa e volta pra comentar como foi. Anota cada série no Bríu. Registre e acompanhe seus treinos gratuitamente. Link na bio.',
         marks={'ponte': 3.872, 'fixa': 5.294, 'link': 7.77}),
]
