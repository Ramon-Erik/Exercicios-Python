from colorama import Fore, Back, Style
from random import randint


nume = (randint(0, 5))
print('Vou pensar em um número...')
num = int(input('Digite um número de 0 a 5... Tente adivinhr.''))
if num == (nume):
    print(Back.GREEN + 'Acertou. Você venceu!')
else:
    print( Fore.RED + f'Errou. você perdeu! o número era {nume}')
    print('Mais sorte na próxima :)')
