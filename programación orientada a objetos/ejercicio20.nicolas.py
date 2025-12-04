

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def calcular_bono(self):
        return self.salario * 0.1

Nicolas_Santiago_Ruiz_Suarez = Empleado("Nicolas_Santiago_Ruiz_Suarez", 3000)
print(Nicolas_Santiago_Ruiz_Suarez.calcular_bono())



