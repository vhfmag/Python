from random import randint
class Dados:
    def __init__(self):
        print('Comecou o jogo de dados!')

    def lanca(self):
        self.dado = randint(1, 6)
        return self.dado

    def resultado(self):
        self.res = self.lanca()
        return print(f'Saiu: {self.res}')
