salário = float(input('>>>>Salário atual (sem desconto)do trabalhador R$'))
porcentagem = float(input('>>>>>Quantos porcentos serão aumentados? (apenas o número por favor.) '))
aumento = salário + (salário * (porcentagem /100))
print(f'>>>>O salário que antes, era de R${salário:.2f} agora, com o aumento de \n{porcentagem}%, será de {aumento:.2f}.')