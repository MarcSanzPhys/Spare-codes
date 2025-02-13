# Headers
import numpy as np
from numpy import diff
from scipy.integrate import solve_ivp
from scipy.integrate import quad
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import fsolve
from scipy.optimize import minimize
#GUI related headers
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

# Subalgorithms

def factorial(x):
    i = 0
    fact = 0
    while(x != 0 and fact != 0):
        fact = x-i
        i = i+1
    return fact

print(factorial(4))

#def binomial(n, p, k):
