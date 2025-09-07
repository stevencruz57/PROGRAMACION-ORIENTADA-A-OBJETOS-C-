class Libro:
    """Representa un libro con tupla inmutable para título y autor."""

    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor, categoria, isbn)
        self.isbn = isbn

    def __getitem__(self, key):
        return self.info[{'titulo': 0, 'autor': 1, 'categoria': 2, 'isbn': 3}[key]]


class Biblioteca:
    """Gestiona la colección de libros y usuarios."""

    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def anadir_libro(self, libro):
        """Añade un libro usando el ISBN como clave."""
        self.libros[libro.isbn] = libro
        print(f"Libro '{libro['titulo']}' añadido.")

    def quitar_libro(self, isbn):
        """Quita un libro por ISBN."""
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} quitado.")
        else:
            print(f"Error: Libro con ISBN {isbn} no encontrado.")

    def registrar_usuario(self, id_usuario, nombre):
        """Registra un usuario con un ID único."""
        if id_usuario in self.usuarios:
            print(f"Error: El usuario con ID {id_usuario} ya existe.")
        else:
            self.usuarios[id_usuario] = {'nombre': nombre, 'libros_prestados': set()}
            print(f"Usuario '{nombre}' con ID {id_usuario} registrado.")

    def prestar_libro(self, isbn, id_usuario):
        """Presta un libro y actualiza los registros."""
        if isbn not in self.libros or id_usuario not in self.usuarios:
            print("Error: El libro o el usuario no existen.")
            return

        self.usuarios[id_usuario]['libros_prestados'].add(self.libros.pop(isbn))
        print(f"Libro prestado a '{self.usuarios[id_usuario]['nombre']}'.")

    def devolver_libro(self, isbn, id_usuario):
        """Devuelve un libro a la biblioteca."""
        if id_usuario not in self.usuarios:
            print("Error: Usuario no encontrado.")
            return

        usuario_libros = self.usuarios[id_usuario]['libros_prestados']
        libro_a_devolver = next((l for l in usuario_libros if l.isbn == isbn), None)

        if libro_a_devolver:
            usuario_libros.remove(libro_a_devolver)
            self.libros[isbn] = libro_a_devolver
            print(f"Libro '{libro_a_devolver['titulo']}' devuelto.")
        else:
            print(f"Error: El usuario no tiene prestado el libro con ISBN {isbn}.")


# --- Ejemplo de Uso ---
mi_biblioteca = Biblioteca()
mi_biblioteca.anadir_libro(Libro("El alquimista", "Paulo Coelho", "Ficción", "978-0061120084"))
mi_biblioteca.registrar_usuario("J123", "Juan")
mi_biblioteca.prestar_libro("978-0061120084", "J123")