# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definimos las probabilidades de los eventos A, B y C
probabilidad_A = 0.4
probabilidad_B = 0.3
probabilidad_C = 0.5

# Definimos las probabilidades condicionadas de A dado C y B dado C
probabilidad_A_dado_C = 0.3
probabilidad_B_dado_C = 0.2

# Verificamos si A y B son independientes dados C
# Si P(A|C) = P(A) y P(B|C) = P(B), entonces A y B son independientes dados C
es_independiente_condicionalmente = abs(probabilidad_A_dado_C - probabilidad_A) < 1e-6 and abs(probabilidad_B_dado_C - probabilidad_B) < 1e-6

# Imprimimos el resultado
if es_independiente_condicionalmente:
    print("Los eventos A y B son independientes dado C.")
else:
    print("Los eventos A y B no son independientes dado C.")
