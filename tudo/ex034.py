s = float(input('Salário do trabalhador:\n>>>R$'))
if s >= 1.250:
    aumento = 10
    print(f'Com o aumento de {aumento}% o salário é de:\n>>>R${s/100 * aumento/100 + s:.2f}.')
if s < 1.250:
    aumento = 15
    print(f'Com o aumento de {aumento}% o salário é de:\n>>>R${s/100 * aumento/100 * s:.2f}.')
