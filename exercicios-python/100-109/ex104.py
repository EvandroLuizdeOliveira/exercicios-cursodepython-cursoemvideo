def leiaint(n='n'):
    while True:
        s = input(f'{n}')
        if s in '0123456789':
            int(s)
            return s
            break
        else:
            print('ERRO! Digite um número inteiro')


#Programa principal
arg = leiaint('Digite um número: ')
print(arg)
