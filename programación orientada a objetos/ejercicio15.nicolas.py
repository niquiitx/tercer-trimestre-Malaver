

class Nadador:
    def nadar(self):
        print("trotando")

class Corredor:
    def correr(self):
        print("trepando")

class Atleta(Nadador, Corredor):
    pass

Nicolas_Santiago_Ruiz_Suarez = Atleta()
Nicolas_Santiago_Ruiz_Suarez.nadar()
Nicolas_Santiago_Ruiz_Suarez.correr()


