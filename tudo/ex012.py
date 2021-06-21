dinheiro = float(input('Qual o preço normal? R$'))
desconto = float(input('Quanto de desconto? \n(sem sinal de porcentagem)'))
des = dinheiro - (dinheiro * (desconto/100))
print(f'Antes o preço era R${dinheiro} e agora,\ncom o desconto de {desconto}% é R${des:.2f}')