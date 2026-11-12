# BRIO_17 — canal de treino (BRIO) · lote adiantado 09/11
TITLE = 'A parte do movimento que você corta é a que mais faz crescer'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"
GATILHO = 'Manda pro seu parceiro de treino que só faz meia repetição.'
GATILHO_TIPO = 3

NARRATION = {'file': 'audio_tight/roteiro_brio_17.mp3', 'starts': [0.0, 3.833, 8.572, 12.894, 18.085, 22.425, 26.974, 31.207, 35.267, 39.985, 46.431]}  # narração enxuta (tighten.py)

BEATS = [
    dict(vis='hook', k='', t1='VOCÊ CORTA', t2='A MELHOR PARTE.',
         text='A parte do movimento que você corta pode ser a que mais faz o músculo crescer.'),
    dict(vis='half', k='', t1='O ERRO', t2='MEIA REPETIÇÃO.',
         text='Muita gente faz só a metade de cima do movimento, onde é mais fácil e cabe mais peso.'),
    dict(vis='stretch', k='', t1='O QUE OS ESTUDOS', t2='APONTAM.',
         text='Só que estudos recentes apontam: o músculo cresce muito quando trabalha bem alongado.'),
    dict(vis='where', k='', t1='ALONGADO', t2='É EMBAIXO.',
         text='Alongado é a parte de baixo. No supino, a barra perto do peito. Na rosca, o braço quase esticado.'),
    dict(vis='squat', k='', t1='NO AGACHAMENTO', t2='DESCE BEM.',
         text='No agachamento, é a descida funda. É ali que o glúteo e a coxa mais trabalham.'),
    dict(vis='partial', k='', t1='O TRUQUE', t2='PARCIAL EMBAIXO.',
         text='Tem até um truque: no fim da série, quando cansar, faz meias repetições na parte de baixo.'),
    dict(vis='control', k='', t1='O SEGREDO', t2='DESCE DEVAGAR.',
         text='O segredo é descer devagar e controlar embaixo, sem quicar e sem soltar o peso.'),
    dict(vis='weight', k='', t1='O PREÇO', t2='MENOS PESO.',
         text='O preço é tirar um pouco do peso. O ego reclama, mas o músculo agradece.'),
    dict(vis='pain', k='', t1='CUIDADO', t2='SEM DOR.',
         text='Sentiu dor na articulação nessa posição? Diminui a amplitude, e procura um profissional.'),
    dict(vis='examples', k='', t1='OUTROS', t2='EXEMPLOS.',
         text='Na cadeira flexora, o joelho bem esticado. No crucifixo, os braços bem abertos. Sempre a parte mais difícil.'),
    dict(vis='cta', k='', t1='MANDA', t2='PRO PARCEIRO.',
         text='Manda pro seu parceiro de treino que só faz meia repetição. No Bríu, vocês veem quem sobe a carga primeiro. Registre e acompanhe seus treinos gratuitamente. Link na bio.',
         marks={'ponte': 3.08, 'fixa': 5.7, 'link': 8.219}),
]
