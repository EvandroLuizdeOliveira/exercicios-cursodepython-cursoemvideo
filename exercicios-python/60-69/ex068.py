"""
Par ou ímpar
"""
from random import randint
contador = mostrar = 0
print(f'{"=-=" * 10}'
      f'\nVAMOS JOGAR PAR OU ÍMPAR'
      f'\n{"=-=" * 10}')
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    base = str(input('Par ou ímpar? [P/I]  ')).strip().upper()[0]
    while base not in 'PI':
        base = str(input('Par ou ímpar? [P/I]  ')).strip().upper()[0]
    soma = jogador + computador
    resultado = soma % 2
    if resultado != 0:
        resultado = 'I'
        mostrar = 'Ímpar'
    elif resultado == 0:
        resultado = 'P'
        mostrar = 'Par'
    print(f'{"-" * 30}'
          f'\nVocê jogou {jogador} e o computador {computador}. Total de {soma} DEU {mostrar}'
          f'\n{"-" * 30}')
    if resultado != base:
        break
    contador += 1
    print(f'Você VENCEU!'
          f'\nVamos jogar novamente...'
          f'\n{"=-=" * 10}')
print(f'Você PERDEU!'
      f'\n{"=-=" * 10}'
      f'\nGAME OVER! Você venceu {contador} vezes.')
