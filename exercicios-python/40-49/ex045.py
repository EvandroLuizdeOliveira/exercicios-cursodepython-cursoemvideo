from time import sleep
from random import randint
aleatorio = randint(1, 3)
true_opcoes = 0
true_game = 0
continuar = 0
while true_opcoes == 0:
    opcoes = int(input('Escolha uma opção:\n'
                  '[1] PEDRA\n'
                  '[2] PAPEL\n'
                  '[3] TESOURA\n\n'))
    if 0 < opcoes < 4:
        true_opcoes = 1
    else:
        print('\n\033[31mOpção indisponível!\033[m')
print('\nE o resultado é:\n')
sleep(2)
if aleatorio == opcoes:
    print('\n\033[33mEMPATE!\033[m')
elif opcoes == 1 and aleatorio == 2:
    print(f'\n\033[31mVocê perdeu!\033[m')
elif opcoes == 2 and aleatorio == 3:
    print('\n\033[31mVocê perdeu!\033[m')
elif opcoes == 3 and aleatorio == 1:
    print('\n\033[31mVocê perdeu!\033[m')
else:
    print('\n\033[32mVocê ganhou!\033[m')
jkp = [0, 'PEDRA', 'PAPEL', 'TESOURA']
print('\n')
print(jkp[aleatorio])
print(jkp[opcoes])

