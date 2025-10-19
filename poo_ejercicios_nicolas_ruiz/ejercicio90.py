class AlumnoNicolasRuiz90:
    def __init__(self, nombre_nicolas_ruiz_90, nota1_nicolas_ruiz_90, nota2_nicolas_ruiz_90):
        self.nombre_nicolas_ruiz_90 = nombre_nicolas_ruiz_90
        self.nota1_nicolas_ruiz_90 = nota1_nicolas_ruiz_90
        self.nota2_nicolas_ruiz_90 = nota2_nicolas_ruiz_90
    def promedio_nicolas_ruiz_90(self):
        print((self.nota1_nicolas_ruiz_90 + self.nota2_nicolas_ruiz_90)/2)
a_nicolas_ruiz_90 = AlumnoNicolasRuiz90("Alumno90", 3, 4)
a_nicolas_ruiz_90.promedio_nicolas_ruiz_90()