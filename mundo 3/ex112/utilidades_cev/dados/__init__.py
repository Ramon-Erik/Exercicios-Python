def leia_dinheiro(msg):
    carac_permit = '1234567890.,'
    while True:
        quebra = True
        num = input(msg).strip()
        for carac in num:
            if carac not in carac_permit:
                quebra = False
                break
        if len(num) == 0:
            quebra = False
        if quebra:
            break
        else:
            print(f'\033[31mERRO: "{num}" não é um valor monetário\033[m')
    return num

