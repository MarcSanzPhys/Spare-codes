# Headers
import numpy as np
from numpy import diff
from scipy.integrate import solve_ivp
from scipy.integrate import quad
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.optimize import curve_fit
from scipy.optimize import fsolve
from scipy.optimize import minimize
import tkinter as tk
from tkinter import Menu, Menubutton, ttk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Some plot settings
import matplotlib as mpl
mpl.rcParams['mathtext.rm'] = 'serif'
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.size'] = 12
mpl.rcParams['text.usetex'] = False

from IPython.display import display, HTML
display(HTML("<style>.container { width:80% !important; }</style>"))

# Constantes
G = 6.67430e-11  # Constante gravitacional
dt = 1e4  # Paso de tiempo

# Definición de las masas y posiciones iniciales
m1 = 1.989e30  # Masa estrella (kg)
m2 = 5.972e24  # Masa planeta 1 (kg)
r1 = np.array([0, 0], dtype='float64')  # Posición inicial estrella (m)
r2 = np.array([1.496e11, 0], dtype='float64')  # Posición inicial planeta 1 (m)
v1 = np.array([0, 0], dtype='float64')  # Velocidad inicial estrella (m/s)
v2 = np.array([0, 29780], dtype='float64')  # Velocidad inicial planeta 1 (m/s)

# Listas para almacenar las posiciones
r1_list = [r1.copy()]
r2_list = [r2.copy()]

# Función para calcular la fuerza gravitacional
def gravitational_force(m1, m2, r1, r2):
    r = np.linalg.norm(r2 - r1)
    force = G * m1 * m2 / r**2
    direction = (r2 - r1) / r
    return force * direction

# Simulación
for step in range(10000):
    f12 = gravitational_force(m1, m2, r1, r2)
    a1 = f12 / m1
    a2 = -f12 / m2
    v1 = v1 + a1 * dt
    v2 = v2 + a2 * dt
    r1 = r1 + v1 * dt
    r2 = r2 + v2 * dt
    r1_list.append(r1.copy())
    r2_list.append(r2.copy())

    if step % 100 == 0:
        print(f"Step: {step}")
        print(f"r1: {r1}")
        print(f"r2: {r2}")

# Conversión a arrays para facilitar la animación
r1_list = np.array(r1_list)
r2_list = np.array(r2_list)

# Configuración de la animación
fig, ax = plt.subplots()
ax.set_xlim(-2e11, 2e11)
ax.set_ylim(-2e11, 2e11)
line1, = ax.plot([], [], 'yo', markersize=10)  # Estrella
line2, = ax.plot([], [], 'bo', markersize=5)  # Planeta 1

# Dibujar las trayectorias iniciales
trajectory1, = ax.plot(r1_list[:, 0], r1_list[:, 1], 'y-', alpha=0.5)  # Trayectoria estrella
trajectory2, = ax.plot(r2_list[:, 0], r2_list[:, 1], 'b-', alpha=0.5)  # Trayectoria planeta 1

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

def update(frame):
    #print(f"Frame: {frame}")
    #print(f"r1_list[frame]: {r1_list[frame]}")
    #print(f"r2_list[frame]: {r2_list[frame]}")

    # Convertir a listas explícitamente
    x1, y1 = r1_list[frame, 0].tolist(), r1_list[frame, 1].tolist()
    x2, y2 = r2_list[frame, 0].tolist(), r2_list[frame, 1].tolist()

    line1.set_data([x1], [y1])
    line2.set_data([x2], [y2])
    # Actualizar las trayectorias
    trajectory1.set_data(r1_list[:frame+1, 0], r1_list[:frame+1, 1])
    trajectory2.set_data(r2_list[:frame+1, 0], r2_list[:frame+1, 1])
    
    return line1, line2, trajectory1, trajectory2

ani = animation.FuncAnimation(fig, update, frames=len(r1_list), init_func=init, blit=True, interval=1)
plt.show()