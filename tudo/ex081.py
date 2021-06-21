keep, lista = '0', list()
s = 'n'
while keep not in 'Nn':
    print('«'*46)
    lista.append(int(input('Digite um valor. ')))
    keep = str(input('Deseja ontinuar? [S/N]  '))[0]
    while keep not in 'SsNn':
        print('Erro de digitação.', end='')
        keep = str(input('Deseja Continuar? [S/N] '))[0]
print('«'*46)

lista.sort(reverse=True)

print('Quantos valores digitados: {}'.format(len(lista)))
print('Os valores em ordem decrescente: {}'.format(lista))
if 5 in lista: 
    print('5 está na lista, pos.', lista.index(5))
else:
    print('5 não esta na lista')
print('«'*46)
