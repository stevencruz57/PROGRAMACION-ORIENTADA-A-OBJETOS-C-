# Definición de la clase base 'Animal'
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def emitir_sonido(self):
        pass

# Definición de la clase derivada 'Perro' que hereda de 'Animal'
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def emitir_sonido(self):
        return '¡Guau!'

# Implementación de encapsulación en la clase 'Perro'
class PerroEncapsulado(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.__raza = raza

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

    def emitir_sonido(self):
        return '¡Guau!'

# Ejemplo de polimorfismo con argumentos múltiples en una función
def presentar_animal(animal):
    print(f"Nombre: {animal.nombre}")
    print(f"Sonido: {animal.emitir_sonido()}")
    if isinstance(animal, PerroEncapsulado):
        print(f"Raza: {animal.get_raza()}")
    print()

# Creación de instancias de las clases y demostración de funcionalidad
if __name__ == '__main__':
    perro1 = Perro("Bobby", "Labrador")
    perro2 = PerroEncapsulado("Rex", "Golden Retriever")

    presentar_animal(perro1)
    presentar_animal(perro2)

    # Modificamos la raza del perro2 utilizando el método set_raza
    perro2.set_raza("Labrador")
    presentar_animal(perro2)