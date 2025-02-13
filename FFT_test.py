import numpy as np
from numpy import diff
from scipy.integrate import solve_ivp
from scipy.integrate import quad
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
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


# Generar una señal de ejemplo: suma de dos ondas sinusoidales con diferentes frecuencias
Fs = 1000  # Frecuencia de muestreo
T = 1.0 / Fs  # Intervalo de muestreo
t = np.arange(0, 1, T)  # Vector de tiempo

# Frecuencias de las ondas sinusoidales
f1 = 110  # Frecuencia de la primera onda sinusoidal
f2 = 120  # Frecuencia de la segunda onda sinusoidal

# Generar la señal
signal = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# Calcular la FFT de la señal
fft_signal = np.fft.fft(signal)
N = len(signal)
frequencies = np.fft.fftfreq(N, T)

# Graficar la señal original
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Señal Original')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')

# Graficar la magnitud de la FFT
plt.subplot(2, 1, 2)
plt.plot(frequencies[:N // 2], np.abs(fft_signal)[:N // 2] * (2 / N))
plt.title('FFT de la Señal')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')

plt.tight_layout()
plt.show()