# BRIO_19 — canal de treino (BRIO) · lote adiantado 09/11
TITLE = 'Travou no supino? 3 saídas pra voltar a subir'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"
GATILHO = 'Comenta há quantas semanas o seu supino não sobe.'
GATILHO_TIPO = 1

NARRATION = {'file': 'audio_tight/roteiro_brio_19.mp3', 'starts': [0.0, 4.634, 9.573, 14.897, 20.317, 24.83, 30.544, 35.072, 38.472, 42.065, 46.906]}  # narração enxuta (tighten.py)

BEATS = [
    dict(vis='hook', k='', t1='SUPINO', t2='TRAVOU?',
         text='Seu supino está travado no mesmo peso há semanas? Tem três saídas, e uma é bem simples.'),
    dict(vis='plateau', k='', t1='O PLATÔ', t2='ACONTECE COM TODOS.',
         text='Travar acontece com todo mundo. O corpo se acostuma, e o mesmo treino para de dar resultado.'),
    dict(vis='one', k='', t1='SAÍDA 1', t2='MAIS REPETIÇÕES.',
         text='Saída um: mantém o peso e busca mais repetições. Quando passar da sua meta, sobe o peso.'),
    dict(vis='two', k='', t1='SAÍDA 2', t2='MAIS SÉRIES.',
         text='Saída dois: acrescenta uma ou duas séries de peito na semana. Às vezes falta volume, não força.'),
    dict(vis='three', k='', t1='SAÍDA 3', t2='SEMANA LEVE.',
         text='Saída três: faz uma semana mais leve. Cansaço acumulado também trava a carga.'),
    dict(vis='tech', k='', t1='O SEGREDO', t2='A TÉCNICA.',
         text='E o segredo que quase ninguém olha: a técnica. Pés firmes, escápulas juntas, barra descendo no peito.'),
    dict(vis='sleep', k='', t1='TAMBÉM CONTA', t2='SONO E COMIDA.',
         text='Sono ruim e comida pouca também seguram o supino. Não adianta mudar só o treino.'),
    dict(vis='change', k='', t1='O ERRO', t2='MUDAR TUDO.',
         text='O erro é mudar tudo de uma vez. Aí você não sabe o que funcionou.'),
    dict(vis='one_thing', k='', t1='A REGRA', t2='UMA COISA POR VEZ.',
         text='Muda uma coisa por vez, por umas três semanas, e compara os números.'),
    dict(vis='patience', k='', t1='PACIÊNCIA', t2='TAMBÉM CONTA.',
         text='E tem paciência. Às vezes a carga para duas semanas e volta a subir sozinha na terceira.'),
    dict(vis='cta', k='', t1='COMENTA', t2='AS SEMANAS.',
         text='Comenta há quantas semanas o seu supino não sobe. No Bríu você vê no gráfico onde ele travou. Registre e acompanhe seus treinos gratuitamente. Link na bio.',
         marks={'ponte': 2.864, 'fixa': 5.234, 'link': 7.606}),
]
