class Contraseña:
    def __init__(self, clave):
        self.__clave = clave
    def mostrar_clave(self):
        print(self.__clave)

Nicolas_Santiago_Ruiz_Suarez = Contraseña("12345")
Nicolas_Santiago_Ruiz_Suarez.mostrar_clave()