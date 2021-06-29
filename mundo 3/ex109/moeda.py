def metade(valor, format=False):
    novo_valor = valor / 2
    if format:
        return moeda(novo_valor)
    return novo_valor


def dobro(valor, format=False):
    novo_valor = valor * 2
    if format:
        return moeda(novo_valor)
    return novo_valor


def aumentar(valor, porcent, format=False):
    novo_valor = valor + (porcent * valor / 100)
    if format:
        return moeda(novo_valor)
    return novo_valor


def diminuir(valor, porcent, format=False):
    novo_valor = valor - (porcent * valor / 100)
    if format:
        return moeda(novo_valor)
    return novo_valor


def moeda(valor, tipo='R$'):
    novo_valor = f'{tipo}{valor:.2f}'.replace('.', ',')
    return novo_valor


