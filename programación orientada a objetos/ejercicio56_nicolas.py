
class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def __str__(self):
        return f"{self.tipo} a {self.velocidad} km/h"

Nicolas_Santiago_Ruiz_Suarez = Vehiculo("Coche", 100)
print(Nicolas_Santiago_Ruiz_Suarez)



