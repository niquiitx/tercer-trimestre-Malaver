class AlumnoNicolasRuiz10:
    def __init__(self, nombre_nicolas_ruiz_10, nota1_nicolas_ruiz_10, nota2_nicolas_ruiz_10):
        self.nombre_nicolas_ruiz_10 = nombre_nicolas_ruiz_10
        self.nota1_nicolas_ruiz_10 = nota1_nicolas_ruiz_10
        self.nota2_nicolas_ruiz_10 = nota2_nicolas_ruiz_10
    def promedio_nicolas_ruiz_10(self):
        print((self.nota1_nicolas_ruiz_10 + self.nota2_nicolas_ruiz_10)/2)
a_nicolas_ruiz_10 = AlumnoNicolasRuiz10("Alumno10", 3, 4)
a_nicolas_ruiz_10.promedio_nicolas_ruiz_10()