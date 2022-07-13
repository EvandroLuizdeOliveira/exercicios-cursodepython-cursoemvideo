"""
Um programa que lê vários números e coloca em uma lista. Depois disso o programa mostra quantos números foram digitados, a lista de valores ordenada de forma decrescente, se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
while True:
    numero = lista.append(int(input('\033[mDigite um valor: \033[30m')))
    continuar = str(input('\033[mQuer continuar? [S/N] \033[30m')).upper().strip()[0]
    if continuar == 'N':
        break
lista.sort(reverse=True)
print(f'\033[m{"-=-" * 20}'
      f'\nVocê digitou {len(lista)} elementos'
      f'\nOs valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O número 5 não faz parte da lista!')
