#ler 6 números e somar somente os pares
resultado = 0
cont = 0
for c in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        resultado += numero
        cont += 1
print(f'Você informou {cont} números e a soma foi {resultado}.')
