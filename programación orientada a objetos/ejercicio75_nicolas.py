class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

Nicolas_Santiago_Ruiz_Suarez = CuentaBancaria("Nicolas_Santiago_Ruiz_Suarez", 1000)
Nicolas_Santiago_Ruiz_Suarez.retirar(200)
print(Nicolas_Santiago_Ruiz_Suarez.saldo)