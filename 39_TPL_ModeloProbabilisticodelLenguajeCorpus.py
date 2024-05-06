# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

from collections import defaultdict

class UnigramLanguageModel:
    def __init__(self):
        self.word_counts = defaultdict(int)
        self.total_words = 0
    
    def train(self, corpus):
        for sentence in corpus:
            for word in sentence.split():
                self.word_counts[word] += 1
                self.total_words += 1
    
    def probability(self, word):
        return self.word_counts[word] / self.total_words

# Ejemplo de uso
corpus = [
    "El gato come pescado",
    "El perro ladra",
    "El pájaro vuela",
    "El pez nada en el agua"
]

model = UnigramLanguageModel()
model.train(corpus)

print("Probabilidad de 'el':", model.probability("el"))
print("Probabilidad de 'gato':", model.probability("gato"))
print("Probabilidad de 'agua':", model.probability("agua"))
