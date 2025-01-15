#Headers
import numpy as np
from scipy import integrate, optimize
import sympy as sp
import matplotlib.pyplot as plt

import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Sumador de Valores con Tkinter")

# Función que se ejecuta al presionar el botón de sumar
def sumar_valores():
    try:
        # Obtener los valores de las cajas de texto
        valor1 = float(entry1.get())
        valor2 = float(entry2.get())
        
        # Sumar los valores
        resultado = valor1 + valor2
        
        # Mostrar el resultado en la etiqueta
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        # Manejar el error si la entrada no es un número válido
        label_resultado.config(text="Error: Por favor ingresa números válidos.")

# Crear etiquetas y cajas de texto para los valores de entrada
label1 = tk.Label(root, text="Valor 1:")
label1.grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="Valor 2:")
label2.grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Crear el botón de sumar y agregarlo a la ventana
boton_sumar = tk.Button(root, text="Sumar", command=sumar_valores)
boton_sumar.grid(row=2, column=0, columnspan=2, pady=20)

# Crear una etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="")
label_resultado.grid(row=3, column=0, columnspan=2, pady=5)

# Cargar la imagen 
imagen = tk.PhotoImage(file="C:/Users/marcs/Documents/GitHub/Tests/captura.png")
label_imagen = tk.Label(root, image=imagen)
label_imagen.place(relx=1.0, rely=0.0, anchor='ne') # Posiciona  en la esquina superior derecha

# Ejecutar el bucle principal de la ventana
root.mainloop()
