# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np

# Función de activación (en este caso, la función sigmoidal)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Clase de la red neuronal
class RedNeuronal:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Inicialización de los pesos de las capas oculta y de salida
        self.W_h = np.random.randn(input_size, hidden_size)
        self.b_h = np.random.randn(hidden_size)
        self.W_o = np.random.randn(hidden_size, output_size)
        self.b_o = np.random.randn(output_size)
        
    # Método para hacer una predicción
    def predecir(self, X):
        # Propagación hacia adelante
        self.z_h = np.dot(X, self.W_h) + self.b_h
        self.a_h = sigmoid(self.z_h)
        self.z_o = np.dot(self.a_h, self.W_o) + self.b_o
        self.a_o = sigmoid(self.z_o)
        return self.a_o
    
    # Método para entrenar la red neuronal utilizando descenso de gradiente
    def entrenar(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            # Propagación hacia adelante
            self.predecir(X)
            
            # Cálculo del error
            error = y - self.a_o
            
            # Retropropagación del error
            delta_o = error * self.a_o * (1 - self.a_o)
            delta_h = np.dot(delta_o, self.W_o.T) * self.a_h * (1 - self.a_h)
            
            # Actualización de los pesos
            self.W_o += learning_rate * np.dot(self.a_h.T, delta_o)
            self.b_o += learning_rate * np.sum(delta_o, axis=0)
            self.W_h += learning_rate * np.dot(X.T, delta_h)
            self.b_h += learning_rate * np.sum(delta_h, axis=0)

# Ejemplo de uso
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Creación y entrenamiento de la red neuronal
red_neuronal = RedNeuronal(input_size=2, hidden_size=4, output_size=1)
red_neuronal.entrenar(X, y, epochs=1000, learning_rate=0.1)

# Predicción
prediccion = red_neuronal.predecir(X)
print("Predicción:", prediccion)
