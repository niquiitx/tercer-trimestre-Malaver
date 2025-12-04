

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return f"Persona: {self.nombre}"

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez")
print(Nicolas_Santiago_Ruiz_Suarez)



