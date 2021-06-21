"""7 valores numéricos
lista de par
lista de impar"""
números = [[], []]
print('=-' * 30)
for c in range(1, 8):
    num = int(input('Digite o {}o. valor. '.format(c)))
    if num % 2 == 0:
        números[1].append(num)
    else:
        números[0].append(num)
for c in range(0, 2):
    números[c].sort()
print('=-' * 30)
print(f'Os valores pares digitados foram: {números[1]}')
print(f'Os valores impares digitados foram: {números[0]}')
