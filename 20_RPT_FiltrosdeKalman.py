# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

# Definimos las variables iniciales del objeto y del filtro de Kalman
posicion_actual = 0
velocidad = 10
varianza_posicion = 5
varianza_ruido_proceso = 2
varianza_ruido_medicion = 3

# Función para simular el movimiento del objeto y la medición del sensor
def simular_movimiento_y_medicion(posicion_actual, velocidad, varianza_ruido_proceso, varianza_ruido_medicion):
    # Simulamos el movimiento del objeto
    nueva_posicion = posicion_actual + velocidad
    
    # Simulamos el ruido del proceso y de la medición
    nueva_posicion += random.gauss(0, varianza_ruido_proceso)
    medicion = nueva_posicion + random.gauss(0, varianza_ruido_medicion)
    
    return nueva_posicion, medicion

# Función para aplicar el filtro de Kalman
def filtro_kalman(posicion_actual, varianza_posicion, velocidad, varianza_ruido_proceso, varianza_ruido_medicion):
    # Simulamos el movimiento y la medición
    nueva_posicion, medicion = simular_movimiento_y_medicion(posicion_actual, velocidad, varianza_ruido_proceso, varianza_ruido_medicion)
    
    # Aplicamos el filtro de Kalman
    ganancia_kalman = varianza_posicion / (varianza_posicion + varianza_ruido_medicion)
    estimacion_posicion = posicion_actual + ganancia_kalman * (medicion - posicion_actual)
    varianza_posicion = (1 - ganancia_kalman) * varianza_posicion
    
    return estimacion_posicion, varianza_posicion

# Aplicamos el filtro de Kalman y mostramos la estimación de la posición
print("Estimación de la posición del objeto usando el filtro de Kalman:")
for paso in range(1, 11):
    posicion_actual, varianza_posicion = filtro_kalman(posicion_actual, varianza_posicion, velocidad, varianza_ruido_proceso, varianza_ruido_medicion)
    print(f"Paso de tiempo {paso}: Estimación de posición = {posicion_actual}, Varianza de estimación = {varianza_posicion}")
