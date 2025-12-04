class Nadador:
    def nadar(self):
        print("Nadando")

class Corredor:
    def correr(self):
        print("Corriendo")

class Atleta(Nadador, Corredor):
    def __init__(self, nombre):
        self.nombre = nombre

Nicolas_Santiago_Ruiz_Suarez = Atleta("Nicolas_Santiago_Ruiz_Suarez")
Nicolas_Santiago_Ruiz_Suarez.nadar()
Nicolas_Santiago_Ruiz_Suarez.correr()