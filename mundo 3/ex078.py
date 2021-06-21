valores = list()
for c in range(5):
    valores.append(int(input(f'Informe o {c}° valor: ')))
print(f'-=-' * 15)
print(f'Você digitou o os valores ', *valores, sep=",")
print(f'O maior valor digitado foi {max(valores)} nas posições', end=' ')
for c, v in enumerate(valores):
    if v == max(valores): print(c, end='... ');
print(f'\nO menor valor digitado foi {min(valores)} nas posições', end=' ')
for c, v in enumerate(valores):
    if v == min(valores): print(c, end='.... ');
