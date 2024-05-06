# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np
import matplotlib.pyplot as plt

# Generamos un proceso estacionario débil (ruido blanco)
np.random.seed(0)
n = 100  # Número de observaciones
media = 0
desviacion_estandar = 1
ruido_blanco = np.random.normal(loc=media, scale=desviacion_estandar, size=n)

# Graficamos el proceso estacionario débil
plt.plot(ruido_blanco)
plt.title("Proceso Estacionario Débil (Ruido Blanco)")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.show()
