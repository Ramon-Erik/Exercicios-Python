ced50 = ced20 = ced10 = ced1 = 0
while True:
    print('=-' * 23)
    print(f' {"BANCO CEV":^12} ')
    print('=-' * 23)
    valor = float(input('Quanto você deseja sacar? '))
    while valor >  50:
        ced50 = ced50 + 1
        valor = valor - 50
    print(f'Quant. cedulas de R$50: {ced50} ')