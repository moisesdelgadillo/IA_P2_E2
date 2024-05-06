# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np

# Función para simular la medición de temperatura con ruido
def medir_temperatura(valor_verdadero, desviacion_estandar):
    return np.random.normal(valor_verdadero, desviacion_estandar)

# Valor verdadero de la temperatura ambiente
temperatura_verdadera = 25  # en grados Celsius

# Desviación estándar del sensor de temperatura (incertidumbre)
desviacion_estandar = 1  # en grados Celsius

# Simular una medición de temperatura
temperatura_medida = medir_temperatura(temperatura_verdadera, desviacion_estandar)

# Imprimir la medición simulada
print("Temperatura medida:", temperatura_medida, "grados Celsius")
