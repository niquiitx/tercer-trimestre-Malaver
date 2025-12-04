
class Producto:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            print("Stock insuficiente")

Nicolas_Santiago_Ruiz_Suarez = Producto("Mouse", 10)
Nicolas_Santiago_Ruiz_Suarez.vender(3)
print(Nicolas_Santiago_Ruiz_Suarez.stock)




