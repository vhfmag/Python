class Bola:

    def __init__(self, cor=None, circ=None, material=None):
        self.cor = cor
        self.circ = circ
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        return self.cor


bola = Bola(circ=30, cor='Vermelho', material='Plástico')
print(bola.mostraCor())
bola.trocaCor('Azul')
print(bola.mostraCor())
