"""
O programa pede uma tupla com várias palavras sem acentos. Mostrando para o usuário cada palavra e quais são as vogais dela
"""
marcas = ('Mitsubishi', 'Toyota', 'Honda', 'Mazda', 'Lexus', 'Datsun', 'Nissan')
vowels = ('aeiou')
for p in marcas:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
