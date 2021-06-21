jogador, gols = dict(), []

jogador['nome'] = str(input('Nome: ')).title()
tot_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for partidas in range(tot_partidas):
    gols.append(int(input(f'    Gols que {jogador["nome"]} fez na partida {partidas + 1}? ')))

jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('-=-' * 17)

for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=-' * 17)

print(f'Jogador {jogador["nome"]} jogou {tot_partidas} vezes.')
for c in range(len(jogador["gols"])):
    print(f'    Na partida {c+1} fez {gols[c]} gols.')
print(f'Foram {jogador["total"]} de gols no total.')
