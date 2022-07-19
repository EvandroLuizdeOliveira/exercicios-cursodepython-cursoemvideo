"""
O exercício pede um programa onde o usuário poss digitar cinco valores numéricos, estes serão cadastrados em uma lista já na posição correta de inserção (sem usar sort()). No final mostra a lista ordenada na tela.
"""
valores = []
for cont in range (0,5):
    num = int(input('Digite um número: '))
    if cont == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na pos {pos} da lista...')
                break
            pos += 1
print(f'{"=-=" * 20}'
      f'\nOs valores digitados em ordem foram {valores}')
