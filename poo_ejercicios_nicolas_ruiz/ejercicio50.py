class AlumnoNicolasRuiz50:
    def __init__(self, nombre_nicolas_ruiz_50, nota1_nicolas_ruiz_50, nota2_nicolas_ruiz_50):
        self.nombre_nicolas_ruiz_50 = nombre_nicolas_ruiz_50
        self.nota1_nicolas_ruiz_50 = nota1_nicolas_ruiz_50
        self.nota2_nicolas_ruiz_50 = nota2_nicolas_ruiz_50
    def promedio_nicolas_ruiz_50(self):
        print((self.nota1_nicolas_ruiz_50 + self.nota2_nicolas_ruiz_50)/2)
a_nicolas_ruiz_50 = AlumnoNicolasRuiz50("Alumno50", 3, 4)
a_nicolas_ruiz_50.promedio_nicolas_ruiz_50()