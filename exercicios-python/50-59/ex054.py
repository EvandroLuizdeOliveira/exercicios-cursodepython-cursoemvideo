#ler data de nascimento e mostrar quantas pessoas já são maiores e idade
from datetime import date
ano = date.today().year
maiores = 0
menores = 0
for c in range(0, 7):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = (int(ano) - nasc)
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
if maiores == 1:
    print(f'\nDas 7 pessoas analisadas {maiores} é maior e {menores} são menores de idade.')
elif menores == 1:
    print(f'\nDas 7 pessoas analisadas {maiores} são maiores e {menores} é menor de idade.')
elif menores == 0:
    print(f'\nDas {maiores} pessoas analisadas todas são maiores.')
elif maiores == 0:
    print(f'\nDas {menores} pessoas analisadas todas são menores.')
else:
    print(f'\nDas 7 pessoas analisadas {maiores} são maiores e {menores} são menores de idade.')
