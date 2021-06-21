ac1 = 0
ac2 = 0
so = 0
for w in range(1, 7):
    n = int(input(f'Digite o {w}° número: '))
    if n % 2 == 0:
        so += n
        ac1 += 1
    elif n % 2 != 0:
        ac2 += 1
print('A soma dos números pares é {}. Há {} número(s) pare(s), e {} ímpar(es).'.format(so, ac1, ac2))
