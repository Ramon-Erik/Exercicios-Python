from random import shuffle
print('Ser o aluno 1 ou  4 não influenciará em nada.')
t1 = int(input('>Número de chamada do aluno 1: '))
t2 = int(input('>Número de chamada do aluno 2: '))
t3 = int(input('>Numero de chamada do aluno 3: '))
t4 = int(input('>Número de chamada do aluno 4: '))
lista = [t1, t2, t3, t4]
(shuffle(lista))
print(f'A ordem será {lista}')