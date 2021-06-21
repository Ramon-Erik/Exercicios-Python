cads = [[], [], []]
soma = 0

while True:
    print('-=-' * 16)
    nome = str(input('Nome: ')).strip().title()
    cads[0].append(nome)
    
    peso = float(input('Peso: '))
    cads[1].append(peso)
    soma += peso
    
    m = max(cads[1])
    if peso == m:
        cads[2].append(nome)
    
    resp = str(input('Continuar? (S/N) ')).upper()[0]
    if resp in 'N':
        break


num = cads[1].index(max(cads[1]))
pum = cads[1].index(min(cads[1]))

print(cads)

print('-=-' * 16)

print(f'São {len(cads[0])} pessoas cadastradas.')

print(f'O maior peso foi {max(cads[1])}Kg de ', end='')
print(f'{cads[0][num]}', end = '')

if len(cads[2]) > 0:
    print(f'{cads[2][-1:1]}')
else:
    print()

print(f'\nO menor peso foi de {min(cads[1])} de ', end='')
print(f'{cads[0][pum]}')

print('Calculando a média aritmética... fica...')
print(f'{soma} / {len(cads[0])} = {soma / len(cads[0]):.3f} \n ')
