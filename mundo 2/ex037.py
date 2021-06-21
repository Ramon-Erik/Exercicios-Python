print('[0] Binario\n[1] Hexadecimal\n[2] Octadecimal\n', '='*45)
valor = int(input('Digite o valor em decimal: '))
c = int(input('Digite o número referente a conversão: '))
if c > 2:
    print('Digite um numero entre 0 e 2 por favor.')
    exit()
elif c == 0:
    print('{} em binário é: {}'.format(valor, bin(valor)[2:]))
elif c == 2:
    print('{} em octadecimal é: {}'.format(valor, oct(valor)[2:]))
elif c == 1:
    print('{} em hexadecimal é {}'.format(valor, hex(valor)[2:]))
