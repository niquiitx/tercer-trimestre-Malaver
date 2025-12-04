class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anos(self):
        self.edad += 1

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez", 25)
Nicolas_Santiago_Ruiz_Suarez.cumplir_anos()
print(Nicolas_Santiago_Ruiz_Suarez.edad)