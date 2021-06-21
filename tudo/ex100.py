from random import randint as ran
from time import sleep as tempo

def soma_par(nums):
    soma = 0
    print(f'Somando os valores pares de {números}, temos ', end=' ')
    for n in nums:
        if n % 2 == 0:
            soma += n
    print(soma)


def sorteie():
    print('Sorteando 5 valores da lista: ', end=' ')
    for c in range(5):
        números.append(ran(1, 10))
        print(números[c], end=' ')
        tempo(0.9)
    print(' PRONTO!')
    soma_par(números)


números = []
sorteie()
