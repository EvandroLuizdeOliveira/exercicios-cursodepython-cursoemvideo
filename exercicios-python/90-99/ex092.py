from datetime import date
pessoas = dict()
pessoas['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
pessoas['idade'] = date.today().year - ano
pessoas['ctps'] = int(input('CTPS: [Caso não tenha digite 0] '))
if pessoas['ctps'] != 0:
    pessoas['contratação'] = int(input('Ano de contratação: '))
    pessoas['salário'] = float(input('Salário: R$'))
    pessoas['aposentadoria'] = pessoas['idade'] + ((pessoas['contratação'] + 35) - date.today().year)
print(f'{"-=-" * 30}')
for indice, key in pessoas.items():
    print(f' - {indice} tem o valor {key}')
