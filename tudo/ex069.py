a = '='*46
keep = 'Ss'
mais18 = homem = mulher20 = cadastrados = 0
while keep in 'Ss':
    print(a)
    print('             CADASTRE UMA PESSOA')
    print(a)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))
    while sexo not in 'Ff' and sexo not in 'Mm':
        sexo = str(input('Sexo: '))
    cadastrados += 1
    keep = str(input('Continuar: '))
    while keep not in 'Ss' and keep not in 'Nn':
        keep = str(input('Continuar: '))
    if idade >= 18:
        mais18 += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
print(a)
print('               FIM DO PROGRAMA')
print(a)
print('Total de pessoas com mais de 18 anos: {}'.format(mais18))
print(f'Ao todo  temos {homem} homens cadastrados.')
print(f'Temos {mulher20} mulheres com menos de 20 anos.')
print(f'Total de cadastrados: {cadastrados}')
print(a)
