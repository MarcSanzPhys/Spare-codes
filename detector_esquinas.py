#Headers
import numpy as np
from numpy import diff
from scipy.integrate import solve_ivp
from scipy.integrate import quad
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import fsolve
from scipy.optimize import minimize

#Some plot settings
import matplotlib as mpl
mpl.rcParams['mathtext.rm'] = 'serif'
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.size'] = 12
mpl.rcParams['text.usetex'] = False

from IPython.display import display, HTML
display(HTML("<style>.container { width:80% !important; }</style>"))

#Detector
import cv2

# Carga la imagen en escala de grises
img = cv2.imread('c:/Users/MG5526/Desktop/Core Losses/tu_imagen.jpg', 0)

# Verifica si la imagen se ha cargado correctamente
if img is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta del archivo.")
    exit()

img = np.float32(img)

# Aplica el detector de esquinas Harris
dst = cv2.cornerHarris(img, blockSize=6, ksize=9, k=0.04)

# Dilata los resultados para marcar mejor las esquinas
dst = cv2.dilate(dst, None)

# Umbral para detectar esquinas
#img[dst > 0.01 * dst.max()] = [255]

# Ajusta el umbral para detectar menos esquinas
threshold = 0.02
corners = np.argwhere(dst > threshold * dst.max())

# Imprime el número de esquinas detectadas
print("Número de esquinas detectadas:", len(corners))

# Dibuja las esquinas detectadas
for corner in corners:
    y, x = corner
    cv2.circle(img, (x, y), 3, 255, -1)

# Muestra la imagen con las esquinas detectadas
plt.imshow(img, cmap='gray')
plt.title('Detección de Esquinas Harris')
plt.show()
