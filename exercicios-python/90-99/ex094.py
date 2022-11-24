formulario = list()
pessoa = dict()
soma_idade = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    formulario.append(pessoa.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if continuar == 'N':
        break
print(f'{"=-=" * 30}')
print(f'- O grupo tem {len(formulario)} pessoas.')
media_idade = soma_idade / len(formulario)
print(f'- A média de idades é de {media_idade:.2F} anos.'
      f'\n- As mulheres cadastradas foram:', end=' ')
for contador3 in formulario:
    if contador3['sexo'] == 'F':
        print(f'{contador3["nome"]}', end=' ')
print()
print(f'- Lista das pessoas que estão acima da média:')
for contador2 in formulario:
    if contador2['idade'] >= media_idade:
        print('    ', end='')
        for k, v in contador2.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
