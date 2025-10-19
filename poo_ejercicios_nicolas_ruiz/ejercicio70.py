class AlumnoNicolasRuiz70:
    def __init__(self, nombre_nicolas_ruiz_70, nota1_nicolas_ruiz_70, nota2_nicolas_ruiz_70):
        self.nombre_nicolas_ruiz_70 = nombre_nicolas_ruiz_70
        self.nota1_nicolas_ruiz_70 = nota1_nicolas_ruiz_70
        self.nota2_nicolas_ruiz_70 = nota2_nicolas_ruiz_70
    def promedio_nicolas_ruiz_70(self):
        print((self.nota1_nicolas_ruiz_70 + self.nota2_nicolas_ruiz_70)/2)
a_nicolas_ruiz_70 = AlumnoNicolasRuiz70("Alumno70", 3, 4)
a_nicolas_ruiz_70.promedio_nicolas_ruiz_70()