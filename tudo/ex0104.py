def valide(num):
    quebra = True
    for carac in num:
        if carac.isalpha(): 
            quebra = False
            break
    if len(num) == 0:
        quebra = False
    return quebra


def leia_int(msg):
    while True:
        n = input(msg).strip()
        if valide(n):
            break
        print(f"\033[31mErro;'{n}' não é número inteiro válido.\033[m")
    return n


# Programa principal
n = leia_int('Informe um número: ')
print(f'\033[32mVocê digitou o valor {n}\33[m')
