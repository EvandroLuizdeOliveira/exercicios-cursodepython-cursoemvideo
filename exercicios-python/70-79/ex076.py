listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livros', 34.9)
print(f'{40 * "-"}\n{10 * " "}LISTAGEM DE PREÇOS\n{40 * "-"}')
for produto in range(0, len(listagem), 2):
    produto_preco = produto + 1
    preco = int(listagem[(produto+1)])
    print(f'{listagem[produto]}{(30 - (len(listagem[produto]))) * "."}R$ {(3 - (len(str(preco)))) * " "}{listagem[(produto+1)]:3.2F}')
print(f'{40 * "-"}')
