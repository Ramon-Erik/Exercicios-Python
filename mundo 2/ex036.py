print('\033[33m—\033[m' * 46)
print('     -Aprovador de Empréstimos Bancários-')
print('\033[33m—\033[m' * 46)


casa = float(input('Qual o valor da casa? R$'))
salario = float(input('O Salario do empreendedor: R$'))
ano = int(input('Em quantos anos sera o pagamento? '))

mês = casa / (ano * 12)
minimo = salario * 30/100
print('='*46)
print(f'A casa custa {casa:.2f} para pagar em {ano} ano(s).')
print(f'A prestação será de R${mês:.2f}!!')
if mês <= minimo:
    print('Emprestimo concedido!')
elif mês >= minimo:
    print('Emprestimo negado!')
print('='*46)