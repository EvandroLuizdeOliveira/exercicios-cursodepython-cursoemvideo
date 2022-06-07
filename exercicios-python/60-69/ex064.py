"""
programa que lê números inteiros até o usuário digitar 999
Mostra quantos números foram digitados e a soma dos números excluindo o gatilho de parada

Resolução 1:

ciclo = 0
cont = 0
soma = 0
while ciclo == 0:
    numero = int(input('Digite um número: '))
    if numero == 999:
        ciclo = 1
        print(f'\nA soma dos números digitados é {soma}'
              f'\nForam contados {cont} números'
              f'\nFIM')
    else:
        cont += 1
        soma += numero
"""

cont = soma = 0
numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um número [999 para parar]: '))
print(f'Foram digitados {cont} números e a soma entre eles foi {soma}.')
