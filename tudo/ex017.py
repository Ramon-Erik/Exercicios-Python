import emoji
from math import hypot
cateto_opos = float(input('Cateto oposto: '))
cateto_adja = float(input('Cateto adjacente: '))
hipotenusa = (hypot(cateto_opos, cateto_adja))
print(emoji.emojize(f'De acordo com os dados, a hipotenusa é igual a {hipotenusa:.2f} :nerd_face::thumbs_up:.'))