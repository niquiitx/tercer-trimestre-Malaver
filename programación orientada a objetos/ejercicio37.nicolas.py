

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"{self.nombre} cuesta {self.precio} USD"

Nicolas_Santiago_Ruiz_Suarez = Producto("Mouse", 25)
print(Nicolas_Santiago_Ruiz_Suarez)



