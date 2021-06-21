por_extenso = ('zero', 'um','dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte' )
print('=' * 46)
while True:
    número = int(input('Informe um número de 0 a 20: '))
    if número == 999:
        break
    while número < 0 or número > 20:
        número = int(input('Tente novamente. Informe um número de 0 a 20: '))
        if número == 999:
            break
    if número > 20:
        break
    print('Você escreveu: ', por_extenso[número])
    print('='*46)
print('='*46)
print('Bye ;)'.center(46))
print('='*46)
