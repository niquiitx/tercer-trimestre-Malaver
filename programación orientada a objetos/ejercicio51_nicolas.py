class Direccion:
    def __init__(self, ciudad):
        self.ciudad = ciudad

class Persona:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

direccion_kslc = Direccion("Bogotá")
Nicolas_Santiago_Ruiz_Suarez = Persona("Nicolas_Santiago_Ruiz_Suarez", direccion_kslc)
print(Nicolas_Santiago_Ruiz_Suarez.direccion.ciudad)