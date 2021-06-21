s = 0
while s != 'M' or s != 'F':
    s = str(input('Seu sexo(M/F): ')).upper()
    if s == 'M' or s == 'F':
        break
    else:
        print('Digite M para masculino ou F para feminino!!')
