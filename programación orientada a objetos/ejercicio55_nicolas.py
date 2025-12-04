
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * porcentaje / 100

Nicolas_Santiago_Ruiz_Suarez = Empleado("Nicolas_Santiago_Ruiz_Suarez", 3000)
Nicolas_Santiago_Ruiz_Suarez.aumentar_salario(10)
print(Nicolas_Santiago_Ruiz_Suarez.salario)