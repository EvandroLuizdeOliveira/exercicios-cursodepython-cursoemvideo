sal = float(input('Qual o salário do funcionário? R$'))
if sal >= 1250:
    print(f'Quem ganhava R${sal:.2F} passa a ganhar R${sal * 1.1:.2F} agora.')
else:
    print(f'Quem ganhava R${sal:.2F} passa a ganhar R${sal * 1.15:.2F} agora.')
