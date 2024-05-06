# ERICK MOISES DELGADILLO LARA
# R: 21310139 - 6E1

# Definición de las variables para el espacio de configuración
posicion_inicial = (0, 0)  # Posición inicial del robot en el espacio
posicion_final = (3, 4)  # Posición final deseada del robot en el espacio

# Función para calcular la distancia euclidiana entre dos puntos en el espacio
def calcular_distancia(punto1, punto2):
    # Calcula la diferencia en coordenadas x e y
    diff_x = punto2[0] - punto1[0]
    diff_y = punto2[1] - punto1[1]
    # Calcula la distancia euclidiana
    distancia = (diff_x ** 2 + diff_y ** 2) ** 0.5
    return distancia

# Función para determinar si un movimiento es posible en el espacio de configuración
def es_movimiento_posible(posicion_actual, nueva_posicion):
    distancia = calcular_distancia(posicion_actual, nueva_posicion)
    # Verifica si la distancia entre las posiciones es menor o igual a 1 (movimiento permitido)
    return distancia <= 1

# Simulación del movimiento en el espacio de configuración
print("Inicio del movimiento en el espacio de configuración")
print("Posición inicial:", posicion_inicial)
print("Posición final:", posicion_final)

# Verificar si el movimiento es posible
if es_movimiento_posible(posicion_inicial, posicion_final):
    print("El movimiento es posible. El robot puede llegar a la posición final.")
else:
    print("El movimiento no es posible. El robot no puede llegar a la posición final.")
