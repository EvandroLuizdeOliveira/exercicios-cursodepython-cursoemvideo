alunos = dict()
alunos['Nome'] = str(input('Nome: '))
alunos['Média'] = float(input(f'Média de {alunos["Nome"]}: '))
if alunos['Média'] >= 7:
    alunos['Situação'] = 'Aprovado'
elif 5<= alunos['Média'] < 7:
    alunos['Situação'] = 'Recuperação'
else:
    alunos['Situação'] = 'Reprovado'
print(f'{"-=-" * 15}')
for key, value in alunos.items():
    print(f'{key} é igual a {value}')
