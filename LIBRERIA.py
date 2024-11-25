import tkinter as tk
from tkinter import messagebox
def mostrar_mensaje():
    nomb= nombre.get()
    messagebox.showinfo("Mensaje", f"hola {nomb} bienvenido al programa")
#crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de GUI ")
#crear una etiqueta
etiqueta = tk.Label(ventana, text="ingresa tu nombre:")
etiqueta.grid(row=0, colum=0, padx=5, pady=10)
#crear una caja de texto (Entry)
nombre = tk.Entry(ventana, width=40)
nombre.grid(row=0, colum=1, padx=5, pady=10)
#crear un boton y asignarle la funcion
boton = tk.Button(ventana, text="saludar", command=mostrar_mensaje)
boton.grid(row=1, colum=0, columnspan=2, padx=5, pady=10)
#iniciar el bucle de eventos
ventana.mainloop()