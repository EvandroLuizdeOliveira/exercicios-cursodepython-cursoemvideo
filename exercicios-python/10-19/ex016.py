from math import trunc
val = float(input('Digite um valor: '))
print(f'O valor digitado foi {val} e a sua porção inteira é {trunc(val)}')
#também poderia ser resolvido usando {val:.0F} ao invés de {trunc(val)}