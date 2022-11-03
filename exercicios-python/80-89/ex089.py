alunos = []
temp = []
while True:
        temp.append(input('Digite o nome do aluno: '))
        temp.append(float(input('Digite a primeira nota: ')))
        temp.append(float(input('Digite a segunda nota: ')))
        alunos.append(temp[:])
        temp.clear()
        continuar = str(input('Deseja continuar? ')).strip().upper()[0]
        while continuar not in 'SN':
            continuar = str(input('Deseja continuar? ')).strip().upper()[0]
        if continuar == 'N':
            break
print(alunos)
