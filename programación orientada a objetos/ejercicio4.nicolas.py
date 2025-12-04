

class Persona:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

Nicolas_Santiago_Ruiz_Suarez1 = Persona("Nicolas_Santiago_Ruiz_Suarez")
Nicolas_Santiago_Ruiz_Suarez2 = Persona("Nicolas_Santiago_Ruiz_Suarez")
print(Persona.contador)


