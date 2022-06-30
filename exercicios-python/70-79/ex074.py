from random import randint
nu = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
nu_ordem_crescente = sorted(nu)
print(f'\nOs valores sorteados foram: {nu}\nO maior valor sorteado foi {nu_ordem_crescente[-1]}\nO menor valor foi {nu_ordem_crescente[0]}\n')
