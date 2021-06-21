nome = str(input('>>Seu nome completo:\n')).strip()
print('>>No seu nome há ', nome.upper().count('A'), 'letra(s) A.')
print('>>Aparece na posição ', nome.upper().find('A')+1)
print('>>A última aparição é na ', nome.upper().rfind('A') + 1)