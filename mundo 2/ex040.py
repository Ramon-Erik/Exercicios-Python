n1 = float(input('Digite a primeira nota: '))
if n1 > 10:
    print('Sem \033[33mfraude\033[m por favor...')
    print('Convido você a \033[31msair\033[m!')
    exit()
n2 = float(input('Digite a segunda nota: '))

me = (n1 + n2) / 2

if me >= 7:
    print(f'Media: \033[32m{me}\033[m. Está \033[32mAPROVADO\033[m!')
elif me >= 5 and me <= 6.9:
    print(f'Media: \033[33m{me}\033[m. Está de \033[33mRECUPERAÇÃO\033[m!')
else:
    print(f'Media: \033[31m{me}\033[m. Está \033[31mREPROVADO\033[m!')
