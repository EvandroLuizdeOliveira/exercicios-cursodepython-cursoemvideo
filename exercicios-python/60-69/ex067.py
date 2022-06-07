"""
Programa Tabuada 3.0
"""
while True:
    nu = int(input('Digite um número para ver sua tabuada: '))
    print(f'{"-" * 40}')
    if nu < 0:
        break
    for c in range(1, 11):
        print(f'{nu} X {c:2} = {nu * c}')
    print(f'{"-" * 40}')
print(f'PROGRAMA TABUADA ENCERRADO. Volte sempre!')
