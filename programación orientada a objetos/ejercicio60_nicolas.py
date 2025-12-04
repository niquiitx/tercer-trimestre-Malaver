class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asistencias = 0
    def registrar_asistencia(self):
        self.asistencias += 1

Nicolas_Santiago_Ruiz_Suarez = Alumno("Nicolas_Santiago_Ruiz_Suarez")
Nicolas_Santiago_Ruiz_Suarez.registrar_asistencia()
print(Nicolas_Santiago_Ruiz_Suarez.asistencias)