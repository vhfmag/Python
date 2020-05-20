def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta
def deposita(conta, valor):
    conta['saldo'] += valor
def saque(conta, valor):
    conta['saldo'] -= valor
def extrato(conta):
    print(f'Numero: {conta["numero"]} e Saldo: {conta["saldo"]}')


