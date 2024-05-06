# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import numpy as np

class MLP:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Inicialización de los pesos y sesgos
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.bias_hidden = np.random.randn(hidden_size)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_output = np.random.randn(output_size)
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        # Propagación hacia adelante
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.output_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.output = self.sigmoid(self.output_input)
        return self.output
    
    def backward(self, X, y, output):
        # Retropropagación del error
        output_error = y - output
        output_delta = output_error * self.sigmoid_derivative(output)
        
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_output)
        
        # Actualización de los pesos y sesgos
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta)
        self.bias_output += np.sum(output_delta, axis=0)
        
        self.weights_input_hidden += X.T.dot(hidden_delta)
        self.bias_hidden += np.sum(hidden_delta, axis=0)
    
    def train(self, X, y, epochs=1000, learning_rate=0.1):
        for epoch in range(epochs):
            # Propagación hacia adelante
            output = self.forward(X)
            
            # Retropropagación del error
            self.backward(X, y, output)
            
            # Calcular la pérdida
            loss = np.mean(np.square(y - output))
            if epoch % 100 == 0:
                print(f'Epoch {epoch}, Loss: {loss}')

# Ejemplo de uso
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

mlp = MLP(input_size=2, hidden_size=4, output_size=1)
mlp.train(X, y)
