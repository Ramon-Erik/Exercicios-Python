n = int(input('Digite um número: '))
cont = n
print(f'Calculando {n}! ', end='')
fat = 1
while cont > 0:
    print('{} '.format(cont, fat), end='')
    print('x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print(fat)
