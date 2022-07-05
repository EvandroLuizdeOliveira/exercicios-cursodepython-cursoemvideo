"""
Programa que pega uma tupla com os 20 primeiros times do brasileirão de 2022 em ordem de classificação e mostra: os primeiros 20 times, os 5 primeiros, os 4 últimos, os 20 times em ordem alfabética e em que posição está o Flamengo.
"""
classificacao_brasileirao = ('Palmeiras', 'Corinthians', 'Athletico-PR', 'Internacional', 'Atlético-MG', 'Fluminense', 'Santos', 'São Paulo', 'Flamengo', 'Botafogo', 'Avaí', 'Bragantino', 'Atlético-GO', 'Goiás', 'Ceará SC', 'Coritiba', 'América-MG', 'Cuiabá', 'Juventude', 'Fortaleza')
print(f'{"=-="*10}\nLista de times do Brasileirão: {classificacao_brasileirao}'
f'\n{"=-="*10}\nOs 5 primeiros são {classificacao_brasileirao[0:5]}'
f'\n{"=-="*10}\nOs 4 últimos são {classificacao_brasileirao[-4:]}'
f'\n{"=-="*10}\nTimes em ordem alfabética: {sorted(classificacao_brasileirao)}'
f'\n{"=-="*10}\nO Flamengo está na {(classificacao_brasileirao.index("Flamengo"))+1}ª posição\n')
