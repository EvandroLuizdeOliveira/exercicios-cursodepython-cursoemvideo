
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livros', 34.9)
for produto in range(0, len(listagem), 2):
    letras = int(len(listagem[produto]))
    letras_1 = letras - 40
    print(f'\n{listagem[produto]}{letras_1 * "-"}{listagem[(produto+1)]}')
