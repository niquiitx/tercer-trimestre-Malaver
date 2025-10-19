class CuentaNicolasRuiz42:
    def __init__(self, titular_nicolas_ruiz_42, saldo_nicolas_ruiz_42=0):
        self.titular_nicolas_ruiz_42 = titular_nicolas_ruiz_42
        self.saldo_nicolas_ruiz_42 = saldo_nicolas_ruiz_42
    def depositar_nicolas_ruiz_42(self, monto_nicolas_ruiz_42):
        self.saldo_nicolas_ruiz_42 += monto_nicolas_ruiz_42
        print(self.titular_nicolas_ruiz_42, "saldo:", self.saldo_nicolas_ruiz_42)

cuenta_nicolas_ruiz_42 = CuentaNicolasRuiz42("Nicolas", 0)
cuenta_nicolas_ruiz_42.depositar_nicolas_ruiz_42(2100)