from datetime import datetime

perfil, ano_atual = {}, datetime.today().year

perfil['nome'] = str(input('Nome: ')).capitalize()
perfil['idade'] = ano_atual - int(input('Ano de nascimento: '))
perfil['CTPS'] = int(input('Carteira de trabalho: [0 == não tem] '))

if  perfil['CTPS'] != 0:
    perfil['ano de contratação'] = int(input('    Ano de contratação: '))
    perfil['salário'] = float(input('    Salário: '))
    perfil['anos para se aposentar'] = (perfil['idade'] + (perfil['ano de contratação'] + 35) - ano_atual)
print('-=' * 30)
for chave, valor in perfil.items():
    print(f'     - {chave} tem o valor {valor}')
