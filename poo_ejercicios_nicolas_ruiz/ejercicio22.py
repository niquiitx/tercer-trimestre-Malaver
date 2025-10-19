class CuentaNicolasRuiz22:
    def __init__(self, titular_nicolas_ruiz_22, saldo_nicolas_ruiz_22=0):
        self.titular_nicolas_ruiz_22 = titular_nicolas_ruiz_22
        self.saldo_nicolas_ruiz_22 = saldo_nicolas_ruiz_22
    def depositar_nicolas_ruiz_22(self, monto_nicolas_ruiz_22):
        self.saldo_nicolas_ruiz_22 += monto_nicolas_ruiz_22
        print(self.titular_nicolas_ruiz_22, "saldo:", self.saldo_nicolas_ruiz_22)

cuenta_nicolas_ruiz_22 = CuentaNicolasRuiz22("Nicolas", 0)
cuenta_nicolas_ruiz_22.depositar_nicolas_ruiz_22(1100)