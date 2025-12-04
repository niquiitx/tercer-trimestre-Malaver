

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

Nicolas_Santiago_Ruiz_Suarez = Estudiante("Nicolas_Santiago_Ruiz_Suarez")
matematicas = Curso()
matematicas.agregar_estudiante(Nicolas_Santiago_Ruiz_Suarez)
print([e.nombre for e in matematicas.estudiantes])

