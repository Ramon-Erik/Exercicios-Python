nome = str(input('>>Seu nome completo:\n')).strip()
print(f'>>Em maiúsculas:\n{nome.upper()}')
print(f'>>Em minúsculas:\n{nome.lower()}')
n = (len(nome) - nome.count(' '))
no = nome.split()
print(f'>>Seu nome tem {n} caracteres.')
print(f'Seu primeiro nome tem {len(no[0])} letras/caracteres')