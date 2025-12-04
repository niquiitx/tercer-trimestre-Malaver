
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Equipo:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

Nicolas_Santiago_Ruiz_Suarez = Jugador("Nicolas_Santiago_Ruiz_Suarez")
mi_equipo = Equipo()
mi_equipo.agregar_jugador(Nicolas_Santiago_Ruiz_Suarez)
for j in mi_equipo.jugadores:
    print(j.nombre)





