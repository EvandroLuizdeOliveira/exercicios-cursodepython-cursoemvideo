"""
O programa vai ler 5 números e guardar em uma lista. Depois vai mostrar qual é o maior e qual o menor e suas posições.
"""
valores = []
for count in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {count}: ')))
print(f'{"=-=" * 20}'
      f'\nVocê digitou os valores {valores}'
      f'\nO maior valor digitado foi {max(valores)} nas posições', end=' ')
for c, v in enumerate(valores):
        if v == max(valores):
            print(f'{c}', end='... ')
print(f'\nO menor valor digitado foi {min(valores)} nas posições', end=' ')
for c, v in enumerate(valores):
        if v == min(valores):
            print(f'{c}', end='... ')
