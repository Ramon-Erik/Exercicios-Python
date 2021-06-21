preço = float(input('                    Preço:\n                  R$'))
print('                 Pagamentos:')
print('=' * 46)
print('''
[1] A vista (dinheiro ou cheque)
>>>Desconto: 10%
[2] A vista (no cartão)
>>>Desconto: 5%
[3] No cartão 2x
>>>Sem desconto | Sem juros
[4] No cartão 3x ou mais
>>>Sem desconto | 20% de juros ''')
print(' ')
print('=' * 46)
print(' ')
n = int(input('Sua opção: '))
if n > 4:
    print('São 4 opções senhor(a), de 1 a 4. Tente novamente.')
    exit()
if n == 1:
    k = (preço - ((preço * 10) / 100))
    print(f'O preço agora será de R${k:.2f}!')
elif n == 2:
    k = (preço - ((preço * 5) / 100))
    print(f'O preço será de R${k:.2f}!')
elif n == 3:
    k = (preço / 2)
    print(f'Serão 2 parcelas de R${k:.2f}!')
elif n == 4:
    total = preço + (preço * 20/100)
    parce = int(input('Quantas parcelas? '))
    parcelas = total / parce
    print(f'Serão {parce} parcelas de R${parcelas:.2f} com o juros de 20%!! Custando R${total:.2f} no final.')
print(' ')
print('=' * 46)
