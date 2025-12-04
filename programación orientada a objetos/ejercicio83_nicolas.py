class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __len__(self):
        return len(self.nombre)

Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez")
print(len(Nicolas_Santiago_Ruiz_Suarez))