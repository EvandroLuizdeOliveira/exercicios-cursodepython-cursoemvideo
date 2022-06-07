"""
Melhoria do ex061 perguntando ao usuário  se ele quer mostrar mais termos
Encerra quando o usuário digita que quer mostrar mais 0 termos

Resolução 1:

print(f'{"=" * 25}'
      f'\n{" " * 3}10 TERMOS DE UMA PA'
      f'\n{"=" * 25}')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
resultado = 0
continuar = 1
termo = 0
termo_final = 0
while continuar == 1:
    if termo == 0:
        termo = int(input('\nDigite quantos termos deseja mostrar: '))
        termo_final = primeiro_termo + (termo - 1) * razao
    if termo == 0:
        continuar = 0
    if continuar == 1:
        while resultado != termo_final:
            if resultado == 0:
                print(primeiro_termo, end=' ')
                resultado = primeiro_termo
            else:
                resultado += razao
                print(resultado, end=' ')
        primeiro_termo = resultado + razao
        resultado = 0
        termo = 0
print('FIM', end=' ')

Resolução 2:

print(f'{"=" * 25}'
      f'\n{" " * 3}10 TERMOS DE UMA PA'
      f'\n{"=" * 25}')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termos = int(input('Digite quantos termos deseja ver: '))
resultado = primeiro_termo
contador = 1
while contador <= termos:
    print(resultado, ' → ' if contador < termos else ' → PAUSA', end='')
    contador += 1
    resultado += razao
    if contador > termos:
        termos += int(input('\n\nDeseja ver mais quantos termos? '))
print(f'Progressão finalizada com {termos} termos mostrados.')
"""

print(f'{"=" * 25}'
      f'\n{" " * 3}10 TERMOS DE UMA PA'
      f'\n{"=" * 25}')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
resultado = primeiro_termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(resultado, end=' → ')
        contador += 1
        resultado += razao
    print('PAUSA')
    mais = int(input('\nQuantos termos você quer mostrar a mais?'))
print(f'Progressão finalizada com {total} termos mostrados.')
