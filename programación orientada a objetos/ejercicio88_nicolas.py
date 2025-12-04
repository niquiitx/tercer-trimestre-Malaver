class Animal:
    def sonido(self):
        print("Hace un sonido")

class Perro(Animal):
    def sonido(self):
        print("Guau!")

Nicolas_Santiago_Ruiz_Suarez = Perro()
Nicolas_Santiago_Ruiz_Suarez.sonido()
