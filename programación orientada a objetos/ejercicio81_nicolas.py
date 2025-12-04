class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, cantidad):
        self.saldo += cantidad

Nicolas_Santiago_Ruiz_Suarez = Cuenta("Nicolas_Santiago_Ruiz_Suarez", 1000)
Nicolas_Santiago_Ruiz_Suarez.depositar(500)
print(Nicolas_Santiago_Ruiz_Suarez.saldo)