class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

personas = []
personas.append(Persona("Nicolas Santiago Ruiz Suarez"))
personas.append(Persona("Andres"))
for p in personas:
    print(p.nombre)