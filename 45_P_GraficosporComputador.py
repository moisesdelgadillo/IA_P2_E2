# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de una lista de puntos en un sistema de coordenadas
puntos = [
    (2, 3),
    (5, 8),
    (7, 2),
    (9, 5),
    (4, 6)
]

# Función para graficar los puntos en un sistema de coordenadas
def graficar_puntos(lista_puntos):
    # Recorrer la lista de puntos y graficar cada uno
    for punto in lista_puntos:
        x, y = punto  # Obtener las coordenadas x e y del punto
        print("x:", x, "y:", y)  # Mostrar las coordenadas del punto en consola

# Llamar a la función para graficar los puntos
print("Puntos en el sistema de coordenadas:")
graficar_puntos(puntos)
