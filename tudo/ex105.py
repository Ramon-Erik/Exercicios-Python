def situacao(*args, aprov=False):
    """=> Analiza as notas e a situação dos alunos
    :param args: notas
    :param aprov: situação com base na média
    :return: retorna o dicionário"""
    boletim = dict()
    boletim['total'] = len(args) 
    boletim['maior'] = max(args)
    boletim['menor'] = min(args)
    boletim['média'] = (sum(args) / len(args))
    if aprov:
        if boletim['média'] >= 7:
            sit = 'Bom'
        elif boletim['média'] >= 5 and boletim['média'] < 7:
            sit = 'Razoavel'
        else:
            sit = 'Péssimo'
        boletim['aproveitamento'] = sit
    return boletim

notas = situacao(4, 6, 1, 9, 4, 9.2, 10, aprov=True)
help(situacao)
print(notas)
