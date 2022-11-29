def Área(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura:.1F}x{comprimento:.1F} é de {area:.1F}m².')


print(f'{"Controle de Terrenos" :^20}'
      f'\n{"-" * 20}')
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
Área(largura, comprimento)
