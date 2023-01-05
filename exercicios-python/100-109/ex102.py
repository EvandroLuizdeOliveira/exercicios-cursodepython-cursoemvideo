def fatorial(numero, show=False):
    num = 1
    for c in range(numero,0,-1):
        if show == True:
            if c > 1:
                print(f'{c}',end=" X ")
            elif c == 1:
                print(f'{c}',end=" = ")
        num *= c
    print(num)


#Programa principal
fatorial(5,show=True)
