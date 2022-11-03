from time import sleep
from random import randint
jogos = []
temp = []
print(f'\n{"-" * 42}'
      f'\n{"JOGA NA MEGA SENA":^42}'
      f'\n{"-" * 42}')
numero_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
sleep(1)
print(f'\n{"-=" * 4} SORTEANDO {numero_jogos} JOGOS {"=-" * 4}')
for contador_jogos in range(0, numero_jogos):
    sleep(1)
    for contador_numeros in range(0,6):
        numero = randint(1, 60)
        while numero in temp:
            numero = randint(1, 60)
        temp.append(numero)
    temp.sort()
    jogos.append(temp[:])
    temp.clear()
    print(f'Jogo {contador_jogos + 1}: {jogos[contador_jogos]}')
sleep(1)
print(f'{"-=" * 5} < BOA SORTE! > {"=-" * 5}\n')
