from random import randint
import time

comp = randint(1, 3)
#print(comp)
print('='*46)
print("""                  Opções:
    	
                 [3]Pedra
                 [1]Papel
                 [2]Tesoura
""")
print('='*46)
print(' ')
jog = int(input('               Qual você usa? \n                      '))
if jog > 3:
    print('Pedra Papel Tesoura, de 1 a 3, escolha!!')
    print(' ')
    print('='*46)
    exit()
print(' ')
print('='*46)
print(' ')
time.sleep(1)
print('                    JO!!!')
time.sleep(1)
print('                    KEN!!')
time.sleep(1)
print('                    PO!!!')
print(' ')
print('='*46)
print(' ')

if jog == comp and jog == 1:
    print('                 Empate!!')
    print('                Você: Papel;\n              Computador: Papel.')
elif jog == comp and jog == 2:
    print('                   Empate!!')
    print('                 Você: Tesoura;\n              Computador: Tesoura.')
elif jog == comp and jog == 3:
    print('                  Empate!!')
    print('                 Você: Pedra;\n               Computador: Pedra.')
elif jog == 3 and comp == 2:
    print('           Escolheu pedra? Ganhou!\n            Computador: Tesoura!')
elif jog == 2 and comp == 1:
    print('          Escolheu tesoura? Ganhou!\n            Computador: Pesoura!')
elif jog == 1 and comp == 3:
    print('           Escolheu papel? Ganhou\n            Computador: Pedra!')

elif jog == 3 and comp == 1:
    print('           Perdeu! Você escolheu Pedra!!\n           Computador Papel!')
elif jog == 2 and comp == 3:
    print('           Perdeu! Você escolheu Tesoura!!\n           Computador Pedra!')
elif jog == 1 and comp == 2:
    print('           Perdeu! Você escolheu papel!!\n          Computador Tesoura!')
print(' ')
print('='*46)
