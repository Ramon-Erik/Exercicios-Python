p = float(input('Seu peso: ')) 
a = float(input('Sua altura: '))

imc = (p / (a ** 2))

if imc <18.5:
    print(f'Seu imc é {imc:.2f}, abaixo do peso.')
elif imc > 18.5 and imc < 25:
    print(f'Seu imc é {imc:.1f}, peso ideal.')
elif imc > 25 and imc < 30:
    print(f'Seu imc é {imc:.1f}, indica sobrepeso.')
elif imc > 30 and imc < 40:
    print(f'Seu imc é {imc:.1f}, indica obesidade.')
elif imc > 40:
    print(f'seu imc é {imc:.1f}, indica Obesidade morbida.')
print('Cuide da sua saúde :)')