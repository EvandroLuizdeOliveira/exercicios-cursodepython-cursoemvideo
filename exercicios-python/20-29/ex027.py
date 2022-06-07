nome = input('Digite seu nome completo: ').strip()
lista = nome.split()
print(f'Muito prazer em te conhecer!'
      f'\nSeu primeiro nome é {lista[0]}'
      f'\nSeu último nome é {lista[-1]}')
