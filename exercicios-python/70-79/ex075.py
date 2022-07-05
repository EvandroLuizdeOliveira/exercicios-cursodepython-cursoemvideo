"""
O programa lê 4 valores digitados pelo usuário e os armazena em uma tupla. Depois mostra para o usuário quantas vezes o número 9 apareceu, em que posição foi digitado o número 3 também avisando caso ele não tenha sido digitado e quais foram os números pares.
"""
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
numeros = (num1, num2, num3, num4)
if 3 in numeros:
    resultado = f'O número 3 foi digitado primeiro na posição {(numeros.index(3))+1}'
else:
    resultado = f'O número 3 não foi digitado'
print(f'\nVocê digitou os valores {numeros}\nO número 9 apareceu {numeros.count(9)} vezes\n{resultado}\nOs valores pares digitados foram', end=' ')
for par in range(0, len(numeros)):
    if par % 2 == 0:
        print(numeros[par], end=' ')
print('\n')