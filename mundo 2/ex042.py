reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))



if reta1 + reta2 > reta3 > reta1 - reta2 and reta2 + reta3 > reta1 > reta2 - reta3 and reta3 + reta1 > reta2 > reta1 - reta3:
    print('É possível fazer um triângulo!') 
elif reta1 == reta2 != reta3 or reta2 == reta3 != reta1 or reta1 == reta3 != reta2:
    print('Triangulo isóceles.')
if reta1 == reta2 == reta3:
    print('Triangulo equilátero.')
else:
    print('Não é possível formar um triângulo!')



if reta1 != reta2 != reta3 and reta2 != reta1 != reta3 and reta3 != reta1 != reta2 and reta1 + reta2 > reta3 > reta1 - reta2 and reta2 + reta3 > reta1 > reta2 - reta3 and reta3 + reta1 > reta2 > reta1 - reta3:
    print('Pode formar um triângulo!\nE ele é um triangulo escaleno.')
#else:
#    print('Não é um triângulo....')
