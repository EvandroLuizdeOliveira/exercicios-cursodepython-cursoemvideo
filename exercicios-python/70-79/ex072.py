numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print('\n')
numero_escolhido = int(input('Digite um número de 0 e 20: '))
while True:
    if numero_escolhido <= 20 and numero_escolhido >= 0:
        break
    else:
        numero_escolhido = int(input('Tente novamente! Digite um número de 0 e 20: '))
print(f'Você digitou o número {numeros[numero_escolhido]}\n')
