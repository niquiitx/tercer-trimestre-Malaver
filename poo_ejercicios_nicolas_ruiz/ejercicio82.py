class CuentaNicolasRuiz82:
    def __init__(self, titular_nicolas_ruiz_82, saldo_nicolas_ruiz_82=0):
        self.titular_nicolas_ruiz_82 = titular_nicolas_ruiz_82
        self.saldo_nicolas_ruiz_82 = saldo_nicolas_ruiz_82
    def depositar_nicolas_ruiz_82(self, monto_nicolas_ruiz_82):
        self.saldo_nicolas_ruiz_82 += monto_nicolas_ruiz_82
        print(self.titular_nicolas_ruiz_82, "saldo:", self.saldo_nicolas_ruiz_82)

cuenta_nicolas_ruiz_82 = CuentaNicolasRuiz82("Nicolas", 0)
cuenta_nicolas_ruiz_82.depositar_nicolas_ruiz_82(4100)