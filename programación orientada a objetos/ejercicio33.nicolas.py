

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def listar_libros(self):
        return [l.titulo for l in self.libros]

Nicolas_Santiago_Ruiz_Suarez = Libro("Python Básico")
mi_biblioteca = Biblioteca()
mi_biblioteca.agregar_libro(Nicolas_Santiago_Ruiz_Suarez)
print(mi_biblioteca.listar_libros())


