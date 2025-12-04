class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.atributos = {}

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez")
Nicolas_Santiago_Ruiz_Suarez.atributos["altura"] = 1.75
print(Nicolas_Santiago_Ruiz_Suarez.atributos)