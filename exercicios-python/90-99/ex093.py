aproveitamento = dict()
gols = list()
total_gols = 0
aproveitamento['jogador'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {aproveitamento["jogador"]} jogou? '))
for contador1 in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {contador1}? ')))
    total_gols += gols[contador1]
aproveitamento['gols'] = gols
aproveitamento['total'] = total_gols
print(f'{"=-=" * 30}'
      f'\n{aproveitamento}'
      f'{"=-=" * 30}')
for k, v  in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}.')
print(f'{"=-=" * 30}'
      f'\nO jogador {aproveitamento["jogador"]} jogou {partidas} partidas.')
for contador2 in range(0, len(aproveitamento['gols'])):
    print(f'{" " * 4}=> Na partida {contador2}, fez {aproveitamento["gols"][contador2]} gols.')
print(f'Foi um total de {aproveitamento["total"]} gols.')
