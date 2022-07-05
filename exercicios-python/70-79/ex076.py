"""
O programa pede uma tupla única com nome de produtos e seus preços na sequencia. Depois que o programa mostre para o usuário a lista de produtos e preços organizada e alinhada de forma tabular
---------------------------------
Outra resolução utilizando if dentro do for
-------------------
for pos in range(0, len(listagem))
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}', end='')

"""
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livros', 34.9)
print(f'{40 * "-"}'
f'\n{"LISTAGEM DE PREÇOS":^40}'
f'\n{40 * "-"}')
for produto in range(0, len(listagem), 2):
    print(f'{listagem[produto]:.<30}R${listagem[(produto+1)]:>7.2F}')
print(f'{40 * "-"}')
