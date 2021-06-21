maior = 0
menor = 0
for c in range(1, 8):
    pe = int(input('Digite seu ano de nascimento: '))
    if pe > 2000:
        print('>>>>Menor de idade!')
        print(' ')
        menor += 1
    else:
        print('>>>>Maior de idade!')
        print(' ')
        maior += 1
print('Foram {} maiores de idade!!\nE {} menores de idade!!'.format(maior, menor))