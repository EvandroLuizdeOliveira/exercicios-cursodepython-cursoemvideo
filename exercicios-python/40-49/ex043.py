peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
#testeimc = float(input())
if imc < 18.5:
    print('Abaixo do Peso')
elif 25 > imc >= 18.5:
    print('Peso ideal')
elif 30 > imc >= 25:
    print('Sobrepeso')
elif 40 >= imc >= 30:
    print('Obesidade')
else:
    print('Obesidade mórbida')
