class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
    def info(self):
        print(f"{self.nombre} trabaja como {self.cargo}")

Nicolas_Santiago_Ruiz_Suarez = Empleado("Nicolas_Santiago_Ruiz_Suarez", "Ingeniero")
Nicolas_Santiago_Ruiz_Suarez.info()
def cuadrados_mayores_que(Nicolas_Santiago_Ruiz_Suarez_lista, Nicolas_Santiago_Ruiz_Suarez_n):
    return [x**2 for x in Nicolas_Santiago_Ruiz_Suarez_lista if x**2 > Nicolas_Santiago_Ruiz_Suarez_n]

print(cuadrados_mayores_que([1,2,3,4,5], 10))



def numeros_pares(Nicolas_Santiago_Ruiz_Suarez_inicio, Nicolas_Santiago_Ruiz_Suarez_fin):
    return [x for x in range(Nicolas_Santiago_Ruiz_Suarez_inicio, Nicolas_Santiago_Ruiz_Suarez_fin+1) if x%2==0]

print(numeros_pares(1,10))