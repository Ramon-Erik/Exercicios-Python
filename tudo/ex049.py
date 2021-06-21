print('''
OPÇÕES:
[ 1 ] SOMA
[ 2 ] SUBTRAÇÃO
[ 3 ] MULTIPLICAÇÃO
[ 4 ] DIVISÃO
''')
op = int(input('Sua opção: '))
if op > 4:
    print('Escolha um número que esteja nas opções.')
    exit()
n = int(input('Digite o número para mostrar sua tabuada: '))
if op == 1:
    for c in range(1, 11):
        print(n, end=' ')
        print(f'+ {c} = {n+c}', end=' ')
elif op == 2:
    for c in range(1, 11):
        print(n, end=' ')
        print(f'- {c} = {c-n}')
elif op == 3:
    for c in range(1, 11):
        print(n, end=' ')
        print(f'x {c} = {c*n}')
elif op == 4:
    for c in range(1, 11):
        print(n, end=' ')
        print('÷ {} = {}'.format(c, int(n/c)))
print(' \n','='*45)
