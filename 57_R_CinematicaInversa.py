# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np

# Función para calcular la cinemática inversa
def cinematica_inversa(x, y, l1, l2):
    # Calcular la distancia al extremo del robot
    distancia = np.sqrt(x**2 + y**2)
    
    # Calcular el ángulo del primer eslabón con respecto al eje x
    theta1 = np.arctan2(y, x)
    
    # Calcular el ángulo del segundo eslabón utilizando el teorema del coseno
    cos_theta2 = (l1**2 + l2**2 - distancia**2) / (2 * l1 * l2)
    theta2 = np.arctan2(np.sqrt(1 - cos_theta2**2), cos_theta2) + np.arctan2(l2 * np.sin(theta1) * np.cos(theta2), l1 + l2 * np.sin(theta2))
    
    return np.degrees(theta1), np.degrees(theta2)

# Definir las longitudes de los eslabones del robot
l1 = 5  # longitud del primer eslabón
l2 = 5  # longitud del segundo eslabón

# Definir la posición deseada del extremo del robot
x_deseado = 6
y_deseado = 4

# Calcular la cinemática inversa
theta1, theta2 = cinematica_inversa(x_deseado, y_deseado, l1, l2)

# Imprimir los ángulos calculados
print("Ángulo de la articulación 1:", theta1, "grados")
print("Ángulo de la articulación 2:", theta2, "grados")
