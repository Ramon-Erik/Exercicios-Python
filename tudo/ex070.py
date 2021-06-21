a = '='*46
keep = 'Ss'
custo = 0 # soma dos preços
maiorq = 0 # produtos maior que 1000
menorq = 0 # produto menor
p = 0 # preço menor 
total = 0 # saber quantos produtos < 1000
while True:
    print(a)
    print('          LOJA SUPER BARATA VOADORA')
    print(a)
    nome = str(input('Nome: ')).title().strip().replace(' ', '_')
    preço = float(input('Preço: R$'))
    total += 1
#    if total == 1 and preço > 1000:
#        menorq = nome
#        p = preço
    if total == 1:
        p = preço
        menorq = nome
    else:
        if preço < p:
            p = preço
            menorq = nome
    custo += preço
    if preço > 1000:
        maiorq += 1
    keep = str(input('Continuar: [S/N] ')).upper()[0]
    while keep not in 'SsNn':
        keep = str(input('Continuar: [S/N] ')).upper()
    if keep in 'Nn':
        break
print(a)
print(f'Total gasto na compra: R${custo:.2f}')
print(f'São {maiorq} produtos custando mais de R$1000.00')
if total == 1 and preço < 1000:
    menorq = nome
    p = preço
    print(f'O menor produto é {menorq} custando R${p:.2f} lembrando, sua lista de itens tem apenas 1 item.\n')
else:
    print(f'O menor produto é {menorq} \ncustando R${p:.2f}.')
print(a)
print('{:-^46}'.format('FIM DO PROGRAMA'))