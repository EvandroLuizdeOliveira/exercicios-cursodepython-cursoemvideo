"""
digitar o primeiro termo e a razão e obter os 10 primeiros números de uma razão aritimética

Resolução 1:

print(f'{"=" * 25}'
      f'\n{" " * 3}10 TERMOS DE UMA PA'
      f'\n{"=" * 25}')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
resultado = 0
while resultado != decimo_termo:
      if resultado == 0:
            print(primeiro_termo, end=' ')
            resultado = primeiro_termo
      else:
            resultado += razao
            print(resultado, end=' ')
print('FIM', end=' ')
"""
print(f'{"=" * 25}'
      f'\n{" " * 3}10 TERMOS DE UMA PA'
      f'\n{"=" * 25}')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
resultado = primeiro_termo
contador = 1
while contador <= 10:
      print(resultado, end=' → ')
      contador += 1
      resultado += razao
print('FIM', end=' ')
