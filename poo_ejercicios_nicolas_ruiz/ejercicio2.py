class CuentaNicolasRuiz2:
    def __init__(self, titular_nicolas_ruiz_2, saldo_nicolas_ruiz_2=0):
        self.titular_nicolas_ruiz_2 = titular_nicolas_ruiz_2
        self.saldo_nicolas_ruiz_2 = saldo_nicolas_ruiz_2
    def depositar_nicolas_ruiz_2(self, monto_nicolas_ruiz_2):
        self.saldo_nicolas_ruiz_2 += monto_nicolas_ruiz_2
        print(self.titular_nicolas_ruiz_2, "saldo:", self.saldo_nicolas_ruiz_2)

cuenta_nicolas_ruiz_2 = CuentaNicolasRuiz2("Nicolas", 0)
cuenta_nicolas_ruiz_2.depositar_nicolas_ruiz_2(100)