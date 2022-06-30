num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite outro número: '))
num4 = int(input('Digite outro número: '))
numeros = (num1, num2, num3, num4)
if 3 in numeros:
    resultado = f'O número 3 foi digitado primeiro na posição {(numeros.index(3))+1}'
else:
    resultado = f'O número 3 não foi digitado'
print(f'\nO número 9 apareceu {numeros.count(9)} vezes\n{resultado}\nOs valores pares digitados foram', end=' ')
for par in range(0, len(numeros)):
    if par % 2 == 0:
        print(numeros[par], end=' ')
print('\n')