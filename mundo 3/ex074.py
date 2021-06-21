from random import randint as r
tupla = (r(1, 10), r(1, 10), r(1, 10), r(1, 10), r(1, 10))
print('Os valores sorteados foram: ', end='')
for c in tupla:
    print(f'{c} ', end='')
print()
print('O maior é:', max(tupla))
print('O menor é:', min(tupla))
