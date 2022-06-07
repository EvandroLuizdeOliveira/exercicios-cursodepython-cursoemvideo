#verificador de palindromos
for c in range(0, 8):
    frase = str(input('Digite uma frase: ')).strip()
    frase_editada = frase.replace(' ', '').upper()
    frase_invertida = frase_editada[::-1]
    if frase_editada == frase_invertida:
        print('\nA frase é um Palíndromo!')
    else:
        print('\nA frase não é um Palíndromo!')
