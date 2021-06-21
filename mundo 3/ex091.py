from random import randint as ran
from time import sleep as pausa_de
from operator import itemgetter

jog = {'jogador 1': ran(1, 6), 'jogador 2': ran(1, 6), 
    'jogador 3': ran(1, 6), 'jogador 4': ran(1,6)}

ranking = list()
print('Valores sorteados:')
for k, v in jog.items():
    print(f'    O {k} tirou: {v} ')
    pausa_de(1)

ranking = sorted(jog.items(), key=itemgetter(1), reverse=True) # colocando o dicionario em ordem decescente
print('Ranking dos jogadores:')
for ind, valor in enumerate(ranking):
    print(f'    Em {ind + 1}° lugar, {valor[0]} com {valor[1]}')
    pausa_de(1)
