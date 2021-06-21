n = str(input('>>Digite seu nome completo.\n')).title().strip().split()
print(f'>>o seu primeiro nome é: "{n[0]}".')
print('>>Já o último é: "{}"'.format(n[len(n) - 1]))