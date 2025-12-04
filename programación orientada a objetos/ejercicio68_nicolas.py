class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def interes(self, porcentaje):
        self.saldo += self.saldo * porcentaje / 100

Nicolas_Santiago_Ruiz_Suarez = Cuenta("Nicolas_Santiago_Ruiz_Suarez", 1000)
Nicolas_Santiago_Ruiz_Suarez.interes(5)
print(Nicolas_Santiago_Ruiz_Suarez.saldo)