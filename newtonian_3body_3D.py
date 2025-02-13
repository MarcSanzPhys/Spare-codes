# Headers
import numpy as np
from numpy import diff
from scipy.integrate import solve_ivp
from scipy.integrate import quad
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
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

# Fuerza gravitacional
def gravitational_force(m1, m2, r1, r2):
    r = np.linalg.norm(r2 - r1)
    force = G * m1 * m2 / r**2
    direction = (r2 - r1) / r
    return force * direction

# Constantes
G = 6.67430e-11  # Constante gravedad universal
dt = 1e4  # Paso de tiempo

# Definición de las masas y posiciones iniciales
m1 = 2e30  #Masa estrella (kg)  1.989e30
m2 = 2e30  #Masa planeta 1 (kg) 5.972e24
m3 = 2e30  #Masa planeta 2 (kg) 6.4191e23
r1 = np.array([0, 0, 0], dtype='float64')  # Posición inicial estrella (m) [0, 0, 0]
r2 = np.array([1.5e11, 0, 0], dtype='float64')  # Posición inicial planeta 1 (m) [1.496e11, 0, 0] perihelio
r3 = np.array([-1.5e11, 0, 0], dtype='float64')  # Posición inicial planeta 2 (m) [2.279e11, 0, 0] perihelio
v1 = np.array([0, 0, 0], dtype='float64')  # Velocidad inicial estrella (m/s) [0, 0, 0]
v2 = np.array([0, 15000, 0], dtype='float64')  # Velocidad inicial planeta 1 (m/s) [0, 30300, 0]
v3 = np.array([0, -15000, 0], dtype='float64')  # Velocidad inicial planeta 2 (m/s) [0, 26500, 0]

# Listas para almacenar las posiciones
r1_list = [r1.copy()]
r2_list = [r2.copy()]
r3_list = [r3.copy()]

# Simulación
for step in range(100000):
    f12 = gravitational_force(m1, m2, r1, r2)
    f13 = gravitational_force(m1, m3, r1, r3)
    f23 = gravitational_force(m2, m3, r2, r3)
    a1 = (f12+f13) / m1
    a2 = (-f12+f23) / m2
    a3 = (-f13-f23) / m3
    v1 = v1 + a1 * dt
    v2 = v2 + a2 * dt
    v3 = v3 + a3 * dt
    r1 = r1 + v1 * dt
    r2 = r2 + v2 * dt
    r3 = r3 + v3 * dt
    r1_list.append(r1.copy())
    r2_list.append(r2.copy())
    r3_list.append(r3.copy())

    if step % 10000 == 0:
        print(f"Step: {step}")
        print(f"r1: {r1}")
        print(f"r2: {r2}")
        print(f"r3: {r3}")

# Conversión a arrays para facilitar la animación
r1_list = np.array(r1_list)
r2_list = np.array(r2_list)
r3_list = np.array(r3_list)

# Configuración de la animación
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-4e11, 4e11)
ax.set_ylim(-4e11, 4e11)
ax.set_zlim(-4e11, 4e11)
#line1, = ax.plot([], [], 'yo', markersize=10)  # Estrella
#line2, = ax.plot([], [], 'bo', markersize=10)  # Planeta 1
#line3, = ax.plot([], [], 'ro', markersize=10)  # Planeta 2
scatter1 = ax.scatter(r1_list[0, 0], r1_list[0, 1], r1_list[0, 2], color='yellow', s=150)  # Estrella
scatter2 = ax.scatter(r2_list[0, 0], r2_list[0, 1], r2_list[0, 2], color='blue', s=150)  # Planeta 1
scatter3 = ax.scatter(r3_list[0, 0], r3_list[0, 1], r3_list[0, 2], color='red', s=150)  # Planeta 2

#ax.grid(False)
ax.set_facecolor('black')  # Color del fondo del gráfico
fig.patch.set_facecolor('black')  # Color del fondo de la figura

# Dibujar las trayectorias iniciales
trajectory1, = ax.plot(r1_list[:, 0], r1_list[:, 1], r1_list[:, 2], 'y-', alpha=0.8)  # Trayectoria de la estrella
trajectory2, = ax.plot(r2_list[:, 0], r2_list[:, 1], r2_list[:, 2], 'b-', alpha=0.8)  # Trayectoria del planeta 1
trajectory3, = ax.plot(r3_list[:, 0], r3_list[:, 1], r3_list[:, 2], 'r-', alpha=0.8)  # Trayectoria del planeta 2

def init():
    scatter1._offsets3d = ([], [], [])
    scatter2._offsets3d = ([], [], [])
    scatter3._offsets3d = ([], [], [])
    return scatter1, scatter2, scatter3

def update(frame):
    # Convertir a listas explícitamente
    x1, y1, z1 = r1_list[frame, 0].tolist(), r1_list[frame, 1].tolist(), r1_list[frame, 2].tolist()
    x2, y2, z2 = r2_list[frame, 0].tolist(), r2_list[frame, 1].tolist(), r2_list[frame, 2].tolist()
    x3, y3, z3 = r3_list[frame, 0].tolist(), r3_list[frame, 1].tolist(), r3_list[frame, 2].tolist()

    scatter1._offsets3d = ([x1], [y1], [z1])
    scatter2._offsets3d = ([x2], [y2], [z2])
    scatter3._offsets3d = ([x3], [y3], [z3])

    # Actualizar las trayectorias
    trajectory1.set_data(r1_list[:frame+1, 0], r1_list[:frame+1, 1])
    trajectory1.set_3d_properties(r1_list[:frame+1, 2])
    trajectory2.set_data(r2_list[:frame+1, 0], r2_list[:frame+1, 1])
    trajectory2.set_3d_properties(r2_list[:frame+1, 2])
    trajectory3.set_data(r3_list[:frame+1, 0], r3_list[:frame+1, 1])
    trajectory3.set_3d_properties(r3_list[:frame+1, 2])
    
    return scatter1, scatter2, scatter3, trajectory1, trajectory2, trajectory3

ani = animation.FuncAnimation(fig, update, frames=len(r1_list), init_func=init, blit=True, interval=1)
plt.show()