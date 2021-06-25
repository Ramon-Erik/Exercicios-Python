def ficha(name='<desconheico>', tot_gols=0): 
    print(f'O jogador {name} fez um total de {tot_gols} gol(s) no campeonato.')

print('~' * 25)
nome = str(input('Nome do jogador: ')).title()
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(tot_gols=gols)
else:
    nome = nome.split()
    nome = nome[0]
    ficha(nome, gols)
