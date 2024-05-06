# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

from collections import defaultdict
import random

class PCFG:
    def __init__(self):
        self.start_symbol = None
        self.productions = defaultdict(list)
        self.non_terminals = set()
    
    def add_production(self, lhs, rhs, probability):
        self.productions[lhs].append((rhs, probability))
        self.non_terminals.add(lhs)
    
    def set_start_symbol(self, symbol):
        self.start_symbol = symbol
    
    def generate_sentence(self):
        return self._generate(self.start_symbol)
    
    def _generate(self, symbol):
        if symbol not in self.non_terminals:
            return symbol
        else:
            productions = self.productions[symbol]
            rhs, probabilities = zip(*productions)
            chosen_production = random.choices(rhs, weights=probabilities)[0]
            return ' '.join(self._generate(s) for s in chosen_production)

# Ejemplo de uso
pcfg = PCFG()

# Definir las reglas de producción con sus probabilidades
pcfg.add_production('S', ['NP', 'VP'], 0.5)
pcfg.add_production('S', ['VP'], 0.5)
pcfg.add_production('NP', ['Det', 'N'], 0.7)
pcfg.add_production('NP', ['Det', 'N', 'PP'], 0.3)
pcfg.add_production('VP', ['V', 'NP'], 0.6)
pcfg.add_production('VP', ['V', 'NP', 'PP'], 0.4)
pcfg.add_production('PP', ['P', 'NP'], 1.0)
pcfg.add_production('Det', ['the'], 1.0)
pcfg.add_production('N', ['cat'], 0.5)
pcfg.add_production('N', ['dog'], 0.5)
pcfg.add_production('V', ['chased'], 1.0)
pcfg.add_production('P', ['with'], 1.0)

pcfg.set_start_symbol('S')

# Generar una oración
sentence = pcfg.generate_sentence()
print("Oración generada:", sentence)
