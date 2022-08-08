"""
Programa lê nome e peso de várias pessoas e guarda tudo em uma lista. No final mostra quantas pessoas foram cadastradas, uma listagem com as pessoas mais pesadas e uma listagem com as pessoas mais leves.
"""
pessoas = []
dados = []
contador = 0
while True:
    dados.append(str(input('Digite o nome: ')).strip())
    dados.append(int(input('Digite o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    contador += 1
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'{contador} pessoas foram cadastradas!')
