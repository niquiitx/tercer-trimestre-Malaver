

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def estudiar(self):
        print(f"{self.nombre} está estudiando")

Nicolas_Santiago_Ruiz_Suarez = Estudiante("Nicolas_Santiago_Ruiz_Suarez")
Nicolas_Santiago_Ruiz_Suarez.estudiar()


