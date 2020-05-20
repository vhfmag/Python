from POO.caracoroa import Caracoroa
from POO.dados import Dados
moeda = Caracoroa()
op = 0
while True:
    moeda.lanca()
    moeda.vence()
    op = int(input('Continua[1] ou para[0]? '))
    if op == 0:
        break
dado = Dados()
dado.resultado()
