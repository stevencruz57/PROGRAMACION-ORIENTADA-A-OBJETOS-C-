import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas Simples")
ventana.geometry("400x300")

# --- Funciones de los botones ---
def agregar_tarea():
    """Agrega el texto del campo de entrada a la lista."""
    tarea = campo_texto.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        campo_texto.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

def limpiar_lista():
    """Borra todos los elementos de la lista."""
    lista_tareas.delete(0, tk.END)

# --- Diseño de la interfaz ---
# Título
titulo_label = tk.Label(ventana, text="Gestor de Tareas", font=("Helvetica", 16))
titulo_label.pack(pady=10)

# Campo de texto y botón Agregar
frame_entrada = tk.Frame(ventana)
frame_entrada.pack()

campo_texto = tk.Entry(frame_entrada, width=30)
campo_texto.pack(side=tk.LEFT, padx=5)

boton_agregar = tk.Button(frame_entrada, text="Agregar", command=agregar_tarea)
boton_agregar.pack(side=tk.LEFT)

# Lista para mostrar las tareas
lista_tareas = tk.Listbox(ventana, width=40, height=10)
lista_tareas.pack(pady=10)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Iniciar el bucle de la aplicación
ventana.mainloop()