n1 = int(input('\033[34mDigite um valor:\033[m '))
n2 = int(input('\033[31mDigite outro valor:\033[m'))

if n1 > n2:
    print(f'\033[34m{n1}\033[m é maior que \033[31m{n2}\033[m')
elif n1 == n2:
    print('\033[32mNão tem valor maior, ambos são igauis.\033[m')
elif n1 < n2:
    print(f'\033[34m{n1}\033[m é menor que \033[31m{n2}\033[m')
