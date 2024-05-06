# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Definir las coordenadas del objeto de interés (en este caso, un círculo)
centro_x = 300
centro_y = 200
radio = 50

# Generar muestras aleatorias dentro de un área alrededor del objeto
n_muestras = 1000
muestras = np.random.randint(0, len(imagen), size=(n_muestras, 2))

# Contar el número de muestras que caen dentro del círculo
n_dentro = 0
for muestra in muestras:
    x, y = muestra
    if (x - centro_x)**2 + (y - centro_y)**2 <= radio**2:
        n_dentro += 1

# Calcular la fracción de muestras que caen dentro del círculo
fraccion_dentro = n_dentro / n_muestras

# Calcular el área del círculo estimada utilizando el método de Monte Carlo
area_circulo_estimada = fraccion_dentro * (len(imagen) * len(imagen[0]))

# Mostrar resultados
print("Área del círculo estimada:", area_circulo_estimada)
