class Conta():
    saldo = 0.0

    def menu(self,op):
        pass

    def __init__(self):
        print('Conta criada com sucesso!')

    def deposita(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print(f'Erro! O valor {valor} nao pode ser depositado!')

    def saca(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor

    def mostrasaldo(self):
        return self.saldo
