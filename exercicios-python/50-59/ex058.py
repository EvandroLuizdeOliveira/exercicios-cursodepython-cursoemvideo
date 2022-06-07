"""
jogo de adivinhação numérica
"""
from time import sleep
from random import randint
nr = randint(0, 10)
acertou = False
cont = 1
print(f'{"-=-"*18}'
      f'\nVou pensar em um número entre 0 e 10. Tente adivinhar!'
      f'\n{"-=-"*18}')
while not acertou:
    num = int(input('\nEm que número eu pensei? '))
    print('\nPROCESSANDO...')
    sleep(2)
    if 11 > num >= 0:
        if num == nr:
            acertou = True
        else:
            if num > nr:
                print(f'\n\033[34mUm pouco menos!\033[m')
            else:
                print(f'\n\033[34mUm pouco mais!\033[m')
            cont += 1
    else:
        print('\n\033[31mOpção inválida!\033[m')
if cont == 1:
    print(f'\n\033[32mPARABÉNS! Você conseguiu me vencer em {cont} tentativa!\033[m')
else:
    print(f'\n\033[32mPARABÉNS! Você conseguiu me vencer em {cont} tentativas!\033[m')
