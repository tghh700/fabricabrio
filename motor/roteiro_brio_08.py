# BRIO_08 — canal de treino (BRIO)
TITLE = 'Cardio está matando seu ganho de massa?'
VOICE = "plASsyS7JE6GCAvx9uIc"  # Marcio
SETTINGS = {"stability": 0.5, "similarity_boost": 0.8, "style": 0.2, "use_speaker_boost": True, "speed": 1.1}
FULL = True
THEME = "brio"
BRAND = "brio"

# 10/11: narração montada (original + frase do Bríu + fechamento novo) e enxugada, sem gastar crédito
NARRATION = {'file': 'audio_tight/roteiro_brio_08.mp3', 'starts': [0.0, 4.1, 9.681, 13.895, 19.316, 24.091]}

BEATS = [
    dict(vis='hook', k='MITO OU VERDADE', t1='CARDIO MATA', t2='SEU MÚSCULO?',
         text='Cardio mata o seu ganho de massa? Muita gente foge da esteira por causa disso.'),
    dict(vis='science', k='O QUE A CIÊNCIA DIZ', t1='NA DOSE CERTA,', t2='NÃO ATRAPALHA.',
         text='As revisões de estudos mostram: na dose certa, o cardio quase não atrapalha o crescimento do músculo.'),
    dict(vis='heart', k='E AINDA', t1='CORAÇÃO', t2='AGRADECE.',
         text='E ainda ajuda o coração, o fôlego e a recuperação entre as séries.'),
    dict(vis='order', k='O SEGREDO', t1='MUSCULAÇÃO', t2='PRIMEIRO.',
         text='O segredo é a ordem: musculação primeiro, cardio depois. Ou em horários separados, se der.'),
    dict(vis='type', k='A ESCOLHA', t1='BIKE OU', t2='CAMINHADA.',
         text='Prefere bike ou caminhada inclinada, que cansam menos a perna. E não exagera no volume.'),
    dict(vis='cta', k='LINK NA BIO', t1='VÊ SE A CARGA', t2='CONTINUA SUBINDO.',
         text='Quer ter certeza? Registra no BRIO e confere no gráfico se sua carga continua subindo. Grátis pra registrar. Link na bio.'),
]
