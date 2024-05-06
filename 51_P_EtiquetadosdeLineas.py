# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('imagen.jpg')
imagen_original = imagen.copy()

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización para detectar los bordes
bordes = cv2.Canny(gris, 50, 150, apertureSize=3)

# Aplicar la Transformada de Hough para detectar líneas
lineas = cv2.HoughLinesP(bordes, rho=1, theta=np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

# Dibujar las líneas detectadas en la imagen original
if lineas is not None:
    for linea in lineas:
        x1, y1, x2, y2 = linea[0]
        cv2.line(imagen_original, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Mostrar la imagen con las líneas etiquetadas
cv2.imshow('Imagen con líneas etiquetadas', imagen_original)
cv2.waitKey(0)
cv2.destroyAllWindows()
