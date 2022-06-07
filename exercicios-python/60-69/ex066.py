"""
Programa lê números até o usuário digitar 999
Após isso mostra quantos números foram digitados e a soma deles excluindo a flag
"""
cont = soma = 0
while True:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'Foram digitados {cont} números e a soma entre eles foi {soma}.')
