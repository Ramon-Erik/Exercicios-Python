lista1, par, imp = [], [], []
temp = 0
while True:
	print('='*46)
	lista1.append(int(input('Digite um valor: ')))
	keep = str(input('Deseja continuar? [S/N] '))
	if lista1[temp] % 2 == 0:
		par.append(lista1[temp])
	else:
		imp.append(lista1[temp])
	if keep.upper() in 'N':
		break
	temp += 1
print('='*46)
print('Sua lista:',lista1)
if len(par) > 0:
	print('Os números par: ', par)
else: print('Você não digitou nenhum número par.')
if len(imp) > 0:
	print('Os números imp: ',imp)
else: print('Você não digitou nenhum número ímpar.')
print('='*46)
