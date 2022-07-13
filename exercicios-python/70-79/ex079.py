"""
Exercício pede que o usuário consiga digitar vários números e cadastre-os em uma lista. Caso o número já exista na lista ele não é adicionado novamente. No final o programa deve mostrar todos os valores únicos digitados em ordem crescente.
"""
valores = []
while True:
    num = int(input('Digite um valor: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'{"-=-" * 20}'
      f'\nVocê digitou os valores {sorted(valores)}')
