a = '='*46
print(a)
print('Sequencia de Fibonacci'.center(46))
print(a)
n = int(input('Quantos termos quer mostrar? '))
print(a)
t1 = 0
t2 = 1
cont = 1
print('{} -> {} -> '.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' {} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
print(a)
