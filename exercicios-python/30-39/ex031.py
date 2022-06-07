dis = float(input('Qual a distância da viagem em Km? '))
if dis <= 200:
    print(f'Você está prestes a começar uma viagem de {dis:.1F}Km.'
          f'\nE o preço da sua passagem será de R${dis * 0.5:.2F}')
else:
    print(f'Você está prestes a começar uma viagem de {dis:.1F}Km.'
          f'\nE o preço da sua passagem será de R${dis * 0.45:.2F}')
