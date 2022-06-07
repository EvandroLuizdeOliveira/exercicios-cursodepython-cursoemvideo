frase = input('Digite uma frase: ').strip().lower()
print(f'A letra A aparece {frase.count("a")} vezes na frase.'
      f'\nA primeira letra A apareceu na posição {frase.find("a") + 1}'
      f'\nA última letra A apareceu na posição {frase.rfind("a") + 1}')
