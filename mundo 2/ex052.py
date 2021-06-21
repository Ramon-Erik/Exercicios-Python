n = int(input('Digite um número: '))
if n % 2 == 0 and n % 3 == 0 and n % 5 == 0:
    print('{} é um número primo!'.format(n))
else:
    print('{} não é um número primo!'.format(n))
