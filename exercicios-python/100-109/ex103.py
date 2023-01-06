def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


#Programa principal
nome = input('Nome do jogador: ')
gols = input('Quantidade de gols: ')
if nome == '' and gols == '':    
    ficha()
elif nome == '' and gols != '':    
    ficha(gols = gols)
elif nome != '' and gols == '':    
    ficha(nome)
else:
    ficha(nome, gols)
