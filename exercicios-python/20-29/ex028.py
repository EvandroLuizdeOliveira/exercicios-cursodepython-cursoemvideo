from time import sleep
from random import randint
nr = randint(0, 5)
print(f'{"-="*20}'
      f'\nVou pensar em um número entre 0 e 5. tente adivinhar...'
      f'\n{"-="*20}')
num = int(input('Em que número eu pensei? '))
if 5 <= num >= 0:
    if num != nr:
        print('PROCESSANDO...')
        sleep(5)
        print(f'GANHEI! Eu pensei no número {nr} e não no {num}!')
    else:
        print('PROCESSANDO...')
        sleep(5)
        print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Número inválido!')
