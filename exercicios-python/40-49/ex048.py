#Soma entre todos os números impares que são  múltiplos de 3 de 1 a 500
resultado = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        resultado += c
        cont += 1
print(f'A soma dos {cont} números é {resultado}')
