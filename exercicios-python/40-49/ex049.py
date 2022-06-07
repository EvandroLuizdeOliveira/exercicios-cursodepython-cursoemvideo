#tabuada com for
nu = int(input('Digite um número para ver sua tabuada: '))
print(f'\n{"-" * 12}\n')
for c in range(1, 11):
    print(f'{nu} X {c:2} = {nu * c}')
print(f'\n{"-" * 12}')
