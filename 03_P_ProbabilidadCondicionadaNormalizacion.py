# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definimos las probabilidades de dos eventos A y B
probabilidad_A = 0.6
probabilidad_B = 0.4

# Calculamos la probabilidad condicionada P(A|B)
probabilidad_condicionada = 0.3  # Ejemplo arbitrario

# Calculamos la probabilidad conjunta P(A ∩ B) usando la fórmula de probabilidad condicionada
probabilidad_conjunta = probabilidad_condicionada * probabilidad_B

# Normalizamos las probabilidades para que sumen 1
probabilidad_total = probabilidad_A + probabilidad_B
probabilidad_A_normalizada = probabilidad_A / probabilidad_total
probabilidad_B_normalizada = probabilidad_B / probabilidad_total

# Imprimimos los resultados
print("Probabilidad condicionada P(A|B):", probabilidad_condicionada)
print("Probabilidad conjunta P(A ∩ B):", probabilidad_conjunta)
print("Probabilidad de A normalizada:", probabilidad_A_normalizada)
print("Probabilidad de B normalizada:", probabilidad_B_normalizada)
