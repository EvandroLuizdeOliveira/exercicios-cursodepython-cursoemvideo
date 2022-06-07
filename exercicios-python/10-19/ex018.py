from math import sin, cos, tan, radians
an = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {an} tem o SENO de {sin(radians(an)):.2f}'
      f'\nO ângulo de {an} tem o COSSENO de {cos(radians(an)):.2f}'
      f'\nO ângulo de {an} tem a TANGENTE de {tan(radians(an)):.2f}')
