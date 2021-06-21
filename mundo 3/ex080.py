lista = []
for c in range(5):
	num = int(input('Informe um valor: '))
	if c == 0 or num > lista[-1]:
		lista.append(num)
		print('    Adicionado ao fim da lista.')
	else:
		pos = 0
		for pos in range(len(lista)):
			if num <= lista[pos]:
				lista.insert(pos, num)
				print(f'	Adicionado na posição {pos}')
				break
print('-=-' * 15)
print(f'Você digitou os números: {lista}')
