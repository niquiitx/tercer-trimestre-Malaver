

class Auto:
    def __init__(self, marca):
        self.marca = marca
        self.encendido = False
    def encender(self):
        self.encendido = True
    def apagar(self):
        self.encendido = False

Nicolas_Santiago_Ruiz_Suarez = Auto("Toyota")
Nicolas_Santiago_Ruiz_Suarez.encender()
print(Nicolas_Santiago_Ruiz_Suarez.encendido)




