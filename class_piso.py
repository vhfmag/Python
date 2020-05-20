class Piso:

    def __init__(self, base = None, altura = None):
        self.base = base
        self.altura = altura

    def mudaLado(self):

        op = int(input('Qual lado deseja mudar? [1] Altura / [2] Base'))
        while True:
            if op == 1:
                self.altura = float(input('Insira o valor da altura: '))
                break
            elif op == 2:
                self.base = float(input('Insira o valor da base: '))
                break
            else:
                print('Opcao nao permitida. Tente novamente:')
                op = int(input('Qual lado deseja mudar? [1] Altura / [2] Base'))
                continue

    def mostraLado(self):
        op = int(input('Qual lado deseja mostrar? [1] Altura / [2] Base: '))
        if op == 1:
            print(f'A altura vale: {self.altura}')
        elif op == 2:
            print(f'A base vale: {self.base}')

    def calcArea(self):

        return self.base * self.altura

    def calcPerimetro(self):

        return 2 * self.base + 2 * self.altura

# main
def main():

    print('Analisador de Terrenos!')
    a = float(input('Qual a altura: '))
    b = float(input('Qual a base: '))
    terreno = Piso()
    terreno.altura = a
    terreno.base = b
    print(terreno.calcArea())
    terreno.mudaLado()
    terreno.mostraLado()
    print(terreno.calcArea())
if __name__ == '__main__':
    main()