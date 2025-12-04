
class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def __gt__(self, otro):
        return self.velocidad > otro.velocidad

v1 = Vehiculo("Coche", 120)
v2 = Vehiculo("Moto", 100)
Nicolas_Santiago_Ruiz_Suarez = v1 > v2
print(Nicolas_Santiago_Ruiz_Suarez)