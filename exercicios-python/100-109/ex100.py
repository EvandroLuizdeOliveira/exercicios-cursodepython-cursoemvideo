from random import randint
from time import sleep


def sorteia():
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        lista.append(randint(0,10))
        print(f'{lista[c]}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar():
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores {lista}, temos {soma}')


# Programa principal
lista = list()
sorteia()
somaPar()