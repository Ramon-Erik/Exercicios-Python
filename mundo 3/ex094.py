ficha, dados, méd = {}, [[], [], []], 0
while True:
    ficha['nome'] = str(input('Nome: ')).title()
    while True:
        ficha['sexo'] = str(input('Sexo: ')).upper()[0]
        if ficha['sexo'] in 'MF':
            break
        print('Apenas M ou F.')
    ficha['idade'] = int(input('Idade: '))

    méd += ficha['idade']
    
    if ficha['sexo'] in 'F':
        dados[2].append(ficha['nome']) # ficha.copy()
    
    dados[0].append(ficha.copy())
    
    while True:
        keep = str(input('Deseja continuar? (S/N) ')).upper()[0]
        if keep in 'SN':
            break
        print('Apenas S ou N')
    if keep in 'N':
        break

méd = méd // len(dados[0])

print('=-' * 30)
for c in range(0, len(dados[0])):
    for k, v in dados[0][c].items():
        if type(v) == int and v > méd:
            dados[1].append(dados[0][c])

print(f'A) o grupo tem {len(dados[0])} pessoas cadastradas.')
print(f'B) A média de idades foi: {méd} anos.')
print('C) As mulheres cadastradas foram:', end='')
for v in dados[2]:
    print(f' [{v}] ', end='')
print()
print('D) Listas de pessoas que estão acima da média: ')
for p in range(0, len(dados[1])):
    for keyy, vallue in dados[1][p].items():
        print(f'{keyy} = {vallue}; ', end='')
    print()
print(f' <<< ENCERRADO >>> ')
