from time import sleep
valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor 2: '))


opção = 0
while opção != 5:
    print('''
==============================================
MENU: 
[1] Somar.
[2] Multiplicar.
[3] Maior.
[4] Novos números.
[5] Sair do programa
''')
    opção = int(input('Digite sua escolha: '))
    if opção == 5:
        print('>>>Finalizando', end='')
        sleep(1)
        print('. ', end='')
        sleep(0.5)
        print('. ', end='')
        sleep(1)
        print('.')
        sleep(2)
        break
        exit()

    if opção == 1:
        print('')
        print('>>>O resultado da soma entre os valores solicitados é {}'.format(valor1 + valor2))
    if opção == 2:
        print('')
        print('>>>O resultado da multiplicação entre os valores é {}'.format(valor1*valor2))
    if opção == 3:
        if valor1 > valor2:
            print('')
            print(f'>>>{valor1} é maior que {valor2}!!')
        else:
            print('')
            print(f'>>>{valor2} é maior que {valor1}')
    if opção == 4 :
        print('')
        print('='*46)
        valor1 = int(input('Valor 1: '))
        valor2 = int(input('Valor 2: '))
print('='*46)
