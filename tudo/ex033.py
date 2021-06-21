v1 = int(input('1° valor: '))
v2 = int(input('2° valor: '))
v3 = int(input('3° valor: '))
menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
maior = v3
if v2 > v3 and v2 > v1:
    maior = v2
if v1 > v3 and v1 > v2:
    maior = v1
print(f'O maior é {maior}.')
print(f'O menor é {menor}.')
