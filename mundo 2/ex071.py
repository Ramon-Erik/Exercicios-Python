# variáveis
sed2 = 0 #somador de sedulas de 2
mod1 = 0 #somador de moedas de 1
cont2 = 0 # cédulas de 2
cont1 = 0 # moedas de 1
sed50 = 00 # cédulas de 50
contCen = 0 # somador de 50
sed20 = 0 # cédulas de 20
contVin = 0 # somador de 20
d10 = 00 # notas de 10
cont10 = 0 # s notas de 10
mill = 00 #notas
contm = 0 #contador
uni = 00
contu = 0
a = '='*46

print(a)
print('BANCO CeV'.center(45))
print(a)
sacar = int(input('Quanto deseja sacar? R$'))


u = sacar // 1 % 10
dez = (sacar // 10 % 10) * 10
cen = (sacar // 100 % 10) *100
mil = (sacar // 1000 % 10) * 1000
unm = (sacar // 10000 % 10) * 10000

while uni < unm:
    uni += 50
    contu += 1
if uni > unm:
    uni -= 10
    contu -= 1

while mill < mil:
    mill += 50
    contCen += 1
if mill > mil:
    mill -= 10
    contCen -= 1


while sed20 < dez:
    sed20 += 20
    contVin += 1
if sed20 > dez:
    sed20 -= 10
    contVin -= 1
    d10 += 10
    cont10 += 1
    
while sed50 < cen:
    sed50 += 50
    contCen += 1
if sed50 > cen:
    sed50 -= 10
    contCen -= 1

while sed2 < u:
    sed2 += 2
    cont2 += 1
if sed2 > u:
    sed2 -= 2
    cont2 -= 1
    cont1 += 1

somador = contm + contCen + contu
if somador > 0:
    print('Total de {} cédulas de R$50'.format(somador))
if contVin > 0:
    print(f'Total de {contVin} cédulas de R$20')
if cont10 > 0:
    print(f'Total de {cont10} cédulas de R$10')
if cont2 > 0:
    print('Total de {} cédulas de R$2'.format(cont2))
if cont1 > 0:
    print('e {} moedas de 1 real'.format(cont1))
print(a)
print('Volte sempre ao banco CeV! Tenha um bom dia :) ')
