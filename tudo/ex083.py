cont = temp = 0
ex = str(input('\nDigite uma expressão que use parentêses: ')).upper()
pa_aberto, pa_fechado = ex.count("("), ex.count(")")

if pa_aberto != pa_fechado:
    print("Sua expressão está incorreta.")
    if pa_aberto > pa_fechado:
        temp = pa_fechado
        while pa_aberto > temp:
            temp += 1
            cont += 1
        print("Faltaram {} parênteses fechados.".format(cont))
    else:
        temp = pa_aberto
        while temp < pa_fechado:            
            temp += 1
            cont += 1
        print("Faltaram {} parênteses abertos.".format(cont))
else:
    print("Sua expressão esta correta.")
print("Você digitou {} parênteses no total. {} abertos e {} fechados.".format(pa_aberto + pa_fechado, pa_aberto, pa_fechado))
