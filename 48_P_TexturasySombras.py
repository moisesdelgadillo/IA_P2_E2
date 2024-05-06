# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_COLOR)

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro de desenfoque gaussiano para suavizar la imagen
gris_suave = cv2.GaussianBlur(gris, (5, 5), 0)

# Calcular el gradiente horizontal y vertical de la imagen
gradiente_x = cv2.Sobel(gris_suave, cv2.CV_64F, 1, 0, ksize=3)
gradiente_y = cv2.Sobel(gris_suave, cv2.CV_64F, 0, 1, ksize=3)

# Calcular la magnitud del gradiente
magnitud_gradiente = np.sqrt(gradiente_x**2 + gradiente_y**2)

# Calcular el ángulo del gradiente
angulo_gradiente = np.arctan2(gradiente_y, gradiente_x) * (180 / np.pi)

# Threshold para detectar bordes
umbral = 50
bordes = cv2.threshold(magnitud_gradiente, umbral, 255, cv2.THRESH_BINARY)[1]

# Mostrar la imagen de bordes
cv2.imshow('Bordes', bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()
