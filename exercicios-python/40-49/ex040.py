nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = ((nota1 + nota2) / 2)
print(f'\nTirando {nota1:.1F} e {nota2:.1F}, a média do aluno é {media:.1F}')
if media < 5:
    print('\nO aluno está REPROVADO!')
#elif media > 4.9 and media < 7:
elif 7 > media > 4.9:
    print('\nO aluno está em RECUPERAÇÃO!')
else:
    print('\nO aluno está APROVADO!')
