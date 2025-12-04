

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

class Curso:
    def __init__(self):
        self.estudiantes = []
    def agregar(self, estudiante):
        self.estudiantes.append(estudiante)
    def aprobados(self):
        return [e.nombre for e in self.estudiantes if e.nota >= 60]

Nicolas_Santiago_Ruiz_Suarez = Estudiante("Nicolas_Santiago_Ruiz_Suarez", 75)
curso = Curso()
curso.agregar(Nicolas_Santiago_Ruiz_Suarez)
print(curso.aprobados())


