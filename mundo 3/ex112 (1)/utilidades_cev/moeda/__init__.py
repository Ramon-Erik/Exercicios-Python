def to_float(valor):
    valor = str(valor)
    valor = valor.replace(',', '.')
    valor = float(valor)
    return valor


def metade(valor, format=True):
    valor = to_float(valor)
    novo_valor = valor / 2
    if format:
        return moeda(novo_valor)
    return novo_valor


def dobro(valor, format=True):
    valor = to_float(valor)
    novo_valor = valor * 2
    if format:
        return moeda(novo_valor)
    return novo_valor


def aumentar(valor, porcent, format=True):
    valor = to_float(valor)
    novo_valor = valor + (porcent * valor / 100)
    if format:
        return moeda(novo_valor)
    return novo_valor


def diminuir(valor, porcent, format=True):
    valor = to_float(valor)
    novo_valor = valor - (porcent * valor / 100)
    if format:
        return moeda(novo_valor)
    return novo_valor


def moeda(valor, tipo='R$'):
    valor = to_float(valor)
    novo_valor = f'{tipo}{valor:.2f}'.replace('.', ',')
    return novo_valor


def resumo(valor, aumenta, redução):
    print('=' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('=' * 30)
    print(f'{"preço informado":<20}{moeda(valor)}')
    print(f'{"metade:":<20}{metade(valor)}')
    print(f'{"dobro:":<20}{dobro(valor)}')
    print(f'{f"aumento de {aumenta}%:":<20}{aumentar(valor, aumenta)}')
    print(f'{f"redução de {redução}%:":<20}{diminuir(valor, redução)}')


