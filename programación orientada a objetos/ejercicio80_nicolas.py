class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Alumno(Persona):
    def estudiar(self):
        print(f"{self.nombre} está estudiando")

Nicolas_Santiago_Ruiz_Suarez = Alumno("Nicolas_Santiago_Ruiz_Suarez")
Nicolas_Santiago_Ruiz_Suarez.estudiar()