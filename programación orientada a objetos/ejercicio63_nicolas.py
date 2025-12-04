class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def crear_amigo(self, nombre_amigo):
        return Persona(nombre_amigo)

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez")
amigo = Nicolas_Santiago_Ruiz_Suarez.crear_amigo("Juan")
print(amigo.nombre)