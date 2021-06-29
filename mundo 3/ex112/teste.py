from utilidades_cev.dados import leia_dinheiro
from utilidades_cev.moeda import resumo 

preço = leia_dinheiro('Informe o valor... R$')
resumo(preço, 20, 8)
