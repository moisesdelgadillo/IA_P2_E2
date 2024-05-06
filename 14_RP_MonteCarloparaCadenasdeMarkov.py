# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

def transicion(nodos, estado_actual):
    estado_siguiente = random.choice(nodos[estado_actual]["valores"])
    return estado_siguiente

def mcmc(n, nodos):
    estado_actual = random.choice(list(nodos.keys()))
    conteo = {"Si": 0, "No": 0}
    for _ in range(n):
        # Realizamos la transición de estado
        estado_siguiente = transicion(nodos, estado_actual)
        nodos[estado_actual]["valor"] = estado_siguiente
        # Actualizamos el conteo de resultados
        if estado_siguiente == "Si":
            conteo["Si"] += 1
        else:
            conteo["No"] += 1
        # Actualizamos el estado actual
        estado_actual = estado_siguiente
    return conteo["Si"] / n

# Definimos los nodos y sus valores posibles
nodos = {
    "A": {"valores": ["Si", "No"]},
    "B": {"valores": ["Si", "No"]},
    "C": {"valores": ["Si", "No"]}
}

# Ejemplo de uso
n = 10000  # Número de iteraciones
probabilidad = mcmc(n, nodos)
print("Probabilidad de A=Si mediante MCMC:", probabilidad)
