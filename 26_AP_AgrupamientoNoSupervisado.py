# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

# Supongamos que tenemos datos de puntos en un plano cartesiano
datos = [
    [1, 2], [1.5, 1.8], [5, 8],
    [8, 8], [1, 0.6], [9, 11]
]

# Función para inicializar centroides de manera aleatoria
def inicializar_centroides(datos, k):
    centroides = random.sample(datos, k)
    return centroides

# Función para asignar cada punto al centroide más cercano
def asignar_puntos_a_centroides(datos, centroides):
    clusters = [[] for _ in range(len(centroides))]
    for punto in datos:
        distancias = [((punto[0] - centroide[0]) ** 2 + (punto[1] - centroide[1]) ** 2) ** 0.5 for centroide in centroides]
        indice_centroide_mas_cercano = distancias.index(min(distancias))
        clusters[indice_centroide_mas_cercano].append(punto)
    return clusters

# Función para recalcular los centroides como la media de los puntos en cada cluster
def actualizar_centroides(clusters):
    nuevos_centroides = []
    for cluster in clusters:
        suma_x = sum(punto[0] for punto in cluster)
        suma_y = sum(punto[1] for punto in cluster)
        nuevo_centroide = [suma_x / len(cluster), suma_y / len(cluster)]
        nuevos_centroides.append(nuevo_centroide)
    return nuevos_centroides

# Algoritmo K-means
def k_means(datos, k, iteraciones):
    centroides = inicializar_centroides(datos, k)
    for _ in range(iteraciones):
        clusters = asignar_puntos_a_centroides(datos, centroides)
        centroides = actualizar_centroides(clusters)
    return clusters

# Ejemplo de uso
k = 3
iteraciones = 3
clusters = k_means(datos, k, iteraciones)
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}: {cluster}")
