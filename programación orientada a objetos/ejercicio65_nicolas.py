class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self, otra_persona):
        print(f"Hola {otra_persona}, soy {self.nombre}")

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez")
Nicolas_Santiago_Ruiz_Suarez.saludar("Juan")