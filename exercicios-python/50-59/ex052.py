#descobrir se um número é primo
resultado = 0
numero = int(input('Digite um número: '))
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[32m', end='')
        resultado += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\n\n\033[mO número é divisível por {resultado} números!')
if resultado == 2:
    print(f'\033[32m\nE por isso é primo!\033[m')
else:
    print(f'\033[31m\nE por isso não é primo!\033[m')
