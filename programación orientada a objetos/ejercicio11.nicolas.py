 

class Banco:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    def mostrar_saldo(self):
        print(self.__saldo)

Nicolas_Santiago_Ruiz_Suarez = Banco("Nicolas_Santiago_Ruiz_Suarez", 1000)
Nicolas_Santiago_Ruiz_Suarez.mostrar_saldo()




