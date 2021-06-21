dia = int(input('Quantos dias alugado? '))
quilometros = float(input('Quantos quilômetros rodados? '))
kmPdia = dia * 60
kmRodado = quilometros * 0.15
pagamento = kmPdia + kmRodado
print(f'O pagamento será de R${pagamento:.2f}')