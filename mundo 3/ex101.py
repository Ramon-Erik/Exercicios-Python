def voto(ano_nasc):
    from datetime import date

    idade = date.today().year -  ano_nasc
    if idade >= 16:
        if idade >= 65:
            return f'Com a sua idade, ({idade}), o voto é: OPCIONAL'
        return f'Com a sua idade, ({idade}), o voto é: OBRIGATÓRIO'
    else:
        return f'Com a sua idade, ({idade}), o voto é: NEGADO'


print('~' * 30)
ano = int(input('Em que ano voê nasceu? '))
print(voto(ano))