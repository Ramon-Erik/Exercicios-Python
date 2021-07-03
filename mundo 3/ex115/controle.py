color = {
    'verde': '\033[92m', 'verm.': '\033[31m',
    'azul': '\033[94m', 'branco': '\033[m',
    'amarelo': '\033[93m', 'v. claro': '\033[91m',
    'am. claro': '\033[93m'} 

def leia_int(msg):
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            print('\nO usuario preferiu não digitar os números')
            return 0
        except:
            print('\033[31mERRO: valor inteiro inválido\033[m')
        else:
            break
    return num


def titulo(msg):
    print('=' * 40)
    print(f'{msg:^39}')
    print('=' * 40)


def mostra_cadastros():
    from time import sleep
    titulo('PESSOAS CADASTRADAS')
    with open('001PythonExercícios/ex115/cadastros.txt', 'r') as file_cads:
        file_cads.seek(0)
        if len(file_cads.readline()) == 0:
            print(f'{"--":^39}')
            print(f'{"SEM REGISTROS AINDA":^39}')
            print(f'{"--":^39}')
        else:
            print(f'{"NOMES":<34}{"IDADES":>6}')
            sleep(0.5)
        file_cads.seek(0)
        with open('001PythonExercícios/ex115/cadastros.txt', 'r') as arquivo:
            for linha in arquivo.readlines():
                obj = linha.split('+')
                print(color['am. claro'], end='')
                print(f'{obj[0]:<37}{color["azul"]}{obj[1]:>4}', end='')
                print(color['branco'], end='')
                sleep(0.5)


def cadastrar_pessoa():
    titulo('CADASTRE ALGUÉM')
    nome = str(input(f'{color["am. claro"]}nome: ')).title()
    idade = leia_int(f'{color["verde"]}idade: ')
    print(f'{color["azul"]}Cadastro adicionado com sucesso.{color["branco"]}')
    with open('001PythonExercícios/ex115/cadastros.txt', 'a') as file:
        file.write(f'{nome}+{idade}' + '\n')


def resp_certa(option):
    if len(option) == 1 and option == '1' or option == '2' or option == '3':
        return True 


def mostra_resp(escolha):
    if resp_certa(escolha):
        if escolha == '1':
                cadastrar_pessoa()
        elif escolha == '2':
            mostra_cadastros()


def menu():
    titulo('SISTEMA PRINCIPAL')
    print(f'{color["amarelo"]}1 - {color["azul"]}adicionar mais uma pessoa a lista{color["branco"]}')
    print(f'{color["amarelo"]}2 - {color["azul"]}mostrar lista de pessoas{color["branco"]}')
    print(f'{color["amarelo"]}3 - {color["azul"]}sair do projeto{color["branco"]}')
    print('=' * 40)
