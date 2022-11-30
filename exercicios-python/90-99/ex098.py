from time import sleep


def contador(ini, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'{"=-=" * 15}')
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    sleep(2.5)
    if ini > fim and passo > 0:
        while ini >= fim:
            print(f'{ini}', end=' ', flush=True)
            sleep(0.5)
            ini -= passo
        print("FIM!")
    elif ini < fim and passo > 0:
        while ini <= fim:
            print(f'{ini}', end=' ', flush=True)
            sleep(0.5)
            ini += passo
        print("FIM!")


# Programa principal
contador(1,10,1)
contador(10,0,2)
print(f'{"=-=" * 15}'
      f'\nAgora é sua vez de personalizar contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
