def fatorial(numero, show=False):
    """
    ->Faz o fatorial de um número seguindo parâmetro do usuário.
    Param numero: Número a ser fatorado.
    Param show: Tem como padrão ser False. Quando True mostra o processo de fatoração.
    Return: não.
    """
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
