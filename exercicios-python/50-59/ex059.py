"""
calculadora
"""
from time import sleep
fim = 0
fim_menu = 0
numeros = 0
menu = 0
primeiro_numero = 0
segundo_numero = 0
while fim != 1:
    if numeros == 0:
        primeiro_numero = float(input('Digite um número: '))
        segundo_numero = float(input('Digite outro número: '))
        numeros += 1
    while fim_menu == 0:
        menu = int(input('\nEscolha uma opção:'
                         '\n[ 1 ] Somar'
                         '\n[ 2 ] Multiplicar'
                         '\n[ 3 ] Maior'
                         '\n[ 4 ] Novos números'
                         '\n[ 5 ] Sair do programa\n\n'))
        if 0 < menu < 6:
            fim_menu += 1
        else:
            print('\nOpção inválida!')
    if menu == 1:
        print(f'\nA soma de {primeiro_numero} com {segundo_numero} é {primeiro_numero + segundo_numero}\n')
        fim_menu -= 1
    elif menu == 2:
        print(f'\nA multiplicação de {primeiro_numero} por {segundo_numero} é {primeiro_numero * segundo_numero}\n')
        fim_menu -= 1
    elif menu == 3:
        if primeiro_numero > segundo_numero:
            print(f'\nO número {primeiro_numero} é maior que o número {segundo_numero}\n')
        elif primeiro_numero < segundo_numero:
            print(f'\nO número {segundo_numero} é maior que o número {primeiro_numero}\n')
        else:
            print('\nOs números são iguais!\n')
        fim_menu -= 1
        fim = 0
    elif menu == 4:
        numeros -= 1
        print('\n')
        fim_menu -= 1
        fim = 0
    elif menu == 5:
        print('\nEncerrando programa...')
        sleep(2)
        fim += 1
    print('=-=' * 10)
