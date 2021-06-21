print('='*46)
termos = int(input('Primeiro termo:  '))
razão = int(input('Razão da progressão: '))
print('='*46)
termo = termos
cont = 0
som = 0
so = 0
while cont < 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    so += termo - razão
    cont += 1
    som += 1
print('PAUSA')
print('\nForam {} termos mostrados e a soma entre eles é: {}'.format(som, so))
print('='*46)
