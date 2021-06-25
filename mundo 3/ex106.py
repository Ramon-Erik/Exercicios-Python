cores = ('\033[m',  # cor anulada
    '\033[0;30;41m', # vermelho
    '\033[0;30;42m', # verde
    '\033[0;30;44m', # azul
    '\033[0;30;43m' ) # branco

def interactve_help(item):
    from time import sleep
    print(cores[3])
    print('~' * 30)
    print(f"Acessando o manual do comando '{item}'", flush=True)
    print('~' * 30)
    print(cores[0])
    sleep(1)
    print(cores[4])
    help(item)
    print(cores[0])


def titulo(msg, cor=0):
    print(cores[cor])
    size = len(msg)+4
    print('~' * size)
    print(f' {msg}')
    print('~' * size)
    print(cores[0])


while True:
    titulo('Sistema de ajuda ;)', 2)
    comando = str(input(' Biblioteca ou função > ')).lower()
    if comando == 'fim':
        print(cores[1])
        print('~' * 27)
        print('Ate mais')
        print('~' * 27)
        print(cores[0])
        break
    interactve_help(comando)
