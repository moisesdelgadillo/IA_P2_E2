# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definimos los nodos y sus distribuciones de probabilidad condicional
nodos = {
    "A": {"valores": ["Si", "No"], "probabilidad": {"": [0.5, 0.5]}},
    "B": {"valores": ["Si", "No"], "probabilidad": {"Si": [0.1, 0.9], "No": [0.9, 0.1]}},
    "C": {"valores": ["Si", "No"], "probabilidad": {"Si": [0.8, 0.2], "No": [0.2, 0.8]}}
}

# Función para calcular la probabilidad condicional de un nodo dado los valores de sus padres
def obtener_probabilidad(nodo, valores_padres):
    distribucion = nodos[nodo]["probabilidad"]
    return distribucion[valores_padres]

# Función para calcular la probabilidad conjunta de los nodos dados ciertos valores
def obtener_probabilidad_conjunta(valores):
    probabilidad_conjunta = 1
    for nodo, valor in valores.items():
        probabilidad_conjunta *= obtener_probabilidad(nodo, valores.get("", ""))
    return probabilidad_conjunta

# Calculamos la probabilidad conjunta de los eventos
probabilidad = obtener_probabilidad_conjunta({"A": "Si", "B": "Si", "C": "No"})
print("Probabilidad conjunta de A='Si', B='Si', C='No':", probabilidad)
