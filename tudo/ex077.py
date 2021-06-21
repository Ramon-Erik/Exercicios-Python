tupla = ('Python', 'felicidade', 'gratuito',
	'amor', 'por', 'aprender',
	'programador', 'curso', 'mercado',
	'trabalho', 'passaro', 'participar',
	'futiro', 'linguagem', 'estudar',
    'ventilador', 'cama', 'cabceira',
    'exe', 'extension')

vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in tupla:
    print(f'\nNa palavra {palavra.upper()} tem as vogais', end=' ')
    for letra in palavra:
        if letra in vogais:
            print(vogais[vogais.index(letra)].upper(), end=' ')
