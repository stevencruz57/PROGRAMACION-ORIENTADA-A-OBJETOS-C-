class RegistroClima:
    def __init__(self):
        self.temperaturas_diarias = []

    def ingresar_temperaturas_diarias(self):
        for i in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas_diarias.append(temperatura)

    def calcular_promedio_semanal(self):
        promedio = sum(self.temperaturas_diarias) / len(self.temperaturas_diarias)
        return promedio

# Creación de objeto RegistroClima
registro = RegistroClima()

# Ingreso de temperaturas diarias
registro.ingresar_temperaturas_diarias()

# Cálculo del promedio semanal
promedio_semanal = registro.calcular_promedio_semanal()
print(f"El promedio de temperaturas de la semana es: {promedio_semanal}")