tupla = (int(input('Digite o 1° número: ')),
    int(input('Digite o 2° número: ')),
    int(input('Digite o 3° número: ')),
    int(input('Digite o 4° número: ')))
conta = 0
print('\nVocê digitou:', tupla)
print('\nO número 9 aparece', tupla.count(9), 'vezes.')
if 3 in tupla:
    print('O número 3 aparce na', tupla.index(3)+1, 'posição.')
else:
    print('O número 3 não foi digitado.')
print('Os números pares são: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
