import numpy as np
import pandas as pd
from scipy.signal import savgol_filter as sf
from scipy.integrate import cumtrapz
def cargar_datos(fichero):
    df = pd.read_excel(fichero)
    t = df.values[1:, 0].astype(float)
    aceleracion_abs = df.values[1:, 1].astype(float)
    aceleracion_y = df.values[1:, 3].astype(float)
    return t, aceleracion_abs, aceleracion_y
   

# Calcular la aceleración corregida
def calcular_aceleracion_correcta(aceleracion_abs, aceleracion_y):
    return aceleracion_abs * np.sign(aceleracion_y)

# Calcular la gravedad
def calcular_gravedad(aceleracion):
    return np.mean(aceleracion[:100])

# Calcular la fuerza
def calcular_fuerza(aceleracion, masa):
    return masa * aceleracion

# Calcular la aceleración corregida para integrar
def calcular_aceleracion_corr(aceleracion, gravedad):
    return aceleracion - gravedad

# Integración numérica para obtener la velocidad
def primitiva_numerica(variable, tiempo, y0):
    return cumtrapz(variable, x=tiempo, initial=y0)

# Calcular la velocidad máxima
def calcular_velocidad_maxima(velocidad):
    return np.max(velocidad)

# Calcular la duración del vuelo
def calcular_duracion_vuelo(velocidad, tiempo):
    max_index = np.argmax(velocidad)
    min_index = np.argmin(velocidad)
    t_max_vel = tiempo[max_index]
    t_min_vel = tiempo[min_index]
    duracion_vuelo = t_min_vel - t_max_vel
    return t_max_vel, t_min_vel, duracion_vuelo

# Calcular la potencia
def calcular_potencia(fuerza, velocidad):
    return fuerza * velocidad

# Calcular la altura del salto
def calcular_altura(v0, gravedad):
    return (v0 ** 2) / (2 * gravedad)

