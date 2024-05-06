# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

#Hamming
def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Las cadenas deben tener la misma longitud")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

#Redes de Hopfield
import numpy as np

class HopfieldNetwork:
    def __init__(self, n):
        self.weights = np.zeros((n, n))
    
    def train(self, patterns):
        for pattern in patterns:
            self.weights += np.outer(pattern, pattern)
        np.fill_diagonal(self.weights, 0)
    
    def predict(self, pattern, max_iterations=100):
        for _ in range(max_iterations):
            new_pattern = np.sign(np.dot(self.weights, pattern))
            if np.array_equal(new_pattern, pattern):
                return new_pattern
            pattern = new_pattern
        return pattern
