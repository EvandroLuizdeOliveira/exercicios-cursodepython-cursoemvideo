"""
Programa Caixa eletrônico
Lê o valor a ser sacado e retorna quantas notas de R$50, R$20, R$10 e R$1 serão entregues.

Resolução 1:

nota_50 = nota_20 = nota_10 = nota_1 = 0
print(f'{"=" * 20}'
      f'\nCAIXA ELETRÔNICO'
      f'\n{"=" * 20}')
valor = int(input('Valor do saque: R$'))
while (valor - 50) >= 0:
      nota_50 += 1
      valor = valor - 50
while (valor - 20) >= 0:
      nota_20 += 1
      valor = valor - 20
while (valor - 10) >= 0:
      nota_10 += 1
      valor = valor - 10
while (valor - 1) >= 0:
      nota_1 += 1
      valor = valor - 1
if nota_50 > 0:
      print(f'{nota_50} notas de R$50')
if nota_20 > 0:
      print(f'{nota_20} notas de R$20')
if nota_10 > 0:
      print(f'{nota_10} notas de R$10')
if nota_1 > 0:
      print(f'{nota_1} notas de R$1')
print(f'{"=" * 20}')
"""

print(f'{"=" * 20}'
      f'\nCAIXA ELETRÔNICO'
      f'\n{"=" * 20}')
valor = int(input('Valor do saque: R$'))
cedula = 50
total_cedula = 0
while True:
      if valor >= cedula:
            valor = valor - cedula
            total_cedula += 1
      else:
            if total_cedula > 0:
                  print(f'{total_cedula} notas de R${cedula}')
            if cedula == 50:
                  cedula = 20
            elif cedula == 20:
                  cedula = 10
            elif cedula == 10:
                  cedula = 1
            total_cedula = 0
            if valor == 0:
                  break
print(f'{"=" * 20}')
