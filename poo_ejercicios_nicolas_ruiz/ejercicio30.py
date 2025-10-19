class AlumnoNicolasRuiz30:
    def __init__(self, nombre_nicolas_ruiz_30, nota1_nicolas_ruiz_30, nota2_nicolas_ruiz_30):
        self.nombre_nicolas_ruiz_30 = nombre_nicolas_ruiz_30
        self.nota1_nicolas_ruiz_30 = nota1_nicolas_ruiz_30
        self.nota2_nicolas_ruiz_30 = nota2_nicolas_ruiz_30
    def promedio_nicolas_ruiz_30(self):
        print((self.nota1_nicolas_ruiz_30 + self.nota2_nicolas_ruiz_30)/2)
a_nicolas_ruiz_30 = AlumnoNicolasRuiz30("Alumno30", 3, 4)
a_nicolas_ruiz_30.promedio_nicolas_ruiz_30()