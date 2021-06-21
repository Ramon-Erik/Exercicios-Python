n = int(input('Digite um número: '))
print(f'Calculando {n}! ', end='')
fact = n
for c in range(1, n):
    fact = c * fact
print(fact)
