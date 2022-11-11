from datetime import date
pessoas = dict()
pessoas['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
today = date.today()
year = today.year
pessoas['idade'] = year - ano
pessoas['ctps'] = int(input('CTPS: [Caso não tenha digite 0] '))
if pessoas['ctps'] != 0:
    pessoas['contratação'] = int(input('Ano de contratação: '))
    pessoas['salário'] = float(input('Salário: R$'))
    aposentadoria = year - pessoas['contratação']
    if aposentadoria >= 60:
        pessoas['aposentadoria'] = 'Aposentado'
    else:
        pessoas['aposentadoria'] = aposentadoria
print(f'{"-=-" * 30}'
      f'\n{pessoas}')
for indice, key in pessoas.items():
    print(f'{indice} tem o valor {key}')
