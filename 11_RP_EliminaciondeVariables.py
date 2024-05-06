# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definimos los nodos y sus distribuciones de probabilidad condicional
nodos = {
    "A": {"valores": ["Si", "No"], "probabilidad": {"": [0.5, 0.5]}},
    "B": {"valores": ["Si", "No"], "probabilidad": {"Si": [0.1, 0.9], "No": [0.9, 0.1]}},
    "C": {"valores": ["Si", "No"], "probabilidad": {"Si": [0.8, 0.2], "No": [0.2, 0.8]}}
}

# Función para calcular la probabilidad de un evento dado ciertas evidencias utilizando eliminación de variables
def eliminacion_de_variables(evento, evidencias):
    variables_no_observadas = [nodo for nodo in nodos.keys() if nodo not in evidencias]
    for nodo in variables_no_observadas:
        distribucion = nodos[nodo]["probabilidad"]
        suma = 0
        for valor in nodos[nodo]["valores"]:
            suma += obtener_probabilidad_conjunta({nodo: valor, **evidencias})
        for valor in nodos[nodo]["valores"]:
            distribucion[""][nodos[nodo]["valores"].index(valor)] = obtener_probabilidad_conjunta({nodo: valor, **evidencias}) / suma
    return nodos[evento]["probabilidad"][""][nodos[evento]["valores"].index("Si")]

# Función para calcular la probabilidad conjunta de los nodos dados ciertos valores
def obtener_probabilidad_conjunta(valores):
    probabilidad_conjunta = 1
    for nodo, valor in valores.items():
        probabilidad_conjunta *= obtener_probabilidad(nodo, valores.get("", ""))
    return probabilidad_conjunta

# Función para calcular la probabilidad condicional de un nodo dado los valores de sus padres
def obtener_probabilidad(nodo, valores_padres):
    distribucion = nodos[nodo]["probabilidad"]
    return distribucion[valores_padres]

# Ejemplo de uso
evidencias = {"B": "Si", "C": "No"}  # Evidencias observadas: B=Si, C=No
probabilidad = eliminacion_de_variables("A", evidencias)
print("Probabilidad de A=Si dado B=Si y C=No:", probabilidad)
