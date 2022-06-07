num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
# Verificando qual número é o menor
if num1 < num2 and num3 > num1:
    print(f'O menor número é {num1}')
elif num2 < num1 and num3 > num2:
    print(f'O menor número é {num2}')
else:
    print(f'O menor número é {num3}')
# Verificando qual número é o maior
if num1 > num2 and num3 < num1:
    print(f'O maior número é {num1}')
elif num2 > num1 and num3 < num2:
    print(f'O maior número é {num2}')
else:
    print(f'O maior número é {num3}')
