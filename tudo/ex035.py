print('—=—' * 15)
print('Analisador de triângulos.')
print('—=—' * 15)


s1 = float(input('Reta 1: '))
s2 = float(input('Reta 2: '))
s3 = float(input('Reta 3: '))


if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Pode formar um triângulo. ')
else:
    print('Não pode formar uma reta.')
