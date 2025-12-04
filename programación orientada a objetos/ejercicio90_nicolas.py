class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def crear_hijo(self):
        return Persona(self.nombre + " Jr.")

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas Santiago Ruiz Suarez")
hijo = Nicolas_Santiago_Ruiz_Suarez.crear_hijo()
print(hijo.nombre)