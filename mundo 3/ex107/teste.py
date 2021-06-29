from moeda import *

preço = float(input('Informe um valor R$'))
print(f'A metade de R${preço} é R${metade(preço)}')
print(f'A dobro de R${preço} é R${dobro(preço)}')
print(f'Aumentando 10% de R${preço} temos R${aumentar(preço, 10)}')
print(f'Diminuindo 13% de R${preço} temos R${diminuir(preço, 13)}')
