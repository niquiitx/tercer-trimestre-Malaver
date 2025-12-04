class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    def mostrar_nombre(self):
        print(self.__nombre)

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez")
Nicolas_Santiago_Ruiz_Suarez.mostrar_nombre()