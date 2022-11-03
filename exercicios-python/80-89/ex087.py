matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
soma_pares = soma_terceira_coluna = maior_segunda_linha = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um val or para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]
        if linha == 1:
            if matriz[linha][coluna] > maior_segunda_linha:
                maior_segunda_linha = matriz[linha][coluna]
print(f'{"=-=" * 12}')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'{"=-=" * 12}'
      f'\nA soma dos valores pares é {soma_pares}'
      f'\nA soma dos valores da terceira coluna é {soma_terceira_coluna}'
      f'\nO maior valor da segunda linha é {maior_segunda_linha}')
