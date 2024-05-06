# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definimos las probabilidades de las variables aleatorias
probabilidad_X1 = 0.3
probabilidad_X2_dado_X1 = 0.6
probabilidad_X3_dado_X1_X2 = 0.7

# Calculamos la probabilidad conjunta utilizando la regla de la cadena
probabilidad_conjunta = probabilidad_X1 * probabilidad_X2_dado_X1 * probabilidad_X3_dado_X1_X2

# Imprimimos el resultado
print("Probabilidad conjunta de X1, X2 y X3:", probabilidad_conjunta)
