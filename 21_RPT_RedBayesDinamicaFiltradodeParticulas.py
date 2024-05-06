# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema dinámico
mu = 0  # Media del proceso
sigma_process = 0.1  # Desviación estándar del proceso
sigma_medida = 0.2  # Desviación estándar de la medición
n_steps = 100  # Número de pasos de tiempo

# Función de transición de estado
def transicion_estado(x):
    return x + np.random.normal(mu, sigma_process)

# Función de observación
def observacion(x):
    return x + np.random.normal(0, sigma_medida)

# Filtrado de partículas
n_particulas = 1000  # Número de partículas
x = np.zeros(n_steps)  # Estado verdadero
z = np.zeros(n_steps)  # Observaciones
x_filtrado = np.zeros(n_steps)  # Estado filtrado
pesos = np.ones(n_particulas) / n_particulas  # Pesos iniciales de las partículas

for t in range(1, n_steps):
    # Transición de estado
    x[t] = transicion_estado(x[t-1])
    
    # Observación
    z[t] = observacion(x[t])
    
    # Muestreo de partículas
    particulas = np.random.normal(x_filtrado[t-1], sigma_process, n_particulas)
    
    # Calculo de los pesos de las partículas
    likelihood = np.exp(-0.5 * ((z[t] - particulas) / sigma_medida) ** 2)
    pesos *= likelihood
    pesos /= np.sum(pesos)
    
    # Estimación del estado filtrado
    x_filtrado[t] = np.sum(particulas * pesos)

# Graficación de resultados
plt.plot(range(n_steps), x, label='Estado Verdadero')
plt.plot(range(n_steps), z, label='Observaciones', marker='o', linestyle='None')
plt.plot(range(n_steps), x_filtrado, label='Estado Filtrado')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Filtrado de Partículas para una Red Bayesiana Dinámica')
plt.legend()
plt.show()
