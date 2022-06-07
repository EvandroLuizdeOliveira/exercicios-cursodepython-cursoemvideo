vc = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
tem = int(input('Quantos anos de financiamento? '))
pre = vc / (tem * 12)
if pre > (sal * 0.3):
    print(f'Para pagar uma casa de R${vc:.2F} em {tem} anos a prestação será de R${pre:.2F}'
          f'\nEmpréstimo \033[31mNEGADO\033[m!')
else:
    print(f'Para pagar uma casa de R${vc:.2F} em {tem} anos a prestação será de R${pre:.2F}'
          f'\nEmpréstimo pode ser \033[32mCONCEDIDO\033[m!')
