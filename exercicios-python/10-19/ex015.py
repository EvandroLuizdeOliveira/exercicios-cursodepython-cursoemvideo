tem = int(input('Quantos dias alugados? '))
dis = float(input('Quantos Km rodados? '))
print(f'O total a pagar é de R${((tem * 60) + (dis * 0.15)):.2F}')
