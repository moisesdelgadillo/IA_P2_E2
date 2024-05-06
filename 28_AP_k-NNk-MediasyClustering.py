# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import math

# Definición de datos de ejemplo
flores = {
    'Flor1': [5.1, 3.5],
    'Flor2': [4.9, 3.0],
    'Flor3': [4.7, 3.2],
    'Flor4': [4.6, 3.1],
    'Flor5': [5.0, 3.6]
}

nueva_flor = [5.5, 3.2]  # Coordenadas de la nueva flor

# Función para calcular la distancia euclidiana entre dos puntos
def distancia_puntos(punto1, punto2):
    return math.sqrt((punto1[0] - punto2[0]) ** 2 + (punto1[1] - punto2[1]) ** 2)

# Función k-NN para clasificar un nuevo punto
def knn(datos, nuevo_punto, k):
    distancias = [(nombre, distancia_puntos(punto, nuevo_punto)) for nombre, punto in datos.items()]
    distancias.sort(key=lambda x: x[1])  # Ordenar distancias de menor a mayor
    k_vecinos = distancias[:k]  # Tomar los k vecinos más cercanos
    clases_vecinos = [nombre for nombre, _ in k_vecinos]
    clase_predicha = max(set(clases_vecinos), key=clases_vecinos.count)  # Clase con mayor frecuencia
    return clase_predicha

# Ejemplo de uso
print("Clase predicha para la nueva flor (k-NN):", knn(flores, nueva_flor, 3))
