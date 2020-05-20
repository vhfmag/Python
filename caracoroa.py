from random import randint
from time import sleep


class Caracoroa:

    def __init__(self):

        print('Jogo iniciado!!')


    def lanca(self):
        lado = randint(0, 1)
        return lado

    def vence(self):

        self.res = self.lanca()
        if self.res == 0:
            return print('Deu cara!')
        else:
            return print('Deu coroa!')

