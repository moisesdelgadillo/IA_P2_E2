# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np

class MLP:
    def __init__(self, input_size, hidden_sizes, output_size):
        self.input_size = input_size
        self.hidden_sizes = hidden_sizes
        self.output_size = output_size
        
        # Inicialización de los pesos y sesgos
        self.weights = []
        self.biases = []
        
        # Capas ocultas
        prev_size = input_size
        for size in hidden_sizes:
            self.weights.append(np.random.randn(prev_size, size))
            self.biases.append(np.random.randn(size))
            prev_size = size
        
        # Capa de salida
        self.weights.append(np.random.randn(prev_size, output_size))
        self.biases.append(np.random.randn(output_size))
    
    def forward(self, inputs):
        activations = inputs
        for w, b in zip(self.weights, self.biases):
            activations = sigmoid(np.dot(activations, w) + b)
        return activations
    
    def train(self, X, y, epochs=100, learning_rate=0.1):
        for _ in range(epochs):
            for inputs, target in zip(X, y):
                # Propagación hacia adelante
                activations = [inputs]
                for w, b in zip(self.weights, self.biases):
                    activations.append(sigmoid(np.dot(activations[-1], w) + b))
                
                # Retropropagación del error
                errors = [activations[-1] - target]
                for i in range(len(self.weights) - 1, 0, -1):
                    errors.append(np.dot(errors[-1], self.weights[i].T) * sigmoid_derivative(activations[i]))
                errors.reverse()
                
                # Actualización de los pesos y sesgos
                for i in range(len(self.weights)):
                    self.weights[i] -= learning_rate * np.dot(activations[i].T, errors[i])
                    self.biases[i] -= learning_rate * np.sum(errors[i], axis=0)

# Función de activación sigmoidal
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoidal
def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Ejemplo de uso
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

mlp = MLP(input_size=2, hidden_sizes=[4], output_size=1)
mlp.train(X, y, epochs=1000, learning_rate=0.1)

print("Predicciones:")
for inputs in X:
    print(inputs, "->", mlp.forward(inputs))
