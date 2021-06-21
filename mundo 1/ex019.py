from random import choice
a1 = int(input('>Número de chamada do aluno 1: '))
a2 = int(input('>Número de chamada do aluno 2: '))
a3 = int(input('>Número de chamada do aluno 3: '))
a4 = int(input('>Número de chamada do aluno 4: '))
print('(Ser o primeiro aluno ou 4° nao influenciará)')
lista = [a1, a2, a3, a4]
escolha = (choice(lista))
print(f'O aluno sorteado foi: {escolha}')