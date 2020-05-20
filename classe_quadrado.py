class Quadrado:
    
    def __init__(self, lado):
        self.lado = lado

    def mudaLado(self, lado):
        self.lado = lado

    def mostraLado(self):
        return self.lado

    def calcArea(self):
        return pow(self.lado, 2)

quadrado = Quadrado(5)

print(quadrado.mostraLado())
quadrado.mudaLado(7)
print(quadrado.mostraLado())
print(quadrado.calcArea())
