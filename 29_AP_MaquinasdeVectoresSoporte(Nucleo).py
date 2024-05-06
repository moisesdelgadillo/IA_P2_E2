# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de datos de ejemplo
datos_entrenamiento = [
    ([3, 4], 1),
    ([1, 5], 1),
    ([5, 2], -1),
    ([7, 8], -1),
    ([2, 1], 1)
]

# Definición de la función para calcular el producto punto entre dos vectores
def producto_punto(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

# Entrenamiento del modelo SVM
def entrenar_svm(datos, max_iter=1000, tasa_aprendizaje=0.01):
    pesos = [0] * len(datos[0][0])  # Inicialización de los pesos
    for _ in range(max_iter):
        for x, y in datos:
            if y * producto_punto(pesos, x) <= 1:  # Si el punto está dentro del margen
                for i in range(len(pesos)):
                    pesos[i] += tasa_aprendizaje * (y * x[i])  # Actualización de los pesos
    return pesos

# Predicción de la clase
def predecir_clase(pesos, instancia):
    if producto_punto(pesos, instancia) >= 0:
        return 1
    else:
        return -1

# Entrenamiento del modelo SVM
pesos_svm = entrenar_svm(datos_entrenamiento)

# Datos de prueba
dato_prueba = [4, 6]

# Predicción de la clase para el dato de prueba
clase_predicha = predecir_clase(pesos_svm, dato_prueba)

# Resultado
if clase_predicha == 1:
    print("El dato de prueba pertenece a la clase positiva.")
else:
    print("El dato de prueba pertenece a la clase negativa.")
