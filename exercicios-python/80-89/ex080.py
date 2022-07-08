"""
O exercício pede um programa onde o usuário poss digitar cinco valores numéricos, estes serão cadastrados em uma lista já na posição correta de inserção (sem usar sort()). No final mostra a lista ordenada na tela.
"""
valores =[]
valores.append(int(input('Digite um número: ')))
for cont in range (0,4):
    num = int(input('Digite um número: '))
    if num >= max(valores):
        valores.insert(5, num)
    elif num <= min(valores):
        valores.insert(0, num)
    else:
        valores.insert(3, num)
print(valores)