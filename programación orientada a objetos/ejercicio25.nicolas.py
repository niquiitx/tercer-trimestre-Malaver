class Poligono:
    def __init__(self, lados):
        self.lados = lados

class Cuadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado
    def area(self):
        return self.lado ** 2

Nicolas_Santiago_Ruiz_Suarez = Cuadrado(5)
print(Nicolas_Santiago_Ruiz_Suarez.area())




