# BRIO_18 — canal de treino (BRIO) · lote adiantado 09/11
TITLE = 'Quanto tempo pro supino subir 10 kg?'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"
GATILHO = 'Salva, anota o seu supino de hoje e volta aqui daqui a um mês pra comentar quanto subiu.'
GATILHO_TIPO = 5

NARRATION = {'file': 'audio_tight/roteiro_brio_18.mp3', 'starts': [0.0, 4.28, 8.893, 13.634, 18.602, 22.38, 27.411, 32.358, 36.675, 41.286, 45.935]}  # narração enxuta (tighten.py)

BEATS = [
    dict(vis='hook', k='', t1='SUPINO', t2='+10 KG?',
         text='Quanto tempo leva pra subir dez quilos no supino? Depende de uma coisa que quase ninguém mede.'),
    dict(vis='beginner', k='', t1='INICIANTE', t2='SOBE RÁPIDO.',
         text='Se você é iniciante, a carga sobe rápido. Em poucos meses, dez quilos a mais é bem comum.'),
    dict(vis='why', k='', t1='POR QUÊ', t2='O CORPO APRENDE.',
         text='Isso acontece porque o corpo está aprendendo o movimento. Cada semana você fica mais eficiente.'),
    dict(vis='inter', k='', t1='QUEM JÁ TREINA', t2='SOBE DEVAGAR.',
         text='Já quem treina há anos sobe bem mais devagar. Dez quilos podem levar um ano ou mais.'),
    dict(vis='normal', k='', t1='E ISSO', t2='É NORMAL.',
         text='E isso é normal. Quanto mais perto do seu limite, menor fica cada passo.'),
    dict(vis='small', k='', t1='O SEGREDO', t2='PASSOS PEQUENOS.',
         text='O segredo é subir em passos pequenos. Um quilo de cada lado, ou uma repetição a mais.'),
    dict(vis='stall', k='', t1='O ERRO', t2='PULAR ETAPAS.',
         text='O erro é tentar pular etapas. Peso alto demais, repetição pela metade, e o supino trava.'),
    dict(vis='math', k='', t1='A CONTA', t2='UM POUCO TODA SEMANA.',
         text='Faz a conta: meio quilo a mais por semana já dá mais de vinte quilos em um ano.'),
    dict(vis='measure', k='', t1='O QUE FALTA', t2='MEDIR.',
         text='Só que pra saber se está subindo, você precisa saber a carga de hoje, e a da semana passada.'),
    dict(vis='lower', k='', t1='E NA PERNA', t2='SOBE MAIS.',
         text='E na perna a carga costuma subir mais rápido que no supino, porque os músculos são maiores.'),
    dict(vis='cta', k='', t1='SALVA', t2='E VOLTA.',
         text='Salva, anota o seu supino de hoje e volta aqui daqui a um mês pra comentar quanto subiu. O Bríu guarda o gráfico. Registre e acompanhe seus treinos gratuitamente. Link na bio.',
         marks={'ponte': 4.346, 'fixa': 5.515, 'link': 8.092}),
]
