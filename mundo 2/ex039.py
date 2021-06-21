a = int(input('Em que ano você nasceu? '))

b = 2021 - a


if b == 18:
    print('Você já deve se alistar.')
elif b < 18:
    c = 18 - b
    print(f'Ainda não chegou seu tempo, faltam {c} anos')
else:
    d = b - 18
    print(f'Passou do tempo, exatamente {d} ano(s)')
