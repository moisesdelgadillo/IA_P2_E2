# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar detección de bordes utilizando el operador Sobel
bordes = cv2.Sobel(imagen, cv2.CV_64F, 1, 1)

# Aplicar umbralización para segmentar los bordes
umbral = 50
_, bordes_segmentados = cv2.threshold(np.abs(bordes), umbral, 255, cv2.THRESH_BINARY)

# Mostrar la imagen original y los bordes segmentados
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Bordes Segmentados', np.uint8(bordes_segmentados))

# Esperar a que se presione una tecla y cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
