from moeda import *
preço = float(input('Informe um valor R$'))
print(f'A metade de {moeda(preço)} é {moeda(metade(preço))}')
print(f'A dobro de {moeda(preço)} é {moeda(dobro(preço))}')
print(f'Aumentando 10% de {moeda(preço)} temos {moeda(aumentar(preço, 10))}')
print(f'Diminuindo 13% de {moeda(preço)} temos {moeda(diminuir(preço, 13))}')
