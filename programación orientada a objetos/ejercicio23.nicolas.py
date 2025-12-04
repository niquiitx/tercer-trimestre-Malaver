from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("omawae wa mou shindeiru")

Nicolas_Santiago_Ruiz_Suarez = Perro()
Nicolas_Santiago_Ruiz_Suarez.sonido()

