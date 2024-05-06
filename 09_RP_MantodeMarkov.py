# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

# Definimos la matriz de transición de la cadena de Markov
matriz_transicion = [
    [0.7, 0.3],  # Probabilidad de transición de estado 0 a estado 0 y estado 0 a estado 1 respectivamente
    [0.4, 0.6]   # Probabilidad de transición de estado 1 a estado 0 y estado 1 a estado 1 respectivamente
]

# Definimos el estado inicial
estado_actual = 0  # Supongamos que comenzamos en el estado 0

# Simulamos la cadena de Markov para 3 pasos de tiempo
for paso in range(3):
    print("Paso de tiempo:", paso)
    print("Estado actual:", estado_actual)

    # Calculamos el próximo estado basado en la matriz de transición y el estado actual
    estado_siguiente = 0 if random.random() < matriz_transicion[estado_actual][0] else 1

    # Actualizamos el estado actual para el próximo paso de tiempo
    estado_actual = estado_siguiente

    print("Estado siguiente:", estado_siguiente)
    print()
