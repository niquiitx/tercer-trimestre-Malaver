

class Deportista:
    def entrenar(self):
        print("Entrenando")

class Musico:
    def tocar(self):
        print("Tocando música")

class Persona(Deportista, Musico):
    def __init__(self, nombre):
        self.nombre = nombre

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez")
Nicolas_Santiago_Ruiz_Suarez.entrenar()
Nicolas_Santiago_Ruiz_Suarez.tocar()



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hobbies = []
    def agregar_hobby(self, hobby):
        self.hobbies.append(hobby)

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez")
Nicolas_Santiago_Ruiz_Suarez.agregar_hobby("voleibol")
print(Nicolas_Santiago_Ruiz_Suarez.hobbies)