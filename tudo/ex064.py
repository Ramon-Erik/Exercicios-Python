print('='*46)
num = int(input('Digite um número -> (999 para parar) '))
nov = 0
quant = 0
while num != 999:
    nov += num
    quant += 1
    num = int(input('Digite um número -> (999 para parar) '))
media = nov / quant
print('='*46)
print('Foram {} números digitados e a soma deles é \n>>>{}'.format(quant, nov))
print('A média entre os números digitados é\n>>>{:.2f}'.format(media))
print('='*46)
