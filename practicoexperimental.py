import threading
import time

# Función que ejecuta una cuenta regresiva
def cuenta_regresiva(numero):
    for i in range(numero, -1, -1):
        if i == 0:
            print("¡Despegue!")
        else:
            print(f"Tiempo restante: {i} segundos")
        time.sleep(1)

# Crear instancias de hilos
hilo1 = threading.Thread(target=cuenta_regresiva, args=(10,))
hilo2 = threading.Thread(target=cuenta_regresiva, args=(5,))

# Iniciar los hilos
hilo1.start()
hilo2.start()

# Esperar a que todos los hilos terminen
hilo1.join()
hilo2.join()

print('¡Finalizado!')