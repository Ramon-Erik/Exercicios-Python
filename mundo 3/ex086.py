matriz = [[], [], []]
for posição_x in range(0, 3):
    for posição_y in range(0, 3):
        num = int(input(f'Digite um valor para a posição [{posição_x}.{posição_y}] '))
        matriz[posição_x].append(num)
print('-=' * 30)
for p in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[p][c]:^5} ]', end='')
    print()
