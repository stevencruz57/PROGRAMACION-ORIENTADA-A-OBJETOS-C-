#Este programa calculará el Índice de Masa Corporal (IMC) de una persona dado su peso en kilogramos y estatura en metros.

# Función para calcular el IMC
def calcular_imc(peso_kg, estatura_m):
    # Fórmula del IMC: peso / estatura^2
    imc = peso_kg / (estatura_m ** 2)
    return imc

# Datos de prueba
peso = 68.5  # Peso en kilogramos
estatura = 1.75  # Estatura en metros

# Calcular el IMC utilizando la función
imc_resultado = calcular_imc(peso, estatura)

# Imprimir el resultado del IMC
print(f"El IMC calculado es: {imc_resultado:.2f}IMC")