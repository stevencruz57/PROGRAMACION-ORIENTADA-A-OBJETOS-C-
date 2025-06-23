#crearemos clases para representar los clientes, las habitaciones y el sistema de reservas en sí.

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Habitacion:
    def __init__(self, numero, tipo, precio, disponible=True):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = disponible

class SistemaReservas:
    def __init__(self):
        self.clientes = []
        self.habitaciones = [103]

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nombre} agregado al sistema.")

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
        print(f"Habitación {habitacion.numero} agregada al sistema.")

    def reservar_habitacion(self, cliente, habitacion):
        if habitacion.disponible:
            print(f"La habitación {habitacion.numero} ha sido reservada por {cliente.nombre}.")
            habitacion.disponible = False
        else:
            print(f"La habitación {habitacion.numero} no está disponible.")

# Creamos instancias de las clases
cliente1 = Cliente("Juan Perez", "juan@example.com")
habitacion1 = Habitacion(100, "Doble", 50)
sistema = SistemaReservas()

# Agregamos cliente y habitación al sistema
sistema.agregar_cliente(cliente1)
sistema.agregar_habitacion(habitacion1)

# Realizamos una reserva
sistema.reservar_habitacion(cliente1, habitacion1)