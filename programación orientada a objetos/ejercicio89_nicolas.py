class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

Nicolas_Santiago_Ruiz_Suarez = Gerente("Nicolas Santiago Ruiz Suarez", 5000, "Ventas")
print(Nicolas_Santiago_Ruiz_Suarez.nombre, Nicolas_Santiago_Ruiz_Suarez.departamento)