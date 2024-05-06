# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import cv2

# Cargar el modelo pre-entrenado de detección de objetos
modelo = cv2.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'ssd_mobilenet_v2_coco.pbtxt')

# Cargar la imagen de entrada
imagen = cv2.imread('imagen.jpg')

# Obtener las dimensiones de la imagen
alto, ancho = imagen.shape[:2]

# Preprocesar la imagen
blob = cv2.dnn.blobFromImage(imagen, size=(300, 300), swapRB=True, crop=False)

# Pasar la imagen preprocesada al modelo
modelo.setInput(blob)

# Realizar la detección de objetos
detecciones = modelo.forward()

# Iterar sobre las detecciones y dibujar los cuadros delimitadores
for i in range(detecciones.shape[2]):
    confianza = detecciones[0, 0, i, 2]
    if confianza > 0.5:  # Filtro de confianza
        clase = int(detecciones[0, 0, i, 1])
        cuadro_delimitador = detecciones[0, 0, i, 3:7] * np.array([ancho, alto, ancho, alto])
        x1, y1, x2, y2 = cuadro_delimitador.astype('int')
        etiqueta = f'{clase}: {confianza:.2f}'
        cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(imagen, etiqueta, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Mostrar la imagen con los objetos detectados
cv2.imshow('Objetos detectados', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
