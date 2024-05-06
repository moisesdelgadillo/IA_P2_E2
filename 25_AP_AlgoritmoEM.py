# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

# Función para calcular la probabilidad de un punto dado un conjunto de parámetros
def calcular_probabilidad(x, mu, sigma):
    exponente = -0.5 * ((x - mu) / sigma) ** 2
    return (1 / (sigma * (2 * 3.14159) ** 0.5)) * 2.71828 ** exponente

# Algoritmo EM para el problema de mezcla de distribuciones gaussianas (GMM)
def em_gmm(datos, n_clusters, max_iter=100, tol=1e-6):
    n, d = len(datos), len(datos[0])
    
    # Inicialización aleatoria de los parámetros
    mu = [[random.uniform(min(datos[:, i]), max(datos[:, i])) for i in range(d)] for _ in range(n_clusters)]
    sigma = [[1] * d] * n_clusters
    pi = [1 / n_clusters] * n_clusters
    
    # Bucle EM
    for _ in range(max_iter):
        # Paso E: Calcular responsabilidades
        resp = []
        for punto in datos:
            responsabilidades = [pi[k] * calcular_probabilidad(punto, mu[k], sigma[k]) for k in range(n_clusters)]
            suma_resp = sum(responsabilidades)
            resp.append([r / suma_resp for r in responsabilidades])
        
        # Paso M: Actualizar parámetros
        nuevos_mu = []
        nuevos_sigma = []
        nuevos_pi = []
        for k in range(n_clusters):
            n_k = sum(resp[i][k] for i in range(n))
            nuevos_mu_k = sum(resp[i][k] * datos[i][j] for i in range(n) for j in range(d)) / n_k
            nuevos_sigma_k = (sum(resp[i][k] * (datos[i][j] - nuevos_mu_k) ** 2 for i in range(n) for j in range(d)) / n_k) ** 0.5
            nuevos_pi_k = n_k / n
            nuevos_mu.append(nuevos_mu_k)
            nuevos_sigma.append(nuevos_sigma_k)
            nuevos_pi.append(nuevos_pi_k)
        
        # Convergencia
        if sum(abs(nuevos_mu[k][j] - mu[k][j]) for k in range(n_clusters) for j in range(d)) < tol:
            break
        
        mu, sigma, pi = nuevos_mu, nuevos_sigma, nuevos_pi
    
    return mu, sigma, pi

# Ejemplo de uso
datos = [[1.5, 2.0], [1.0, 1.8], [2.5, 3.0], [2.0, 2.5], [3.0, 3.5]]
n_clusters = 2
mu_estimado, sigma_estimado, pi_estimado = em_gmm(datos, n_clusters)
print("Media estimada:", mu_estimado)
print("Desviación estándar estimada:", sigma_estimado)
print("Peso estimado:", pi_estimado)
