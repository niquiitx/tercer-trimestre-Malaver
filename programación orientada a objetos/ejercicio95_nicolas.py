
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas Santiago Ruiz Suarez")
Nicolas_Santiago_Ruiz_Suarez.saludar()
