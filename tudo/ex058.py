from random import randint as r
vezes = 0
comp = r(0, 10)
#print(comp)
jog = 99
print('')
while jog != comp:
    jog = int(input('\033[32mEm que número o computador pesnou? \033[m'))
    vezes += 1
    print('')
    if jog != comp and comp < 5:
        print('Dica: Um pouco menor!!')
    elif jog + 1 == comp or jog - 1 == comp:
        print('Ta muito perto ;)')
    elif jog != comp and comp > 5:
        print('Dica: Um pouco maior!!')
    print('')
print('PARABÉNS, CONSEGUIU!!!!')
print('Numero: {}\nTentativas {}'.format(comp, vezes))
