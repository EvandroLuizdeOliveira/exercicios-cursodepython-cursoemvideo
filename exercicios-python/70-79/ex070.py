"""
Programa lê nome do produto e o preço
Retorna quanto foi gasto no total, quantos produtos ultrapassaram o valor de R$1000,00
e retorna o nome e o preço do produto mais barato
"""
contador_total = contador_1000 = menor_preco = contador = 0
nome = ' '
print(f'{"-" * 30}'
      f'\n{" " * 8}LOJA OLIVEIRA'
      f'\n{"-" * 30}')
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    contador += 1
    contador_total += preco
    if contador == 1 or preco < menor_preco:
        nome = produto
        menor_preco = preco
    if preco > 1000:
        contador_1000 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\nDeseja continuar? [S/N] ')).upper().strip()[0]
        print('\n')
    if continuar == 'N':
        break
print(f'{"-" * 15} FIM DO PROGRAMA {"-" * 15}'
      f'\nO total gasto na compra foi R${contador_total:.2F}'
      f'\nTemos {contador_1000} produtos acima de R$1000,00'
      f'\nO produto mais barato foi o {nome} que custa R${menor_preco:.2F}')
