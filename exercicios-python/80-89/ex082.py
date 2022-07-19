"""
O programa lê vários números e coloca em uma lista. Depois disso ele separa os números em uma lista par e uma lista ímpar e ao final mostra as três listas. 
"""
lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
for num in range(0, len(lista)):
    if lista[num] % 2 == 0:
        par.append(lista[num])
    else:
        impar.append(lista[num])
print(f'{"-=-" * 20}'
      f'\nA lista completa é {lista}'
      f'\nA lista de pares é {par}'
      f'\nA lista de ímpares é {impar}')
