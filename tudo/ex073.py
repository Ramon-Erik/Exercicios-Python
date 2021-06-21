primeiros_colocados =  ('Corinthias', 'Palmeiras', 'Santos',
    'Grêmio', 'Cruzeiro', 'Flamengo',
    'Vasco', 'Chapecoence', 'Atlético',
    'BotaFogo', 'Atlético-PR', 'Bahia',
    'São Paulo', 'Fluminence', 'Sport Recife',
    'EC  Vitória', 'Curitiba', 'Avaí',
    'Ponte Preta', 'Atlético-GO')
print("A tupla completa: ", primeiros_colocados)
print('=-' * 23)
print('5 primeiros colocados ', primeiros_colocados[0:5])
print('=-' * 23)
print('Os 4 ultimos ', primeiros_colocados[-4:])
print('=-' * 23)
print('Em ordem alfábetica ', sorted(primeiros_colocados))
print('=-' * 23)
print(f'Chapecoence esta na {primeiros_colocados.index("Chapecoence")+1}a posição' )
