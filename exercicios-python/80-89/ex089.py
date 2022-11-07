ficha = list()
while True:
        nome = str(input('Digite o nome do aluno: ')).strip()
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        media = (nota1 + nota2) / 2
        ficha.append([nome,[nota1, nota2], media])
        continuar = str(input('Deseja continuar? ')).strip().upper()[0]
        while continuar not in 'SN':
            continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'N':
            break
print(f'{"-=-" * 15}'
      f'\n{"No.":<4}{"NOME":<10}{"MÉDIA":>8}'
      f'\n{"-" * 25}')
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}'
          f'{aluno[0]:<10}'
          f'{aluno[2]:>8.1F}')
print(f'{"-" * 30}')
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        print('FINALIZANDO...')
        break
    if aluno >= len(ficha):
        print(f'Aluno não encontrado!'
              f'\n{"-" * 30}')
    else:
        print(f'Notas de {ficha[aluno][0]} são {ficha[aluno][1]}'
              f'\n{"-" * 30}')
print('<<<VOLTE SEMPRE>>>')
