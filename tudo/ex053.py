frase = str(input('Sua frase: ')).upper().replace(' ', '')
if frase == frase[::-1]:
   print('Sua frase é um palíndromo!!! observe: ', frase[::-1])
else:
    print('A sua frase, não é um palíndromo!!')
print('\nPorém ao contrário fica: {}'.format(frase[::-1]))
