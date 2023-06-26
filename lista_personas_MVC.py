import tkinter as tk
from tkinter import messagebox

class Persona:
    def __init__(self, id, nombre, edad):
        self.id = id
        self.nombre = nombre
        self.edad = edad

class Controlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def agregar_persona(self):
        id = self.vista.id_entry.get()
        nombre = self.vista.nombre_entry.get()
        edad = self.vista.edad_entry.get()

        if id and nombre and edad:
            persona = Persona(id, nombre, edad)
            self.modelo.agregar_persona(persona)
            self.vista.actualizar_lista()
            self.vista.limpiar_campos()
        else:
            messagebox.showerror("Error", "Debes completar todos los campos.")

    def eliminar_persona(self):
        seleccion = self.vista.lista_personas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.modelo.eliminar_persona(indice)
            self.vista.actualizar_lista()
        else:
            messagebox.showerror("Error", "Debes seleccionar una persona de la lista.")

class Modelo:
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def eliminar_persona(self, indice):
        del self.personas[indice]

class Vista:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador

        self.id_label = tk.Label(root, text="ID:")
        self.id_label.grid(row=0, column=0)
        self.id_entry = tk.Entry(root)
        self.id_entry.grid(row=0, column=1)

        self.nombre_label = tk.Label(root, text="Nombre:")
        self.nombre_label.grid(row=1, column=0)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=1, column=1)

        self.edad_label = tk.Label(root, text="Edad:")
        self.edad_label.grid(row=2, column=0)
        self.edad_entry = tk.Entry(root)
        self.edad_entry.grid(row=2, column=1)

        self.agregar_button = tk.Button(root, text="Agregar", command=self.controlador.agregar_persona)
        self.agregar_button.grid(row=3, column=0)

        self.eliminar_button = tk.Button(root, text="Eliminar", command=self.controlador.eliminar_persona)
        self.eliminar_button.grid(row=3, column=1)

        self.lista_personas = tk.Listbox(root)
        self.lista_personas.grid(row=4, columnspan=2)

    def actualizar_lista(self):
        self.lista_personas.delete(0, tk.END)
        for persona in self.controlador.modelo.personas:
            self.lista_personas.insert(tk.END, f"ID: {persona.id} - Nombre: {persona.nombre} - Edad: {persona.edad}")

    def limpiar_campos(self):
        self.id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.edad_entry.delete(0, tk.END)

# Crear la aplicación
root = tk.Tk()
root.title("Lista de Personas")

# Crear el modelo
modelo = Modelo()

# Crear el controlador
controlador = Controlador(modelo, None)

# Crear la vista y asignar el controlador
vista = Vista(root, controlador)
controlador.vista = vista

# Iniciar el bucle de eventos
root.mainloop()
