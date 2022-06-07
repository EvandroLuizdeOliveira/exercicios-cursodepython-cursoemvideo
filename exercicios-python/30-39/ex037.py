num = int(input('Digite um número inteiro: '))
esc = int(input(f'\nEscolha uma opção:'
      f'\n[1] Para Binário'
      f'\n[2] Para Octal'
      f'\n[3] Para Hexadecimal\n\n'))
res2 = []
if esc == 1:
    while num >= 2:
        res1 = int(num % 2)
        num = int(num / 2)
        res2.append(res1)
    res2.append(num)
    res2.reverse()
    print('\n')
    print(*res2)
elif esc == 2:
    while num >= 8:
        res1 = int(num % 8)
        num = int(num / 8)
        res2.append(res1)
    res2.append(num)
    res2.reverse()
    print('\n')
    print(*res2)
elif esc == 3:
    while num >= 16:
        res1 = int(num % 16)
        num = int(num / 16)
        res2.append(res1)
    res2.append(num)
    for index, value in enumerate(res2):
        if value == 10:
            res2[index] = 'a'
        elif value == 11:
            res2[index] = 'b'
        elif value == 12:
            res2[index] = 'c'
        elif value == 13:
            res2[index] = 'd'
        elif value == 14:
            res2[index] = 'e'
        elif value == 15:
            res2[index] = 'f'
    res2.reverse()
    print('\n')
    print(*res2)
else:
    print('\n')
    print('Opção inválida!')
