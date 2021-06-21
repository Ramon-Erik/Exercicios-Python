from datetime import date
print(' ')
print('≈' * 46)


ano = int(input('Ano em que você  nasceu: ')) # ano do participante
atual =  date.today().year# ano atual
i = (atual- ano) # idade dele

print('≈' *46)
print(' ')

print(f'                Sua idade: {i}')



#14 infantil
#19 júnior
#20 senior
#acima master


print(' ')
print('×' * 46)
print(' ')


if i > 6 and i <= 9:
    print('Dado a sua idade, você é do grupo "mirim". ')

elif i < 6:
    print('Muito jovem. necessário ter no mínimo 7 anos \nde idade. ')
    exit()

elif i > 9 and i <= 14:
    print('Dado a sua idade, você é do grupo "infantil".')

elif i > 14 and i <= 19:
    print('Dado a sua idade, você é do grupo "junior".')

elif i == 20:
    print('Dado a sua idade, você é do grupo "sênior".')

elif i > 20:
    print('Dado a sua idade, você é do grupo "master".')
print(' ')
print('='*46)