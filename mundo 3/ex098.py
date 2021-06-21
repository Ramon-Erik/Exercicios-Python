from time import sleep as temp


def contador(ini, fim, passo):
    if passo > 0 and ini > fim:
        passo = -passo
    if passo == 0 and fim < ini:
        passo = -1
    else: passo = 1;
    print(f'Contagem de {ini} até {fim} de {abs(passo)} em {abs(passo)}')
    for c in range(ini, fim + passo, passo):
        print(c, end=' ')
        temp(0.9)
    print('FIM!')


# Programa principal
print('-=' * 20)
print('Contagem de 1 até 10 de 1 em 1')
for c in range(1, 11):
    print(c, end=' ')
print('FIM!')
print('-=' * 20)
print('Contagem de 10 até 1 de 2 em 2')
for c in range(11, 0, -2):
    print(c, end=' ')
print('FIM!')
print('-=' * 20)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim   : '))
passo = int(input('Passo : '))
print('-=' * 20)
contador(inicio, fim, passo)
