jogadores, jogador, gols =[],  dict(), []
while True:
    print('-=-' * 15)
    jogador['nome'] = str(input('Nome: ')).title()
    tot_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for partidas in range(tot_partidas):
        gols.append(int(input(f'    Gols que {jogador["nome"]} fez na partida {partidas + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    gols.clear()

    while True:
        keep = str(input('Deseja continuar? ')).upper()[0]
        if keep in 'NS': break;
        print('ERRO, apenas S ou N')
    if keep in 'N': break;

print('-=-' * 15)
print(f'{"cod":>6}  {"nome":<15}{"gols":<14}{"total":>8}')
for c in range(len(jogadores)):
    print(f'{c:>6}  {jogadores[c]["nome"]:<15}{str(jogadores[c]["gols"]):<15}{jogadores[c]["total"]:>4}')

while True:
    print(f"{'-=-':^40}")
    while True:
        ind = int(input('Mostrar dados de qual jogador? 999 interrompe '))
        if ind < len(jogadores) and ind >= 0 or ind == 999: break;
        else:
            print('tente novamente...')
    if ind == 999:print('Até mais!'); break;

    print(f'LEVANTAMENTO DO JOGADOR {jogadores[ind]["nome"]}:')
    gols_list = jogadores[ind]["gols"]
    for c in range(len(jogadores[ind]["gols"])):
        print(f'    No jogo {c} fez: {gols_list[c]} gols')
