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
    continuar = str(input('Quer continuar? [S/N]')).strip()[0]
    if continuar not in "SsNn":
        continuar = str(input('Quer continuar? [S/N] '))
    if continuar in "Nn":
        break
    print(f'{"-"  * 40}')
print(f'{"=-=" * 30}'
    f'\n{"cod":>3} {"nome":<14} {"gols":<14} {"total":<6}'
    f'\n{"-" * 40}')
for k in range (len(jogadores)):
    print(f'{k:>3} {jogadores[k]["jogador"]:<14} {jogadores[k]["gols"]}{" " * (14-((len(jogadores[k]["gols"]))+((len(jogadores[k]["gols"])-1)*2)+2))} {jogadores[k]["total"]}')
print(f'{"-" * 40}')
while True:
    escolha = int(input('Mostrar dados de qual jogador? '))
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
