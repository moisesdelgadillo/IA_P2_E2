# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

from collections import defaultdict
import random

class LPCFG:
    def __init__(self):
        self.start_symbol = None
        self.productions = defaultdict(list)
        self.non_terminals = set()
    
    def add_production(self, lhs, rhs, word, probability):
        self.productions[lhs].append((rhs, word, probability))
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
            rhs, words, probabilities = zip(*productions)
            chosen_production = random.choices(range(len(productions)), weights=probabilities)[0]
            sentence = ' '.join(self._generate(s) for s in rhs[chosen_production])
            return sentence + ' ' + words[chosen_production]

# Ejemplo de uso
lpcfg = LPCFG()

# Definir las reglas de producción con sus probabilidades
lpcfg.add_production('S', ['NP', 'VP'], 'is', 0.5)
lpcfg.add_production('S', ['VP'], 'am', 0.5)
lpcfg.add_production('NP', ['Det', 'N'], 'a', 0.7)
lpcfg.add_production('NP', ['Det', 'N', 'PP'], 'the', 0.3)
lpcfg.add_production('VP', ['V', 'NP'], 'playing', 0.6)
lpcfg.add_production('VP', ['V', 'NP', 'PP'], 'running', 0.4)
lpcfg.add_production('PP', ['P', 'NP'], 'with', 1.0)
lpcfg.add_production('Det', ['the'], '', 1.0)
lpcfg.add_production('N', ['cat'], '', 0.5)
lpcfg.add_production('N', ['dog'], '', 0.5)
lpcfg.add_production('V', ['chased'], '', 1.0)
lpcfg.add_production('P', ['with'], '', 1.0)

lpcfg.set_start_symbol('S')

# Generar una oración
sentence = lpcfg.generate_sentence()
print("Oración generada:", sentence)
