'''faça um progra que ajude um jogador
da mega sena a criar palpites.
o programa vai perguntar quantos
jogos serão gerados e vai sortear
6 números entre 1 e 60 para cada jogo,
cadastrando em uma lista composta.'''
from time import sleep as tempo
from random import randint as ran
print('=' * 40)
print('JOGAR NA MEGA CENA DA VIRADA'.center(35))
print('=' * 40)
quant_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
palpites = []
clone = []
for c in range(0,quant_jogos):
    for c in range(0, 6):
        clone.append(ran(1, 60))
        if clone[c] in clone[0:c]:
            clone.pop()
            clone.append(ran(1, 60))
    palpites.append(clone[:])
    clone.clear()
for ci in range(0, len(palpites)):
    palpites[ci].sort()
for creating in range(0, quant_jogos):
    print(f'Jogo {creating+1}: {palpites[creating]}')
    tempo(1)
print('=-' * 5, ' < BOA SORTE > ', end=' ')
print('=-' * 5)
