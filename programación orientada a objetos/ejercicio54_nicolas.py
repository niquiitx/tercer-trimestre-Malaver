class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def filtrar_por_autor(self, autor):
        return [l.titulo for l in self.libros if l.autor == autor]

Nicolas_Santiago_Ruiz_Suarez = Libro("Python Avanzado", "Nicolas_Santiago_Ruiz_Suarez")
biblioteca = Biblioteca()
biblioteca.agregar_libro(Nicolas_Santiago_Ruiz_Suarez)
print(biblioteca.filtrar_por_autor("Nicolas_Santiago_Ruiz_Suarez"))