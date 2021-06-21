#Perguntas básicas e formatação
print('='*46)
num = int(input('Digite um número: '))
keep = str(input('Deseja continuar? (S/N) '))
print('='*46)


#Opções inválidas
if keep not in 'SsNn':
    print('Opção inválida!!')
    print('='*46)
    exit()


#Váriaveis para a média
divisor = 1
med = 0
numeros = num
mai = 0
men = 0
while keep in 'Ss':
    divisor += 1
    num = int(input('Digite um número: '))
    keep = str(input('Deseja continuar? (S/N) '))
    if keep not in 'SsNn':
        print('Opção inválida!!')
        print('='*46)
        exit()
    print('='*46)
    numeros += num
    med = numeros / divisor
    if num > mai:
        mai = num
    else:
        men = num
print('A média entre os números digitados é: {}!!\nO maior é {}\nE o menor é {}'.format(med, mai, men))
print('='*46)
