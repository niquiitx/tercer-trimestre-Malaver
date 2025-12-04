class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datos = {}

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez")
Nicolas_Santiago_Ruiz_Suarez.datos["edad"] = 25
print(Nicolas_Santiago_Ruiz_Suarez.datos)