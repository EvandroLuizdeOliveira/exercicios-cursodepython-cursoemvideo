from time import sleep


def maior(* num):
    maior_numero = 0
    print(f'{"-=" *25}'
          f'\nAnalisando os valores passados...')
    if len(num) != 0:
        maior_numero = max(num)
        for c in num:
            print(c, end=' ', flush=True)
            sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior_numero}.')


# Programa principal
maior(2,9,5,7,1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
