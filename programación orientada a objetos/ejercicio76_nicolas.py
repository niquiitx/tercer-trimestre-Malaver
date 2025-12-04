class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Juego:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

Nicolas_Santiago_Ruiz_Suarez = Jugador("Nicolas_Santiago_Ruiz_Suarez")
juego1 = Juego()
juego1.agregar_jugador(Nicolas_Santiago_Ruiz_Suarez)
for j in juego1.jugadores:
    print(j.nombre)