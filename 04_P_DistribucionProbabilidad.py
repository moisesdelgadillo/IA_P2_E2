# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definimos la cantidad total de caras en el dado
total_caras = 6

# Calculamos la probabilidad para cada resultado posible (distribución uniforme)
probabilidad_uniforme = 1 / total_caras

# Creamos un diccionario para almacenar los resultados y sus probabilidades
distribucion_probabilidad = {}

# Asignamos la misma probabilidad a cada resultado posible
for cara in range(1, total_caras + 1):
    distribucion_probabilidad[cara] = probabilidad_uniforme

# Imprimimos la distribución de probabilidad resultante
print("Distribución de probabilidad uniforme para el lanzamiento de un dado justo:")
for cara, probabilidad in distribucion_probabilidad.items():
    print("Número:", cara, "- Probabilidad:", probabilidad)
