print(f'{"-=-"*10}'
      f'\nAnalisador de Triângulos'
      f'\n{"-=-"*10}')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    if a == b == c:
        print('Os segmentos acima \033[32mPODEM\033[m formar um triângulo \033[32mEquilátero\033[m!')
    elif a != b != c:
        print('Os segmentos acima \033[32mPODEM\033[m formar um triângulo \033[32mEscaleno\033[m!')
    else:
        print('Os segmentos acima \033[32mPODEM\033[m formar um triângulo \033[32mIsósceles\033[m!')
else:
    print('Os segmentos acima \033[31mNÃO PODEM\033[m formar um triângulo!')
