def voto(a):
    """
    ->Função verifica através do input do usuário a condição do voto do mesmo: NEGADO, OPCIONAL ou OBRIGATÓRIO.
    Parametro a : ano de nascimento
    retorno: Não
    """
    from datetime import date
    s = (date.today().year) - a
    print(f'Com {s} anos: VOTO',end=" ")
    if 15 < s < 18 or s > 69:
        s = 'OPCIONAL!'
    elif 17 < s < 70:
        s = 'OBRIGATÓRIO!'
    else:
        s = 'NEGADO!'
    return s


#Programa principal
ano_nascimento = int(input('Em que ano você nasceu? '))
resultado = voto(ano_nascimento)
print(f'{resultado}')
