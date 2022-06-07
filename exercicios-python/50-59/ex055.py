peso_maior = 0
peso_menor = 0
for c in range(0, 5):
    peso = float(input('Digite o peso: '))
    if c == 0:
        peso_menor = peso
        peso_maior = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < peso_menor:
            peso_menor = peso
print(f'\nO maior peso foi {peso_maior:.1F}'
      f'\nO menor foi {peso_menor:.1F}')
