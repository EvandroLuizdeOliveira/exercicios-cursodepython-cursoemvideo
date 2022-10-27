"""
Programa lê nome e peso de várias pessoas e guarda tudo em uma lista. No final mostra quantas pessoas foram cadastradas, uma listagem com as pessoas mais pesadas e uma listagem com as pessoas mais leves.
"""
temporario = []
dados = []
oas_leves = []
while True:
    temporario.append(str(input('Digite o nome: ')).strip())
    temporario.append(float(input('Digite o peso: ')))
    dados.append(temporario[:])
    temporario.clear()
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if continuar == "S" or continuar == "N":
            break
    if continuar == 'N':
        break
print(f'{"=-=" * 20}'
      f'\n{len(dados)} pessoas foram cadastradas!')
print(f'O maior peso foi de {max(dados)[1]}Kg. Peso de ', end='')
for posicao in dados:
    if posicao[1] == max(dados)[1]:
        print(f'[{posicao[0]}]')
print(f'O menor peso foi de {min(dados)[1]}Kg. Peso de ', end='')
for posicao in dados:
    if posicao[1] == min(dados)[1]:
        print(f'[{posicao[0]}]')
