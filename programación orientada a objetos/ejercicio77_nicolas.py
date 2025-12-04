class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def acelerar(self, aumento):
        self.velocidad += aumento

Nicolas_Santiago_Ruiz_Suarez = Vehiculo("Coche", 50)
Nicolas_Santiago_Ruiz_Suarez.acelerar(20)
print(Nicolas_Santiago_Ruiz_Suarez.velocidad)