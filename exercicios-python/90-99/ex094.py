formulario = list()
mulheres = list()
acima = list()
pessoa = dict()
soma_idade = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    formulario.append(pessoa.copy())
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar not in 'Ss':
        break
print(f'{"=-=" * 30}')
print(f'- O grupo tem {len(formulario)} pessoas.')
for contador1 in formulario:
    soma_idade += contador1['idade']
    if contador1['sexo'] in 'Ff':
        mulheres.append(contador1['nome'])
media_idade = soma_idade / len(formulario)
print(f'- A média de idades é de {media_idade:.2F} anos.'
      f'\n- As mulheres cadastradas foram:', end=' ')
for contador3 in mulheres:
    print(f'{contador3}', end=' ')
print()
for contador2 in formulario:
    if contador2['idade'] > media_idade:
        acima.append(contador2)
print(f'- Lista das pessoas que estão acima da média:')
for contador4 in acima:
    print('\n')
    for k, v in contador4.items():
        print(f'{k} = {v}', end='; ')
    print()
print('<< ENCERRADO>>')
