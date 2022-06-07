#digitar o primeiro termo e a razão e obter os 10 primeiros números de uma razão aritimética
print(f'{"=" * 25}'
      f'\n{" " * 3}10 TERMOS DE UMA PA'
      f'\n{"=" * 25}')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo_termo, razao):
    print(c, end=' -> ')
print('FIM')
