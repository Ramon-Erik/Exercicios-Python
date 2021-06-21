lista = []
for per in range(1, 6):
    peso = lista.append(float(input(f'Peso da {per}° pessoa: Kg ')))
print('O peso maior é de Kg {:.3f}!!\nE o menor {:.3f}!!'.format(max(lista), min(lista)))
