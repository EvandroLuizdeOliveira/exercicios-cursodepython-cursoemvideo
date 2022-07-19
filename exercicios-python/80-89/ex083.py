"""
Um programa que lê uma expressão matemática que use parênteses digitada pelo usuário e analisa se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
expressao = str(input('Digite uma expressão: ')).strip()
pilha = []
for caractere in expressao:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')
