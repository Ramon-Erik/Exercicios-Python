termo1 = int(input('Primeiro termo: '))    
razão = int(input('Razão: '))
u = termo1 + (10 - 1) * razão
for c in range (termo1, u + razão, razão):
    print(c,'-', end=' ')
print('Pronto')
