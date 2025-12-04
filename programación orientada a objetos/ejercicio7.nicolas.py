
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def info(self):
        print(f"moto: {self.marca} {self.modelo}")

Nicolas_Santiago_Ruiz_Suarez = Vehiculo("bmw", "voge")
Nicolas_Santiago_Ruiz_Suarez.info()




