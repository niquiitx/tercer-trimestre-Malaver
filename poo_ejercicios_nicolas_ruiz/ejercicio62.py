class CuentaNicolasRuiz62:
    def __init__(self, titular_nicolas_ruiz_62, saldo_nicolas_ruiz_62=0):
        self.titular_nicolas_ruiz_62 = titular_nicolas_ruiz_62
        self.saldo_nicolas_ruiz_62 = saldo_nicolas_ruiz_62
    def depositar_nicolas_ruiz_62(self, monto_nicolas_ruiz_62):
        self.saldo_nicolas_ruiz_62 += monto_nicolas_ruiz_62
        print(self.titular_nicolas_ruiz_62, "saldo:", self.saldo_nicolas_ruiz_62)

cuenta_nicolas_ruiz_62 = CuentaNicolasRuiz62("Nicolas", 0)
cuenta_nicolas_ruiz_62.depositar_nicolas_ruiz_62(3100)