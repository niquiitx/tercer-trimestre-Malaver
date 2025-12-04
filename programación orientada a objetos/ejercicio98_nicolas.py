class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def duplicar(self):
        return Persona(self.nombre + " Jr.")

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas Santiago Ruiz Suarez")
nuevo_yeison = Nicolas_Santiago_Ruiz_Suarez.duplicar()
print(nuevo_yeison.nombre)