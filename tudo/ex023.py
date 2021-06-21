número = int(input('>Digite um número de 0 a 9999: '))
u = número // 1 % 10
d = número // 10 % 10
c = número // 100 % 10
m = número // 1000 % 10
print(f'Unidade: {u}.')
print(f'Dezenas: {d}.')
print(f'Centenas: {c}.')
print(f'Milhares: {m}')
