matriz = [[],[],[],[0, 0]]
for x in range(0, 3):
    for y in range(0, 3):
        num = int(input(f'Digite um número pra a posição [{x}.{y}]: '))
        if y == 2:
            matriz[3][1] += num
        matriz[x].append(num)
        if num % 2 == 0:
            matriz[3][0] += num
print('-=' * 30)
for p in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[p][c]:^5} ]', end='')
    print()
print('-=' * 30)
print(f'A a soma de todos os pares é: {matriz[3][0]}.')
print(f'A soma dos valores da terceira coluna é: {matriz[3][1]}.')
print(f'O maior número da segunda coluna foi: {max(matriz[1])}.')
