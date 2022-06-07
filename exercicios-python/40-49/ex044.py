print(f'{10 * "="}\nLoja ELO\n{10 * "="}')
preco = float(input('\nDigite o valor do produto: R$'))
true_opcoes = 0
while true_opcoes == 0:
    opcoes = int(input('\nOpções de pagamento:\n'
                   '1 - À vista dinheiro/cheque\n'
                   '2 - À vista no cartão\n'
                   '3 - 2x no cartão\n'
                   '4 - 3x ou mais no cartão\n\n'))
    if 0 < opcoes < 5:
        true_opcoes = 1
    else:
        print('\n\033[31mOpção indisponível!\033[m')
if opcoes == 1:
    print(f'\n\033[33mO produto que custava R${preco:.2F} passou a custar R${(preco * 0.9):.2F} com 10% de desconto!\033[m')
elif opcoes == 2:
    print(f'\n\033[33mO produto que custava R${preco:.2F} passou a custar R${(preco * 0.95):.2F} com 5% de desconto!\033[m')
elif opcoes == 3:
    print(f'\n\033[33mO produto custa R${preco:.2F}\n'
          f'O valor parcelado será de 2x de R${(preco / 2):.2F} sem juros!\033[m')
elif opcoes == 4:
    true_vezes = 0
    while true_vezes == 0:
        vezes = int(input('\nDigite em quantas vezes será parcelada a compra: '))
        if 2 < vezes <= 12:
            true_vezes = 1
        else:
            print('\n\033[31mOpção indisponível!\033[m')
    print(f'\n\033[33mO produto que custava R${preco:.2F} passou a custar R${(preco * 1.2):.2F} com 20% de juros\n'
          f'O valor parcelado será de {vezes}x de R${(preco * 1.2) / vezes:.2F}!\033[m')
