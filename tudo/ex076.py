tupla = ('Lápis', 1.75, 'borracha', 2.00, 'Caderno', 15.00, 'Lava-Louça', 145.78,
    'Computador', 210.33)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":-^40}')
print('-' * 40)
for pos in range(1, len(tupla), 2):
    print(f'{tupla[pos-1]:.<34} R${tupla[pos]:>6}')
