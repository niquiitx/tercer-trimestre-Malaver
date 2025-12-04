
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def aplicar_descuento(self, porcentaje):
        self.precio *= (1 - porcentaje/100)

Nicolas_Santiago_Ruiz_Suarez = Producto("traje", 50)
Nicolas_Santiago_Ruiz_Suarez.aplicar_descuento(20)
print(Nicolas_Santiago_Ruiz_Suarez.precio)




