from random import randint
comp = randint(0, 10)
a = '=-'*23
plac = 'GANHOU'
vi = 0
while True:
    print(a)
    jog = int(input('Diga um valor: '))
    esc = str(input('ÍMPAR ou PAR? [P/I] '))
    if esc not in 'Pp' and esc not in 'Ii':
        print('opção inválida :(')
        print(a)
        break
        exit()
    print(a)
    placar = jog + comp
    if placar % 2 == 0:
        des = 'PAR'
    else:
        des = 'ÍMPAR'
    if placar % 2 == 0 and esc in 'Pp':
        plac = 'GANHOU'
        vi += 1
    elif placar % 2 != 0 and esc in 'Ii':
        plac = 'GANHOU'
        vi += 1
    elif placar % 2 == 0 and esc in 'Ii':
        plac = 'PERDEU'
    elif placar % 2 != 0 and esc in 'Pp':
        plac = 'PERDEU'
    print(f'Você jogou {jog} e o computador {comp}.\nTotal: {placar}, deu {des}!! ')
    print(a)
    print('Você', plac, '!!')
    if plac != 'GANHOU':
        print(a)
        break
        exit()
    else:
        print('Vamos jogar novamente...')
    comp = randint(0, 10)
if esc not in 'Pp' and esc not in 'Ii':
    print()
else:
    print(f'Seu número de vitórias é {vi}')
