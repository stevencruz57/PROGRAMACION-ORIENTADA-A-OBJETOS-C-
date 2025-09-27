import tkinter as tk
from tkinter import messagebox


class ListaDeTareasApp:
    # Constructor de la clase
    def __init__(self, master):
        self.master = master
        master.title("Lista de Tareas (To-Do List)")
        master.geometry("500x400")  # Establece un tamaño inicial para una mejor presentación

        # Lógica central: Almacenar las tareas.
        # Cada tarea es un diccionario para manejar tanto el texto como su estado.
        # Formato: [{"texto": "Comprar leche", "completada": False}, ...]
        self.tareas = []

        # --- Configuración de Estilos ---
        # Definir colores para diferenciar visualmente el estado de las tareas
        self.COLOR_PENDIENTE = '#ffffff'  # Fondo blanco para tareas activas
        self.COLOR_COMPLETADA = '#d4edda'  # Fondo verde claro para tareas terminadas

        # --- 1. Componentes de la Lista (Listbox y Scrollbar) ---
        # Usamos un Frame para contener el Listbox y su Scrollbar, facilitando el empaquetado ('pack')
        # y la capacidad de expandirse ('fill="both", expand=True').
        self.listbox_frame = tk.Frame(master)
        self.listbox_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.listbox_scrollbar = tk.Scrollbar(self.listbox_frame)
        self.listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox: El componente principal para mostrar las tareas.
        self.lista_tareas = tk.Listbox(
            self.listbox_frame,
            height=15,
            width=50,
            yscrollcommand=self.listbox_scrollbar.set,
            selectmode=tk.SINGLE,  # SOLO permite seleccionar UNA tarea a la vez (es crucial para las acciones)
            font=('Arial', 12)
        )
        self.lista_tareas.pack(side=tk.LEFT, fill="both", expand=True)
        self.listbox_scrollbar.config(command=self.lista_tareas.yview)

        # --- 2. Componentes de Entrada (Entry) ---
        self.entrada_frame = tk.Frame(master)
        self.entrada_frame.pack(pady=5, padx=10, fill='x')

        self.entrada_tarea = tk.Entry(
            self.entrada_frame,
            width=50,
            font=('Arial', 12)
        )
        self.entrada_tarea.pack(side=tk.LEFT, fill='x', expand=True)

        # MANEJO DE EVENTOS (Requisito): Añadir tarea al presionar Enter.
        # <Return> es el evento de presionar la tecla Enter. Se llama al método con 'lambda'
        # porque el evento Tkinter pasa un argumento que 'añadir_tarea' no espera.
        self.entrada_tarea.bind("<Return>", lambda event: self.añadir_tarea())

        # --- 3. Botones de Acción ---
        self.botones_frame = tk.Frame(master)
        self.botones_frame.pack(pady=10, padx=10)

        # Botones con estilo básico para mejorar la usabilidad.
        self.btn_añadir = tk.Button(
            self.botones_frame,
            text="Añadir Tarea",
            command=self.añadir_tarea,  # Llama a añadir_tarea()
            bg='#4CAF50', fg='white', font=('Arial', 10, 'bold')
        )
        self.btn_añadir.pack(side=tk.LEFT, padx=5)

        self.btn_completar = tk.Button(
            self.botones_frame,
            text="Marcar como Completada",
            command=self.marcar_completada,  # Llama a marcar_completada()
            bg='#2196F3', fg='white', font=('Arial', 10, 'bold')
        )
        self.btn_completar.pack(side=tk.LEFT, padx=5)

        self.btn_eliminar = tk.Button(
            self.botones_frame,
            text="Eliminar Tarea",
            command=self.eliminar_tarea,  # Llama a eliminar_tarea()
            bg='#F44336', fg='white', font=('Arial', 10, 'bold')
        )
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

        # --- 4. Evento Opcional: Doble Clic para Completar ---
        # <Double-1> es el evento de doble clic del botón izquierdo del ratón.
        # Permite una interacción rápida sin usar el botón dedicado.
        self.lista_tareas.bind("<Double-1>", lambda event: self.marcar_completada())

        # Inicializa la vista de la lista.
        self.actualizar_listbox()

    # MÉTODOS DE MANEJO DE EVENTOS Y LÓGICA

    def añadir_tarea(self):
        """Manejador para el botón Añadir y la tecla Enter."""
        texto_tarea = self.entrada_tarea.get().strip()

        if texto_tarea:
            # Lógica: Añadir el diccionario de la nueva tarea (por defecto, NO completada)
            self.tareas.append({"texto": texto_tarea, "completada": False})
            self.entrada_tarea.delete(0, tk.END)  # Limpiar el Entry para el siguiente ingreso
            self.actualizar_listbox()
        else:
            # Mostrar una advertencia si el campo está vacío
            messagebox.showwarning("Atención", "Por favor, escribe una tarea.")

    def marcar_completada(self):
        """Manejador para el botón Marcar y el evento Doble Clic."""