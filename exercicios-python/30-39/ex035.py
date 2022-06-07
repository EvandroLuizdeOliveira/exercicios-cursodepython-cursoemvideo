print(f'{"-=-"*10}'
      f'\nAnalisador de Triângulos'
      f'\n{"-=-"*10}')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Os segmentos acima \033[32mPODEM\033[m formar um triângulo!')
else:
    print('Os segmentos acima \033[31mNÃO PODEM\033[m formar um triângulo!')
