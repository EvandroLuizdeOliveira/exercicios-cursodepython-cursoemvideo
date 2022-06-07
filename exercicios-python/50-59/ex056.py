"""
Programa analisa a média da idade do grupo
Fala qual o nome do homem mais velho
Quantas mulheres tem menos de 20 anos
"""
soma_idade = homem_velho = nome_homem = mulher_20 = 0
for c in range(0, 4):
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
    print('\n')
    soma_idade += idade
    if sexo == 'M' and idade > homem_velho:
        nome_homem = nome
        homem_velho = idade
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
print(f'\nA média da idade do grupo é de {soma_idade / 4 :.0F} anos.'
      f'\nO nome do homem mais velho é {nome_homem}.'
      f'\nTem {mulher_20} mulheres com menos de 20 anos.')
