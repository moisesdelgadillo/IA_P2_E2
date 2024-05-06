# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np

# Función para calcular la distancia euclidiana entre dos vectores
def distancia_euclidiana(v1, v2):
    return np.sqrt(np.sum((v1 - v2) ** 2))

# Función para calcular la matriz de costos acumulados utilizando el algoritmo DTW
def dtw_matriz_costos(s1, s2):
    n = len(s1)
    m = len(s2)
    matriz_costos = np.zeros((n, m))

    # Rellenar la primera fila y la primera columna de la matriz de costos
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                matriz_costos[i, j] = distancia_euclidiana(s1[i], s2[j])
            elif i == 0:
                matriz_costos[i, j] = matriz_costos[i, j-1] + distancia_euclidiana(s1[i], s2[j])
            elif j == 0:
                matriz_costos[i, j] = matriz_costos[i-1, j] + distancia_euclidiana(s1[i], s2[j])
            else:
                matriz_costos[i, j] = min(matriz_costos[i-1, j], matriz_costos[i, j-1], matriz_costos[i-1, j-1]) + distancia_euclidiana(s1[i], s2[j])

    return matriz_costos

# Función para encontrar la ruta de alineación óptima utilizando el algoritmo DTW
def dtw_ruta_optima(matriz_costos):
    n, m = matriz_costos.shape
    ruta_optima = [(n-1, m-1)]
    i = n - 1
    j = m - 1
    while i > 0 or j > 0:
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if matriz_costos[i-1, j] == min(matriz_costos[i-1, j-1], matriz_costos[i-1, j], matriz_costos[i, j-1]):
                i -= 1
            elif matriz_costos[i, j-1] == min(matriz_costos[i-1, j-1], matriz_costos[i-1, j], matriz_costos[i, j-1]):
                j -= 1
            else:
                i -= 1
                j -= 1
        ruta_opti
