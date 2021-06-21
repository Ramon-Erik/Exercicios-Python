km = int(input('Informe os quilômetros a serem percorridos: \n'))
if km <= (200):
    print(f'Você pagará R${km * 0.50:.2f} pela sua viagem de {km}Km')
else:
    print(f'Você pagara R${km * 0.45:.2f} pela sua viagem de {km}Km.')
