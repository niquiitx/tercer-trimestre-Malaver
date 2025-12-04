

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

Nicolas_Santiago_Ruiz_Suarez = Curso("software")
Nicolas_Santiago_Ruiz_Suarez.agregar_estudiante("Nicolas_Santiago_Ruiz_Suarez")
print(Nicolas_Santiago_Ruiz_Suarez.estudiantes)



