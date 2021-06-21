mu = 0
me = 0
ho = 0
no = 0
for p in range(1, 5):
    print(f'----*---- {p}° PESSOA: ----*----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))    
    sexo = str(input('Sexo (M/F): ')).upper()
    if sexo  == 'F' and idade <= 20:
        mu += 1
    me += idade
    if p == 1 and sexo == 'M':
        ho = idade
        no = nome
    if sexo == 'M' and idade > ho:
        ho = idade
        no = nome
print('------------------------------')
med = me / 4

print('''>>A media de idade do grupo é de {:.1f} anos.
	
>>Ao todo são {} mulheres com menos de 20.

>>O nome do homem mais velho é {} e a idade é de: {} anos.'''.format(med, mu, no, ho))
