

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

Nicolas_Santiago_Ruiz_Suarez = Estudiante("Nicolas_Santiago_Ruiz_Suarez", "Ingeniería")
print(Nicolas_Santiago_Ruiz_Suarez.nombre, Nicolas_Santiago_Ruiz_Suarez.carrera)


