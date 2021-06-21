print('='*46)
termos = int(input('Termo inicial? '))
razão = int(input('Qual a razão? '))
termo = termos
cont = 1
som = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
        som += 1
    print('PAUSA')
    print('='*46)
    mais = int(input('Quantos termos quer mostrar?[0 para parar] '))
print('='*46)
print (f'Prgoreção aritmética finalizada com {som} termos.')
print('='*46)
print('                 ATÉ MAIS!!')