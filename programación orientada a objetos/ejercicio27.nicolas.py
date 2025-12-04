

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez", 25)
Nicolas_Santiago_Ruiz_Suarez.presentarse()



