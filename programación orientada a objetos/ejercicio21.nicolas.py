

class Persona:
    def actividad(self):
        print("actuando como persona")

class Profesor(Persona):
    def actividad(self):
        print("pensando en la clase")

Nicolas_Santiago_Ruiz_Suarez = Profesor()
Nicolas_Santiago_Ruiz_Suarez.actividad()


