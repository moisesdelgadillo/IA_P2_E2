# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

#pip install pytesseract

import cv2
import pytesseract

# Configurar la ubicación de Tesseract
pytesseract.pytesseract.tesseract_cmd = 'ruta/al/ejecutable/tesseract'

# Cargar la imagen
imagen = cv2.imread('imagen.jpg')

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización para mejorar la legibilidad del texto
_, umbral = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Realizar el reconocimiento de escritura utilizando Tesseract
texto_reconocido = pytesseract.image_to_string(umbral, lang='eng')

# Mostrar el texto reconocido
print("Texto reconocido:")
print(texto_reconocido)
