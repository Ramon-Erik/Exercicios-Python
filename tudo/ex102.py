def fatorial(num, show=False):
    """ -> Calcula o fatorial de um número
    :param num: número a ter o fatorial calculado
    :param show: (opcional) mostra a conta
    :retorno: retorna o valor do Fatorial de {num}"""
    fat = 1
    for c in range(num, 0, -1):
        if show:
            print(f' {c} ', end='')
            if c == 1:
                print('=', end=' ')
            else:
                print('x', end='')
        fat *= c
    return fat


print('~' * 25)
num = int(input(' '))
print(fatorial(num, True))
print('~' * 25)
