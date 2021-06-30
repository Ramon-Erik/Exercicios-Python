def leia_int(msg):
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            print('\nO usuario preferiu não digitar os números')
            return 0
        except:
            print('\033[31mERRO: valor inteiro inválido\033[m')
        else:
            break
    return num


def leia_float(msg):
    while True:
        try:
            num = float(input(msg))
        except KeyboardInterrupt:
            print('\nO usuario preferiu não digitar os números')
            return 0
        except:
            print('\033[31mERRO: valor float inválido\033[m')
        else:
            break
    return num

num_int = leia_int('Informe um valor ineiro: ')
num_float = leia_float('Informe um valor real: ')
print(f'Você digitou o inteiro: \033[32m{num_int}\033[m e o valor real \033[33m{num_float}\033[m')
