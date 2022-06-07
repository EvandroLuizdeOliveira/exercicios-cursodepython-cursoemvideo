x = float(input('Digite uma medida em metros: '))
print(f'A medida {x:.1F}m corresponde a:'
      f'\n{x/1000}km'
      f'\n{x/100}hm'
      f'\n{x/10}dam'
      f'\n{x*10:.0F}dm'
      f'\n{x*100:.0F}cm'
      f'\n{x*1000:.0F}mm')
