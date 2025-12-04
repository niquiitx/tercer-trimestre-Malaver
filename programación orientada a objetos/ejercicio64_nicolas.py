class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def __repr__(self):
        return f"Vehiculo('{self.tipo}', {self.velocidad})"

Nicolas_Santiago_Ruiz_Suarez = Vehiculo("Bicicleta", 20)
print(repr(Nicolas_Santiago_Ruiz_Suarez))