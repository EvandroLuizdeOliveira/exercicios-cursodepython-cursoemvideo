"""
Um programa que lê uma expressão matemática que use parênteses digitada pelo usuário e analisa se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
expressao = str(input('Digite uma expressão: ')).strip()
expressao = list(expressao)
if expressao.count('(') == expressao.count(')'):
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')
