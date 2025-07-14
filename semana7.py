class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        print(f"A new {color} {brand} {model} has been created.")

    def drive(self):
        print(f"The {self.color} {self.brand} {self.model} is being driven.")

    def __del__(self):
        print(f"The {self.color} {self.brand} {self.model} is being destroyed.")

# Crear un objeto de la clase Car
my_car = Car("Toyota", "Corolla", "blue")

# Llamar al método drive
my_car.drive()

# Al salir del bloque, el constructor __del__ se activará automáticamente para destruir el objeto