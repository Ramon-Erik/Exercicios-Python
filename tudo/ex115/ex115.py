from controle import menu, mostra_resp, resp_certa, titulo

color = {'verde': '\033[92m', 'verm.': '\033[91m', 'branco': '\033[m'}

while True:
    menu()
    resp = str(input(f'{color["verde"]}Sua escolha: {color["branco"]}')).strip()
    while not resp_certa(resp):
        resp = str(input(f'{color["verm."]}Sua escolha: {color["branco"]}')).strip()
    if resp in '3':
        break
    mostra_resp(resp)

titulo('SAINDO DO SISTMA! VOLTE SEMPRE ;)')
