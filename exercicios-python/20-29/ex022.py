nome = input('Digite seu nome completo: ').strip()
e1 = nome.find(" ")
te = nome.count(" ")
ct = len(nome)
print(f'Analisando seu nome...'
      f'\nSeu nome em maiúsculas é {nome.upper()}'
      f'\nSeu nome em minúsculas é {nome.lower()}'
      f'\nSeu nome tem ao todo {ct - te} letras'
      f'\nSeu primeiro nome é {nome[:e1]} e ele tem {e1} letras')
