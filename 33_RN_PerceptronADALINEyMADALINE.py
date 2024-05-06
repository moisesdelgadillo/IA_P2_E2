# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

#Perceptron
class Perceptron:
    def __init__(self, n_inputs):
        self.weights = [0] * n_inputs
        self.bias = 0
    
    def predict(self, inputs):
        activation = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        return 1 if activation > 0 else 0
    
    def train(self, training_data, epochs=100, learning_rate=0.1):
        for _ in range(epochs):
            for inputs, label in training_data:
                prediction = self.predict(inputs)
                self.weights = [w + learning_rate * (label - prediction) * x for w, x in zip(self.weights, inputs)]
                self.bias += learning_rate * (label - prediction)

#Adaline
class Adaline:
    def __init__(self, n_inputs):
        self.weights = [0] * n_inputs
        self.bias = 0
    
    def predict(self, inputs):
        activation = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        return activation
    
    def train(self, training_data, epochs=100, learning_rate=0.1):
        for _ in range(epochs):
            for inputs, label in training_data:
                prediction = self.predict(inputs)
                error = label - prediction
                self.weights = [w + learning_rate * error * x for w, x in zip(self.weights, inputs)]
                self.bias += learning_rate * error

#Madaline
class Madaline:
    def __init__(self, n_inputs, n_units):
        self.units = [Adaline(n_inputs) for _ in range(n_units)]
    
    def predict(self, inputs):
        return [unit.predict(inputs) for unit in self.units]
    
    def train(self, training_data, epochs=100, learning_rate=0.1):
        for _ in range(epochs):
            for inputs, label in training_data:
                predictions = self.predict(inputs)
                for unit, prediction in zip(self.units, predictions):
                    error = label - prediction
                    unit.train([(inputs, error)], epochs=1, learning_rate=learning_rate)

