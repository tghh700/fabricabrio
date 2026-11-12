# BRIO_16 — canal de treino (BRIO) · lote adiantado 09/11
TITLE = 'Abdominal todo dia não tira barriga'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"
GATILHO = 'Time abdominal todo dia ou time treino completo? Comenta.'
GATILHO_TIPO = 4

NARRATION = {'file': 'audio_tight/roteiro_brio_16.mp3', 'starts': [0.0, 3.894, 7.539, 11.776, 15.913, 20.851, 25.584, 30.304, 35.302, 40.145, 45.275]}  # narração enxuta (tighten.py)

BEATS = [
    dict(vis='hook', k='', t1='ABDOMINAL', t2='TODO DIA?',
         text='Você faz abdominal todo dia pra secar a barriga? Isso quase não mexe na gordura dali.'),
    dict(vis='spot', k='', t1='O MITO', t2='QUEIMAR NO LUGAR.',
         text='O mito é achar que treinar uma região queima a gordura daquela região.'),
    dict(vis='body', k='', t1='COMO FUNCIONA', t2='O CORPO TODO.',
         text='O corpo tira gordura do corpo todo, na ordem que ele quer. Você não escolhe de onde sai.'),
    dict(vis='abs', k='', t1='O ABDÔMEN', t2='JÁ EXISTE.',
         text='E o abdômen trincado você já tem. Ele só está escondido embaixo da gordura.'),
    dict(vis='what', k='', t1='O QUE SECA', t2='TOTAL DO DIA.',
         text='O que seca a barriga é o total do dia: comer um pouco menos do que você gasta, com constância.'),
    dict(vis='lift', k='', t1='O QUE AJUDA', t2='MUSCULAÇÃO.',
         text='A musculação ajuda muito. Você gasta energia e mantém o músculo enquanto perde gordura.'),
    dict(vis='walk', k='', t1='E MAIS', t2='ANDAR MAIS.',
         text='Somar passos no dia também ajuda. Caminhar é simples e conta muito no final da semana.'),
    dict(vis='core', k='', t1='ENTÃO PARO?', t2='NÃO. DOSA.',
         text='Então para o abdominal? Não. Ele fortalece o tronco. Só não precisa ser todo dia.'),
    dict(vis='time', k='', t1='O SEGREDO', t2='PACIÊNCIA.',
         text='O segredo é paciência. A barriga costuma ser a última a sair, e a primeira a voltar.'),
    dict(vis='proof', k='', t1='A PROVA', t2='NA FITA.',
         text='E pra ver se a barriga está diminuindo, usa a fita métrica na cintura, uma vez por semana, no mesmo horário.'),
    dict(vis='cta', k='', t1='COMENTA', t2='SEU TIME.',
         text='Time abdominal todo dia ou time treino completo? Comenta. No Bríu você monta um treino que cabe no seu tempo. Registre e acompanhe seus treinos gratuitamente. Link na bio.',
         marks={'ponte': 3.212, 'fixa': 5.537, 'link': 8.039}),
]
