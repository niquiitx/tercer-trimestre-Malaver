
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Persona):
    def __init__(self, nombre, salario):
        super().__init__(nombre)
        self.salario = salario

Nicolas_Santiago_Ruiz_Suarez = Empleado("Nicolas_Santiago_Ruiz_Suarez", 3000)
print(Nicolas_Santiago_Ruiz_Suarez.nombre, Nicolas_Santiago_Ruiz_Suarez.salario)
 

