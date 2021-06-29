def metade(valor):
    novo_valor = valor / 2
    return novo_valor


def dobro(valor):
    novo_valor = valor * 2
    return novo_valor


def aumentar(valor, porcent):
    novo_valor = valor + (porcent * valor / 100)
    return novo_valor


def diminuir(valor, porcent):
    novo_valor = valor - (porcent * valor / 100)
    return novo_valor


def moeda(valor, tipo='R$'):
    novo_valor = f'{tipo}{valor:.2f}'.replace('.', ',')
    return novo_valor


