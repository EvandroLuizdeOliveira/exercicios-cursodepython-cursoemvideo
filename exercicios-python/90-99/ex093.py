aproveitamento = dict()
gols = list()
aproveitamento['jogador'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {aproveitamento["jogador"]} jogou? '))
for contador1 in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {contador1}? ')))
aproveitamento['gols'] = gols[:]
aproveitamento['total'] = sum(gols)
print(f'{"=-=" * 30}'
      f'\n{aproveitamento}'
      f'{"=-=" * 30}')
for k, v  in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}.')
print(f'{"=-=" * 30}'
      f'\nO jogador {aproveitamento["jogador"]} jogou {partidas} partidas.')
for k, v in enumerate(aproveitamento["gols"]):
    print(f'    => Na partida {k}, fez {v} gols.')
print(f'Foi um total de {aproveitamento["total"]} gols.')
