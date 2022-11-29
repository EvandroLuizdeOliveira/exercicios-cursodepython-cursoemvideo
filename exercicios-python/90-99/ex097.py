def escreva(txt):
    print(f'{"~" * (len(txt)+4)}'
          f'\n  {texto}'
          f'\n{"~" * (len(txt)+4)}')


texto = str(input('Escreva uma mensagem: ')).strip()
escreva(texto)
