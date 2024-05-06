# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

def muestreo_directo(n, nodos):
    resultados = {"Si": 0, "No": 0}
    for _ in range(n):
        for nodo, distribucion in nodos.items():
            # Seleccionar un valor aleatorio basado en la distribución de probabilidad
            valor = random.choices(distribucion["valores"], weights=distribucion["probabilidad"]["Si"])[0]
            nodos[nodo]["valor"] = valor
        if nodos["A"]["valor"] == "Si":
            resultados["Si"] += 1
        else:
            resultados["No"] += 1
    return resultados["Si"] / n

# Definimos los nodos y sus distribuciones de probabilidad condicional
nodos = {
    "A": {"valores": ["Si", "No"], "probabilidad": {"Si": [0.5, 0.5]}},
    "B": {"valores": ["Si", "No"], "probabilidad": {"Si": [0.1, 0.9], "No": [0.9, 0.1]}},
    "C": {"valores": ["Si", "No"], "probabilidad": {"Si": [0.8, 0.2], "No": [0.2, 0.8]}}
}

# Ejemplo de uso
n = 10000  # Número de muestras
probabilidad = muestreo_directo(n, nodos)
print("Probabilidad de A=Si mediante muestreo directo:", probabilidad)
