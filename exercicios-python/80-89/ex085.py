numeros = [[], []]
for contador_variaveis in range(0,7):
    valor_digitado = int(input('Digite um número: '))
    if valor_digitado % 2 == 0:
        numeros[0].append(valor_digitado)
    else:
        numeros[1].append(valor_digitado)
numeros[0].sort()
numeros[1].sort()
print(f'{"=-=" * 20}'
      f'\nOs valores pares digitados foram: {numeros[0]}'
      f'\nOs valores ímpares digitados foram: {numeros[1]}')
