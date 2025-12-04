class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

Nicolas_Santiago_Ruiz_Suarez = Profesor("Nicolas_Santiago_Ruiz_Suarez")
Nicolas_Santiago_Ruiz_Suarez.agregar_materia("Matemáticas")
print(Nicolas_Santiago_Ruiz_Suarez.materias)