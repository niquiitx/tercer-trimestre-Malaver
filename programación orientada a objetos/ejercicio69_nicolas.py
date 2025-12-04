class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
    def mostrar_materias(self, materias):
        for m in materias:
            print(f"{self.nombre} estudia {m}")

Nicolas_Santiago_Ruiz_Suarez = Alumno("Nicolas_Santiago_Ruiz_Suarez")
Nicolas_Santiago_Ruiz_Suarez.mostrar_materias(["Matemáticas", "Física"])