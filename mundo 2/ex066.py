num = int(input('Digite um número: '))
cont = 0
soma = 0
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
print(f'Você digitou {cont} números, e a soma é {soma}')
