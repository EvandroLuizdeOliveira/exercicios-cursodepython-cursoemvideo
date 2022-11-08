from random import randint
from time import sleep
posicao = 0
jogadores = dict()
print('Valores sorteados:')
for contador in range(1,5):
    jogadores[f'jogador{contador}'] = randint(1,6)
    print(f'{" " * 3}O jogador{contador} tirou {jogadores[f"jogador{contador}"]} ')
    sleep(1)
print('Ranking dos jogadores:')
for indice in sorted(jogadores, key = jogadores.get, reverse=True):
    posicao += 1
    print(f'{" " * 3}{posicao}º lugar: {indice} com {jogadores[indice]}')
    sleep(1)
