logados = []
while True:
    print('='*46)
    num = int(input('Digite um número: '))
    if num in logados:
        print('Numero duplicado... Não adicionarei...')
    else:
        print('Adicionado com sucesso.')
        logados.append(num)
    keep = str(input('Deseja continuar? [S/N] '))
    while keep[0] not in 'NnSs':
        keep = str(input('Apenas Sim ou Não. por favor.: '))
    if keep[0] in 'Nn':
        break
logados.sort()
print('='*46)
print('Você digitou os valores', *logados, sep=' ')
