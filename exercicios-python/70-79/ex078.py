"""
O programa vai ler 5 números e guardar em uma lista. Depois vai mostrar qual é o maior e qual o menor e suas posições.
"""
valores = []
for count in range(0, 5):
    valores.append(int(input('Digite um número: ')))
print(f'Você digitou os valores {valores}'
f'\nO maior valor digitado foi {max(valores)} nas posições {valores.index(max(valores))}'
f'\nO menor valor digitado foi {min(valores)} nas posições ')
