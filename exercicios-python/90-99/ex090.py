alunos = dict()
alunos['Nome'] = str(input('Nome: '))
alunos['Média'] = float(input(f'Média de {alunos["Nome"]}: '))
if alunos['Média'] >= 7:
    alunos['Situação'] = 'Aprovado'
else:
    alunos['Situação'] = 'Reprovado'
for key, value in alunos.items():
    print(f'{key} é igual a {value}')
