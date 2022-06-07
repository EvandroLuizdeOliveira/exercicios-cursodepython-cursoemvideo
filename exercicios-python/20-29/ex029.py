vel = float(input('Velocidade atual do carro: '))
if vel <= 80:
    print('Tenha um bom dia! Dirija em segurança!')
else:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h'
          f'\nVocê deve pagar uma multa de R${(vel - 80) * 7:.2F}'
          f'\nTenha um bom dia! Dirija em segurança!')
