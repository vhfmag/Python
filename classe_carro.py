
class Carro():

    def __init__(self, fabricante, modelo, portas, motor, rpm):
        self.fabricante = fabricante
        self.modelo = modelo
        self.portas = portas
        self.motor = motor
        self.rpm = rpm
        print('Carro criado!')

    def ligar(self):
        from time import sleep
        self.ligado = True
        print('Dando partida...')
        sleep(1)
        print('Carro ligado!')

    def desligar(self, ligado):
        if
        self.ligado = False

    def locomover(self, *velocidade):
        if self.ligado == True:
            self.velocidade = int(input('Insira a velocidade: '))
            print(f'Carro andando à {self.velocidade}')
        else:
            print('Carro precisa estar ligado para se locomover!!')
