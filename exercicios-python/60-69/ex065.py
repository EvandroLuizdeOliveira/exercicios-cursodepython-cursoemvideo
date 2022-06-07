"""
Programa le vários números inteiros e no final mostra a média entre todos
Qual foi o maior número e o menor
Também pergunta se o usuário deseja ou não continuar

Resolução 1:

ciclo = 0
cont = 0
soma = 0
menor = 0
maior = 0
while ciclo == 0:
    if cont == 0:
        numero = int(input('Digite um número: '))
        if cont == 0:
            menor = numero
            maior = numero
        cont += 1
        soma += numero
    elif cont > 0:
        ciclo = int(input('\nDeseja continuar?'
                          '\n[0] SIM'
                          '\n[1] NÃO\n'))
        if ciclo == 0:
            numero = int(input('\nDigite um número: '))
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
            cont += 1
            soma += numero
        else:
            print(f'\nA média dos números digitados é {soma / cont:.1F}'
                  f'\nO maior número é {maior}'
                  f'\nO menor número é {menor}')

Resolução 2:

contador = continuar = soma = 0
while continuar == 0:
    numero = int(input('Digite um número [999 para parar]: '))
    menor = maior = numero
    while numero != 999:
        soma += numero
        contador += 1
        while numero < menor:
            menor = numero
        while numero > maior:
            maior = numero
        numero = int(input('Digite um número [999 para parar]: '))
    media = soma / contador
    print(f'A média dos números digitados foi {media} o maior número foi {maior} e o menor foi {menor}')
    continuar = int(input('\nDeseja continuar?'
                          '\n[ 0 ] SIM'
                          '\n[ 1 ] NÃO\n'))
    soma = contador = 0
"""

contador = soma = flag = menor = maior = 0
continuar = 'S'
while continuar in 'Ss':
    numero = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    while flag == 0:
        menor = maior = numero
        flag += 1
    while numero > maior:
        maior = numero
    while numero < menor:
        menor = numero
    soma += numero
    contador += 1
media = soma / contador
print(f'Foram digitados {contador} números e a média entre eles foi {media:.2F}'
      f'\nO maior número foi {maior} e o menor foi {menor}')
