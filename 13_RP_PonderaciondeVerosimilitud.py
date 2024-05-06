# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

import random

def ponderacion_de_verosimilitud(n, nodos, evidencias):
    resultados = {"Si": 0, "No": 0}
    for _ in range(n):
        peso = 1
        for nodo, distribucion in nodos.items():
            # Seleccionar un valor aleatorio basado en la distribución de probabilidad
            valor = random.choices(distribucion["valores"], weights=distribucion["probabilidad"]["Si"])[0]
            nodos[nodo]["valor"] = valor
            # Actualizar el peso basado en la verosimilitud del valor generado
            if nodo in evidencias:
                peso *= distribucion["probabilidad"]["Si"][distribucion["valores"].index(evidencias[nodo])]
        if nodos["A"]["valor"] == "Si":
            resultados["Si"] += peso
        else:
            resultados["No"] += peso
    return resultados["Si"] / sum(resultados.values())

# Definimos los nodos y sus distribuciones de probabilidad condicional
nodos = {
    "A": {"valores": ["Si", "No"], "probabilidad": {"Si": [0.5, 0.5]}},
    "B": {"valores": ["Si", "No"], "probabilidad": {"Si": [0.1, 0.9], "No": [0.9, 0.1]}},
    "C": {"valores": ["Si", "No"], "probabilidad": {"Si": [0.8, 0.2], "No": [0.2, 0.8]}}
}

# Ejemplo de uso
n = 10000  # Número de muestras
evidencias = {"B": "Si", "C": "No"}  # Evidencias observadas: B=Si, C=No
probabilidad = ponderacion_de_verosimilitud(n, nodos, evidencias)
print("Probabilidad de A=Si mediante ponderación de verosimilitud:", probabilidad)
