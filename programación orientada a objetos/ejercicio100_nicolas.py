class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hobbies = []
    def agregar_hobby(self, hobby):
        self.hobbies.append(hobby)

yeison_david_moreno_nieto = Persona("Yeison David Moreno Nieto")
yeison_david_moreno_nieto.agregar_hobby("matar zombies")
print(yeison_david_moreno_nieto.hobbies)