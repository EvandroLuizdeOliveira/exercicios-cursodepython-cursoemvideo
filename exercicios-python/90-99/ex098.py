from time import sleep
def contador(ini, fim, passo):
    print(f'{"=-=" * 15}')
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    if ini > fim and passo > 0:
        while ini >= fim:
            sleep(1)
            print(f'{ini}', end=' ')
            ini -= passo
        print("FIM!")
    elif ini < fim and passo > 0:
        while ini <= fim:
            sleep(1)
            print(f'{ini}', end=' ')
            ini += passo
        print("FIM!")


contador(1,10,1)
contador(10,0,2)
print(f'{"=-=" * 15}'
      f'\nAgora é sua vez de personalizar contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
