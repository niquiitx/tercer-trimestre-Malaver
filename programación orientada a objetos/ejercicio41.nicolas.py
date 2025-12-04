
class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def obtener_velocidad(self):
        return self.velocidad

Nicolas_Santiago_Ruiz_Suarez = Vehiculo("Moto", 80)
print(Nicolas_Santiago_Ruiz_Suarez.obtener_velocidad())


