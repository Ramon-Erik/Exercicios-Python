def área(h, l):
    print(f' A área de um terreno {h:.2f}x{l:.2f} é de {h*l:.2f}m²')


print('=' * 27, '\n  Controle de Terreno\n', '=' * 27)
h = float(input('Altura (m): '))
l = float(input('largura (m): '))
área(h, l)
