num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print('\nO PRIMEIRO valor é maior')
elif num2 > num1:
    print('\nO SEGUNDO valor é maior')
elif num1 == num2:
    print('\nNão existe valor maior, os dois são iguais')
