from colorama import Fore, Back, Style
carro = float(input(Fore.CYAN + '>>>Quantos quilômetros por hora está o carro? \n'))
multa = ((carro - 80) * 7)
if carro > 80:
    print( Fore.RED + f'>>>MULTADO! Pague a multa de R${multa:.2f}.')
else:
    print( Fore.GREEN + '>>>Ok, pode ir e tenha um bom dia.')
