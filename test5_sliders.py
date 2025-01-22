import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.geometry("1500x650")
root.title("No Load Losses Calculator")

# Crear un Frame que contendrá el contenido desplazable
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, sticky='nsew')

# Crear un Canvas dentro del Frame
canvas = tk.Canvas(main_frame)
canvas.grid(row=0, column=0, sticky='nsew')

# Añadir Scrollbars al Canvas
scrollbar_y = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar_y.grid(row=0, column=1, sticky='ns')

scrollbar_x = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
scrollbar_x.grid(row=1, column=0, sticky='ew')

canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

# Crear otro Frame dentro del Canvas
content_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Función para ajustar el tamaño del Canvas a los widgets
def ajustar_canvas(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

content_frame.bind("<Configure>", ajustar_canvas)

# Añadir widgets al content_frame
for i in range(50):  # Añadir múltiples etiquetas como ejemplo
    label = tk.Label(content_frame, text=f"Label {i+1}")
    label.grid(row=i, column=0, padx=10, pady=5)

# Asegurar que el canvas y las scrollbars se expandan con la ventana
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Ejecutar el bucle principal de la ventana
root.mainloop()