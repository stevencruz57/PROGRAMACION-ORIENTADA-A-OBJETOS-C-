#Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio
#Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado")

    def actualizar_cantidad(self, id, cantidad):
        if id in self.productos:
            self.productos[id].set_cantidad(cantidad)
        else:
            print("Producto no encontrado")

    def actualizar_precio(self, id, precio):
        if id in self.productos:
            self.productos[id].set_precio(precio)
        else:
            print("Producto no encontrado")

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.productos.values():
            if producto.get_nombre() == nombre:
                print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_precio()}")