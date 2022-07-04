numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print('\n')
continuar = 's'
while continuar in 'sS':
    while True:
        numero_escolhido = int(input('Digite um número de 0 e 20: '))
        if 0 <= numero_escolhido <= 20:
            break
        print('Tente Novamente!', end=' ')
    print(f'Você digitou o número {numeros[numero_escolhido]}\n')
    continuar = input('Deseja continuar? [S/N]').strip()[0]
