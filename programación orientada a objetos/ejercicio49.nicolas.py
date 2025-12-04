


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self):
        self.estudiantes = []
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

Nicolas_Santiago_Ruiz_Suarez = Estudiante("Nicolas_Santiago_Ruiz_Suarez")
curso = Curso()
curso.agregar_estudiante(Nicolas_Santiago_Ruiz_Suarez)
print([e.nombre for e in curso.estudiantes])



class Persona:
    def actividad(self):
        print("Realizando actividad")

class Estudiante(Persona):
    def actividad(self):
        print("Estudiando")

Nicolas_Santiago_Ruiz_Suarez = Estudiante()
Nicolas_Santiago_Ruiz_Suarez.actividad()
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anos(self):
        self.edad += 1

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez", 25)
Nicolas_Santiago_Ruiz_Suarez.cumplir_anos()
print(Nicolas_Santiago_Ruiz_Suarez.edad)





