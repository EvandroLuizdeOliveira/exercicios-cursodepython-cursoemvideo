"""
Um programa que lê uma expressão matemática que use parênteses digitada pelo usuário  e analisa se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
expressao = str(input('Digite uma expressão: ')).strip()
dividido = expressao.split('(')
print(dividido)
print(expressao.count(')'))
print(len(dividido))
