# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

# Función para simular la medición de la temperatura diaria
def medir_temperatura():
    # Simulamos una medición de temperatura con un ligero ruido aleatorio
    temperatura_actual = random.uniform(20, 30)  # Temperatura actual
    ruido = random.uniform(-2, 2)  # Ruido aleatorio
    temperatura_medida = temperatura_actual + ruido
    return temperatura_medida

# Definimos los parámetros iniciales del filtro de Kalman
temperatura_inicial = 25  # Temperatura inicial estimada
varianza_inicial = 5  # Varianza inicial de la estimación

# Función para realizar el filtrado, predicción, suavizado y explicación de la temperatura
def filtro_kalman(temperatura_medida, temperatura_estimada, varianza_estimada):
    # Varianza de la medición
    varianza_medicion = 2  # Valor de ejemplo
    
    # Actualizamos la estimación de la temperatura utilizando la medición actual
    ganancia_kalman = varianza_estimada / (varianza_estimada + varianza_medicion)
    temperatura_estimada = temperatura_estimada + ganancia_kalman * (temperatura_medida - temperatura_estimada)
    varianza_estimada = (1 - ganancia_kalman) * varianza_estimada
    
    # Realizamos la predicción de la temperatura para el próximo día
    temperatura_predicha = temperatura_estimada
    varianza_predicha = varianza_estimada
    
    # Realizamos el suavizado de la temperatura utilizando las mediciones anteriores
    # (No se implementa en este ejemplo)
    
    # Explicamos la estimación de la temperatura actual y la predicción para el próximo día
    print("Estimación actual de la temperatura:", temperatura_estimada)
    print("Predicción de la temperatura para mañana:", temperatura_predicha)

# Simulamos el proceso de filtrado, predicción, suavizado y explicación de la temperatura
print("Simulación del filtro de Kalman para la temperatura:")
for dia in range(1, 8):  # Simulamos una semana de mediciones
    print("\nDía", dia)
    temperatura_medida = medir_temperatura()  # Medición de la temperatura diaria
    filtro_kalman(temperatura_medida, temperatura_inicial, varianza_inicial)
