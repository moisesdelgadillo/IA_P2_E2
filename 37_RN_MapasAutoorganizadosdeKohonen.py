# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np

class SOM:
    def __init__(self, input_size, map_size):
        self.input_size = input_size
        self.map_size = map_size
        
        # Inicialización de los pesos
        self.weights = np.random.rand(map_size[0], map_size[1], input_size)
    
    def find_best_matching_unit(self, input_vector):
        # Calcular la distancia euclidiana entre el vector de entrada y todos los pesos
        distances = np.linalg.norm(self.weights - input_vector, axis=2)
        
        # Encontrar la unidad ganadora (la que tiene el menor valor de distancia)
        bmu_index = np.unravel_index(np.argmin(distances), distances.shape)
        return bmu_index
    
    def update_weights(self, input_vector, bmu_index, learning_rate, radius):
        # Calcular la vecindad de la unidad ganadora
        distance_from_bmu = np.linalg.norm(np.indices(self.map_size) - np.array(bmu_index)[:, np.newaxis, np.newaxis], axis=0)
        neighborhood = np.exp(-distance_from_bmu / (2 * radius ** 2))
        
        # Actualizar los pesos de las unidades vecinas
        self.weights += learning_rate * neighborhood[:, :, np.newaxis] * (input_vector - self.weights)
    
    def train(self, data, num_epochs, learning_rate_initial, radius_initial):
        for epoch in range(1, num_epochs + 1):
            # Actualizar la tasa de aprendizaje y el radio del vecindario
            learning_rate = learning_rate_initial * np.exp(-epoch / num_epochs)
            radius = radius_initial * np.exp(-epoch / num_epochs)
            
            # Iterar sobre los datos de entrada
            for input_vector in data:
                # Encontrar la unidad ganadora
                bmu_index = self.find_best_matching_unit(input_vector)
                
                # Actualizar los pesos
                self.update_weights(input_vector, bmu_index, learning_rate, radius)

# Ejemplo de uso
# Generar datos de ejemplo (en este caso, puntos en un círculo)
num_points = 1000
theta = np.random.rand(num_points) * 2 * np.pi
radius = np.sqrt(np.random.rand(num_points))
data = np.array([radius * np.cos(theta), radius * np.sin(theta)]).T

# Normalizar los datos
data /= np.max(data)

# Crear y entrenar el SOM
input_size = 2  # Tamaño de los vectores de entrada (en este caso, coordenadas x e y)
map_size = (10, 10)  # Tamaño del mapa SOM
som = SOM(input_size, map_size)
som.train(data, num_epochs=100, learning_rate_initial=0.1, radius_initial=max(map_size) / 2)

# Visualizar el mapa SOM
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 8))
for i in range(map_size[0]):
    for j in range(map_size[1]):
        plt.scatter(i, j, color=som.weights[i, j], marker='s', s=200, edgecolor='k')
plt.title('Mapa Autoorganizado de Kohonen')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.grid(True)
plt.show()
