

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.set_edad(edad)

    def set_edad(self, edad):
        if edad < 0:
            self.edad = 0
        else:
            self.edad = edad

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas Santiago Ruiz Suarez", -5)
print(Nicolas_Santiago_Ruiz_Suarez.edad)