import numpy as np
from numpy import diff
from scipy.integrate import solve_ivp
from scipy.integrate import quad
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from scipy.interpolate import CubicSpline
from scipy.interpolate import UnivariateSpline
from lmfit.models import SkewedGaussianModel

#Some plot settings
import matplotlib as mpl
mpl.rcParams['mathtext.rm'] = 'serif'
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.size'] = 14
mpl.rcParams['text.usetex'] = False

from IPython.display import display, HTML
display(HTML("<style>.container { width:80% !important; }</style>"))

# smoothing filters
from scipy.signal import savgol_filter
from scipy.signal import butter, filtfilt


# Parámetros
Fs = 1000  # Frecuencia de muestreo
T = 1.0 / Fs  # Intervalo de muestreo
t = np.arange(0, 1, T)  # Vector de tiempo

# Frecuencia constante
f_constant = 50  # Frecuencia de la onda sinusoidal constante

# Rango de frecuencias para el barrido
f_sweep_start = 10
f_sweep_end = 100
f_sweep_step = 1

# Crear una figura y ejes para la animación
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

def update(f_sweep):
    ax1.clear()
    ax2.clear()
    
    # Generar la señal con la frecuencia de barrido actual
    signal = np.sin(2 * np.pi * f_constant * t) + np.sin(2 * np.pi * f_sweep * t)
    
    # Calcular la FFT de la señal
    fft_signal = np.fft.fft(signal)
    N = len(signal)
    frequencies = np.fft.fftfreq(N, T)
    
    # Graficar la señal original
    ax1.plot(t, signal)
    ax1.set_title(f'Señal Original (Frecuencia de Barrido: {f_sweep} Hz)')
    ax1.set_xlabel('Tiempo (s)')
    ax1.set_ylabel('Amplitud')
    
    # Graficar la magnitud de la FFT
    ax2.plot(frequencies[:N // 2], np.abs(fft_signal)[:N // 2] * (2 / N))
    ax2.set_title('FFT de la Señal')
    ax2.set_xlabel('Frecuencia (Hz)')
    ax2.set_ylabel('Magnitud')
    ax2.set_xlim(0,100)

    plt.tight_layout()

# Crear una animación
ani = FuncAnimation(fig, update, frames=np.arange(f_sweep_start, f_sweep_end + f_sweep_step, f_sweep_step), repeat=True)

# Guardar la animación como un GIF
ani.save('frequency_sweep.gif', writer=PillowWriter(fps=2))

plt.show()