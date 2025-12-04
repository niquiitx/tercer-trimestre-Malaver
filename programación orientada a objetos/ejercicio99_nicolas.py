class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __repr__(self):
        return f"Persona('{self.nombre}')"

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas Santiago Ruiz Suarez")
print(repr(Nicolas_Santiago_Ruiz_Suarez))