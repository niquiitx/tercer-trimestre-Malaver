

class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class Tienda:
    def __init__(self):
        self.inventario = []
    def agregar_producto(self, producto):
        self.inventario.append(producto)

Nicolas_Santiago_Ruiz_Suarez = Producto("Laptop", 5)
mi_tienda = Tienda()
mi_tienda.agregar_producto(Nicolas_Santiago_Ruiz_Suarez)
print([(p.nombre, p.cantidad) for p in mi_tienda.inventario])



class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def acelerar(self, incremento):
        self.velocidad += incremento
    def frenar(self, decremento):
        self.velocidad -= decremento

Nicolas_Santiago_Ruiz_Suarez = Vehiculo("Coche", 60)
Nicolas_Santiago_Ruiz_Suarez.acelerar(20)
Nicolas_Santiago_Ruiz_Suarez.frenar(10)
print(Nicolas_Santiago_Ruiz_Suarez.velocidad)