def ingresar_temperaturas_diarias():
    temperaturas = []
    for i in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio

# Ingreso de temperaturas diarias
temperaturas_diarias = ingresar_temperaturas_diarias()

# Cálculo del promedio semanal
promedio_semanal = calcular_promedio_semanal(temperaturas_diarias)
print(f"El promedio de temperaturas de la semana es: {promedio_semanal}")