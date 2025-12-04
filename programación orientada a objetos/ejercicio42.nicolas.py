

class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
    def promedio(self):
        return sum(self.notas) / len(self.notas)

Nicolas_Santiago_Ruiz_Suarez = Estudiante("Nicolas_Santiago_Ruiz_Suarez", [80, 90, 70])
print(Nicolas_Santiago_Ruiz_Suarez.promedio())


