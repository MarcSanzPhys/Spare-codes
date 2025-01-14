#Detector de líneas con transformada de Hough en imágenes
#Nota: Antes de ejecutar recordar intalar: pip install opencv-python

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

#Detector lineas
import cv2

# Carga la imagen en escala de grises
img = cv2.imread('c:/Users/MG5526/Desktop/Core Losses/tu_imagen.jpg')

if img is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta del archivo.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Filtro gaussiano
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Crea una máscara para excluir sombras
_, mask = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
gray = cv2.bitwise_and(gray, gray, mask=mask)

# Aplica el detector de bordes Canny
edges = cv2.Canny(gray, 100, 200, apertureSize=3)

# Ajusta los parámetros de la Transformada de Hough Probabilística
rho = 1/2               # Resolución en la distancia de la acumulación (en píxeles)
theta = (np.pi / 180)/2 # Resolución en el ángulo de la acumulación (en radianes)
threshold = 200         # Número mínimo de intersecciones en la acumulación para detectar una línea
minLineLength = 600     # Longitud mínima de una línea
maxLineGap = 20         # Máxima separación entre segmentos de línea para considerarlos una sola línea

# Aplica la Transformada de Hough Probabilística
lines = cv2.HoughLinesP(edges, rho, theta, threshold, minLineLength=minLineLength, maxLineGap=maxLineGap)

# Verifica si se detectaron líneas
if lines is not None:
    # Imprime el número de líneas detectadas
    print("Número de líneas detectadas:", len(lines))

    # Dibuja las líneas detectadas
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Muestra la imagen con las líneas detectadas
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(f'Detección de Líneas con Transformada de Hough\nNúmero de líneas detectadas: {len(lines)}')
    plt.show()
else:
    print("No se detectaron líneas.")