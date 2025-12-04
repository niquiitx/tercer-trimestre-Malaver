class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        print("Miau")

Nicolas_Santiago_Ruiz_Suarez = Gato()
Nicolas_Santiago_Ruiz_Suarez.sonido()