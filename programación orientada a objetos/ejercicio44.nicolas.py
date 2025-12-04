class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = []
    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez")
juan = Persona("pepe")
Nicolas_Santiago_Ruiz_Suarez.agregar_amigo(juan)
print([a.nombre for a in Nicolas_Santiago_Ruiz_Suarez.amigos])