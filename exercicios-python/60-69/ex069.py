"""
Programa analisa quantas pessoas tem mais de 18 anos
Quantos homens foram cadastrados
Quantas mulheres tem menos de 20 anos
"""
contador_18 = contador_m = contador_f20 = 0
while True:
    print(f'{"-" * 30}'
          f'\n{" " * 5}CADASTRE UMA PESSOA'
          f'\n{"-" * 30}')
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo: [F/M] ')).upper().strip()[0]
    print(f'{"-" * 30}')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if idade > 18:
        contador_18 += 1
    if sexo == 'M':
        contador_m += 1
    if sexo == 'F' and idade < 20:
        contador_f20 += 1
    if continuar == 'N':
        break
print(f'{"=" * 8} FIM DO PROGRAMA {"=" * 8}'
      f'\n{contador_18} pessoas tem mais de 18 anos.'
      f'\n{contador_m} pessoas cadastradas são Homens.'
      f'\n{contador_f20} mulheres tem menos de 20 anos.')
