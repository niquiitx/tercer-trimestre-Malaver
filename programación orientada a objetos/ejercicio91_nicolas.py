class Luz:
    def __init__(self):
        self.encendida = False
    def cambiar_estado(self):
        self.encendida = not self.encendida

Nicolas_Santiago_Ruiz_Suarez = Luz()
Nicolas_Santiago_Ruiz_Suarez.cambiar_estado()
print(Nicolas_Santiago_Ruiz_Suarez.encendida)