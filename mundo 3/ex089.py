alunos_e_notas, media, cont = [[], [], []], 0, 0 # 0 nomes \ 1 notas \ 2 médias
notas = list()
while True:
    alunos_e_notas[0].append(str(input('Nome: ')).capitalize())
    for c in range(2):
        notas.append(float(input(f'Nota {c+1}: ')))
    alunos_e_notas[1].append(notas[:])
    media = sum(notas) / 2
    alunos_e_notas[2].append(media)
    keep = str(input('Deseja continuar? [S/N]? ')).upper()[0]
    if keep in 'N':
        break
    cont += 2
    notas.clear()
print('-='*20)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>8}')
print('=' * 40)
for c in range(len(alunos_e_notas[0])):
    print(F'{c:<4} {alunos_e_notas[0][c]:<16} {alunos_e_notas[2][c]:.1f}')
print('-=' * 20)
while True:
    while True:
        print(f'{"-=-":^35}')
        keep = int(input('Qual o indicie a ser mostrado? 999 para parar. '))
        if keep >= 0 and keep < len(alunos_e_notas[0]) or keep == 999: break;
    if keep == 999: print('Até mais!'); break;
    print(f'Notas de {alunos_e_notas[0][keep]} são {alunos_e_notas[1][keep]}')
