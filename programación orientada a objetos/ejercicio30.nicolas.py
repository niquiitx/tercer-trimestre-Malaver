

class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Restaurante:
    def __init__(self):
        self.menu = []

    def agregar_plato(self, plato):
        self.menu.append(plato)

Nicolas_Santiago_Ruiz_Suarez = Plato("Pizza", 20)
mi_restaurante = Restaurante()
mi_restaurante.agregar_plato(Nicolas_Santiago_Ruiz_Suarez)
for plato in mi_restaurante.menu:
    print(plato.nombre, plato.precio)




