# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definimos las probabilidades priori y condicionales
probabilidad_enfermedad = 0.01  # Probabilidad de tener la enfermedad (priori)
probabilidad_positivo_dado_enfermedad = 0.9  # Probabilidad de dar positivo en la prueba dado que se tiene la enfermedad
probabilidad_negativo_dado_no_enfermedad = 0.9  # Probabilidad de dar negativo en la prueba dado que no se tiene la enfermedad
probabilidad_no_enfermedad = 1 - probabilidad_enfermedad  # Probabilidad de no tener la enfermedad

# Calculamos la probabilidad de dar positivo en la prueba
probabilidad_positivo = (probabilidad_positivo_dado_enfermedad * probabilidad_enfermedad) + (probabilidad_negativo_dado_no_enfermedad * probabilidad_no_enfermedad)

# Calculamos la probabilidad de tener la enfermedad dado un resultado positivo en la prueba
probabilidad_enfermedad_dado_positivo = (probabilidad_positivo_dado_enfermedad * probabilidad_enfermedad) / probabilidad_positivo

# Imprimimos el resultado
print("Probabilidad de tener la enfermedad dado un resultado positivo en la prueba:", probabilidad_enfermedad_dado_positivo)
