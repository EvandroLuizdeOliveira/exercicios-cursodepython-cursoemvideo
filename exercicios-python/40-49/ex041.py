from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))
date = date.today()
ano = date.strftime('%Y')
idade = (int(ano) - nasc)
if idade < 10:
    print('MIRIM')
elif 9 < idade < 15:
    print('INFANTIL')
elif 14 < idade < 20:
    print('JUNIOR')
elif 19 < idade < 26:
    print('SÊNIOR')
else:
    print('MASTER')
