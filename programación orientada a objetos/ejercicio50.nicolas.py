
class Persona:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1
    @classmethod
    def total_personas(cls):
        return cls.contador

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez")
otra_persona = Persona("Juan")
print(Persona.total_personas())


