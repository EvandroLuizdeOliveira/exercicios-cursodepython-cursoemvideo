from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
date = date.today()
ano = date.strftime('%Y')
idade = (int(ano) - nasc)
if idade < 17:
    print(f'\nFaltam {18 - idade} anos para o alistamento')
elif idade == 17:
    print(f'\nFalta {18 - idade} ano para o alistamento')
elif idade == 18:
    print('\nHora de se alistar')
elif idade == 19:
    print(f'\nPassou {idade - 18} ano do tempo do alistamento')
else:
    print(f'\nPassaram-se {idade - 18} anos do tempo do alistamento')