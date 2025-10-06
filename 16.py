import tkinter as tk
from tkinter import messagebox
from functools import partial


# --- Clase Principal de la Aplicación ---
class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Tareas con Atajos 📝")
        self.geometry("450x400")
        self.tasks = []  # Almacenará las tareas como un diccionario {'text': str, 'completed': bool}

        # 1. Interfaz Gráfica
        self.create_widgets()

        # 3. Atajos de Teclado
        self.bind_shortcuts()

        # Cargar algunas tareas iniciales para la demostración
        self.tasks.append({'text': "Pagar facturas 💰", 'completed': False})
        self.tasks.append({'text': "Estudiar Tkinter ✅", 'completed': True})
        self.update_listbox()

    def create_widgets(self):
        # Frame de entrada (arriba)
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10, padx=10, fill='x')

        # Campo de entrada (Entry)
        self.task_entry = tk.Entry(input_frame, width=35, font=('Arial', 12))
        self.task_entry.pack(side=tk.LEFT, padx=(0, 10), fill='x', expand=True)

        # Botón Añadir Tarea
        add_button = tk.Button(input_frame, text="Añadir ➕", command=self.add_task, bg='#4CAF50', fg='white')
        add_button.pack(side=tk.LEFT)

        # Listbox para mostrar tareas
        self.task_listbox = tk.Listbox(self, width=60, height=15, selectmode=tk.SINGLE, font=('Arial', 11))
        self.task_listbox.pack(pady=10, padx=10, fill='both', expand=True)

        # 4. Feedback visual al seleccionar (opcional, Tkinter Listbox es limitado)
        self.task_listbox.bind('<<ListboxSelect>>', self.show_selection_feedback)

        # Frame de botones de acción (abajo)
        action_frame = tk.Frame(self)
        action_frame.pack(pady=5)

        # Botones de acción
        complete_button = tk.Button(action_frame, text="Completar ✅ (C)", command=self.mark_completed, bg='#2196F3',
                                    fg='white')
        complete_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(action_frame, text="Eliminar 🗑️ (D)", command=self.delete_task, bg='#F44336',
                                  fg='white')
        delete_button.pack(side=tk.LEFT, padx=5)

    # -------------------------------------
    # 2. Manejo de Eventos y Funcionalidad
    # -------------------------------------

    def update_listbox(self):
        """Actualiza el Listbox con las tareas de la lista 'self.tasks'."""
        self.task_listbox.delete(0, tk.END)  # Limpia el Listbox
        for idx, task_data in enumerate(self.tasks):
            text = task_data['text']
            is_completed = task_data['completed']

            # Inserta la tarea en el Listbox
            self.task_listbox.insert(tk.END, text)

            # 4. Proporcionar feedback visual (cambiar color si está completada)
            if is_completed:
                self.task_listbox.itemconfig(idx, {'fg': 'gray', 'bg': '#e0ffe0'})  # Gris y fondo verde claro
            else:
                self.task_listbox.itemconfig(idx, {'fg': 'black', 'bg': 'white'})

    def add_task(self, event=None):
        """Añade una tarea al listado."""
        new_task = self.task_entry.get().strip()
        if new_task:
            self.tasks.append({'text': new_task, 'completed': False})
            self.task_entry.delete(0, tk.END)  # Limpia el campo de entrada
            self.update_listbox()
        else:
            messagebox.showwarning("Advertencia", "Debes ingresar una tarea.")

    def delete_task(self, event=None):
        """Elimina la tarea seleccionada."""
        try:
            selected_index_tuple = self.task_listbox.curselection()
            if selected_index_tuple:
                index_to_delete = selected_index_tuple[0]
                # Elimina la tarea de la lista de tareas
                self.tasks.pop(index_to_delete)
                self.update_listbox()
            else:
                messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")
        except IndexError:
            # Captura un error si la selección está vacía por alguna razón
            messagebox.showwarning("Advertencia", "Selecciona una tarea válida.")

    def mark_completed(self, event=None):
        """Marca la tarea seleccionada como completada o pendiente."""
        try:
            selected_index_tuple = self.task_listbox.curselection()
            if selected_index_tuple:
                index_to_mark = selected_index_tuple[0]

                # Invierte el estado de 'completed'
                current_state = self.tasks[index_to_mark]['completed']
                self.tasks[index_to_mark]['completed'] = not current_state

                self.update_listbox()
                # Selecciona la tarea de nuevo para mantener el foco visual
                self.task_listbox.selection_set(index_to_mark)
            else:
                messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar.")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea válida.")

    def show_selection_feedback(self, event):
        """Muestra una simple retroalimentación en la consola al seleccionar (opcional)."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_text = self.tasks[selected_index]['text']
            print(f"Tarea seleccionada: {task_text}")
        except IndexError:
            pass

    # -------------------------------------
    # 3. Atajos de Teclado (Uso de bind)
    # -------------------------------------

    def bind_shortcuts(self):
        """Define los atajos de teclado para la aplicación."""

        # Requisito: Añadir tarea presionando la tecla "Enter" en el campo de entrada
        # Binding en el widget Entry (campo de entrada)
        self.task_entry.bind("<Return>", self.add_task)

        # Requisito: Cerrar la aplicación usando la tecla "Escape"
        # Binding en el widget principal (Root)
        self.bind("<Escape>", lambda event: self.destroy())

        # Requisito: Marcar la tarea seleccionada como completada (tecla "C")
        # Binding en el widget principal (Root) para que funcione en cualquier lugar
        self.bind("<KeyPress-c>", self.mark_completed)
        self.bind("<KeyPress-C>", self.mark_completed)

        # Requisito: Eliminar la tarea seleccionada (tecla "Delete" o "D")
        # Binding para la tecla 'Delete' (especial)
        self.bind("<Delete>", self.delete_task)
        # Binding para la tecla 'D'
        self.bind("<KeyPress-d>", self.delete_task)
        self.bind("<KeyPress-D>", self.delete_task)


# --- Ejecución ---
if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()