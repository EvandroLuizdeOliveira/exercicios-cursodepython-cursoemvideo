"""
Programa lê nome e peso de várias pessoas e guarda tudo em uma lista. No final mostra quantas pessoas foram cadastradas, uma listagem com as pessoas mais pesadas e uma listagem com as pessoas mais leves.
"""
pessoas = []
dados = []
maiores = []
menores = []
contador = maior = menor = 0
while True:
    dados.append(str(input('Digite o nome: ')).strip())
    dados.append(int(input('Digite o peso: ')))
    pessoas.append(dados[:])
    if contador == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
            maiores.append(dados[0])
        if dados[1] < menor:
            menor = dados[1]
            menores.append(dados[0])
    dados.clear()
    contador += 1
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'{contador} pessoas foram cadastradas!'
      f'\n{maior} {maiores}'
      f'\n{menor} {menores}')
