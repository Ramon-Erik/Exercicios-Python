from moeda import *

preço = float(input('Informe um valor R$'))
resp = str(input('Você deseja apreentar o preço como R$? ')).lower()

if resp == 's':
    resp = True
else:
    resp = False

print('=' * 30)
print(f'A metade de {moeda(preço)} é {metade(preço, resp)}')
print(f'A dobro de {moeda(preço)} é {dobro(preço, resp)}')
print(f'Aumentando 10% de {moeda(preço)} temos {aumentar(preço, 10, resp)}')
print(f'Diminuindo 13% de {moeda(preço)} temos {diminuir(preço, 13, resp)}')
