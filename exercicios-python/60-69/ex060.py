"""
Programa que resolve fatorial

Resolução 1:

numero = int(input('Digite um número: '))
resultado = numero
while numero != 1:
    conta = (resultado * (numero - 1))
    resultado = conta
    numero -= 1
print(f'O fatorial de {numero} é {resultado}.')

Resolução 2:

from math import factorial
numero = int(input('Digite um número: '))
resultado = factorial(numero)
contador = numero
while contador > 0:
    print(contador,  end='')
    print(' x ' if contador > 1 else ' = ', end='')
    contador -= 1
print(resultado, end='')
"""
numero = int(input('Digite um número: '))
resultado = 1
contador = numero
print(f'Calculando {numero}! = ', end='')
while contador > 0:
    print(contador,  end='')
    print(' x ' if contador > 1 else ' = ', end='')
    resultado *= contador
    contador -= 1
print(resultado, end='')
