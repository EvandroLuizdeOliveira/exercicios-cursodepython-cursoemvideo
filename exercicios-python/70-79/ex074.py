"""
Programa que gera 5 numeros aleatórios de e coloca em uma tupla. Depois mostra a lista de numeros gerados, o maior número e o menor
-------------------------------------
1 resolução
-----------
from random import randint
nu = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
nu_ordem_crescente = sorted(nu)
print(f'\nOs valores sorteados foram: {nu}\nO maior valor sorteado foi {nu_ordem_crescente[-1]}\nO menor valor foi {nu_ordem_crescente[0]}\n')
"""
from random import randint
nu = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ', end='')
for n in nu:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(nu)}')
print(f'O maior valor sorteado foi {min(nu)}')