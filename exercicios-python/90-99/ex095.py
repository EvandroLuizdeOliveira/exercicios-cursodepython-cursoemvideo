aproveitamento = dict()
jogadores = list()
gols = list()
while True:
    aproveitamento['jogador'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {aproveitamento["jogador"]} jogou? '))
    for contador1 in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {contador1}? ')))
    aproveitamento['gols'] = gols[:]
    aproveitamento['total'] = sum(gols)
    jogadores.append(aproveitamento.copy())
    gols.clear()
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in "SN":
            break
        print('ERRO! Responda apenas S ou N')
    if continuar == "N":
        break
    print(f'{"-"  * 40}')
print(f'{"=-=" * 30}'
    f'\ncod ', end='')
for i in aproveitamento.keys():
    print(f'{i:<15}', end='')
print()
print(f'{"-" * 40}')
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(f'{"-" * 40}')
while True:
    escolha = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if escolha == 999:
        break
    elif escolha >= len(jogadores) or escolha < 0:
        print(f'ERRO! Não existe jogador com código {escolha}! Tente novamente')
    else:
        print(f'{"-" * 2} LEVANTAMENTO DO JOGADOR {jogadores[escolha]["jogador"]}:')
        for k, i in enumerate(jogadores[escolha]["gols"]):
            print(f'{" " * 3}No jogo {k} fez {i} gols.')
    print(f'{"-" * 40}')
print("<< VOLTE SEMPRE >>")
