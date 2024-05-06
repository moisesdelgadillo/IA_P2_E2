# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Variables para contar las camisas por talla
camisas_xs = 1
camisas_s = 4
camisas_m = 3
camisas_l = 9

# Calculamos el total de canicas en la bolsa
total_camisas = camisas_xs + camisas_s + camisas_m + camisas_l

# Función para calcular la probabilidad de sacar una camisa de talla especifica
def calc_probabilidad(nocamisas, total):
    # La probabilidad se calcula como la relación entre el número de canicas de un color y el total de canicas
    probabilidad = nocamisas / total
    # Convertimos la probabilidad a porcentaje para que sea más fácil de entender
    probabilidad_porcentaje = probabilidad * 100
    return probabilidad_porcentaje

# Calculamos la probabilidad para cada color
probabilidad_xs = calc_probabilidad(camisas_xs, total_camisas)
probabilidad_s = calc_probabilidad(camisas_s, total_camisas)
probabilidad_m = calc_probabilidad(camisas_m, total_camisas)
probabilidad_l = calc_probabilidad(camisas_l, total_camisas)

# Imprimimos los resultados
print(f"Probabilidad de sacar una camisa xs: {probabilidad_xs:.2f}%")
print(f"Probabilidad de sacar una camisa s: {probabilidad_s:.2f}%")
print(f"Probabilidad de sacar una camisa m: {probabilidad_m:.2f}%")
print(f"Probabilidad de sacar una camisa l: {probabilidad_l:.2f}%")
