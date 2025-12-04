 

class Secreto:
    def __init__(self, mensaje):
        self.__mensaje = mensaje
    def revelar(self):
        print(self.__mensaje)

Nicolas_Santiago_Ruiz_Suarez = Secreto("Nicolas_Santiago_Ruiz_Suarez")
Nicolas_Santiago_Ruiz_Suarez.revelar()

